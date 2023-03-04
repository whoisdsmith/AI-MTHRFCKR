# coding: utf-8
# author: luuil@outlook.com

r"""Train audio model."""

from __future__ import print_function
import sys
sys.path.append('./audio')

import os
import numpy as np
import natsort
import shutil

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
# get_ipython().run_line_magic('matplotlib', 'inline')

import tensorflow as tf
from tensorflow.python.platform import gfile

from sklearn.metrics import accuracy_score

import audio_params as params
import audio_util as util
from audio_records import RecordsParser
from audio_model import define_audio_slim
from audio_feature_extractor import VGGishExtractor

tf.logging.set_verbosity(tf.logging.DEBUG)

flags = tf.app.flags

flags.DEFINE_string(
    'vggish_ckpt_dir', params.VGGISH_CHECKPOINT_DIR,
    'Path to the VGGish checkpoint file.')

flags.DEFINE_string(
    'audio_ckpt_dir', params.AUDIO_CHECKPOINT_DIR,
    'Path to the audio checkpoint file.')

flags.DEFINE_string(
    'train_name', params.AUDIO_TRAIN_NAME,
    'Directory name for audio checkpoint file to save, i.e. audio checkpoint'
    'file will save to `audio_ckpt_dir/train_name`.')

flags.DEFINE_string(
    'wavfile_parent_dir', params.WAV_FILE_PARENT_DIR,
    "Path to wav file's parent directory, each subdirectory is a class of files.")

flags.DEFINE_string(
    'records_dir', params.TF_RECORDS_DIR,
    "Path to the TF records file's parent directory.")

flags.DEFINE_bool(
    'restore_if_possible', True,
    "Restore variables from checkpoint if checkpoint is exists.")

FLAGS = flags.FLAGS

MAX_NUM_PER_CLASS = 2 ** 27 - 1  # ~134M


train_records_path = os.path.join(FLAGS.records_dir, 
    params.TF_RECORDS_TRAIN_NAME)

test_records_path = os.path.join(FLAGS.records_dir, 
    params.TF_RECORDS_TEST_NAME)

val_records_path = os.path.join(FLAGS.records_dir,
    params.TF_RECORDS_VAL_NAME)

vggish_ckpt_path = os.path.join(FLAGS.vggish_ckpt_dir,
    params.VGGISH_CHECKPOINT_NAME)

vggish_pca_path = os.path.join(FLAGS.vggish_ckpt_dir,
    params.VGGISH_PCA_PARAMS_NAME)

tensorboard_dir = os.path.join(params.TENSORBOARD_DIR,
    FLAGS.train_name)

audio_ckpt_dir = os.path.join(FLAGS.audio_ckpt_dir,
    FLAGS.train_name)

util.maybe_create_directory(tensorboard_dir)
util.maybe_create_directory(audio_ckpt_dir)

# backup params
shutil.copy(os.path.join(os.path.dirname(__file__), 'audio_params.py'), audio_ckpt_dir)

def _add_triaining_graph():
    with tf.Graph().as_default() as graph:
        logits = define_audio_slim(training=True)
        tf.summary.histogram('logits', logits)
        # define training subgraph
        with tf.variable_scope('train'):
            labels = tf.placeholder(tf.float32, 
                shape=[None, params.NUM_CLASSES], name='labels')
            cross_entropy = tf.nn.softmax_cross_entropy_with_logits_v2(
                        logits=logits, labels=labels, name='cross_entropy')
            loss = tf.reduce_mean(cross_entropy, name='loss_op')
            tf.summary.scalar('loss', loss)
            # training
            global_step = tf.Variable(0, name='global_step', trainable=False,
                                      collections=[tf.GraphKeys.GLOBAL_VARIABLES,
                                                   tf.GraphKeys.GLOBAL_STEP])
            optimizer = tf.train.AdamOptimizer(
                learning_rate=params.LEARNING_RATE,
                epsilon=params.ADAM_EPSILON)
            optimizer.minimize(loss, global_step=global_step, name='train_op')
        return graph


def _check_vggish_ckpt_exists():
    """check VGGish checkpoint exists or not."""
    util.maybe_create_directory(FLAGS.vggish_ckpt_dir)
    if not util.is_exists(vggish_ckpt_path):
        url = 'https://storage.googleapis.com/audioset/vggish_model.ckpt'
        util.maybe_download(url, params.VGGISH_CHECKPOINT_DIR)
    if not util.is_exists(vggish_pca_path):
        url = 'https://storage.googleapis.com/audioset/vggish_pca_params.npz'
        util.maybe_download(url, params.VGGISH_CHECKPOINT_DIR)


