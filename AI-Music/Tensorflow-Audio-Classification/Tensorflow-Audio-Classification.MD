# Audio Classification

---

Classify The Audios. In This Repo, I Train A Model On [UrbanSound8K][data-urban] Dataset,  
And Achieve About `80%` Accuracy On Test Dataset.

There Is A Pre-trained Model In [Urban_sound_train][i-ckpt], Trained Epoch Is `1000`

## Usage

- [`Audio_train.py`][i-train]: Train Audio Model From Scratch Or Restore From Checkpoint.
- [`Audio_params.py`][i-params]: Configuration For Training A Model.
- [`Audio_inference_demo.py`][i-demo]: Demo For Test The Trained Model.
- [`./Audio/*`][i-audio]: Dependencies Of Training, Model And Datasets.
- [`./Vggish/*`][i-vggish]: Dependencies Of [VGGish][tool-vggish] For Feature Extracting.

### Env Setup

Conda Are Recommended, Just Need One Line: `Conda Env Create -F Conda.env.yml`

### Train & Test

1. Config Parameters: `Audio_params.py`.
2. Train The Model: `Python Audio_train.py`. (It Will **Create Tfrecords Automatically** If Not Exists)
3. Check The Training Process From Tensorboard: `Tensorboard --Logdir=./data/tensorboard`
4. Test The Model: `Python Audio_inference_demo.py`.

### Tools

- [TensorFlow: VGGish][tool-vggish]
- [Google AudioSet][tool-as]
    - [VGGish Model Checkpoint][tool-as-ckpt]
    - [Embedding PCA Parameters][tool-as-pca]
- [PyAudioAnalysis][tool-pyaa](Ref.)

### Dataset

- [Urban Sound Dataset][data-urban]

### Ref. Blogs

- [AudioSet: An Ontology And Human-labelled Dataset For Audio Events][blog-as]
- [CNN Architectures For Large-Scale Audio Classification][blog-accnn]

[I-train]: ./Audio_train.py
[I-params]: ./Audio_params.py
[I-demo]: ./Audio_inference_demo.py
[I-audio]: ./Audio
[I-vggish]: ./Vggish
[I-ckpt]: ./Data/train/urban_sound_train
[Tool-vggish]: Https://github.com/tensorflow/models/tree/master/research/audioset
[Tool-pyaa]: Https://github.com/tyiannak/pyAudioAnalysis
[Tool-as]: Https://research.google.com/audioset/index.html
[Tool-as-ckpt]: Https://storage.googleapis.com/audioset/vggish_model.ckpt
[Tool-as-pca]: Https://storage.googleapis.com/audioset/vggish_pca_params.npz
[Data-urban]: Https://serv.cusp.nyu.edu/projects/urbansounddataset/urbansound8k.html
[Blog-as]: Https://research.google.com/pubs/pub45857.html
[Blog-accnn]: Https://research.google.com/pubs/pub45611.html

---