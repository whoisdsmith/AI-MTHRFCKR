# coding: utf-8
# author: luuil@outlook.com

r"""Global parameters for the audio model.

See audio_model.py for more information.
"""

from os.path import join as pjoin

# Training
AUDIO_TRAIN_NAME = 'urban_sound_train'  # train name
NUM_EPOCHS = 2000
BATCH_SIZE = 128
TENSORBOARD_DIR = './data/tensorboard'      # Tensorboard

# Path to UrbanSound8K
WAV_FILE_PARENT_DIR = '/data1/data/UrbanSound8K-16bit/audio-classfied'
NUM_VGGISH_FEATURE_PER_EXAMPLE = 1

# Architectural constants.
EMBEDDING_SIZE = 128 * NUM_VGGISH_FEATURE_PER_EXAMPLE # Size of embedding layer.
NUM_FEATURES = EMBEDDING_SIZE
NUM_CLASSES = 10


# Hyperparameters used in training.
INIT_STDDEV = 0.01      # Standard deviation used to initialize weights.
LEARNING_RATE = 1e-5    # Learning rate for the Adam optimizer.
ADAM_EPSILON = 1e-8     # Epsilon for the Adam optimizer.
NUM_UNITS = 10          # hidden units


# Names of ops, tensors, and features.
AUDIO_INPUT_OP_NAME = 'audio/vggish_input'
AUDIO_INPUT_TENSOR_NAME = AUDIO_INPUT_OP_NAME + ':0'
AUDIO_OUTPUT_OP_NAME = 'audio/prediction'
AUDIO_OUTPUT_TENSOR_NAME = AUDIO_OUTPUT_OP_NAME + ':0'


# Checkpoint
AUDIO_CHECKPOINT_DIR = './data/train'
AUDIO_CHECKPOINT_NAME = 'audio_urban_model.ckpt'
AUDIO_CHECKPOINT = pjoin(AUDIO_CHECKPOINT_DIR, AUDIO_TRAIN_NAME, AUDIO_CHECKPOINT_NAME)


# Records
AUDIO_FEATURE_NAME = 'feature'
AUDIO_LABEL_NAME = 'label'

TF_RECORDS_TRAIN_NAME = 'urban_sound_train.tfrecords'
TF_RECORDS_TEST_NAME = 'urban_sound_test.tfrecords'
TF_RECORDS_VAL_NAME = 'urban_sound_val.tfrecords'

TF_RECORDS_DIR = './data/records'
TF_RECORDS_TRAIN = pjoin(TF_RECORDS_DIR, TF_RECORDS_TRAIN_NAME)
TF_RECORDS_TEST = pjoin(TF_RECORDS_DIR, TF_RECORDS_TEST_NAME)
TF_RECORDS_VAL = pjoin(TF_RECORDS_DIR, TF_RECORDS_VAL_NAME)


# Vggish
VGGISH_CHECKPOINT_DIR = './data/vggish'
VGGISH_CHECKPOINT_NAME = 'vggish_model.ckpt'
VGGISH_PCA_PARAMS_NAME = 'vggish_pca_params.npz'
VGGISH_CHECKPOINT = pjoin(VGGISH_CHECKPOINT_DIR, VGGISH_CHECKPOINT_NAME)
VGGISH_PCA_PARAMS = pjoin(VGGISH_CHECKPOINT_DIR, VGGISH_PCA_PARAMS_NAME)

VGGISH_INPUT_OP_NAME = 'vggish/input_features'
VGGISH_INPUT_TENSOR_NAME = VGGISH_INPUT_OP_NAME + ':0'
VGGISH_OUTPUT_OP_NAME = 'vggish/embedding'
VGGISH_OUTPUT_TENSOR_NAME = VGGISH_OUTPUT_OP_NAME + ':0'