def _wav_files_and_labels():
    """Get wav files path and labels as a dict object.

    Args:
        None
    Returns:
        result = { label:wav_file_list }
    """
    if not util.is_exists(FLAGS.wavfile_parent_dir):
        tf.logging.error("Can not find wav files at: {}, or you can download one at "
            "https://serv.cusp.nyu.edu/projects/urbansounddataset.".format(
                FLAGS.wavfile_parent_dir))
        exit(1)


    sub_dirs = [x[0] for x in gfile.Walk(FLAGS.wavfile_parent_dir)]
    sub_dirs = natsort.natsorted(sub_dirs)
    sub_dirs = sub_dirs[1:] # The root directory comes first, so skip it.

    wav_files = []
    wav_labels = []
    for label_idx, sub_dir in enumerate(sub_dirs):
        extensions = ['wav']
        file_list = []
        dir_name = os.path.basename(sub_dir)
        if dir_name == FLAGS.wavfile_parent_dir:
            continue
        if dir_name[0] == '.':
            continue
        tf.logging.info("Looking for wavs in '" + dir_name + "'")
        for extension in extensions:
            file_glob = os.path.join(FLAGS.wavfile_parent_dir, dir_name, '*.' + extension)
            file_list.extend(gfile.Glob(file_glob))
        if not file_list:
            tf.logging.warning('No files found')
            continue
        if len(file_list) < 20:
            tf.logging.warning('WARNING: Folder has less than 20 wavs,'
                'which may cause issues.')
        elif len(file_list) > MAX_NUM_PER_CLASS:
            tf.logging.warning(
                'WARNING: Folder {} has more than {} wavs. Some wavs will '
                'never be selected.'.format(dir_name, MAX_NUM_PER_CLASS))
        # label_name = re.sub(r'[^a-z0-9]+', ' ', dir_name.lower())
        wav_files.extend(file_list)
        wav_labels.extend([label_idx]*len(file_list))
    assert len(wav_files) == len(wav_labels), \
        'Length of wav files and wav labels should be in consistent.'
    return wav_files, wav_labels

def _create_records():
    """Create audio `train`, `test` and `val` records file."""
    tf.logging.info("Create records..")
    util.maybe_create_directory(FLAGS.records_dir)
    _check_vggish_ckpt_exists()
    wav_files, wav_labels = _wav_files_and_labels()
    tf.logging.info('Possible labels: {}'.format(set(wav_labels)))
    train, test, val = util.train_test_val_split(wav_files, wav_labels)
    with VGGishExtractor(vggish_ckpt_path,
                         vggish_pca_path,
                         params.VGGISH_INPUT_TENSOR_NAME,
                         params.VGGISH_OUTPUT_TENSOR_NAME) as ve:
        
        train_x, train_y = train
        ve.create_records(train_records_path, train_x, train_y)
        
        test_x, test_y = test
        ve.create_records(test_records_path, test_x, test_y)
        
        val_x, val_y = val
        ve.create_records(val_records_path, val_x, val_y)
        tf.logging.info('Dataset size: Train-{} Test-{} Val-{}'.format(
            len(train_y), len(test_y), len(val_y)))

def _get_records_iterator(records_path, batch_size):
    """Get records iterator"""
    if not util.is_exists(records_path):
        _create_records()
    rp = RecordsParser([records_path], params.NUM_CLASSES, feature_shape=None)
    return rp.iterator(is_onehot=True, batch_size=batch_size)


def _add_scalar_summary(writer, tag, value, step):
    scalar_summary = tf.Summary(value=[tf.Summary.Value(tag=tag, simple_value=value)])
    writer.add_summary(scalar_summary, step)


