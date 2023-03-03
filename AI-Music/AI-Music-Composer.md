# AI-Music-Composer

---

A project that trains a LSTM recurrent neural network over a data-set of MIDI files.

## Dependencies
Numpy (http://www.numpy.org/)

Tensorflow 0.8 (https://github.com/tensorflow/tensorflow) its best to uses virtual env to do this

virtual env (https://virtualenv.pypa.io/en/stable/)

Python Midi (https://github.com/vishnubob/python-midi.git)

Mingus (https://github.com/bspaans/python-mingus)

Matplotlib (https://github.com/matplotlib/matplotlib)

## How to use it?

1. `mkdir data && mkdir models`
2. run `python main.py`. This will collect the data, create the chord mapping file in data/nottingham.pickle, and train the model
3. Run `python rnn_sample.py --config_file new_config_file.config` to generate a new MIDI song.

Give it 1-2 hours to train on your local machine, then generate the new song. 
You don't have to wait for it to finish, just wait until you see the 'saving model' message in terminal. 
To increase speed you can use a cloud based GPU such as www.fomoro.com

## Credits

This is an adaptation of an idea from [Yoav Zimmerman](https://github.com/yoavz). The main use of this project is as a proof of concept for a RNN.