def main(_):

    # initialize all log data containers:
    train_loss_per_epoch = []
    val_loss_per_epoch = []
    # initialize a list containing the 5 best val losses (is used to tell when to
    # save a model checkpoint):
    best_epoch_losses = [1000, 1000, 1000, 1000, 1000]

    sess_config = tf.ConfigProto(allow_soft_placement=True)
    sess_config.gpu_options.allow_growth = True

    with tf.Session(graph=_add_triaining_graph(), config=sess_config) as sess:
        train_iterator, train_batch = _get_records_iterator(train_records_path,
            batch_size=params.BATCH_SIZE)
        val_iterator, val_batch = _get_records_iterator(val_records_path, batch_size=128)
        test_iterator, test_batch = _get_records_iterator(test_records_path, batch_size=128)

        # op and tensors
        features_tensor = sess.graph.get_tensor_by_name(params.AUDIO_INPUT_TENSOR_NAME)
        output_tensor = sess.graph.get_tensor_by_name(params.AUDIO_OUTPUT_TENSOR_NAME)
        labels_tensor = sess.graph.get_tensor_by_name('train/labels:0')
        global_step_tensor = sess.graph.get_tensor_by_name('train/global_step:0')
        loss_tensor = sess.graph.get_tensor_by_name('train/loss_op:0')
        train_op = sess.graph.get_operation_by_name('train/train_op')

        summary_op = tf.summary.merge_all()
        summary_writer = tf.summary.FileWriter(tensorboard_dir, graph=sess.graph)
        saver = tf.train.Saver()
        
        init = tf.global_variables_initializer()
        sess.run(init)


        checkpoint_path = os.path.join(audio_ckpt_dir, params.AUDIO_CHECKPOINT_NAME)
        if util.is_exists(checkpoint_path+'.meta') and FLAGS.restore_if_possible:
            saver.restore(sess, checkpoint_path)

        # training and validation loop
        for epoch in range(params.NUM_EPOCHS):

            # training loop
            train_batch_losses = []
            sess.run(train_iterator.initializer)
            while True:
                try:
                    # feature: [batch_size, num_features]
                    # label: [batch_size, num_classes]
                    tr_features, tr_labels = sess.run(train_batch)
                except tf.errors.OutOfRangeError:
                    break
                [num_steps, loss, summaries, _] = sess.run([global_step_tensor, loss_tensor, summary_op, train_op],
                                                feed_dict={features_tensor: tr_features, labels_tensor: tr_labels})
                train_batch_losses.append(loss)
                summary_writer.add_summary(summaries, num_steps)
                print('Epoch {}/{}, Step {}: train loss {}'.format(epoch, params.NUM_EPOCHS, num_steps, loss))

            # compute the train epoch loss:
            train_epoch_loss = np.mean(train_batch_losses)
            # save the train epoch loss:
            train_loss_per_epoch.append(train_epoch_loss)
            print("train epoch loss: %g" % train_epoch_loss)


            # validation loop
            val_batch_losses = []
            sess.run(val_iterator.initializer)
            while True:
                try:
                    val_features, val_labels = sess.run(val_batch)
                except tf.errors.OutOfRangeError:
                    break
                [prediction, loss] = sess.run(
                    [output_tensor, loss_tensor],
                    feed_dict={features_tensor: val_features, labels_tensor: val_labels})
                val_batch_losses.append(loss)
                # print('predict shape:', prediction.shape)
                # print("Example val loss: {:.5f}".format(loss))
            val_loss = np.mean(val_batch_losses)
            val_loss_per_epoch.append(val_loss)
            print("validation loss: %g" % val_loss)
            _add_scalar_summary(summary_writer, 'train/val_loss', val_loss, num_steps) # add to summary

            # testing loop
            predicted = []
            groundtruth = []
            sess.run(test_iterator.initializer)
            while True:
                try:
                    te_features, te_labels = sess.run(test_batch)
                except tf.errors.OutOfRangeError:
                    break
                predictions = sess.run(output_tensor, feed_dict={features_tensor: te_features, labels_tensor: te_labels})
                predicted.extend(np.argmax(predictions, axis=1))
                groundtruth.extend(np.argmax(te_labels, axis=1))
            test_acc = accuracy_score(groundtruth, predicted, normalize=True)
            print(f"test_acc: {test_acc}")
            _add_scalar_summary(summary_writer, 'train/test_acc', test_acc, num_steps) # add to summary


            if val_loss < min(best_epoch_losses): # (if top 5 performance on val:)
                # save the model weights to disk:
                checkpoint_path2 = os.path.join(audio_ckpt_dir, 
                    'l{loss:.2f}_{name}'.format(loss=val_loss, name=params.AUDIO_CHECKPOINT_NAME))
                saver.save(sess, checkpoint_path)
                saver.save(sess, checkpoint_path2)
                print("checkpoint saved in file: %s" % checkpoint_path)

                # update the top 5 val losses:
                index = best_epoch_losses.index(min(best_epoch_losses))
                best_epoch_losses[index] = val_loss

            # plot the training loss vs epoch and save to disk:
            plt.figure(1)
            plt.plot(train_loss_per_epoch, "k^-")
            # plt.plot(train_loss_per_epoch, "k")
            plt.ylabel("loss")
            plt.xlabel("epoch")
            plt.title("training loss per epoch")
            plt.savefig("%s/train_loss_per_epoch.png" % audio_ckpt_dir)
            # plt.show()

            # plot the val loss vs epoch and save to disk:
            plt.figure(2)
            plt.plot(val_loss_per_epoch, "k^-")
            # plt.plot(val_loss_per_epoch, "k")
            plt.ylabel("loss")
            plt.xlabel("epoch")
            plt.title("validation loss per epoch")
            plt.savefig("%s/val_loss_per_epoch.png" % audio_ckpt_dir)
            # plt.show()

if __name__ == '__main__':
     tf.app.run()