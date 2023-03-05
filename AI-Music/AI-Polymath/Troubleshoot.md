# Troubleshoot

```
tensorboard 2.9.1 has requirement setuptools>=41.0.0, but you'll have setuptools 39.0.1 which is incompatible.
Installing collected packages: urllib3, certifi, charset-normalizer, idna, requests, packaging, typing-extensions, platformdirs, pooch, numpy, soxr, scipy, threadpoolctl, joblib, scikit-learn, msgpack, decorator, pycparser, cffi, soundfile, audioread, llvmlite, zipp, importlib-metadata, numba, lazy-loader, librosa, future, six, mir-eval, mido, pretty-midi, resampy, keras-preprocessing, opt-einsum, libclang, google-pasta, wrapt, gast, protobuf, tensorflow-estimator, MarkupSafe, werkzeug, cachetools, pyasn1, rsa, pyasn1-modules, google-auth, oauthlib, requests-oauthlib, google-auth-oauthlib, wheel, absl-py, tensorboard-data-server, grpcio, markdown, tensorboard-plugin-wit, tensorboard, astunparse, h5py, tensorflow-io-gcs-filesystem, flatbuffers, keras, termcolor, tensorflow, basic-pitch

The script normalizer.exe is installed in 'c:\program files\python37\Scripts' which is not on PATH.
Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
The script f2py.exe is installed in 'c:\program files\python37\Scripts' which is not on PATH.Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Running setup.py install for soxr ... error
    Complete output from command "c:\program files\python37\python.exe" -u -c "import setuptools, tokenize;__file__='C:\\Users\\Ninja\\AppData\\Local\\Temp\\pip-install-zh8rrcon\\soxr\\setup.py';f=getattr(tokenize, 'open', open)(__file__);code=f.read().replace('\r\n', '\n');f.close();exec(compile(code, __file__, 'exec'))" install --record C:\Users\Ninja\AppData\Local\Temp\pip-record-9182dzrb\install-record.txt --single-version-externally-managed --compile:
    running install
    C:\Users\Ninja\AppData\Local\Temp\pip-build-env-pwoxluk8\Lib\site-packages\setuptools\command\install.py:37: SetuptoolsDeprecationWarning: setup.py install is deprecated. Use build and pip and other standards-based tools.
      setuptools.SetuptoolsDeprecationWarning,
    running build
    running build_py
    creating build
    creating build\lib.win-amd64-cpython-37
    creating build\lib.win-amd64-cpython-37\soxr
    copying src\soxr\version.py -> build\lib.win-amd64-cpython-37\soxr
    copying src\soxr\__init__.py -> build\lib.win-amd64-cpython-37\soxr
    running egg_info
    writing src\soxr.egg-info\PKG-INFO
    writing dependency_links to src\soxr.egg-info\dependency_links.txt
    writing requirements to src\soxr.egg-info\requires.txt
    writing top-level names to src\soxr.egg-info\top_level.txt
    listing git files failed - pretending there aren't any
    reading manifest file 'src\soxr.egg-info\SOURCES.txt'
    reading manifest template 'MANIFEST.in'
    warning: no files found matching 'src\soxr\*.pyd'
    warning: no previously-included files matching '__pycache__' found anywhere in distribution
    warning: no previously-included files matching '*.py[cod]' found anywhere in distribution
    warning: no previously-included files matching '.*' found anywhere in distribution
    adding license file 'LICENSE.txt'
    adding license file 'COPYING.LGPL'
    writing manifest file 'src\soxr.egg-info\SOURCES.txt'
    copying src\soxr\__init__.pxd -> build\lib.win-amd64-cpython-37\soxr
    copying src\soxr\csoxr.pxd -> build\lib.win-amd64-cpython-37\soxr
    copying src\soxr\cysoxr.c -> build\lib.win-amd64-cpython-37\soxr
    copying src\soxr\cysoxr.pyx -> build\lib.win-amd64-cpython-37\soxr
    copying src\soxr\soxr-config.h -> build\lib.win-amd64-cpython-37\soxr
    running build_ext
    building 'soxr.cysoxr' extension
    error: Microsoft Visual C++ 14.0 or greater is required. Get it with "Microsoft C++ Build Tools": https://visualstudio.microsoft.com/visual-cpp-build-tools/

    ----------------------------------------
Command ""c:\program files\python37\python.exe" -u -c "import setuptools, tokenize;__file__='C:\\Users\\Ninja\\AppData\\Local\\Temp\\pip-install-zh8rrcon\\soxr\\setup.py';f=getattr(tokenize, 'open', open)(__file__);code=f.read().replace('\r\n', '\n');f.close();exec(compile(code, __file__, 'exec'))" install --record C:\Users\Ninja\AppData\Local\Temp\pip-record-9182dzrb\install-record.txt --single-version-externally-managed --compile" failed with error code 1 in C:\Users\Ninja\AppData\Local\Temp\pip-install-zh8rrcon\soxr\
You are using pip version 10.0.1, however version 23.0.1 is available.
You should consider upgrading via the 'python -m pip install --upgrade pip' command.
```

python polymath.py -s db8ce9a06c6b5ec2cc40edcbc7c13570592c21a8bd9b100bb8934fa708fa445c -sa 10

```
2/8 pitch tracking
2023-03-03 17:34:07.301764: E tensorflow/stream_executor/cuda/cuda_driver.cc:271] failed call to cuInit: UNKNOWN ERROR (100)

2023-03-03 17:34:07.308243: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:169] retrieving CUDA diagnostic information for host: DESKTOP-WIN10

2023-03-03 17:34:07.309180: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:176] hostname: DESKTOP-WIN10

2023-03-03 17:34:07.315350: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX

To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.

1476/1476 [==============================] - 79s 53ms/step

3/8 load sample

4/8 sample separation

5/8 beat tracking

6/8 feature extraction

C:\Program Files\Python37\lib\site-packages\librosa\util\decorators.py:88: UserWarning: power_to_db was called on complex input so phase information will be discarded. To suppress this warning, call power_to_db(np.abs(D)**2) instead.
  return f(*args, **kwargs)
polymath.py:302: FutureWarning: Pass y=[0. 0. 0. ... 0. 0. 0.] as keyword args. From version 0.10 passing these as positional arguments will result in an error
  S = librosa.feature.melspectrogram(y, sr=sr, n_mels=128)


7/8 feature aggregation

8/8 split stems

Selected model is a bag of 1 models. You will see that many progress bars per track.

Separated tracks will be stored in C:\Users\Ninja\polymath\separated\htdemucs_6s

Separating track C:\Users\Ninja\polymath\library\a-letter-to-write_6efb86a5da47e3e7ad5c2a1242a080128b95e964f51f6efb22dce052c62df8af.wav
```

```
C:\Users\Ninja\polymath>python polymath.py -a C:/Users/Ninja/polymath/input/edited/
2023-03-03 17:31:42.963002: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'cudart64_110.dll'; dlerror: cudart64_110.dll not found
2023-03-03 17:31:42.963808: I tensorflow/stream_executor/cuda/cudart_stub.cc:29] Ignore above cudart dlerror if you do not have a GPU set up on your machine.
---------------------------------------------------------------------------- 
--------------------------------- POLYMATH --------------------------------- 
----------------------------------------------------------------------------
No Database file found: library/database.p
add video: C:/Users/Ninja/polymath/input/edited/ to videos: 0
add directory with wav or mp3 files
C:/Users/Ninja/polymath/input/edited/a-letter-to-write.mp3
C:/Users/Ninja/polymath/input/edited/cemeteries-and-greyhound-busses.mp3
C:/Users/Ninja/polymath/input/edited/diet-coke-and-mentos.mp3
C:/Users/Ninja/polymath/input/edited/goodbye-mr-perfection.mp3
C:/Users/Ninja/polymath/input/edited/our-perfect-ending.mp3
C:/Users/Ninja/polymath/input/edited/seven-days.mp3
C:/Users/Ninja/polymath/input/edited/the-great-escape.mp3
C:/Users/Ninja/polymath/input/edited/view-of-coma.mp3
C:/Users/Ninja/polymath/input/edited/when-open-air-becomes-a-battlefield.mp3
Found 9 wav or mp3 files
------ process audio C:/Users/Ninja/polymath/input/edited/a-letter-to-write.mp3
converting mp3 to wav: C:/Users/Ninja/polymath/input/edited/a-letter-to-write.mp3
C:\Program Files\Python37\lib\site-packages\librosa\util\decorators.py:88: UserWarning: PySoundFile failed. Trying audioread instead.
  return f(*args, **kwargs)
Finished procesing files: 1
------ process audio C:/Users/Ninja/polymath/input/edited/cemeteries-and-greyhound-busses.mp3
converting mp3 to wav: C:/Users/Ninja/polymath/input/edited/cemeteries-and-greyhound-busses.mp3
converting audio file to 44100: C:/Users/Ninja/polymath/input/edited/cemeteries-and-greyhound-busses.mp3
Finished procesing files: 2
------ process audio C:/Users/Ninja/polymath/input/edited/diet-coke-and-mentos.mp3
converting mp3 to wav: C:/Users/Ninja/polymath/input/edited/diet-coke-and-mentos.mp3
C:\Program Files\Python37\lib\site-packages\librosa\util\decorators.py:88: UserWarning: PySoundFile failed. Trying audioread instead.
  return f(*args, **kwargs)
Finished procesing files: 3
------ process audio C:/Users/Ninja/polymath/input/edited/goodbye-mr-perfection.mp3
converting mp3 to wav: C:/Users/Ninja/polymath/input/edited/goodbye-mr-perfection.mp3
Finished procesing files: 4
------ process audio C:/Users/Ninja/polymath/input/edited/our-perfect-ending.mp3
converting mp3 to wav: C:/Users/Ninja/polymath/input/edited/our-perfect-ending.mp3
Finished procesing files: 5
------ process audio C:/Users/Ninja/polymath/input/edited/seven-days.mp3
converting mp3 to wav: C:/Users/Ninja/polymath/input/edited/seven-days.mp3
Finished procesing files: 6
------ process audio C:/Users/Ninja/polymath/input/edited/the-great-escape.mp3
converting mp3 to wav: C:/Users/Ninja/polymath/input/edited/the-great-escape.mp3
Finished procesing files: 7
------ process audio C:/Users/Ninja/polymath/input/edited/view-of-coma.mp3
converting mp3 to wav: C:/Users/Ninja/polymath/input/edited/view-of-coma.mp3
Finished procesing files: 8
------ process audio C:/Users/Ninja/polymath/input/edited/when-open-air-becomes-a-battlefield.mp3
converting mp3 to wav: C:/Users/Ninja/polymath/input/edited/when-open-air-becomes-a-battlefield.mp3
converting audio file to 44100: C:/Users/Ninja/polymath/input/edited/when-open-air-becomes-a-battlefield.mp3
Finished procesing files: 9
------------------------------ Files in DB: 9 ------------------------------
is audio a-letter-to-write_6efb86a5da47e3e7ad5c2a1242a080128b95e964f51f6efb22dce052c62df8af a-letter-to-write C:\Users\Ninja\polymath\library\a-letter-to-write_6efb86a5da47e3e7ad5c2a1242a080128b95e964f51f6efb22dce052c62df8af.wav
------------------------------ get_audio_features: a-letter-to-write_6efb86a5da47e3e7ad5c2a1242a080128b95e964f51f6efb22dce052c62df8af ------------------------------
1/8 segementation

2/8 pitch tracking
2023-03-03 17:34:07.301764: E tensorflow/stream_executor/cuda/cuda_driver.cc:271] failed call to cuInit: UNKNOWN ERROR (100)
2023-03-03 17:34:07.308243: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:169] retrieving CUDA diagnostic information for host: DESKTOP-WIN10
2023-03-03 17:34:07.309180: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:176] hostname: DESKTOP-WIN10
2023-03-03 17:34:07.315350: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use to use the following CPU instructions in performance-critical operations:  AVX
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
1476/1476 [==============================] - 79s 53ms/step
3/8 load sample
4/8 sample separation
5/8 beat tracking
6/8 feature extraction                                                                                                                                                  To sup
C:\Program Files\Python37\lib\site-packages\librosa\util\decorators.py:88: UserWarning: power_to_db was called on complex input so phase information will be discarded. To suppress this warning, call power_to_db(np.abs(D)**2) instead.
  return f(*args, **kwargs)
polymath.py:302: FutureWarning: Pass y=[0. 0. 0. ... 0. 0. 0.] as keyword args. From version 0.10 passing these as positional arguments will result in an error        
  S = librosa.feature.melspectrogram(y, sr=sr, n_mels=128)
7/8 feature aggregation
8/8 split stems
Selected model is a bag of 1 models. You will see that many progress bars per track.
Separated tracks will be stored in C:\Users\Ninja\polymath\separated\htdemucs_6s
Separating track C:\Users\Ninja\polymath\library\a-letter-to-write_6efb86a5da47e3e7ad5c2a1242a080128b95e964f51f6efb22dce052c62df8af.wav
100%|██████████████████████████████████████████████| 473.84999999999997/473.84999999999997 [11:34<00:00,  1.47s/seconds]
a-letter-to-write_6efb86a5da47e3e7ad5c2a1242a080128b95e964f51f6efb22dce052c62df8af tempo 126.05 duration 472.14 timbre -7.86 pitch 0.35 intensity -40.98 segments 69 frequency 284.64 key C#4 name a-letter-to-write
is audio cemeteries-and-greyhound-busses_68ee27932a358f0da40bed24e2d3d6c366056decb74299c7702fa431cdb96ac2 cemeteries-and-greyhound-busses C:\Users\Ninja\polymath\library\cemeteries-and-greyhound-busses_68ee27932a358f0da40bed24e2d3d6c366056decb74299c7702fa431cdb96ac2.wav
------------------------------ get_audio_features: cemeteries-and-greyhound-busses_68ee27932a358f0da40bed24e2d3d6c366056decb74299c7702fa431cdb96ac2 ------------------------------
1/8 segementation

2/8 pitch tracking
1723/1723 [==============================] - 95s 55ms/step
3/8 load sample
4/8 sample separation
5/8 beat tracking
6/8 feature extraction
C:\Program Files\Python37\lib\site-packages\librosa\util\decorators.py:88: UserWarning: power_to_db was called on complex input so phase information will be discarded. To suppress this warning, call power_to_db(np.abs(D)**2) instead.
  return f(*args, **kwargs)
polymath.py:302: FutureWarning: Pass y=[-3.0517578e-05  0.0000000e+00 -3.0517578e-05 ...  0.0000000e+00
  0.0000000e+00  0.0000000e+00] as keyword args. From version 0.10 passing these as positional arguments will result in an error
  S = librosa.feature.melspectrogram(y, sr=sr, n_mels=128)
7/8 feature aggregation
8/8 split stems
Selected model is a bag of 1 models. You will see that many progress bars per track.
Separated tracks will be stored in C:\Users\Ninja\polymath\separated\htdemucs_6s
Separating track C:\Users\Ninja\polymath\library\cemeteries-and-greyhound-busses_68ee27932a358f0da40bed24e2d3d6c366056decb74299c7702fa431cdb96ac2.wav
100%|██████████████████████████████████████████████████████████████████████| 555.75/555.75 [14:15<00:00,  1.54s/seconds]
cemeteries-and-greyhound-busses_68ee27932a358f0da40bed24e2d3d6c366056decb74299c7702fa431cdb96ac2 tempo 136.0 duration 551.14 timbre -8.21 pitch 0.48 intensity -42.58 segments 68 frequency 254.92 key C4 name cemeteries-and-greyhound-busses
is audio diet-coke-and-mentos_2ebb90d50670d1153113d1314f640829bbeedfe9d0f35fd7bcf85ffc40c0a5cb diet-coke-and-mentos C:\Users\Ninja\polymath\library\diet-coke-and-mentos_2ebb90d50670d1153113d1314f640829bbeedfe9d0f35fd7bcf85ffc40c0a5cb.wav
------------------------------ get_audio_features: diet-coke-and-mentos_2ebb90d50670d1153113d1314f640829bbeedfe9d0f35fd7bcf85ffc40c0a5cb ------------------------------       
1/8 segementation

2/8 pitch tracking
1285/1285 [==============================] - 69s 54ms/step
3/8 load sample
4/8 sample separation
5/8 beat tracking
6/8 feature extraction
C:\Program Files\Python37\lib\site-packages\librosa\util\decorators.py:88: UserWarning: power_to_db was called on complex input so phase information will be discarded. To suppress this warning, call power_to_db(np.abs(D)**2) instead.
  return f(*args, **kwargs)
polymath.py:302: FutureWarning: Pass y=[0. 0. 0. ... 0. 0. 0.] as keyword args. From version 0.10 passing these as positional arguments will result in an error
  S = librosa.feature.melspectrogram(y, sr=sr, n_mels=128)
7/8 feature aggregation
8/8 split stems
Selected model is a bag of 1 models. You will see that many progress bars per track.
Separated tracks will be stored in C:\Users\Ninja\polymath\separated\htdemucs_6s
Separating track C:\Users\Ninja\polymath\library\diet-coke-and-mentos_2ebb90d50670d1153113d1314f640829bbeedfe9d0f35fd7bcf85ffc40c0a5cb.wav
100%|██████████████████████████████████████████████| 415.34999999999997/415.34999999999997 [09:53<00:00,  1.43s/seconds]
diet-coke-and-mentos_2ebb90d50670d1153113d1314f640829bbeedfe9d0f35fd7bcf85ffc40c0a5cb tempo 120.19 duration 411.12 timbre -8.31 pitch 0.4 intensity -40.68 segments 64 frequency 228.46 key A#3 name diet-coke-and-mentos
is audio goodbye-mr-perfection_4ee19add8d0df6ac261b132da0163d67f94c1fa4c5145a0211bfb53f30968b37 goodbye-mr-perfection C:\Users\Ninja\polymath\library\goodbye-mr-perfection_4ee19add8d0df6ac261b132da0163d67f94c1fa4c5145a0211bfb53f30968b37.wav
------------------------------ get_audio_features: goodbye-mr-perfection_4ee19add8d0df6ac261b132da0163d67f94c1fa4c5145a0211bfb53f30968b37 ------------------------------      

1/8 segementation
2/8 pitch tracking
1445/1445 [==============================] - 74s 51ms/step
3/8 load sample
4/8 sample separation
5/8 beat tracking
6/8 feature extraction
C:\Program Files\Python37\lib\site-packages\librosa\util\decorators.py:88: UserWarning: power_to_db was called on complex input so phase information will be discarded. To suppress this warning, call power_to_db(np.abs(D)**2) instead.
  return f(*args, **kwargs)
polymath.py:302: FutureWarning: Pass y=[0.         0.         0.         ... 0.00177002 0.00177002 0.00177002] as keyword args. From version 0.10 passing these as positional 
arguments will result in an error
  S = librosa.feature.melspectrogram(y, sr=sr, n_mels=128)
7/8 feature aggregation
8/8 split stems

Selected model is a bag of 1 models. You will see that many progress bars per track.
Separated tracks will be stored in C:\Users\Ninja\polymath\separated\htdemucs_6s
Separating track C:\Users\Ninja\polymath\library\goodbye-mr-perfection_4ee19add8d0df6ac261b132da0163d67f94c1fa4c5145a0211bfb53f30968b37.wav
100%|████████████████████████████████████████████████████████████████████████| 468.0/468.0 [11:03<00:00,  1.42s/seconds]
goodbye-mr-perfection_4ee19add8d0df6ac261b132da0163d67f94c1fa4c5145a0211bfb53f30968b37 tempo 143.55 duration 462.32 timbre -8.64 pitch 0.33 intensity -42.34 segments 68 frequency 263.09 key C4 name goodbye-mr-perfection
is audio our-perfect-ending_7b949ba5a05cbb5030e6961a073dfbe6aeaabf62d8b8913fa2ad3c0e68eead68 our-perfect-ending C:\Users\Ninja\polymath\library\our-perfect-ending_7b949ba5a05cbb5030e6961a073dfbe6aeaabf62d8b8913fa2ad3c0e68eead68.wav
------------------------------ get_audio_features: our-perfect-ending_7b949ba5a05cbb5030e6961a073dfbe6aeaabf62d8b8913fa2ad3c0e68eead68 ------------------------------

1/8 segementation
2/8 pitch tracking
1494/1494 [==============================] - 75s 50ms/step
3/8 load sample
4/8 sample separation
5/8 beat tracking
6/8 feature extraction
C:\Program Files\Python37\lib\site-packages\librosa\util\decorators.py:88: UserWarning: power_to_db was called on complex input so phase information will be discarded. To suppress this warning, call power_to_db(np.abs(D)**2) instead.
  return f(*args, **kwargs)
polymath.py:302: FutureWarning: Pass y=[0. 0. 0. ... 0. 0. 0.] as keyword args. From version 0.10 passing these as positional arguments will result in an error
  S = librosa.feature.melspectrogram(y, sr=sr, n_mels=128)
7/8 feature aggregation
8/8 split stems

Selected model is a bag of 1 models. You will see that many progress bars per track.
Separated tracks will be stored in C:\Users\Ninja\polymath\separated\htdemucs_6s
Separating track C:\Users\Ninja\polymath\library\our-perfect-ending_7b949ba5a05cbb5030e6961a073dfbe6aeaabf62d8b8913fa2ad3c0e68eead68.wav
100%|████████████████████████████████████████████████████████████████████████| 479.7/479.7 [11:10<00:00,  1.40s/seconds]
our-perfect-ending_7b949ba5a05cbb5030e6961a073dfbe6aeaabf62d8b8913fa2ad3c0e68eead68 tempo 139.67 duration 477.78 timbre -12.4 pitch 0.25 intensity -49.55 segments 76 frequency 235.66 key A#3 name our-perfect-ending
is audio seven-days_dfd68b93e298ca6eeeba645e3e7eda8755fe3fc2436554821adbdca5da57d167 seven-days C:\Users\Ninja\polymath\library\seven-days_dfd68b93e298ca6eeeba645e3e7eda8755fe3fc2436554821adbdca5da57d167.wav
------------------------------ get_audio_features: seven-days_dfd68b93e298ca6eeeba645e3e7eda8755fe3fc2436554821adbdca5da57d167 ------------------------------

1/8 segementation
2/8 pitch tracking
1158/1158 [==============================] - 61s 52ms/step
3/8 load sample
4/8 sample separation
5/8 beat tracking
6/8 feature extraction
C:\Program Files\Python37\lib\site-packages\librosa\util\decorators.py:88: UserWarning: power_to_db was called on complex input so phase information will be discarded. To suppress this warning, call power_to_db(np.abs(D)**2) instead.
  return f(*args, **kwargs)
polymath.py:302: FutureWarning: Pass y=[0. 0. 0. ... 0. 0. 0.] as keyword args. From version 0.10 passing these as positional arguments will result in an error
  S = librosa.feature.melspectrogram(y, sr=sr, n_mels=128)
7/8 feature aggregation
8/8 split stems

Selected model is a bag of 1 models. You will see that many progress bars per track.
Separated tracks will be stored in C:\Users\Ninja\polymath\separated\htdemucs_6s
Separating track C:\Users\Ninja\polymath\library\seven-days_dfd68b93e298ca6eeeba645e3e7eda8755fe3fc2436554821adbdca5da57d167.wav
100%|████████████████████████████████████████████████████████████████████████| 374.4/374.4 [10:54<00:00,  1.75s/seconds]

seven-days_dfd68b93e298ca6eeeba645e3e7eda8755fe3fc2436554821adbdca5da57d167 tempo 126.05 duration 370.31 timbre -7.79 pitch 0.44 intensity -38.7 segments 42 frequency 274.96 
key C#4 name seven-days
```

```
free-bones-type-beat-purple-trees-prod-seshtillirest-_05b2db8eff84808e0f1a44be508fa6027799143b62f576da0f5ad438e566618e tempo 120.19 duration 333.02 timbre -12.21 pitch 0.28 intensity -53.62 segments 57 frequency 317.79 key D#4 name free-bones-type-beat-purple-trees-prod-seshtillirest-
free-bones-x-lil-peep-type-beat-falling-asleep-prod-yago-g-m-g-m_ccf8a999b3cbe65745eedb25645954eaa1904365319462a04517d9f960104f6c tempo 120.19 duration 324.1 timbre -10.13 pitch 0.36 intensity -48.92 segments 40 frequency 238.82 key A#3 name free-bones-x-lil-peep-type-beat-falling-asleep-prod-yago-g-m-g-m
free-bones-x-lil-peep-x-greaf-type-beat-amazing-prod-seshtillirest-g-m-g-m_9285924f32bedae35254a1ae06c203f2b12067344bcb6ab46127b7ccc446af47 tempo 129.2 duration 360.23 timbre -13.32 pitch 0.38 intensity -60.22 segments 49 frequency 277.42 key C#4 name free-bones-x-lil-peep-x-greaf-type-beat-amazing-prod-seshtillirest-g-m-g-m  
free-capoxxo-x-syko-x-oaf1-hyperpop-type-beat-underworld-prod-pro-z-_8cef0bedf65434e7f1e76b5732a49708aae9881d3ee639e62418aa93cbda3e8f tempo 136.0 duration 249.47 timbre -10.13 pitch 0.45 intensity -47.49 segments 29 frequency 374.09 key F#4 name free-capoxxo-x-syko-x-oaf1-hyperpop-type-beat-underworld-prod-pro-z-
free-chill-x-sad-jhene-aiko-type-beat-rnb-instrumental-2019-early-in-the-morning-g-m-g-m_dd473358d39e95948044c7da1b151b88f3578396fa57cfc1557163a95f8a5a19 tempo 123.05 duration 533.03 timbre -14.65 pitch 0.36 intensity -62.15 segments 81 frequency 344.04 key F4 name free-chill-x-sad-jhene-aiko-type-beat-rnb-instrumental-2019-early-in-the-morning-g-m-g-m
free-digital-original-god-x-angst-x-hellasketchy-type-beat-prod-loopy-g-m-g-m_41580b40da8123f069aabaca336c36df04db53a77da64e1bdea9459a8b8d1b56 tempo 126.05 duration 310.13 timbre -9.97 pitch 0.35 intensity -53.63 segments 43 frequency 217.82 key A3 name free-digital-original-god-x-angst-x-hellasketchy-type-beat-prod-loopy-g-m-g-m
free-ecco2k-x-deadmau5-x-crystal-castles-type-beat-sangang_899d3c266e228c33a7d73b78ca6574c86de02e89586bf299b2b4c09058e2dab2 tempo 123.05 duration 420.02 timbre -11.69 pitch 0.31 intensity -46.31 segments 96 frequency 432.17 key A4 name free-ecco2k-x-deadmau5-x-crystal-castles-type-beat-sangang
free-for-profit-hatred-part-2-lil-peep-x-xxxtentacion-type-beat-g-m-g-m_e411e9feb0927f5747028f079f9ea09e9c75326f0e2e8de1ace48739f0e3aaef tempo 123.05 duration 385.67 timbre -11.75 pitch 0.34 intensity -55.37 segments 57 frequency 218.3 key A3 name free-for-profit-hatred-part-2-lil-peep-x-xxxtentacion-type-beat-g-m-g-m
free-for-profit-hyperpop-x-glitchcore-x-lxner-type-beat-synth-prod-soft-clipper-pn_65c44a347f1e5a7509dbd36ac4b1466baad77f4717126a917a0924fe28b66334 tempo 132.51 duration 290.3 timbre -11.46 pitch 0.39 intensity -55.12 segments 41 frequency 314.03 key D#4 name free-for-profit-hyperpop-x-glitchcore-x-lxner-type-beat-synth-prod-soft-clipper-pn
free-for-profit-open-ended-alternative-rock-type-beat_b195caeabdaf42fb1044359add520fd01378da6389e2b92ed057f96572cc76c5 tempo 132.51 duration 306.04 timbre -11.54 pitch 0.46 intensity -48.55 segments 38 frequency 206.14 key G#3 name free-for-profit-open-ended-alternative-rock-type-beat
free-for-profit-witt-lowry-hurt-type-beat-longing-g-m-g-m_0210ef59a8fa64a0092a73e2ee4606449a8e01e3377baebdb7e84888f852168a tempo 129.2 duration 429.03 timbre -12.44 pitch 0.32 intensity -61.69 segments 67 frequency 366.1 key F#4 name free-for-profit-witt-lowry-hurt-type-beat-longing-g-m-g-m
free-guilt-alt-rock-lil-peep-x-nothing-nowhere-type-beat-prod-loopy-g-m-g-m_b3bd210d80f777cc2bbfcb9a2ec6f50750cbc5408dadb0208a4e48abbc0ca83a tempo 114.84 duration 310.13 timbre -15.54 pitch 0.36 intensity -64.17 segments 62 frequency 238.62 key A#3 name free-guilt-alt-rock-lil-peep-x-nothing-nowhere-type-beat-prod-loopy-g-m-g-m
free-gunna-x-lil-baby-type-beat-at-sea-trap-instrumental-2020_e2605169cc469fadde84792b0ce0c1946a782d299bd63b1a677f9295da101807 tempo 129.2 duration 396.22 timbre -11.13 pitch 0.4 intensity -56.62 segments 56 frequency 404.79 key G#4 name free-gunna-x-lil-baby-type-beat-at-sea-trap-instrumental-2020
free-juice-wrld-x-iann-dior-type-beat-reality_a27f934e1119b3679217b05dcd417f1e5a3ad3c8c1b2e63ab1a94ba6055fe391 tempo 129.2 duration 331.36 timbre -11.78 pitch 0.29 
intensity -57.32 segments 48 frequency 223.58 key A3 name free-juice-wrld-x-iann-dior-type-beat-reality
free-juice-wrld-x-iann-dior-type-beat-reborn-trap-instrumental-2020_9fa29fe52fba614133eaa8f04e95e96e4d03edff52b53af9e2ce46c3f9fb9db7 tempo 129.2 duration 336.03 timbre -10.76 pitch 0.37 intensity -54.59 segments 42 frequency 96.5 key G2 name free-juice-wrld-x-iann-dior-type-beat-reborn-trap-instrumental-2020
free-lil-peep-x-coldhart-x-horse-head-x-wicca-phase-type-beat-mistakes-prod-metlastmp3-g-m-g-m_d9694fe1ae9068e9900d8fb76e988e647105f2310e0f4210b2bb1f556c21b53a tempo 120.19 duration 330.08 timbre -12.99 pitch 0.29 intensity -58.87 segments 60 frequency 287.71 key D4 name free-lil-peep-x-coldhart-x-horse-head-x-wicca-phase-type-beat-mistakes-prod-metlastmp3-g-m-g-m
free-lil-peep-x-horse-head-x-lil-lotus-x-smrtdeath-type-beat-midnight-prod-metlast-b-135-00_54224408ed8149b51e9e48844ebf11b7768fa44bf90a69a191fc2f92ed1df2ce tempo 136.0 duration 320.16 timbre -12.25 pitch 0.29 intensity -63.89 segments 48 frequency 103.17 key G#2 name free-lil-peep-x-horse-head-x-lil-lotus-x-smrtdeath-type-beat-midnight-prod-metlast-b-135-00
free-lil-peep-x-lil-tracy-type-beat-heart-hurt-sad-guitar-instrumental-2019-g-m-g-m_2731d94a8c1c5ef18f2739493c886e8f1c7112e05ee70d0d16d93c4cec258c7d tempo 136.0 duration 455.25 timbre -14.12 pitch 0.27 intensity -65.04 segments 64 frequency 185.31 key F#3 name free-lil-peep-x-lil-tracy-type-beat-heart-hurt-sad-guitar-instrumental-2019-g-m-g-m
free-mac-miller-x-j-cole-type-beat-mirrors-2020_b89ce2151bae8d1fce643482e9857d6c8b4a6a9940440dc2925349aae1f8e898 tempo 120.19 duration 404.02 timbre -14.07 pitch 0.48 intensity -63.87 segments 87 frequency 322.16 key E4 name free-mac-miller-x-j-cole-type-beat-mirrors-2020
free-metalcore-x-melodic-post-hardcore-type-beat-dark-horse-melodic-metalcore-instrumental_5ea9250320d2b426a89330e14901d0fee31315cb2da5954c3b450fbb5233a961 tempo 132.51 duration 268.04 timbre -7.72 pitch 0.45 intensity -43.94 segments 33 frequency 238.74 key A#3 name free-metalcore-x-melodic-post-hardcore-type-beat-dark-horse-melodic-metalcore-instrumental
free-no-friends-juice-wrld-x-lil-mosey-x-lil-skies-type-beat-2019-prod-kcaaz-g-m-g-m_0e450b7477e21b8c76723e0fc075a0f57a69bb5dcaff6978d170160ec641de6a tempo 136.0 duration 362.62 timbre -11.49 pitch 0.27 intensity -59.82 segments 39 frequency 127.33 key C3 name free-no-friends-juice-wrld-x-lil-mosey-x-lil-skies-type-beat-2019-prod-kcaaz-g-m-g-m
free-nothing-nowhere-tothegood-lil-lotus-type-beat-i-can-t-leave-yet-prod-remghost-_e93134232c6187318d35e7f57e15c494115ae47be35229b00e96f84925f32421 tempo 120.19 duration 288.59 timbre -10.49 pitch 0.25 intensity -58.26 segments 38 frequency 76.53 key D#2 name free-nothing-nowhere-tothegood-lil-lotus-type-beat-i-can-t-leave-yet-prod-remghost-
free-nothing-nowhere-x-family-pet-x-shinigami-type-beat-keep-it-together-prod-suttee-_d9192fd92c08baa0dbd71822763e21fb0167269181b701373557411cbf44f0c8 tempo 120.19 
duration 324.1 timbre -9.98 pitch 0.38 intensity -51.83 segments 66 frequency 231.54 key A#3 name free-nothing-nowhere-x-family-pet-x-shinigami-type-beat-keep-it-together-prod-suttee-
free-phora-ft-post-malone-type-beat-diamonds-instrumental-2019-g-m-g-m_f20887d1167fb52b61004b77f148bfc2a9ef5800962cf9824ba11aa7061ad9be tempo 114.84 duration 474.12 timbre -14.12 pitch 0.28 intensity -67.4 segments 56 frequency 215.45 key A3 name free-phora-ft-post-malone-type-beat-diamonds-instrumental-2019-g-m-g-m
free-pnb-rock-x-lil-tjay-type-beat-2019-broke-me-prod-midlowbeats-g-m-g-m_dc8662cbb9ca2d845b37b026bfe324c2eba3dbc7ad713ae7fe02b1e1a144feae tempo 129.2 duration 480.22 timbre -10.89 pitch 0.27 intensity -61.51 segments 65 frequency 117.69 key A#2 name free-pnb-rock-x-lil-tjay-type-beat-2019-broke-me-prod-midlowbeats-g-m-g-m    
free-pop-punk-emo-scenecore-type-beat-almost-had-u-pn_feb7e9b184fddb4e920e4f3bd8adb91e9c1442cdf39d938798f405a19ab0941d tempo 129.2 duration 390.14 timbre -8.03 pitch 0.39 intensity -40.23 segments 57 frequency 249.77 key B3 name free-pop-punk-emo-scenecore-type-beat-almost-had-u-pn
free-pop-rock-mgk-x-jxdn-x-iann-dior-pop-punk-type-beat-still-here_73cf7504165037f75db1090e9b55f02e19b6809137fa825b11cacb915bec980f tempo 126.05 duration 372.59 timbre -8.58 pitch 0.45 intensity -49.6 segments 56 frequency 77.03 key D#2 name free-pop-rock-mgk-x-jxdn-x-iann-dior-pop-punk-type-beat-still-here
free-post-malone-guitar-type-beat-apologize-pop-instrumental-2019_a55e6f0ce28d3bcdcbfc31e8f1722a5b6aded62d0817ad43cb32c89f514a6e03 tempo 117.45 duration 460.09 timbre -12.14 pitch 0.24 intensity -63.71 segments 55 frequency 178.87 key F3 name free-post-malone-guitar-type-beat-apologize-pop-instrumental-2019
free-sad-chill-jazzy-type-beat-emma-prod-noria-beats-_e96d131ae2d8290b5f031c1702ea00c9fa6ed169e52103fa551e5e1151c45651 tempo 136.0 duration 458.64 timbre -12.81 pitch 0.29 intensity -63.12 segments 95 frequency 136.79 key C#3 name free-sad-chill-jazzy-type-beat-emma-prod-noria-beats-
free-sad-chill-lofi-type-beat-emotional-deep-piano-trap-2019-_15b9aac06093456ebc5dd245b46b270facf18d890e979bed55b6c17c2cfdb85f tempo 126.05 duration 434.17 timbre -13.58 pitch 0.26 intensity -66.62 segments 65 frequency 234.29 key A#3 name free-sad-chill-lofi-type-beat-emotional-deep-piano-trap-2019-
free-sad-guitar-xxxtentacion-x-lil-peep-type-beat-lakes-pn_ac78d876ffba367a63ff8196f326808ec1d40627ee25d5e229195b9704abe055 tempo 123.05 duration 567.31 timbre -12.0 pitch 0.24 intensity -56.68 segments 119 frequency 360.9 key F#4 name free-sad-guitar-xxxtentacion-x-lil-peep-type-beat-lakes-pn
free-sad-xxxtentacion-type-beat-fly-prod-xenshel-_3c8a2bcd3e39526ad308f4cf2b47acf16e7162a3180d85e15cd02b58cd482030 tempo 120.19 duration 212.15 timbre -10.41 pitch 
0.25 intensity -57.41 segments 31 frequency 227.17 key A#3 name free-sad-xxxtentacion-type-beat-fly-prod-xenshel-
free-scenecore-x-rave-x-hyperpop-type-beat-opals-prod-pro-z-_19431a48572226ddda07c68015a73371f08d41990ff56b919bd9698706a4f0ab tempo 136.0 duration 249.74 timbre -9.1 pitch 0.63 intensity -47.35 segments 41 frequency 318.81 key D#4 name free-scenecore-x-rave-x-hyperpop-type-beat-opals-prod-pro-z-
free-scenecore-x-rave-x-hyperpop-type-beat-unseen-forces-prod-pro-z-_fa186c820758c9380592cd777cfc69cabdcfe29018ad27702745cce1518a43c5 tempo 136.0 duration 239.53 timbre -9.31 pitch 0.53 intensity -46.55 segments 40 frequency 133.58 key C3 name free-scenecore-x-rave-x-hyperpop-type-beat-unseen-forces-prod-pro-z-
free-uicideboy-x-pouya-type-beat-other-body-prod-eykey-beats-x-phil-good-beats-g-m-g-m-g-m_46e33e55c61ca5f35dacef7d6b31136abff4d1f13842e83c8aa878bfc1c3b926 tempo 132.51 duration 294.67 timbre -8.97 pitch 0.31 intensity -50.94 segments 46 frequency 241.73 key B3 name free-uicideboy-x-pouya-type-beat-other-body-prod-eykey-beats-x-phil-good-beats-g-m-g-m-g-m
free-whitearmor-x-crystal-castles-x-thaiboy-digital-type-beat_9a4ac66e722140b5f910dc21e89eb63c9e756f82cb0bac3085ab80b4778eb990 tempo 129.2 duration 410.05 timbre -13.41 pitch 0.34 intensity -54.66 segments 56 frequency 267.09 key C4 name free-whitearmor-x-crystal-castles-x-thaiboy-digital-type-beat
free-witt-lowry-x-nf-type-beat-memories-hip-hop-rap-instrumental-2020-g-m-g-m-130-00_4b3907809b803b57b80b67fb80b24b6a14661199213d32c7acd91e0fd7dd58de tempo 129.2 duration 473.93 timbre -11.41 pitch 0.36 intensity -56.9 segments 74 frequency 81.64 key E2 name free-witt-lowry-x-nf-type-beat-memories-hip-hop-rap-instrumental-2020-g-m-g-m-130-00
free-xxxtentacion-type-beat-forever-emotional-sad-piano-rap-beat-2019_081bb9eb5de563a60d7bef01c36feed5758c200f5cac66dfbd5d70a88ecf4a2c tempo 129.2 duration 400.13 timbre -12.65 pitch 0.34 intensity -58.9 segments 75 frequency 393.56 key G4 name free-xxxtentacion-type-beat-forever-emotional-sad-piano-rap-beat-2019
free-xxxtentacion-x-lil-peep-type-beat-im-sorry-sad-guitar-instrumental-2019-g-m-g-m_cd260a84f796f76fff33e8911934cc6e4eaa7ec0d3bd0b890cb7e043e1832558 tempo 129.2 duration 343.37 timbre -10.5 pitch 0.39 intensity -57.59 segments 59 frequency 183.32 key F#3 name free-xxxtentacion-x-lil-peep-type-beat-im-sorry-sad-guitar-instrumental-2019-g-m-g-m
free-xxxtentacion-x-nf-type-beat-wishes-sad-rap-piano-instrumental-2019-g-m-g-m_55f306c8a95ac4bf7d90739449f0e27d31456cf4c696d4f3d9f4cb26798615cc tempo 126.05 duration 432.07 timbre -11.64 pitch 0.33 intensity -56.3 segments 93 frequency 156.68 key D#3 name free-xxxtentacion-x-nf-type-beat-wishes-sad-rap-piano-instrumental-2019-g-m-g-m
g-m-g-m-116-00_0789686c6614391ebb58d0b524b1cb472f2c81f6dd70bec447e319949638f173 tempo 114.84 duration 240.78 timbre -12.16 pitch 0.27 intensity -58.4 segments 47 frequency 175.32 key F3 name g-m-g-m-116-00
guccihighwaters-9tails-convolk-guardin-shinigami-lil-lotus-type-beat-sad-guitar_fee4136b71f10588c595e9d6c830637de01a5cf8359db292121112b2b4a0eabe tempo 129.2 duration 483.02 timbre -10.87 pitch 0.35 intensity -53.7 segments 82 frequency 304.4 key D#4 name guccihighwaters-9tails-convolk-guardin-shinigami-lil-lotus-type-beat-sad-guitar
gunner-prod-fantom-_e6b23d20b29b923d9951a3cdf006217003a9ab22d80cc18642db66581669bfe2 tempo 123.05 duration 302.79 timbre -10.2 pitch 0.39 intensity -57.58 segments 
30 frequency 70.31 key C#2 name gunner-prod-fantom-
hot-mulligan-tiny-moving-parts_b56d4e39828c3a73916074523c34b69a0bb9ae4d53630cd9d6893b42bb2b9914 tempo 123.05 duration 288.48 timbre -8.27 pitch 0.35 intensity -44.24 segments 49 frequency 212.55 key G#3 name hot-mulligan-tiny-moving-parts
i-miss-you-free-nf-x-ivan-b-type-beat-emotional-sad-instrumental-prod-starbeats-2019-g-m-g-m-125-00_f877bc649cb0a304f03fdbb965137b29b6844a5b5ed3abb68d7303f3c4722b09 tempo 126.05 duration 537.69 timbre -9.48 pitch 0.3 intensity -55.5 segments 81 frequency 153.23 key D#3 name i-miss-you-free-nf-x-ivan-b-type-beat-emotional-sad-instrumental-prod-starbeats-2019-g-m-g-m-125-00
i-miss-you-g-m-g-m_5888aa4efe963eca2694d28723c6ae2e2c7639caa3f842c2495eef85f0a9cf35 tempo 120.19 duration 357.28 timbre -12.12 pitch 0.3 intensity -54.9 segments 62 frequency 280.86 key C#4 name i-miss-you-g-m-g-m
ill-faded-prod-bassment-_b0b27b0cccae442b0f0f3bb13f3d8871c79210a8a2b4e590f544ce2079cf9a2d tempo 126.05 duration 320.16 timbre -12.08 pitch 0.39 intensity -56.05 segments 42 frequency 242.89 key B3 name ill-faded-prod-bassment-
illusions-soft-chill-rap-instrumental-atmospheric-trap-beat-2019-g-m-g-m_664a1b256bcd2f461d7d5b23526a696a2c7c46fdae2a24f93f67a3b2032bec3b tempo 136.0 duration 384.1 timbre -9.34 pitch 0.37 intensity -53.89 segments 54 frequency 72.87 key D2 name illusions-soft-chill-rap-instrumental-atmospheric-trap-beat-2019-g-m-g-m
is-love-bones-x-teamsesh-type-beat-prod-rareflowermp3-g-m-g-m_0936412db01ae4b1593bd0697ebf723552125152e2a10f4948c5cf0e9454584e tempo 129.2 duration 580.08 timbre -11.54 pitch 0.37 intensity -49.64 segments 76 frequency 241.86 key B3 name is-love-bones-x-teamsesh-type-beat-prod-rareflowermp3-g-m-g-m
ivan-b-x-witt-lowry-type-beat-shedding-my-tears-deep-storytelling-g-m-g-m_5e1ed52eff0e50d680e44d1d245c0ff3b873e75a0d0a319f9f21dfec3245a0ea tempo 126.05 duration 354.47 timbre -11.19 pitch 0.29 intensity -61.02 segments 58 frequency 142.89 key D3 name ivan-b-x-witt-lowry-type-beat-shedding-my-tears-deep-storytelling-g-m-g-m    
kevin-gates-x-future-type-beat-hate-me-iii-prod-by-mb13beatz-g-m-g-m_773c9df75276ea13fe03ba957fce3d360a5b802f7ec86191dfc3cb22560ab661 tempo 129.2 duration 540.04 timbre -12.12 pitch 0.29 intensity -57.73 segments 92 frequency 204.95 key G#3 name kevin-gates-x-future-type-beat-hate-me-iii-prod-by-mb13beatz-g-m-g-m
letter-2-the-weeknd_4d59a21756d8f88cbac9b330b347d1ca3abb2b05d67521108de4219f963a8dc4 tempo 126.05 duration 430.08 timbre -10.52 pitch 0.59 intensity -49.02 segments 54 frequency 245.85 key B3 name letter-2-the-weeknd
lipstick-prod-qb-trap-beat-for-singing_e38cbaabd562f84239d27034c28d10a1acea66f5a60c7b6ebd897dfeb1f48c5c tempo 132.51 duration 480.1 timbre -13.05 pitch 0.26 intensity -62.08 segments 69 frequency 99.02 key G2 name lipstick-prod-qb-trap-beat-for-singing
midwest-emo-type-beat_41e4cee0420bf1becfc09770dc95a4f2c6007f0cc768ec8dfd189c0419f36604 tempo 136.0 duration 406.08 timbre -11.64 pitch 0.27 intensity -59.74 segments 52 frequency 224.0 key A3 name midwest-emo-type-beat
new-year-prod-metlast-_2e06a190d773f0c2a8e1667f92969bcf0718cca2070c920a32b4bf0080107ff7 tempo 120.19 duration 288.25 timbre -11.9 pitch 0.28 intensity -60.38 segments 29 frequency 349.82 key F4 name new-year-prod-metlast-
nineteen_39d06763a0ff50d8553eba900b60c5ecc4a2f70b12083b98f546bccbcdbf333e tempo 136.0 duration 287.1 timbre -15.67 pitch 0.36 intensity -61.77 segments 33 frequency 256.04 key C4 name nineteen
nothing-nowhere-fats-e-iann-dior_259e5911ddd61c3faae1860d1bc8daaf97416ea805700edfbf6418823ea47227 tempo 136.0 duration 474.19 timbre -9.63 pitch 0.25 intensity -55.03 segments 63 frequency 121.45 key B2 name nothing-nowhere-fats-e-iann-dior
numb-g-m-g-m_185b1083d3ae30b7a0c539dc7dc7e5e20da4c5d9b11ce9a1b12ad8001c75d2b0 tempo 123.05 duration 504.12 timbre -12.14 pitch 0.31 intensity -57.66 segments 77 frequency 133.59 key C3 name numb-g-m-g-m
prod-capsctrl-silo-g-m-g-m_6c71eb80c1a8700ccd0ba117217e77c80fd2ee0007b470ffb9a71d23b729bbd8 tempo 120.19 duration 392.11 timbre -11.48 pitch 0.31 intensity -57.48 segments 63 frequency 268.18 key C4 name prod-capsctrl-silo-g-m-g-m
rain_cbf08b90a080cdec19295a666cf18eae5c913d88725e6cc9e76ed09a65766bfb tempo 129.2 duration 391.72 timbre -12.63 pitch 0.29 intensity -60.26 segments 61 frequency 77.21 key D#2 name rain
raptrap-beat-trapnew-school-instrumental-2019-prod-kyu-tracks-g-m-g-m_d2c06ebe76db5e6d0b6d02bda5a8a5ada73358d53ed3d4bb633358274fca67e6 tempo 126.05 duration 373.25 
timbre -9.86 pitch 0.27 intensity -53.4 segments 57 frequency 268.98 key C4 name raptrap-beat-trapnew-school-instrumental-2019-prod-kyu-tracks-g-m-g-m
ripsquad-x-nosgov-x-senses-x-bladee-type-beat-prod-ev333-_b3b015df97d837ef4b834c089d9b8e3545b360ba5c80e12214fc6756fe2ae739 tempo 123.05 duration 300.05 timbre -12.36 pitch 0.3 intensity -54.6 segments 46 frequency 457.15 key A#4 name ripsquad-x-nosgov-x-senses-x-bladee-type-beat-prod-ev333-
sad-ambient-piano-type-beat-piece-320-kbps-_643ca8237d17a55c06dad6aaaccd50882e348efa95cf88c1f049f8ffbafa20a6 tempo 120.19 duration 427.73 timbre -13.91 pitch 0.36 intensity -64.23 segments 69 frequency 281.38 key C#4 name sad-ambient-piano-type-beat-piece-320-kbps-
save-me-sad-piano-instrumental-2019_0f27a2faccd6dc111a74522a22572edebd975c726a23e8946ddd88d09d2a504d tempo 136.0 duration 427.34 timbre -12.84 pitch 0.3 intensity -60.38 segments 109 frequency 307.66 key D#4 name save-me-sad-piano-instrumental-2019
sold-dark-xxxtentacion-x-denzel-curry-type-beat-plague-trap-intrumental-2020_ed7882cdee3d26fe38ad55cac61ea079cd945c01484b0bf7918382fc6a857318 tempo 129.2 duration 304.08 timbre -10.23 pitch 0.44 intensity -54.77 segments 35 frequency 341.02 key F4 name sold-dark-xxxtentacion-x-denzel-curry-type-beat-plague-trap-intrumental-2020
sold-xxxtentacion-sad-lofi-type-beat-scars-ft-mishaal-g-m-g-m_e054b3218482c95fffbc2cc8c53c0c7a7f48fa4782c77393d3c0215800e67c55 tempo 120.19 duration 309.81 timbre -13.55 pitch 0.32 intensity -56.13 segments 43 frequency 285.71 key D4 name sold-xxxtentacion-sad-lofi-type-beat-scars-ft-mishaal-g-m-g-m
synth_d5637fa2aa32345a3792c1fa7c357cb31c2dd0e6b447340a5950c41b5dbd2b19 tempo 132.51 duration 290.19 timbre -11.68 pitch 0.4 intensity -56.12 segments 36 frequency 305.53 key D#4 name synth
time-free-nf-type-beat-emotional-sad-piano-instrumental-2019-prod-starbeats-g-m-g-m-g-m-135-00_da1fcece5188a3427a800a8a0191b14d2f67699293db80c5ea6b4e0c6f15f2f8 tempo 136.0 duration 551.19 timbre -11.44 pitch 0.43 intensity -54.57 segments 81 frequency 270.33 key C#4 name time-free-nf-type-beat-emotional-sad-piano-instrumental-2019-prod-starbeats-g-m-g-m-g-m-135-00
waifu_ca3105d05ff8fada0dbcd0a695cc40f8b2d3900175bf28c4a1cf75e8f95f17b1 tempo 126.05 duration 262.75 timbre -8.86 pitch 0.36 intensity -45.87 segments 45 frequency 187.13 key F#3 name waifu
zen_e88e86af4b2e47a4ea4e6d6a5f95455bc6b0acae99e117f644977ba71dac8bd2 tempo 114.84 duration 271.52 timbre -11.19 pitch 0.3 intensity -58.57 segments 60 frequency 173.46 key F3 name zen
--------------------------------------------------------------------------

C:\Users\Ninja\polymath>python polymath.py -a C:/Users/Ninja/polymath/input/coma/
2023-03-04 14:39:46.380482: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'cudart64_110.dll'; dlerror: cudart64_110.dll not found
2023-03-04 14:39:46.381614: I tensorflow/stream_executor/cuda/cudart_stub.cc:29] Ignore above cudart dlerror if you do not have a GPU set up on your machine.
---------------------------------------------------------------------------- 
--------------------------------- POLYMATH --------------------------------- 
----------------------------------------------------------------------------
add video: C:/Users/Ninja/polymath/input/coma/ to videos: 94
add directory with wav or mp3 files
Found 0 wav or mp3 files
------------------------------ Files in DB: 94 ------------------------------
a-letter-to-write_6efb86a5da47e3e7ad5c2a1242a080128b95e964f51f6efb22dce052c62df8af tempo 126.05 duration 472.14 timbre -7.86 pitch 0.35 intensity -40.98 segments 69 frequency 284.64 key C#4 name a-letter-to-write
cemeteries-and-greyhound-busses_68ee27932a358f0da40bed24e2d3d6c366056decb74299c7702fa431cdb96ac2 tempo 136.0 duration 551.14 timbre -8.21 pitch 0.48 intensity -42.58 segments 68 frequency 254.92 key C4 name cemeteries-and-greyhound-busses
diet-coke-and-mentos_2ebb90d50670d1153113d1314f640829bbeedfe9d0f35fd7bcf85ffc40c0a5cb tempo 120.19 duration 411.12 timbre -8.31 pitch 0.4 intensity -40.68 segments 
64 frequency 228.46 key A#3 name diet-coke-and-mentos
goodbye-mr-perfection_4ee19add8d0df6ac261b132da0163d67f94c1fa4c5145a0211bfb53f30968b37 tempo 143.55 duration 462.32 timbre -8.64 pitch 0.33 intensity -42.34 segments 68 frequency 263.09 key C4 name goodbye-mr-perfection
our-perfect-ending_7b949ba5a05cbb5030e6961a073dfbe6aeaabf62d8b8913fa2ad3c0e68eead68 tempo 139.67 duration 477.78 timbre -12.4 pitch 0.25 intensity -49.55 segments 76 frequency 235.66 key A#3 name our-perfect-ending
seven-days_dfd68b93e298ca6eeeba645e3e7eda8755fe3fc2436554821adbdca5da57d167 tempo 126.05 duration 370.31 timbre -7.79 pitch 0.44 intensity -38.7 segments 42 frequency 274.96 key C#4 name seven-days
the-great-escape_5f14bbc778ab78ebe0adff825fa96d0ea01c3385df3b5fdefce6ba8d3c15dec2 tempo 117.45 duration 416.97 timbre -7.65 pitch 0.41 intensity -42.24 segments 60 
frequency 258.09 key C4 name the-great-escape
view-of-coma_79fc23932086e9530542150c47857bb03b65b11d1fd7c455e2dd238eca100cfa tempo 107.67 duration 445.91 timbre -8.21 pitch 0.43 intensity -42.77 segments 64 frequency 222.6 key A3 name view-of-coma
when-open-air-becomes-a-battlefield_f922c336e1eefdb69496e4a2fb030652728be6ad7c99bc34be4d5a09960ffc11 tempo 152.0 duration 386.21 timbre -7.9 pitch 0.44 intensity -38.7 segments 45 frequency 293.47 key D4 name when-open-air-becomes-a-battlefield
100-free-xxxtentacion-type-beat-angel-raptrap-instrumental_b20fc5ffacc2737c7880e3ba9b79c3c74d82195151c93482c31169890ed1d330 tempo 120.19 duration 361.04 timbre -14.53 pitch 0.44 intensity -58.9 segments 50 frequency 334.44 key E4 name 100-free-xxxtentacion-type-beat-angel-raptrap-instrumental
130-01_f1c3e675d845fe1f825a670fbcfcf8810a504890da960574b434cca88e094104 tempo 129.2 duration 458.26 timbre -12.01 pitch 0.22 intensity -59.66 segments 66 frequency 
233.78 key A#3 name 130-01
be-yourself_37ad5163700b7faa927526b2e48a11b76835c4a5776a6664cb086f2bb33d5009 tempo 114.84 duration 496.87 timbre -8.2 pitch 0.39 intensity -46.33 segments 76 frequency 263.74 key C4 name be-yourself
breathe_c3916db375d4e9b22565ae65367646472770dcce0b494c92b26aa82d453511ce tempo 126.05 duration 390.02 timbre -9.68 pitch 0.42 intensity -50.33 segments 67 frequency 207.7 key G#3 name breathe
cold-trap-beat-instrumental-trap-type-beat-prod-by-gherah-g-m-g-m_a3737d5654ccd679e6407db611d58bd2aeeab6101bce49a870159d103e7a1355 tempo 120.19 duration 360.97 timbre -11.72 pitch 0.27 intensity -54.64 segments 39 frequency 662.82 key E5 name cold-trap-beat-instrumental-trap-type-beat-prod-by-gherah-g-m-g-m
diabla-trap-beat-emotional-bryant-mayers-mike-beatz-g-m-g-m_78ddf057fea8a69b45bb5b56cf9d978d6613722fcb1b2072f5b60b7edf9bfbbd tempo 86.13 duration 346.01 timbre -10.99 pitch 0.28 intensity -56.76 segments 48 frequency 215.0 key A3 name diabla-trap-beat-emotional-bryant-mayers-mike-beatz-g-m-g-m
disaster_590e25b9f3eb4ef3102e0f7e5887237886296dc6a162670b20b21ddbff983bdc tempo 132.51 duration 315.36 timbre -11.24 pitch 0.29 intensity -57.96 segments 45 frequency 153.13 key D#3 name disaster
drops_41baa90392281d60931ae009a0b2ad5727288707e94fab59c75033e04f1b8d61 tempo 120.19 duration 180.48 timbre -13.47 pitch 0.35 intensity -54.55 segments 29 frequency 
298.6 key D4 name drops
ea7-sad-lofi-piano-type-beat-320-kbps-_3e3261c31899b53111fdf6a38dc9a41163ad61948281f9e32c75887f3686ba28 tempo 129.2 duration 405.94 timbre -11.69 pitch 0.43 intensity -60.82 segments 55 frequency 186.59 key F#3 name ea7-sad-lofi-piano-type-beat-320-kbps-
enough_641750e90ad696c3c7da3ac8a6eb3c925e459b75a05cf4550ae81e11abeae479 tempo 132.51 duration 269.02 timbre -12.25 pitch 0.3 intensity -52.89 segments 46 frequency 
285.66 key D4 name enough
free-6lack-type-beat-piano-ambient-instrumental-no-connection-2019-g-m-g-m_ceaf5ecaa0314b5c6edf4b28829041dcfba2b05cb4ffdcc92b8f7f6f4ecd82c9 tempo 114.84 duration 432.39 timbre -13.62 pitch 0.25 intensity -59.58 segments 73 frequency 209.21 key G#3 name free-6lack-type-beat-piano-ambient-instrumental-no-connection-2019-g-m-g-m 
free-alternative-rock-type-beat-prod-useless-320-kbps-g-m-g-m_1121fdde50d6f160892868bc4f7894f240ce5ddbfb726cab9461d8b2db3bddb6 tempo 129.2 duration 295.73 timbre -10.47 pitch 0.31 intensity -52.05 segments 44 frequency 276.59 key C#4 name free-alternative-rock-type-beat-prod-useless-320-kbps-g-m-g-m
free-balcony-bones-x-6dogs-type-beat-prod-bleach-g-m-g-m_eb64a24bbaf033d57b0dfa05f80fd6b6fac24fc5b3a1715cb526cc3d857b071c tempo 136.0 duration 263.5 timbre -11.82 pitch 0.27 intensity -61.12 segments 29 frequency 177.36 key F3 name free-balcony-bones-x-6dogs-type-beat-prod-bleach-g-m-g-m
free-bladee-x-capoxxo-hyperpop-type-beat-redo-prod-pro-z-_faaa4050e487ad959a070f4dc25652223c920901d0c704cd5566f54de2bb7f86 tempo 129.2 duration 236.6 timbre -12.31 
pitch 0.26 intensity -57.95 segments 25 frequency 243.59 key B3 name free-bladee-x-capoxxo-hyperpop-type-beat-redo-prod-pro-z-
free-bones-type-beat-ashes-prod-ojhi_a3fdf5f3c06d1df2ae42b84f1cca986b5f98333897f183c5f2cb59118f69ecf7 tempo 129.2 duration 358.09 timbre -13.71 pitch 0.35 intensity -56.7 segments 50 frequency 508.62 key C5 name free-bones-type-beat-ashes-prod-ojhi
free-bones-type-beat-purple-trees-prod-seshtillirest-_05b2db8eff84808e0f1a44be508fa6027799143b62f576da0f5ad438e566618e tempo 120.19 duration 333.02 timbre -12.21 pitch 0.28 intensity -53.62 segments 57 frequency 317.79 key D#4 name free-bones-type-beat-purple-trees-prod-seshtillirest-
free-bones-x-lil-peep-type-beat-falling-asleep-prod-yago-g-m-g-m_ccf8a999b3cbe65745eedb25645954eaa1904365319462a04517d9f960104f6c tempo 120.19 duration 324.1 timbre -10.13 pitch 0.36 intensity -48.92 segments 40 frequency 238.82 key A#3 name free-bones-x-lil-peep-type-beat-falling-asleep-prod-yago-g-m-g-m
free-bones-x-lil-peep-x-greaf-type-beat-amazing-prod-seshtillirest-g-m-g-m_9285924f32bedae35254a1ae06c203f2b12067344bcb6ab46127b7ccc446af47 tempo 129.2 duration 360.23 timbre -13.32 pitch 0.38 intensity -60.22 segments 49 frequency 277.42 key C#4 name free-bones-x-lil-peep-x-greaf-type-beat-amazing-prod-seshtillirest-g-m-g-m  
free-capoxxo-x-syko-x-oaf1-hyperpop-type-beat-underworld-prod-pro-z-_8cef0bedf65434e7f1e76b5732a49708aae9881d3ee639e62418aa93cbda3e8f tempo 136.0 duration 249.47 timbre -10.13 pitch 0.45 intensity -47.49 segments 29 frequency 374.09 key F#4 name free-capoxxo-x-syko-x-oaf1-hyperpop-type-beat-underworld-prod-pro-z-
free-chill-x-sad-jhene-aiko-type-beat-rnb-instrumental-2019-early-in-the-morning-g-m-g-m_dd473358d39e95948044c7da1b151b88f3578396fa57cfc1557163a95f8a5a19 tempo 123.05 duration 533.03 timbre -14.65 pitch 0.36 intensity -62.15 segments 81 frequency 344.04 key F4 name free-chill-x-sad-jhene-aiko-type-beat-rnb-instrumental-2019-early-in-the-morning-g-m-g-m
free-digital-original-god-x-angst-x-hellasketchy-type-beat-prod-loopy-g-m-g-m_41580b40da8123f069aabaca336c36df04db53a77da64e1bdea9459a8b8d1b56 tempo 126.05 duration 310.13 timbre -9.97 pitch 0.35 intensity -53.63 segments 43 frequency 217.82 key A3 name free-digital-original-god-x-angst-x-hellasketchy-type-beat-prod-loopy-g-m-g-m
free-ecco2k-x-deadmau5-x-crystal-castles-type-beat-sangang_899d3c266e228c33a7d73b78ca6574c86de02e89586bf299b2b4c09058e2dab2 tempo 123.05 duration 420.02 timbre -11.69 pitch 0.31 intensity -46.31 segments 96 frequency 432.17 key A4 name free-ecco2k-x-deadmau5-x-crystal-castles-type-beat-sangang
free-for-profit-hatred-part-2-lil-peep-x-xxxtentacion-type-beat-g-m-g-m_e411e9feb0927f5747028f079f9ea09e9c75326f0e2e8de1ace48739f0e3aaef tempo 123.05 duration 385.67 timbre -11.75 pitch 0.34 intensity -55.37 segments 57 frequency 218.3 key A3 name free-for-profit-hatred-part-2-lil-peep-x-xxxtentacion-type-beat-g-m-g-m
free-for-profit-hyperpop-x-glitchcore-x-lxner-type-beat-synth-prod-soft-clipper-pn_65c44a347f1e5a7509dbd36ac4b1466baad77f4717126a917a0924fe28b66334 tempo 132.51 duration 290.3 timbre -11.46 pitch 0.39 intensity -55.12 segments 41 frequency 314.03 key D#4 name free-for-profit-hyperpop-x-glitchcore-x-lxner-type-beat-synth-prod-soft-clipper-pn
free-for-profit-open-ended-alternative-rock-type-beat_b195caeabdaf42fb1044359add520fd01378da6389e2b92ed057f96572cc76c5 tempo 132.51 duration 306.04 timbre -11.54 pitch 0.46 intensity -48.55 segments 38 frequency 206.14 key G#3 name free-for-profit-open-ended-alternative-rock-type-beat
free-for-profit-witt-lowry-hurt-type-beat-longing-g-m-g-m_0210ef59a8fa64a0092a73e2ee4606449a8e01e3377baebdb7e84888f852168a tempo 129.2 duration 429.03 timbre -12.44 pitch 0.32 intensity -61.69 segments 67 frequency 366.1 key F#4 name free-for-profit-witt-lowry-hurt-type-beat-longing-g-m-g-m
free-guilt-alt-rock-lil-peep-x-nothing-nowhere-type-beat-prod-loopy-g-m-g-m_b3bd210d80f777cc2bbfcb9a2ec6f50750cbc5408dadb0208a4e48abbc0ca83a tempo 114.84 duration 310.13 timbre -15.54 pitch 0.36 intensity -64.17 segments 62 frequency 238.62 key A#3 name free-guilt-alt-rock-lil-peep-x-nothing-nowhere-type-beat-prod-loopy-g-m-g-m
free-gunna-x-lil-baby-type-beat-at-sea-trap-instrumental-2020_e2605169cc469fadde84792b0ce0c1946a782d299bd63b1a677f9295da101807 tempo 129.2 duration 396.22 timbre -11.13 pitch 0.4 intensity -56.62 segments 56 frequency 404.79 key G#4 name free-gunna-x-lil-baby-type-beat-at-sea-trap-instrumental-2020
free-juice-wrld-x-iann-dior-type-beat-reality_a27f934e1119b3679217b05dcd417f1e5a3ad3c8c1b2e63ab1a94ba6055fe391 tempo 129.2 duration 331.36 timbre -11.78 pitch 0.29 
intensity -57.32 segments 48 frequency 223.58 key A3 name free-juice-wrld-x-iann-dior-type-beat-reality
free-juice-wrld-x-iann-dior-type-beat-reborn-trap-instrumental-2020_9fa29fe52fba614133eaa8f04e95e96e4d03edff52b53af9e2ce46c3f9fb9db7 tempo 129.2 duration 336.03 timbre -10.76 pitch 0.37 intensity -54.59 segments 42 frequency 96.5 key G2 name free-juice-wrld-x-iann-dior-type-beat-reborn-trap-instrumental-2020
free-lil-peep-x-coldhart-x-horse-head-x-wicca-phase-type-beat-mistakes-prod-metlastmp3-g-m-g-m_d9694fe1ae9068e9900d8fb76e988e647105f2310e0f4210b2bb1f556c21b53a tempo 120.19 duration 330.08 timbre -12.99 pitch 0.29 intensity -58.87 segments 60 frequency 287.71 key D4 name free-lil-peep-x-coldhart-x-horse-head-x-wicca-phase-type-beat-mistakes-prod-metlastmp3-g-m-g-m
free-lil-peep-x-horse-head-x-lil-lotus-x-smrtdeath-type-beat-midnight-prod-metlast-b-135-00_54224408ed8149b51e9e48844ebf11b7768fa44bf90a69a191fc2f92ed1df2ce tempo 136.0 duration 320.16 timbre -12.25 pitch 0.29 intensity -63.89 segments 48 frequency 103.17 key G#2 name free-lil-peep-x-horse-head-x-lil-lotus-x-smrtdeath-type-beat-midnight-prod-metlast-b-135-00
free-lil-peep-x-lil-tracy-type-beat-heart-hurt-sad-guitar-instrumental-2019-g-m-g-m_2731d94a8c1c5ef18f2739493c886e8f1c7112e05ee70d0d16d93c4cec258c7d tempo 136.0 duration 455.25 timbre -14.12 pitch 0.27 intensity -65.04 segments 64 frequency 185.31 key F#3 name free-lil-peep-x-lil-tracy-type-beat-heart-hurt-sad-guitar-instrumental-2019-g-m-g-m
free-mac-miller-x-j-cole-type-beat-mirrors-2020_b89ce2151bae8d1fce643482e9857d6c8b4a6a9940440dc2925349aae1f8e898 tempo 120.19 duration 404.02 timbre -14.07 pitch 0.48 intensity -63.87 segments 87 frequency 322.16 key E4 name free-mac-miller-x-j-cole-type-beat-mirrors-2020
free-metalcore-x-melodic-post-hardcore-type-beat-dark-horse-melodic-metalcore-instrumental_5ea9250320d2b426a89330e14901d0fee31315cb2da5954c3b450fbb5233a961 tempo 132.51 duration 268.04 timbre -7.72 pitch 0.45 intensity -43.94 segments 33 frequency 238.74 key A#3 name free-metalcore-x-melodic-post-hardcore-type-beat-dark-horse-melodic-metalcore-instrumental
free-no-friends-juice-wrld-x-lil-mosey-x-lil-skies-type-beat-2019-prod-kcaaz-g-m-g-m_0e450b7477e21b8c76723e0fc075a0f57a69bb5dcaff6978d170160ec641de6a tempo 136.0 duration 362.62 timbre -11.49 pitch 0.27 intensity -59.82 segments 39 frequency 127.33 key C3 name free-no-friends-juice-wrld-x-lil-mosey-x-lil-skies-type-beat-2019-prod-kcaaz-g-m-g-m
free-nothing-nowhere-tothegood-lil-lotus-type-beat-i-can-t-leave-yet-prod-remghost-_e93134232c6187318d35e7f57e15c494115ae47be35229b00e96f84925f32421 tempo 120.19 duration 288.59 timbre -10.49 pitch 0.25 intensity -58.26 segments 38 frequency 76.53 key D#2 name free-nothing-nowhere-tothegood-lil-lotus-type-beat-i-can-t-leave-yet-prod-remghost-
free-nothing-nowhere-x-family-pet-x-shinigami-type-beat-keep-it-together-prod-suttee-_d9192fd92c08baa0dbd71822763e21fb0167269181b701373557411cbf44f0c8 tempo 120.19 
duration 324.1 timbre -9.98 pitch 0.38 intensity -51.83 segments 66 frequency 231.54 key A#3 name free-nothing-nowhere-x-family-pet-x-shinigami-type-beat-keep-it-together-prod-suttee-
free-phora-ft-post-malone-type-beat-diamonds-instrumental-2019-g-m-g-m_f20887d1167fb52b61004b77f148bfc2a9ef5800962cf9824ba11aa7061ad9be tempo 114.84 duration 474.12 timbre -14.12 pitch 0.28 intensity -67.4 segments 56 frequency 215.45 key A3 name free-phora-ft-post-malone-type-beat-diamonds-instrumental-2019-g-m-g-m
free-pnb-rock-x-lil-tjay-type-beat-2019-broke-me-prod-midlowbeats-g-m-g-m_dc8662cbb9ca2d845b37b026bfe324c2eba3dbc7ad713ae7fe02b1e1a144feae tempo 129.2 duration 480.22 timbre -10.89 pitch 0.27 intensity -61.51 segments 65 frequency 117.69 key A#2 name free-pnb-rock-x-lil-tjay-type-beat-2019-broke-me-prod-midlowbeats-g-m-g-m    
free-pop-punk-emo-scenecore-type-beat-almost-had-u-pn_feb7e9b184fddb4e920e4f3bd8adb91e9c1442cdf39d938798f405a19ab0941d tempo 129.2 duration 390.14 timbre -8.03 pitch 0.39 intensity -40.23 segments 57 frequency 249.77 key B3 name free-pop-punk-emo-scenecore-type-beat-almost-had-u-pn
free-pop-rock-mgk-x-jxdn-x-iann-dior-pop-punk-type-beat-still-here_73cf7504165037f75db1090e9b55f02e19b6809137fa825b11cacb915bec980f tempo 126.05 duration 372.59 timbre -8.58 pitch 0.45 intensity -49.6 segments 56 frequency 77.03 key D#2 name free-pop-rock-mgk-x-jxdn-x-iann-dior-pop-punk-type-beat-still-here
free-post-malone-guitar-type-beat-apologize-pop-instrumental-2019_a55e6f0ce28d3bcdcbfc31e8f1722a5b6aded62d0817ad43cb32c89f514a6e03 tempo 117.45 duration 460.09 timbre -12.14 pitch 0.24 intensity -63.71 segments 55 frequency 178.87 key F3 name free-post-malone-guitar-type-beat-apologize-pop-instrumental-2019
free-sad-chill-jazzy-type-beat-emma-prod-noria-beats-_e96d131ae2d8290b5f031c1702ea00c9fa6ed169e52103fa551e5e1151c45651 tempo 136.0 duration 458.64 timbre -12.81 pitch 0.29 intensity -63.12 segments 95 frequency 136.79 key C#3 name free-sad-chill-jazzy-type-beat-emma-prod-noria-beats-
free-sad-chill-lofi-type-beat-emotional-deep-piano-trap-2019-_15b9aac06093456ebc5dd245b46b270facf18d890e979bed55b6c17c2cfdb85f tempo 126.05 duration 434.17 timbre -13.58 pitch 0.26 intensity -66.62 segments 65 frequency 234.29 key A#3 name free-sad-chill-lofi-type-beat-emotional-deep-piano-trap-2019-
free-sad-guitar-xxxtentacion-x-lil-peep-type-beat-lakes-pn_ac78d876ffba367a63ff8196f326808ec1d40627ee25d5e229195b9704abe055 tempo 123.05 duration 567.31 timbre -12.0 pitch 0.24 intensity -56.68 segments 119 frequency 360.9 key F#4 name free-sad-guitar-xxxtentacion-x-lil-peep-type-beat-lakes-pn
free-sad-xxxtentacion-type-beat-fly-prod-xenshel-_3c8a2bcd3e39526ad308f4cf2b47acf16e7162a3180d85e15cd02b58cd482030 tempo 120.19 duration 212.15 timbre -10.41 pitch 
0.25 intensity -57.41 segments 31 frequency 227.17 key A#3 name free-sad-xxxtentacion-type-beat-fly-prod-xenshel-
free-scenecore-x-rave-x-hyperpop-type-beat-opals-prod-pro-z-_19431a48572226ddda07c68015a73371f08d41990ff56b919bd9698706a4f0ab tempo 136.0 duration 249.74 timbre -9.1 pitch 0.63 intensity -47.35 segments 41 frequency 318.81 key D#4 name free-scenecore-x-rave-x-hyperpop-type-beat-opals-prod-pro-z-
free-scenecore-x-rave-x-hyperpop-type-beat-unseen-forces-prod-pro-z-_fa186c820758c9380592cd777cfc69cabdcfe29018ad27702745cce1518a43c5 tempo 136.0 duration 239.53 timbre -9.31 pitch 0.53 intensity -46.55 segments 40 frequency 133.58 key C3 name free-scenecore-x-rave-x-hyperpop-type-beat-unseen-forces-prod-pro-z-
free-uicideboy-x-pouya-type-beat-other-body-prod-eykey-beats-x-phil-good-beats-g-m-g-m-g-m_46e33e55c61ca5f35dacef7d6b31136abff4d1f13842e83c8aa878bfc1c3b926 tempo 132.51 duration 294.67 timbre -8.97 pitch 0.31 intensity -50.94 segments 46 frequency 241.73 key B3 name free-uicideboy-x-pouya-type-beat-other-body-prod-eykey-beats-x-phil-good-beats-g-m-g-m-g-m
free-whitearmor-x-crystal-castles-x-thaiboy-digital-type-beat_9a4ac66e722140b5f910dc21e89eb63c9e756f82cb0bac3085ab80b4778eb990 tempo 129.2 duration 410.05 timbre -13.41 pitch 0.34 intensity -54.66 segments 56 frequency 267.09 key C4 name free-whitearmor-x-crystal-castles-x-thaiboy-digital-type-beat
free-witt-lowry-x-nf-type-beat-memories-hip-hop-rap-instrumental-2020-g-m-g-m-130-00_4b3907809b803b57b80b67fb80b24b6a14661199213d32c7acd91e0fd7dd58de tempo 129.2 duration 473.93 timbre -11.41 pitch 0.36 intensity -56.9 segments 74 frequency 81.64 key E2 name free-witt-lowry-x-nf-type-beat-memories-hip-hop-rap-instrumental-2020-g-m-g-m-130-00
free-xxxtentacion-type-beat-forever-emotional-sad-piano-rap-beat-2019_081bb9eb5de563a60d7bef01c36feed5758c200f5cac66dfbd5d70a88ecf4a2c tempo 129.2 duration 400.13 timbre -12.65 pitch 0.34 intensity -58.9 segments 75 frequency 393.56 key G4 name free-xxxtentacion-type-beat-forever-emotional-sad-piano-rap-beat-2019
free-xxxtentacion-x-lil-peep-type-beat-im-sorry-sad-guitar-instrumental-2019-g-m-g-m_cd260a84f796f76fff33e8911934cc6e4eaa7ec0d3bd0b890cb7e043e1832558 tempo 129.2 duration 343.37 timbre -10.5 pitch 0.39 intensity -57.59 segments 59 frequency 183.32 key F#3 name free-xxxtentacion-x-lil-peep-type-beat-im-sorry-sad-guitar-instrumental-2019-g-m-g-m
free-xxxtentacion-x-nf-type-beat-wishes-sad-rap-piano-instrumental-2019-g-m-g-m_55f306c8a95ac4bf7d90739449f0e27d31456cf4c696d4f3d9f4cb26798615cc tempo 126.05 duration 432.07 timbre -11.64 pitch 0.33 intensity -56.3 segments 93 frequency 156.68 key D#3 name free-xxxtentacion-x-nf-type-beat-wishes-sad-rap-piano-instrumental-2019-g-m-g-m
g-m-g-m-116-00_0789686c6614391ebb58d0b524b1cb472f2c81f6dd70bec447e319949638f173 tempo 114.84 duration 240.78 timbre -12.16 pitch 0.27 intensity -58.4 segments 47 frequency 175.32 key F3 name g-m-g-m-116-00
guccihighwaters-9tails-convolk-guardin-shinigami-lil-lotus-type-beat-sad-guitar_fee4136b71f10588c595e9d6c830637de01a5cf8359db292121112b2b4a0eabe tempo 129.2 duration 483.02 timbre -10.87 pitch 0.35 intensity -53.7 segments 82 frequency 304.4 key D#4 name guccihighwaters-9tails-convolk-guardin-shinigami-lil-lotus-type-beat-sad-guitar
gunner-prod-fantom-_e6b23d20b29b923d9951a3cdf006217003a9ab22d80cc18642db66581669bfe2 tempo 123.05 duration 302.79 timbre -10.2 pitch 0.39 intensity -57.58 segments 
30 frequency 70.31 key C#2 name gunner-prod-fantom-
hot-mulligan-tiny-moving-parts_b56d4e39828c3a73916074523c34b69a0bb9ae4d53630cd9d6893b42bb2b9914 tempo 123.05 duration 288.48 timbre -8.27 pitch 0.35 intensity -44.24 segments 49 frequency 212.55 key G#3 name hot-mulligan-tiny-moving-parts
i-miss-you-free-nf-x-ivan-b-type-beat-emotional-sad-instrumental-prod-starbeats-2019-g-m-g-m-125-00_f877bc649cb0a304f03fdbb965137b29b6844a5b5ed3abb68d7303f3c4722b09 tempo 126.05 duration 537.69 timbre -9.48 pitch 0.3 intensity -55.5 segments 81 frequency 153.23 key D#3 name i-miss-you-free-nf-x-ivan-b-type-beat-emotional-sad-instrumental-prod-starbeats-2019-g-m-g-m-125-00
i-miss-you-g-m-g-m_5888aa4efe963eca2694d28723c6ae2e2c7639caa3f842c2495eef85f0a9cf35 tempo 120.19 duration 357.28 timbre -12.12 pitch 0.3 intensity -54.9 segments 62 frequency 280.86 key C#4 name i-miss-you-g-m-g-m
ill-faded-prod-bassment-_b0b27b0cccae442b0f0f3bb13f3d8871c79210a8a2b4e590f544ce2079cf9a2d tempo 126.05 duration 320.16 timbre -12.08 pitch 0.39 intensity -56.05 segments 42 frequency 242.89 key B3 name ill-faded-prod-bassment-
illusions-soft-chill-rap-instrumental-atmospheric-trap-beat-2019-g-m-g-m_664a1b256bcd2f461d7d5b23526a696a2c7c46fdae2a24f93f67a3b2032bec3b tempo 136.0 duration 384.1 timbre -9.34 pitch 0.37 intensity -53.89 segments 54 frequency 72.87 key D2 name illusions-soft-chill-rap-instrumental-atmospheric-trap-beat-2019-g-m-g-m
is-love-bones-x-teamsesh-type-beat-prod-rareflowermp3-g-m-g-m_0936412db01ae4b1593bd0697ebf723552125152e2a10f4948c5cf0e9454584e tempo 129.2 duration 580.08 timbre -11.54 pitch 0.37 intensity -49.64 segments 76 frequency 241.86 key B3 name is-love-bones-x-teamsesh-type-beat-prod-rareflowermp3-g-m-g-m
ivan-b-x-witt-lowry-type-beat-shedding-my-tears-deep-storytelling-g-m-g-m_5e1ed52eff0e50d680e44d1d245c0ff3b873e75a0d0a319f9f21dfec3245a0ea tempo 126.05 duration 354.47 timbre -11.19 pitch 0.29 intensity -61.02 segments 58 frequency 142.89 key D3 name ivan-b-x-witt-lowry-type-beat-shedding-my-tears-deep-storytelling-g-m-g-m    
kevin-gates-x-future-type-beat-hate-me-iii-prod-by-mb13beatz-g-m-g-m_773c9df75276ea13fe03ba957fce3d360a5b802f7ec86191dfc3cb22560ab661 tempo 129.2 duration 540.04 timbre -12.12 pitch 0.29 intensity -57.73 segments 92 frequency 204.95 key G#3 name kevin-gates-x-future-type-beat-hate-me-iii-prod-by-mb13beatz-g-m-g-m
letter-2-the-weeknd_4d59a21756d8f88cbac9b330b347d1ca3abb2b05d67521108de4219f963a8dc4 tempo 126.05 duration 430.08 timbre -10.52 pitch 0.59 intensity -49.02 segments 54 frequency 245.85 key B3 name letter-2-the-weeknd
lipstick-prod-qb-trap-beat-for-singing_e38cbaabd562f84239d27034c28d10a1acea66f5a60c7b6ebd897dfeb1f48c5c tempo 132.51 duration 480.1 timbre -13.05 pitch 0.26 intensity -62.08 segments 69 frequency 99.02 key G2 name lipstick-prod-qb-trap-beat-for-singing
midwest-emo-type-beat_41e4cee0420bf1becfc09770dc95a4f2c6007f0cc768ec8dfd189c0419f36604 tempo 136.0 duration 406.08 timbre -11.64 pitch 0.27 intensity -59.74 segments 52 frequency 224.0 key A3 name midwest-emo-type-beat
new-year-prod-metlast-_2e06a190d773f0c2a8e1667f92969bcf0718cca2070c920a32b4bf0080107ff7 tempo 120.19 duration 288.25 timbre -11.9 pitch 0.28 intensity -60.38 segments 29 frequency 349.82 key F4 name new-year-prod-metlast-
nineteen_39d06763a0ff50d8553eba900b60c5ecc4a2f70b12083b98f546bccbcdbf333e tempo 136.0 duration 287.1 timbre -15.67 pitch 0.36 intensity -61.77 segments 33 frequency 256.04 key C4 name nineteen
nothing-nowhere-fats-e-iann-dior_259e5911ddd61c3faae1860d1bc8daaf97416ea805700edfbf6418823ea47227 tempo 136.0 duration 474.19 timbre -9.63 pitch 0.25 intensity -55.03 segments 63 frequency 121.45 key B2 name nothing-nowhere-fats-e-iann-dior
numb-g-m-g-m_185b1083d3ae30b7a0c539dc7dc7e5e20da4c5d9b11ce9a1b12ad8001c75d2b0 tempo 123.05 duration 504.12 timbre -12.14 pitch 0.31 intensity -57.66 segments 77 frequency 133.59 key C3 name numb-g-m-g-m
prod-capsctrl-silo-g-m-g-m_6c71eb80c1a8700ccd0ba117217e77c80fd2ee0007b470ffb9a71d23b729bbd8 tempo 120.19 duration 392.11 timbre -11.48 pitch 0.31 intensity -57.48 segments 63 frequency 268.18 key C4 name prod-capsctrl-silo-g-m-g-m
rain_cbf08b90a080cdec19295a666cf18eae5c913d88725e6cc9e76ed09a65766bfb tempo 129.2 duration 391.72 timbre -12.63 pitch 0.29 intensity -60.26 segments 61 frequency 77.21 key D#2 name rain
raptrap-beat-trapnew-school-instrumental-2019-prod-kyu-tracks-g-m-g-m_d2c06ebe76db5e6d0b6d02bda5a8a5ada73358d53ed3d4bb633358274fca67e6 tempo 126.05 duration 373.25 
timbre -9.86 pitch 0.27 intensity -53.4 segments 57 frequency 268.98 key C4 name raptrap-beat-trapnew-school-instrumental-2019-prod-kyu-tracks-g-m-g-m
ripsquad-x-nosgov-x-senses-x-bladee-type-beat-prod-ev333-_b3b015df97d837ef4b834c089d9b8e3545b360ba5c80e12214fc6756fe2ae739 tempo 123.05 duration 300.05 timbre -12.36 pitch 0.3 intensity -54.6 segments 46 frequency 457.15 key A#4 name ripsquad-x-nosgov-x-senses-x-bladee-type-beat-prod-ev333-
sad-ambient-piano-type-beat-piece-320-kbps-_643ca8237d17a55c06dad6aaaccd50882e348efa95cf88c1f049f8ffbafa20a6 tempo 120.19 duration 427.73 timbre -13.91 pitch 0.36 intensity -64.23 segments 69 frequency 281.38 key C#4 name sad-ambient-piano-type-beat-piece-320-kbps-
save-me-sad-piano-instrumental-2019_0f27a2faccd6dc111a74522a22572edebd975c726a23e8946ddd88d09d2a504d tempo 136.0 duration 427.34 timbre -12.84 pitch 0.3 intensity -60.38 segments 109 frequency 307.66 key D#4 name save-me-sad-piano-instrumental-2019
sold-dark-xxxtentacion-x-denzel-curry-type-beat-plague-trap-intrumental-2020_ed7882cdee3d26fe38ad55cac61ea079cd945c01484b0bf7918382fc6a857318 tempo 129.2 duration 304.08 timbre -10.23 pitch 0.44 intensity -54.77 segments 35 frequency 341.02 key F4 name sold-dark-xxxtentacion-x-denzel-curry-type-beat-plague-trap-intrumental-2020
sold-xxxtentacion-sad-lofi-type-beat-scars-ft-mishaal-g-m-g-m_e054b3218482c95fffbc2cc8c53c0c7a7f48fa4782c77393d3c0215800e67c55 tempo 120.19 duration 309.81 timbre -13.55 pitch 0.32 intensity -56.13 segments 43 frequency 285.71 key D4 name sold-xxxtentacion-sad-lofi-type-beat-scars-ft-mishaal-g-m-g-m
synth_d5637fa2aa32345a3792c1fa7c357cb31c2dd0e6b447340a5950c41b5dbd2b19 tempo 132.51 duration 290.19 timbre -11.68 pitch 0.4 intensity -56.12 segments 36 frequency 305.53 key D#4 name synth
time-free-nf-type-beat-emotional-sad-piano-instrumental-2019-prod-starbeats-g-m-g-m-g-m-135-00_da1fcece5188a3427a800a8a0191b14d2f67699293db80c5ea6b4e0c6f15f2f8 tempo 136.0 duration 551.19 timbre -11.44 pitch 0.43 intensity -54.57 segments 81 frequency 270.33 key C#4 name time-free-nf-type-beat-emotional-sad-piano-instrumental-2019-prod-starbeats-g-m-g-m-g-m-135-00
waifu_ca3105d05ff8fada0dbcd0a695cc40f8b2d3900175bf28c4a1cf75e8f95f17b1 tempo 126.05 duration 262.75 timbre -8.86 pitch 0.36 intensity -45.87 segments 45 frequency 187.13 key F#3 name waifu
zen_e88e86af4b2e47a4ea4e6d6a5f95455bc6b0acae99e117f644977ba71dac8bd2 tempo 114.84 duration 271.52 timbre -11.19 pitch 0.3 intensity -58.57 segments 60 frequency 173.46 key F3 name zen
--------------------------------------------------------------------------

C:\Users\Ninja\polymath>python polymath.py -a C:/Users/Ninja/polymath/input/gmp/ 
2023-03-04 14:40:28.181691: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'cudart64_110.dll'; dlerror: cudart64_110.dll not found
2023-03-04 14:40:28.182582: I tensorflow/stream_executor/cuda/cudart_stub.cc:29] Ignore above cudart dlerror if you do not have a GPU set up on your machine.
---------------------------------------------------------------------------- 
--------------------------------- POLYMATH --------------------------------- 
----------------------------------------------------------------------------
add video: C:/Users/Ninja/polymath/input/gmp/ to videos: 94
add directory with wav or mp3 files
Found 0 wav or mp3 files
------------------------------ Files in DB: 94 ------------------------------
a-letter-to-write_6efb86a5da47e3e7ad5c2a1242a080128b95e964f51f6efb22dce052c62df8af tempo 126.05 duration 472.14 timbre -7.86 pitch 0.35 intensity -40.98 segments 69 frequency 284.64 key C#4 name a-letter-to-write
cemeteries-and-greyhound-busses_68ee27932a358f0da40bed24e2d3d6c366056decb74299c7702fa431cdb96ac2 tempo 136.0 duration 551.14 timbre -8.21 pitch 0.48 intensity -42.58 segments 68 frequency 254.92 key C4 name cemeteries-and-greyhound-busses
diet-coke-and-mentos_2ebb90d50670d1153113d1314f640829bbeedfe9d0f35fd7bcf85ffc40c0a5cb tempo 120.19 duration 411.12 timbre -8.31 pitch 0.4 intensity -40.68 segments 
64 frequency 228.46 key A#3 name diet-coke-and-mentos
goodbye-mr-perfection_4ee19add8d0df6ac261b132da0163d67f94c1fa4c5145a0211bfb53f30968b37 tempo 143.55 duration 462.32 timbre -8.64 pitch 0.33 intensity -42.34 segments 68 frequency 263.09 key C4 name goodbye-mr-perfection
our-perfect-ending_7b949ba5a05cbb5030e6961a073dfbe6aeaabf62d8b8913fa2ad3c0e68eead68 tempo 139.67 duration 477.78 timbre -12.4 pitch 0.25 intensity -49.55 segments 76 frequency 235.66 key A#3 name our-perfect-ending
seven-days_dfd68b93e298ca6eeeba645e3e7eda8755fe3fc2436554821adbdca5da57d167 tempo 126.05 duration 370.31 timbre -7.79 pitch 0.44 intensity -38.7 segments 42 frequency 274.96 key C#4 name seven-days
the-great-escape_5f14bbc778ab78ebe0adff825fa96d0ea01c3385df3b5fdefce6ba8d3c15dec2 tempo 117.45 duration 416.97 timbre -7.65 pitch 0.41 intensity -42.24 segments 60 
frequency 258.09 key C4 name the-great-escape
view-of-coma_79fc23932086e9530542150c47857bb03b65b11d1fd7c455e2dd238eca100cfa tempo 107.67 duration 445.91 timbre -8.21 pitch 0.43 intensity -42.77 segments 64 frequency 222.6 key A3 name view-of-coma
when-open-air-becomes-a-battlefield_f922c336e1eefdb69496e4a2fb030652728be6ad7c99bc34be4d5a09960ffc11 tempo 152.0 duration 386.21 timbre -7.9 pitch 0.44 intensity -38.7 segments 45 frequency 293.47 key D4 name when-open-air-becomes-a-battlefield
100-free-xxxtentacion-type-beat-angel-raptrap-instrumental_b20fc5ffacc2737c7880e3ba9b79c3c74d82195151c93482c31169890ed1d330 tempo 120.19 duration 361.04 timbre -14.53 pitch 0.44 intensity -58.9 segments 50 frequency 334.44 key E4 name 100-free-xxxtentacion-type-beat-angel-raptrap-instrumental
130-01_f1c3e675d845fe1f825a670fbcfcf8810a504890da960574b434cca88e094104 tempo 129.2 duration 458.26 timbre -12.01 pitch 0.22 intensity -59.66 segments 66 frequency 
233.78 key A#3 name 130-01
be-yourself_37ad5163700b7faa927526b2e48a11b76835c4a5776a6664cb086f2bb33d5009 tempo 114.84 duration 496.87 timbre -8.2 pitch 0.39 intensity -46.33 segments 76 frequency 263.74 key C4 name be-yourself
breathe_c3916db375d4e9b22565ae65367646472770dcce0b494c92b26aa82d453511ce tempo 126.05 duration 390.02 timbre -9.68 pitch 0.42 intensity -50.33 segments 67 frequency 207.7 key G#3 name breathe
cold-trap-beat-instrumental-trap-type-beat-prod-by-gherah-g-m-g-m_a3737d5654ccd679e6407db611d58bd2aeeab6101bce49a870159d103e7a1355 tempo 120.19 duration 360.97 timbre -11.72 pitch 0.27 intensity -54.64 segments 39 frequency 662.82 key E5 name cold-trap-beat-instrumental-trap-type-beat-prod-by-gherah-g-m-g-m
diabla-trap-beat-emotional-bryant-mayers-mike-beatz-g-m-g-m_78ddf057fea8a69b45bb5b56cf9d978d6613722fcb1b2072f5b60b7edf9bfbbd tempo 86.13 duration 346.01 timbre -10.99 pitch 0.28 intensity -56.76 segments 48 frequency 215.0 key A3 name diabla-trap-beat-emotional-bryant-mayers-mike-beatz-g-m-g-m
disaster_590e25b9f3eb4ef3102e0f7e5887237886296dc6a162670b20b21ddbff983bdc tempo 132.51 duration 315.36 timbre -11.24 pitch 0.29 intensity -57.96 segments 45 frequency 153.13 key D#3 name disaster
drops_41baa90392281d60931ae009a0b2ad5727288707e94fab59c75033e04f1b8d61 tempo 120.19 duration 180.48 timbre -13.47 pitch 0.35 intensity -54.55 segments 29 frequency 
298.6 key D4 name drops
ea7-sad-lofi-piano-type-beat-320-kbps-_3e3261c31899b53111fdf6a38dc9a41163ad61948281f9e32c75887f3686ba28 tempo 129.2 duration 405.94 timbre -11.69 pitch 0.43 intensity -60.82 segments 55 frequency 186.59 key F#3 name ea7-sad-lofi-piano-type-beat-320-kbps-
enough_641750e90ad696c3c7da3ac8a6eb3c925e459b75a05cf4550ae81e11abeae479 tempo 132.51 duration 269.02 timbre -12.25 pitch 0.3 intensity -52.89 segments 46 frequency 
285.66 key D4 name enough
free-6lack-type-beat-piano-ambient-instrumental-no-connection-2019-g-m-g-m_ceaf5ecaa0314b5c6edf4b28829041dcfba2b05cb4ffdcc92b8f7f6f4ecd82c9 tempo 114.84 duration 432.39 timbre -13.62 pitch 0.25 intensity -59.58 segments 73 frequency 209.21 key G#3 name free-6lack-type-beat-piano-ambient-instrumental-no-connection-2019-g-m-g-m 
free-alternative-rock-type-beat-prod-useless-320-kbps-g-m-g-m_1121fdde50d6f160892868bc4f7894f240ce5ddbfb726cab9461d8b2db3bddb6 tempo 129.2 duration 295.73 timbre -10.47 pitch 0.31 intensity -52.05 segments 44 frequency 276.59 key C#4 name free-alternative-rock-type-beat-prod-useless-320-kbps-g-m-g-m
free-balcony-bones-x-6dogs-type-beat-prod-bleach-g-m-g-m_eb64a24bbaf033d57b0dfa05f80fd6b6fac24fc5b3a1715cb526cc3d857b071c tempo 136.0 duration 263.5 timbre -11.82 pitch 0.27 intensity -61.12 segments 29 frequency 177.36 key F3 name free-balcony-bones-x-6dogs-type-beat-prod-bleach-g-m-g-m
free-bladee-x-capoxxo-hyperpop-type-beat-redo-prod-pro-z-_faaa4050e487ad959a070f4dc25652223c920901d0c704cd5566f54de2bb7f86 tempo 129.2 duration 236.6 timbre -12.31 
pitch 0.26 intensity -57.95 segments 25 frequency 243.59 key B3 name free-bladee-x-capoxxo-hyperpop-type-beat-redo-prod-pro-z-
free-bones-type-beat-ashes-prod-ojhi_a3fdf5f3c06d1df2ae42b84f1cca986b5f98333897f183c5f2cb59118f69ecf7 tempo 129.2 duration 358.09 timbre -13.71 pitch 0.35 intensity -56.7 segments 50 frequency 508.62 key C5 name free-bones-type-beat-ashes-prod-ojhi
free-bones-type-beat-purple-trees-prod-seshtillirest-_05b2db8eff84808e0f1a44be508fa6027799143b62f576da0f5ad438e566618e tempo 120.19 duration 333.02 timbre -12.21 pitch 0.28 intensity -53.62 segments 57 frequency 317.79 key D#4 name free-bones-type-beat-purple-trees-prod-seshtillirest-
free-bones-x-lil-peep-type-beat-falling-asleep-prod-yago-g-m-g-m_ccf8a999b3cbe65745eedb25645954eaa1904365319462a04517d9f960104f6c tempo 120.19 duration 324.1 timbre -10.13 pitch 0.36 intensity -48.92 segments 40 frequency 238.82 key A#3 name free-bones-x-lil-peep-type-beat-falling-asleep-prod-yago-g-m-g-m
free-bones-x-lil-peep-x-greaf-type-beat-amazing-prod-seshtillirest-g-m-g-m_9285924f32bedae35254a1ae06c203f2b12067344bcb6ab46127b7ccc446af47 tempo 129.2 duration 360.23 timbre -13.32 pitch 0.38 intensity -60.22 segments 49 frequency 277.42 key C#4 name free-bones-x-lil-peep-x-greaf-type-beat-amazing-prod-seshtillirest-g-m-g-m  
free-capoxxo-x-syko-x-oaf1-hyperpop-type-beat-underworld-prod-pro-z-_8cef0bedf65434e7f1e76b5732a49708aae9881d3ee639e62418aa93cbda3e8f tempo 136.0 duration 249.47 timbre -10.13 pitch 0.45 intensity -47.49 segments 29 frequency 374.09 key F#4 name free-capoxxo-x-syko-x-oaf1-hyperpop-type-beat-underworld-prod-pro-z-
free-chill-x-sad-jhene-aiko-type-beat-rnb-instrumental-2019-early-in-the-morning-g-m-g-m_dd473358d39e95948044c7da1b151b88f3578396fa57cfc1557163a95f8a5a19 tempo 123.05 duration 533.03 timbre -14.65 pitch 0.36 intensity -62.15 segments 81 frequency 344.04 key F4 name free-chill-x-sad-jhene-aiko-type-beat-rnb-instrumental-2019-early-in-the-morning-g-m-g-m
free-digital-original-god-x-angst-x-hellasketchy-type-beat-prod-loopy-g-m-g-m_41580b40da8123f069aabaca336c36df04db53a77da64e1bdea9459a8b8d1b56 tempo 126.05 duration 310.13 timbre -9.97 pitch 0.35 intensity -53.63 segments 43 frequency 217.82 key A3 name free-digital-original-god-x-angst-x-hellasketchy-type-beat-prod-loopy-g-m-g-m
free-ecco2k-x-deadmau5-x-crystal-castles-type-beat-sangang_899d3c266e228c33a7d73b78ca6574c86de02e89586bf299b2b4c09058e2dab2 tempo 123.05 duration 420.02 timbre -11.69 pitch 0.31 intensity -46.31 segments 96 frequency 432.17 key A4 name free-ecco2k-x-deadmau5-x-crystal-castles-type-beat-sangang
free-for-profit-hatred-part-2-lil-peep-x-xxxtentacion-type-beat-g-m-g-m_e411e9feb0927f5747028f079f9ea09e9c75326f0e2e8de1ace48739f0e3aaef tempo 123.05 duration 385.67 timbre -11.75 pitch 0.34 intensity -55.37 segments 57 frequency 218.3 key A3 name free-for-profit-hatred-part-2-lil-peep-x-xxxtentacion-type-beat-g-m-g-m
free-for-profit-hyperpop-x-glitchcore-x-lxner-type-beat-synth-prod-soft-clipper-pn_65c44a347f1e5a7509dbd36ac4b1466baad77f4717126a917a0924fe28b66334 tempo 132.51 duration 290.3 timbre -11.46 pitch 0.39 intensity -55.12 segments 41 frequency 314.03 key D#4 name free-for-profit-hyperpop-x-glitchcore-x-lxner-type-beat-synth-prod-soft-clipper-pn
free-for-profit-open-ended-alternative-rock-type-beat_b195caeabdaf42fb1044359add520fd01378da6389e2b92ed057f96572cc76c5 tempo 132.51 duration 306.04 timbre -11.54 pitch 0.46 intensity -48.55 segments 38 frequency 206.14 key G#3 name free-for-profit-open-ended-alternative-rock-type-beat
free-for-profit-witt-lowry-hurt-type-beat-longing-g-m-g-m_0210ef59a8fa64a0092a73e2ee4606449a8e01e3377baebdb7e84888f852168a tempo 129.2 duration 429.03 timbre -12.44 pitch 0.32 intensity -61.69 segments 67 frequency 366.1 key F#4 name free-for-profit-witt-lowry-hurt-type-beat-longing-g-m-g-m
free-guilt-alt-rock-lil-peep-x-nothing-nowhere-type-beat-prod-loopy-g-m-g-m_b3bd210d80f777cc2bbfcb9a2ec6f50750cbc5408dadb0208a4e48abbc0ca83a tempo 114.84 duration 310.13 timbre -15.54 pitch 0.36 intensity -64.17 segments 62 frequency 238.62 key A#3 name free-guilt-alt-rock-lil-peep-x-nothing-nowhere-type-beat-prod-loopy-g-m-g-m
free-gunna-x-lil-baby-type-beat-at-sea-trap-instrumental-2020_e2605169cc469fadde84792b0ce0c1946a782d299bd63b1a677f9295da101807 tempo 129.2 duration 396.22 timbre -11.13 pitch 0.4 intensity -56.62 segments 56 frequency 404.79 key G#4 name free-gunna-x-lil-baby-type-beat-at-sea-trap-instrumental-2020
free-juice-wrld-x-iann-dior-type-beat-reality_a27f934e1119b3679217b05dcd417f1e5a3ad3c8c1b2e63ab1a94ba6055fe391 tempo 129.2 duration 331.36 timbre -11.78 pitch 0.29 
intensity -57.32 segments 48 frequency 223.58 key A3 name free-juice-wrld-x-iann-dior-type-beat-reality
free-juice-wrld-x-iann-dior-type-beat-reborn-trap-instrumental-2020_9fa29fe52fba614133eaa8f04e95e96e4d03edff52b53af9e2ce46c3f9fb9db7 tempo 129.2 duration 336.03 timbre -10.76 pitch 0.37 intensity -54.59 segments 42 frequency 96.5 key G2 name free-juice-wrld-x-iann-dior-type-beat-reborn-trap-instrumental-2020
free-lil-peep-x-coldhart-x-horse-head-x-wicca-phase-type-beat-mistakes-prod-metlastmp3-g-m-g-m_d9694fe1ae9068e9900d8fb76e988e647105f2310e0f4210b2bb1f556c21b53a tempo 120.19 duration 330.08 timbre -12.99 pitch 0.29 intensity -58.87 segments 60 frequency 287.71 key D4 name free-lil-peep-x-coldhart-x-horse-head-x-wicca-phase-type-beat-mistakes-prod-metlastmp3-g-m-g-m
free-lil-peep-x-horse-head-x-lil-lotus-x-smrtdeath-type-beat-midnight-prod-metlast-b-135-00_54224408ed8149b51e9e48844ebf11b7768fa44bf90a69a191fc2f92ed1df2ce tempo 136.0 duration 320.16 timbre -12.25 pitch 0.29 intensity -63.89 segments 48 frequency 103.17 key G#2 name free-lil-peep-x-horse-head-x-lil-lotus-x-smrtdeath-type-beat-midnight-prod-metlast-b-135-00
free-lil-peep-x-lil-tracy-type-beat-heart-hurt-sad-guitar-instrumental-2019-g-m-g-m_2731d94a8c1c5ef18f2739493c886e8f1c7112e05ee70d0d16d93c4cec258c7d tempo 136.0 duration 455.25 timbre -14.12 pitch 0.27 intensity -65.04 segments 64 frequency 185.31 key F#3 name free-lil-peep-x-lil-tracy-type-beat-heart-hurt-sad-guitar-instrumental-2019-g-m-g-m
free-mac-miller-x-j-cole-type-beat-mirrors-2020_b89ce2151bae8d1fce643482e9857d6c8b4a6a9940440dc2925349aae1f8e898 tempo 120.19 duration 404.02 timbre -14.07 pitch 0.48 intensity -63.87 segments 87 frequency 322.16 key E4 name free-mac-miller-x-j-cole-type-beat-mirrors-2020
free-metalcore-x-melodic-post-hardcore-type-beat-dark-horse-melodic-metalcore-instrumental_5ea9250320d2b426a89330e14901d0fee31315cb2da5954c3b450fbb5233a961 tempo 132.51 duration 268.04 timbre -7.72 pitch 0.45 intensity -43.94 segments 33 frequency 238.74 key A#3 name free-metalcore-x-melodic-post-hardcore-type-beat-dark-horse-melodic-metalcore-instrumental
free-no-friends-juice-wrld-x-lil-mosey-x-lil-skies-type-beat-2019-prod-kcaaz-g-m-g-m_0e450b7477e21b8c76723e0fc075a0f57a69bb5dcaff6978d170160ec641de6a tempo 136.0 duration 362.62 timbre -11.49 pitch 0.27 intensity -59.82 segments 39 frequency 127.33 key C3 name free-no-friends-juice-wrld-x-lil-mosey-x-lil-skies-type-beat-2019-prod-kcaaz-g-m-g-m
free-nothing-nowhere-tothegood-lil-lotus-type-beat-i-can-t-leave-yet-prod-remghost-_e93134232c6187318d35e7f57e15c494115ae47be35229b00e96f84925f32421 tempo 120.19 duration 288.59 timbre -10.49 pitch 0.25 intensity -58.26 segments 38 frequency 76.53 key D#2 name free-nothing-nowhere-tothegood-lil-lotus-type-beat-i-can-t-leave-yet-prod-remghost-
free-nothing-nowhere-x-family-pet-x-shinigami-type-beat-keep-it-together-prod-suttee-_d9192fd92c08baa0dbd71822763e21fb0167269181b701373557411cbf44f0c8 tempo 120.19 
duration 324.1 timbre -9.98 pitch 0.38 intensity -51.83 segments 66 frequency 231.54 key A#3 name free-nothing-nowhere-x-family-pet-x-shinigami-type-beat-keep-it-together-prod-suttee-
free-phora-ft-post-malone-type-beat-diamonds-instrumental-2019-g-m-g-m_f20887d1167fb52b61004b77f148bfc2a9ef5800962cf9824ba11aa7061ad9be tempo 114.84 duration 474.12 timbre -14.12 pitch 0.28 intensity -67.4 segments 56 frequency 215.45 key A3 name free-phora-ft-post-malone-type-beat-diamonds-instrumental-2019-g-m-g-m
free-pnb-rock-x-lil-tjay-type-beat-2019-broke-me-prod-midlowbeats-g-m-g-m_dc8662cbb9ca2d845b37b026bfe324c2eba3dbc7ad713ae7fe02b1e1a144feae tempo 129.2 duration 480.22 timbre -10.89 pitch 0.27 intensity -61.51 segments 65 frequency 117.69 key A#2 name free-pnb-rock-x-lil-tjay-type-beat-2019-broke-me-prod-midlowbeats-g-m-g-m    
free-pop-punk-emo-scenecore-type-beat-almost-had-u-pn_feb7e9b184fddb4e920e4f3bd8adb91e9c1442cdf39d938798f405a19ab0941d tempo 129.2 duration 390.14 timbre -8.03 pitch 0.39 intensity -40.23 segments 57 frequency 249.77 key B3 name free-pop-punk-emo-scenecore-type-beat-almost-had-u-pn
free-pop-rock-mgk-x-jxdn-x-iann-dior-pop-punk-type-beat-still-here_73cf7504165037f75db1090e9b55f02e19b6809137fa825b11cacb915bec980f tempo 126.05 duration 372.59 timbre -8.58 pitch 0.45 intensity -49.6 segments 56 frequency 77.03 key D#2 name free-pop-rock-mgk-x-jxdn-x-iann-dior-pop-punk-type-beat-still-here
free-post-malone-guitar-type-beat-apologize-pop-instrumental-2019_a55e6f0ce28d3bcdcbfc31e8f1722a5b6aded62d0817ad43cb32c89f514a6e03 tempo 117.45 duration 460.09 timbre -12.14 pitch 0.24 intensity -63.71 segments 55 frequency 178.87 key F3 name free-post-malone-guitar-type-beat-apologize-pop-instrumental-2019
free-sad-chill-jazzy-type-beat-emma-prod-noria-beats-_e96d131ae2d8290b5f031c1702ea00c9fa6ed169e52103fa551e5e1151c45651 tempo 136.0 duration 458.64 timbre -12.81 pitch 0.29 intensity -63.12 segments 95 frequency 136.79 key C#3 name free-sad-chill-jazzy-type-beat-emma-prod-noria-beats-
free-sad-chill-lofi-type-beat-emotional-deep-piano-trap-2019-_15b9aac06093456ebc5dd245b46b270facf18d890e979bed55b6c17c2cfdb85f tempo 126.05 duration 434.17 timbre -13.58 pitch 0.26 intensity -66.62 segments 65 frequency 234.29 key A#3 name free-sad-chill-lofi-type-beat-emotional-deep-piano-trap-2019-
free-sad-guitar-xxxtentacion-x-lil-peep-type-beat-lakes-pn_ac78d876ffba367a63ff8196f326808ec1d40627ee25d5e229195b9704abe055 tempo 123.05 duration 567.31 timbre -12.0 pitch 0.24 intensity -56.68 segments 119 frequency 360.9 key F#4 name free-sad-guitar-xxxtentacion-x-lil-peep-type-beat-lakes-pn
free-sad-xxxtentacion-type-beat-fly-prod-xenshel-_3c8a2bcd3e39526ad308f4cf2b47acf16e7162a3180d85e15cd02b58cd482030 tempo 120.19 duration 212.15 timbre -10.41 pitch 
0.25 intensity -57.41 segments 31 frequency 227.17 key A#3 name free-sad-xxxtentacion-type-beat-fly-prod-xenshel-
free-scenecore-x-rave-x-hyperpop-type-beat-opals-prod-pro-z-_19431a48572226ddda07c68015a73371f08d41990ff56b919bd9698706a4f0ab tempo 136.0 duration 249.74 timbre -9.1 pitch 0.63 intensity -47.35 segments 41 frequency 318.81 key D#4 name free-scenecore-x-rave-x-hyperpop-type-beat-opals-prod-pro-z-
free-scenecore-x-rave-x-hyperpop-type-beat-unseen-forces-prod-pro-z-_fa186c820758c9380592cd777cfc69cabdcfe29018ad27702745cce1518a43c5 tempo 136.0 duration 239.53 timbre -9.31 pitch 0.53 intensity -46.55 segments 40 frequency 133.58 key C3 name free-scenecore-x-rave-x-hyperpop-type-beat-unseen-forces-prod-pro-z-
free-uicideboy-x-pouya-type-beat-other-body-prod-eykey-beats-x-phil-good-beats-g-m-g-m-g-m_46e33e55c61ca5f35dacef7d6b31136abff4d1f13842e83c8aa878bfc1c3b926 tempo 132.51 duration 294.67 timbre -8.97 pitch 0.31 intensity -50.94 segments 46 frequency 241.73 key B3 name free-uicideboy-x-pouya-type-beat-other-body-prod-eykey-beats-x-phil-good-beats-g-m-g-m-g-m
free-whitearmor-x-crystal-castles-x-thaiboy-digital-type-beat_9a4ac66e722140b5f910dc21e89eb63c9e756f82cb0bac3085ab80b4778eb990 tempo 129.2 duration 410.05 timbre -13.41 pitch 0.34 intensity -54.66 segments 56 frequency 267.09 key C4 name free-whitearmor-x-crystal-castles-x-thaiboy-digital-type-beat
free-witt-lowry-x-nf-type-beat-memories-hip-hop-rap-instrumental-2020-g-m-g-m-130-00_4b3907809b803b57b80b67fb80b24b6a14661199213d32c7acd91e0fd7dd58de tempo 129.2 duration 473.93 timbre -11.41 pitch 0.36 intensity -56.9 segments 74 frequency 81.64 key E2 name free-witt-lowry-x-nf-type-beat-memories-hip-hop-rap-instrumental-2020-g-m-g-m-130-00
free-xxxtentacion-type-beat-forever-emotional-sad-piano-rap-beat-2019_081bb9eb5de563a60d7bef01c36feed5758c200f5cac66dfbd5d70a88ecf4a2c tempo 129.2 duration 400.13 timbre -12.65 pitch 0.34 intensity -58.9 segments 75 frequency 393.56 key G4 name free-xxxtentacion-type-beat-forever-emotional-sad-piano-rap-beat-2019
free-xxxtentacion-x-lil-peep-type-beat-im-sorry-sad-guitar-instrumental-2019-g-m-g-m_cd260a84f796f76fff33e8911934cc6e4eaa7ec0d3bd0b890cb7e043e1832558 tempo 129.2 duration 343.37 timbre -10.5 pitch 0.39 intensity -57.59 segments 59 frequency 183.32 key F#3 name free-xxxtentacion-x-lil-peep-type-beat-im-sorry-sad-guitar-instrumental-2019-g-m-g-m
free-xxxtentacion-x-nf-type-beat-wishes-sad-rap-piano-instrumental-2019-g-m-g-m_55f306c8a95ac4bf7d90739449f0e27d31456cf4c696d4f3d9f4cb26798615cc tempo 126.05 duration 432.07 timbre -11.64 pitch 0.33 intensity -56.3 segments 93 frequency 156.68 key D#3 name free-xxxtentacion-x-nf-type-beat-wishes-sad-rap-piano-instrumental-2019-g-m-g-m
g-m-g-m-116-00_0789686c6614391ebb58d0b524b1cb472f2c81f6dd70bec447e319949638f173 tempo 114.84 duration 240.78 timbre -12.16 pitch 0.27 intensity -58.4 segments 47 frequency 175.32 key F3 name g-m-g-m-116-00
guccihighwaters-9tails-convolk-guardin-shinigami-lil-lotus-type-beat-sad-guitar_fee4136b71f10588c595e9d6c830637de01a5cf8359db292121112b2b4a0eabe tempo 129.2 duration 483.02 timbre -10.87 pitch 0.35 intensity -53.7 segments 82 frequency 304.4 key D#4 name guccihighwaters-9tails-convolk-guardin-shinigami-lil-lotus-type-beat-sad-guitar
gunner-prod-fantom-_e6b23d20b29b923d9951a3cdf006217003a9ab22d80cc18642db66581669bfe2 tempo 123.05 duration 302.79 timbre -10.2 pitch 0.39 intensity -57.58 segments 
30 frequency 70.31 key C#2 name gunner-prod-fantom-
hot-mulligan-tiny-moving-parts_b56d4e39828c3a73916074523c34b69a0bb9ae4d53630cd9d6893b42bb2b9914 tempo 123.05 duration 288.48 timbre -8.27 pitch 0.35 intensity -44.24 segments 49 frequency 212.55 key G#3 name hot-mulligan-tiny-moving-parts
i-miss-you-free-nf-x-ivan-b-type-beat-emotional-sad-instrumental-prod-starbeats-2019-g-m-g-m-125-00_f877bc649cb0a304f03fdbb965137b29b6844a5b5ed3abb68d7303f3c4722b09 tempo 126.05 duration 537.69 timbre -9.48 pitch 0.3 intensity -55.5 segments 81 frequency 153.23 key D#3 name i-miss-you-free-nf-x-ivan-b-type-beat-emotional-sad-instrumental-prod-starbeats-2019-g-m-g-m-125-00
i-miss-you-g-m-g-m_5888aa4efe963eca2694d28723c6ae2e2c7639caa3f842c2495eef85f0a9cf35 tempo 120.19 duration 357.28 timbre -12.12 pitch 0.3 intensity -54.9 segments 62 frequency 280.86 key C#4 name i-miss-you-g-m-g-m
ill-faded-prod-bassment-_b0b27b0cccae442b0f0f3bb13f3d8871c79210a8a2b4e590f544ce2079cf9a2d tempo 126.05 duration 320.16 timbre -12.08 pitch 0.39 intensity -56.05 segments 42 frequency 242.89 key B3 name ill-faded-prod-bassment-
illusions-soft-chill-rap-instrumental-atmospheric-trap-beat-2019-g-m-g-m_664a1b256bcd2f461d7d5b23526a696a2c7c46fdae2a24f93f67a3b2032bec3b tempo 136.0 duration 384.1 timbre -9.34 pitch 0.37 intensity -53.89 segments 54 frequency 72.87 key D2 name illusions-soft-chill-rap-instrumental-atmospheric-trap-beat-2019-g-m-g-m
is-love-bones-x-teamsesh-type-beat-prod-rareflowermp3-g-m-g-m_0936412db01ae4b1593bd0697ebf723552125152e2a10f4948c5cf0e9454584e tempo 129.2 duration 580.08 timbre -11.54 pitch 0.37 intensity -49.64 segments 76 frequency 241.86 key B3 name is-love-bones-x-teamsesh-type-beat-prod-rareflowermp3-g-m-g-m
ivan-b-x-witt-lowry-type-beat-shedding-my-tears-deep-storytelling-g-m-g-m_5e1ed52eff0e50d680e44d1d245c0ff3b873e75a0d0a319f9f21dfec3245a0ea tempo 126.05 duration 354.47 timbre -11.19 pitch 0.29 intensity -61.02 segments 58 frequency 142.89 key D3 name ivan-b-x-witt-lowry-type-beat-shedding-my-tears-deep-storytelling-g-m-g-m    
kevin-gates-x-future-type-beat-hate-me-iii-prod-by-mb13beatz-g-m-g-m_773c9df75276ea13fe03ba957fce3d360a5b802f7ec86191dfc3cb22560ab661 tempo 129.2 duration 540.04 timbre -12.12 pitch 0.29 intensity -57.73 segments 92 frequency 204.95 key G#3 name kevin-gates-x-future-type-beat-hate-me-iii-prod-by-mb13beatz-g-m-g-m
letter-2-the-weeknd_4d59a21756d8f88cbac9b330b347d1ca3abb2b05d67521108de4219f963a8dc4 tempo 126.05 duration 430.08 timbre -10.52 pitch 0.59 intensity -49.02 segments 54 frequency 245.85 key B3 name letter-2-the-weeknd
lipstick-prod-qb-trap-beat-for-singing_e38cbaabd562f84239d27034c28d10a1acea66f5a60c7b6ebd897dfeb1f48c5c tempo 132.51 duration 480.1 timbre -13.05 pitch 0.26 intensity -62.08 segments 69 frequency 99.02 key G2 name lipstick-prod-qb-trap-beat-for-singing
midwest-emo-type-beat_41e4cee0420bf1becfc09770dc95a4f2c6007f0cc768ec8dfd189c0419f36604 tempo 136.0 duration 406.08 timbre -11.64 pitch 0.27 intensity -59.74 segments 52 frequency 224.0 key A3 name midwest-emo-type-beat
new-year-prod-metlast-_2e06a190d773f0c2a8e1667f92969bcf0718cca2070c920a32b4bf0080107ff7 tempo 120.19 duration 288.25 timbre -11.9 pitch 0.28 intensity -60.38 segments 29 frequency 349.82 key F4 name new-year-prod-metlast-
nineteen_39d06763a0ff50d8553eba900b60c5ecc4a2f70b12083b98f546bccbcdbf333e tempo 136.0 duration 287.1 timbre -15.67 pitch 0.36 intensity -61.77 segments 33 frequency 256.04 key C4 name nineteen
nothing-nowhere-fats-e-iann-dior_259e5911ddd61c3faae1860d1bc8daaf97416ea805700edfbf6418823ea47227 tempo 136.0 duration 474.19 timbre -9.63 pitch 0.25 intensity -55.03 segments 63 frequency 121.45 key B2 name nothing-nowhere-fats-e-iann-dior
numb-g-m-g-m_185b1083d3ae30b7a0c539dc7dc7e5e20da4c5d9b11ce9a1b12ad8001c75d2b0 tempo 123.05 duration 504.12 timbre -12.14 pitch 0.31 intensity -57.66 segments 77 frequency 133.59 key C3 name numb-g-m-g-m
prod-capsctrl-silo-g-m-g-m_6c71eb80c1a8700ccd0ba117217e77c80fd2ee0007b470ffb9a71d23b729bbd8 tempo 120.19 duration 392.11 timbre -11.48 pitch 0.31 intensity -57.48 segments 63 frequency 268.18 key C4 name prod-capsctrl-silo-g-m-g-m
rain_cbf08b90a080cdec19295a666cf18eae5c913d88725e6cc9e76ed09a65766bfb tempo 129.2 duration 391.72 timbre -12.63 pitch 0.29 intensity -60.26 segments 61 frequency 77.21 key D#2 name rain
raptrap-beat-trapnew-school-instrumental-2019-prod-kyu-tracks-g-m-g-m_d2c06ebe76db5e6d0b6d02bda5a8a5ada73358d53ed3d4bb633358274fca67e6 tempo 126.05 duration 373.25 
timbre -9.86 pitch 0.27 intensity -53.4 segments 57 frequency 268.98 key C4 name raptrap-beat-trapnew-school-instrumental-2019-prod-kyu-tracks-g-m-g-m
ripsquad-x-nosgov-x-senses-x-bladee-type-beat-prod-ev333-_b3b015df97d837ef4b834c089d9b8e3545b360ba5c80e12214fc6756fe2ae739 tempo 123.05 duration 300.05 timbre -12.36 pitch 0.3 intensity -54.6 segments 46 frequency 457.15 key A#4 name ripsquad-x-nosgov-x-senses-x-bladee-type-beat-prod-ev333-
sad-ambient-piano-type-beat-piece-320-kbps-_643ca8237d17a55c06dad6aaaccd50882e348efa95cf88c1f049f8ffbafa20a6 tempo 120.19 duration 427.73 timbre -13.91 pitch 0.36 intensity -64.23 segments 69 frequency 281.38 key C#4 name sad-ambient-piano-type-beat-piece-320-kbps-
save-me-sad-piano-instrumental-2019_0f27a2faccd6dc111a74522a22572edebd975c726a23e8946ddd88d09d2a504d tempo 136.0 duration 427.34 timbre -12.84 pitch 0.3 intensity -60.38 segments 109 frequency 307.66 key D#4 name save-me-sad-piano-instrumental-2019
sold-dark-xxxtentacion-x-denzel-curry-type-beat-plague-trap-intrumental-2020_ed7882cdee3d26fe38ad55cac61ea079cd945c01484b0bf7918382fc6a857318 tempo 129.2 duration 304.08 timbre -10.23 pitch 0.44 intensity -54.77 segments 35 frequency 341.02 key F4 name sold-dark-xxxtentacion-x-denzel-curry-type-beat-plague-trap-intrumental-2020
sold-xxxtentacion-sad-lofi-type-beat-scars-ft-mishaal-g-m-g-m_e054b3218482c95fffbc2cc8c53c0c7a7f48fa4782c77393d3c0215800e67c55 tempo 120.19 duration 309.81 timbre -13.55 pitch 0.32 intensity -56.13 segments 43 frequency 285.71 key D4 name sold-xxxtentacion-sad-lofi-type-beat-scars-ft-mishaal-g-m-g-m
synth_d5637fa2aa32345a3792c1fa7c357cb31c2dd0e6b447340a5950c41b5dbd2b19 tempo 132.51 duration 290.19 timbre -11.68 pitch 0.4 intensity -56.12 segments 36 frequency 305.53 key D#4 name synth
time-free-nf-type-beat-emotional-sad-piano-instrumental-2019-prod-starbeats-g-m-g-m-g-m-135-00_da1fcece5188a3427a800a8a0191b14d2f67699293db80c5ea6b4e0c6f15f2f8 tempo 136.0 duration 551.19 timbre -11.44 pitch 0.43 intensity -54.57 segments 81 frequency 270.33 key C#4 name time-free-nf-type-beat-emotional-sad-piano-instrumental-2019-prod-starbeats-g-m-g-m-g-m-135-00
waifu_ca3105d05ff8fada0dbcd0a695cc40f8b2d3900175bf28c4a1cf75e8f95f17b1 tempo 126.05 duration 262.75 timbre -8.86 pitch 0.36 intensity -45.87 segments 45 frequency 187.13 key F#3 name waifu
zen_e88e86af4b2e47a4ea4e6d6a5f95455bc6b0acae99e117f644977ba71dac8bd2 tempo 114.84 duration 271.52 timbre -11.19 pitch 0.3 intensity -58.57 segments 60 frequency 173.46 key F3 name zen
--------------------------------------------------------------------------

C:\Users\Ninja\polymath>python polymath.py -a C:/Users/Ninja/polymath/input/ope/
2023-03-04 14:41:02.124857: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'cudart64_110.dll'; dlerror: cudart64_110.dll not found
2023-03-04 14:41:02.125725: I tensorflow/stream_executor/cuda/cudart_stub.cc:29] Ignore above cudart dlerror if you do not have a GPU set up on your machine.
---------------------------------------------------------------------------- 
--------------------------------- POLYMATH --------------------------------- 
----------------------------------------------------------------------------
add video: C:/Users/Ninja/polymath/input/ope/ to videos: 94
add directory with wav or mp3 files
Found 0 wav or mp3 files
------------------------------ Files in DB: 94 ------------------------------
a-letter-to-write_6efb86a5da47e3e7ad5c2a1242a080128b95e964f51f6efb22dce052c62df8af tempo 126.05 duration 472.14 timbre -7.86 pitch 0.35 intensity -40.98 segments 69 frequency 284.64 key C#4 name a-letter-to-write
cemeteries-and-greyhound-busses_68ee27932a358f0da40bed24e2d3d6c366056decb74299c7702fa431cdb96ac2 tempo 136.0 duration 551.14 timbre -8.21 pitch 0.48 intensity -42.58 segments 68 frequency 254.92 key C4 name cemeteries-and-greyhound-busses
diet-coke-and-mentos_2ebb90d50670d1153113d1314f640829bbeedfe9d0f35fd7bcf85ffc40c0a5cb tempo 120.19 duration 411.12 timbre -8.31 pitch 0.4 intensity -40.68 segments 
64 frequency 228.46 key A#3 name diet-coke-and-mentos
goodbye-mr-perfection_4ee19add8d0df6ac261b132da0163d67f94c1fa4c5145a0211bfb53f30968b37 tempo 143.55 duration 462.32 timbre -8.64 pitch 0.33 intensity -42.34 segments 68 frequency 263.09 key C4 name goodbye-mr-perfection
our-perfect-ending_7b949ba5a05cbb5030e6961a073dfbe6aeaabf62d8b8913fa2ad3c0e68eead68 tempo 139.67 duration 477.78 timbre -12.4 pitch 0.25 intensity -49.55 segments 76 frequency 235.66 key A#3 name our-perfect-ending
seven-days_dfd68b93e298ca6eeeba645e3e7eda8755fe3fc2436554821adbdca5da57d167 tempo 126.05 duration 370.31 timbre -7.79 pitch 0.44 intensity -38.7 segments 42 frequency 274.96 key C#4 name seven-days
the-great-escape_5f14bbc778ab78ebe0adff825fa96d0ea01c3385df3b5fdefce6ba8d3c15dec2 tempo 117.45 duration 416.97 timbre -7.65 pitch 0.41 intensity -42.24 segments 60 
frequency 258.09 key C4 name the-great-escape
view-of-coma_79fc23932086e9530542150c47857bb03b65b11d1fd7c455e2dd238eca100cfa tempo 107.67 duration 445.91 timbre -8.21 pitch 0.43 intensity -42.77 segments 64 frequency 222.6 key A3 name view-of-coma
when-open-air-becomes-a-battlefield_f922c336e1eefdb69496e4a2fb030652728be6ad7c99bc34be4d5a09960ffc11 tempo 152.0 duration 386.21 timbre -7.9 pitch 0.44 intensity -38.7 segments 45 frequency 293.47 key D4 name when-open-air-becomes-a-battlefield
100-free-xxxtentacion-type-beat-angel-raptrap-instrumental_b20fc5ffacc2737c7880e3ba9b79c3c74d82195151c93482c31169890ed1d330 tempo 120.19 duration 361.04 timbre -14.53 pitch 0.44 intensity -58.9 segments 50 frequency 334.44 key E4 name 100-free-xxxtentacion-type-beat-angel-raptrap-instrumental
130-01_f1c3e675d845fe1f825a670fbcfcf8810a504890da960574b434cca88e094104 tempo 129.2 duration 458.26 timbre -12.01 pitch 0.22 intensity -59.66 segments 66 frequency 
233.78 key A#3 name 130-01
be-yourself_37ad5163700b7faa927526b2e48a11b76835c4a5776a6664cb086f2bb33d5009 tempo 114.84 duration 496.87 timbre -8.2 pitch 0.39 intensity -46.33 segments 76 frequency 263.74 key C4 name be-yourself
breathe_c3916db375d4e9b22565ae65367646472770dcce0b494c92b26aa82d453511ce tempo 126.05 duration 390.02 timbre -9.68 pitch 0.42 intensity -50.33 segments 67 frequency 207.7 key G#3 name breathe
cold-trap-beat-instrumental-trap-type-beat-prod-by-gherah-g-m-g-m_a3737d5654ccd679e6407db611d58bd2aeeab6101bce49a870159d103e7a1355 tempo 120.19 duration 360.97 timbre -11.72 pitch 0.27 intensity -54.64 segments 39 frequency 662.82 key E5 name cold-trap-beat-instrumental-trap-type-beat-prod-by-gherah-g-m-g-m
diabla-trap-beat-emotional-bryant-mayers-mike-beatz-g-m-g-m_78ddf057fea8a69b45bb5b56cf9d978d6613722fcb1b2072f5b60b7edf9bfbbd tempo 86.13 duration 346.01 timbre -10.99 pitch 0.28 intensity -56.76 segments 48 frequency 215.0 key A3 name diabla-trap-beat-emotional-bryant-mayers-mike-beatz-g-m-g-m
disaster_590e25b9f3eb4ef3102e0f7e5887237886296dc6a162670b20b21ddbff983bdc tempo 132.51 duration 315.36 timbre -11.24 pitch 0.29 intensity -57.96 segments 45 frequency 153.13 key D#3 name disaster
drops_41baa90392281d60931ae009a0b2ad5727288707e94fab59c75033e04f1b8d61 tempo 120.19 duration 180.48 timbre -13.47 pitch 0.35 intensity -54.55 segments 29 frequency 
298.6 key D4 name drops
ea7-sad-lofi-piano-type-beat-320-kbps-_3e3261c31899b53111fdf6a38dc9a41163ad61948281f9e32c75887f3686ba28 tempo 129.2 duration 405.94 timbre -11.69 pitch 0.43 intensity -60.82 segments 55 frequency 186.59 key F#3 name ea7-sad-lofi-piano-type-beat-320-kbps-
enough_641750e90ad696c3c7da3ac8a6eb3c925e459b75a05cf4550ae81e11abeae479 tempo 132.51 duration 269.02 timbre -12.25 pitch 0.3 intensity -52.89 segments 46 frequency 
285.66 key D4 name enough
free-6lack-type-beat-piano-ambient-instrumental-no-connection-2019-g-m-g-m_ceaf5ecaa0314b5c6edf4b28829041dcfba2b05cb4ffdcc92b8f7f6f4ecd82c9 tempo 114.84 duration 432.39 timbre -13.62 pitch 0.25 intensity -59.58 segments 73 frequency 209.21 key G#3 name free-6lack-type-beat-piano-ambient-instrumental-no-connection-2019-g-m-g-m 
free-alternative-rock-type-beat-prod-useless-320-kbps-g-m-g-m_1121fdde50d6f160892868bc4f7894f240ce5ddbfb726cab9461d8b2db3bddb6 tempo 129.2 duration 295.73 timbre -10.47 pitch 0.31 intensity -52.05 segments 44 frequency 276.59 key C#4 name free-alternative-rock-type-beat-prod-useless-320-kbps-g-m-g-m
free-balcony-bones-x-6dogs-type-beat-prod-bleach-g-m-g-m_eb64a24bbaf033d57b0dfa05f80fd6b6fac24fc5b3a1715cb526cc3d857b071c tempo 136.0 duration 263.5 timbre -11.82 pitch 0.27 intensity -61.12 segments 29 frequency 177.36 key F3 name free-balcony-bones-x-6dogs-type-beat-prod-bleach-g-m-g-m
free-bladee-x-capoxxo-hyperpop-type-beat-redo-prod-pro-z-_faaa4050e487ad959a070f4dc25652223c920901d0c704cd5566f54de2bb7f86 tempo 129.2 duration 236.6 timbre -12.31 
pitch 0.26 intensity -57.95 segments 25 frequency 243.59 key B3 name free-bladee-x-capoxxo-hyperpop-type-beat-redo-prod-pro-z-
free-bones-type-beat-ashes-prod-ojhi_a3fdf5f3c06d1df2ae42b84f1cca986b5f98333897f183c5f2cb59118f69ecf7 tempo 129.2 duration 358.09 timbre -13.71 pitch 0.35 intensity -56.7 segments 50 frequency 508.62 key C5 name free-bones-type-beat-ashes-prod-ojhi
free-bones-type-beat-purple-trees-prod-seshtillirest-_05b2db8eff84808e0f1a44be508fa6027799143b62f576da0f5ad438e566618e tempo 120.19 duration 333.02 timbre -12.21 pitch 0.28 intensity -53.62 segments 57 frequency 317.79 key D#4 name free-bones-type-beat-purple-trees-prod-seshtillirest-
free-bones-x-lil-peep-type-beat-falling-asleep-prod-yago-g-m-g-m_ccf8a999b3cbe65745eedb25645954eaa1904365319462a04517d9f960104f6c tempo 120.19 duration 324.1 timbre -10.13 pitch 0.36 intensity -48.92 segments 40 frequency 238.82 key A#3 name free-bones-x-lil-peep-type-beat-falling-asleep-prod-yago-g-m-g-m
free-bones-x-lil-peep-x-greaf-type-beat-amazing-prod-seshtillirest-g-m-g-m_9285924f32bedae35254a1ae06c203f2b12067344bcb6ab46127b7ccc446af47 tempo 129.2 duration 360.23 timbre -13.32 pitch 0.38 intensity -60.22 segments 49 frequency 277.42 key C#4 name free-bones-x-lil-peep-x-greaf-type-beat-amazing-prod-seshtillirest-g-m-g-m  
free-capoxxo-x-syko-x-oaf1-hyperpop-type-beat-underworld-prod-pro-z-_8cef0bedf65434e7f1e76b5732a49708aae9881d3ee639e62418aa93cbda3e8f tempo 136.0 duration 249.47 timbre -10.13 pitch 0.45 intensity -47.49 segments 29 frequency 374.09 key F#4 name free-capoxxo-x-syko-x-oaf1-hyperpop-type-beat-underworld-prod-pro-z-
free-chill-x-sad-jhene-aiko-type-beat-rnb-instrumental-2019-early-in-the-morning-g-m-g-m_dd473358d39e95948044c7da1b151b88f3578396fa57cfc1557163a95f8a5a19 tempo 123.05 duration 533.03 timbre -14.65 pitch 0.36 intensity -62.15 segments 81 frequency 344.04 key F4 name free-chill-x-sad-jhene-aiko-type-beat-rnb-instrumental-2019-early-in-the-morning-g-m-g-m
free-digital-original-god-x-angst-x-hellasketchy-type-beat-prod-loopy-g-m-g-m_41580b40da8123f069aabaca336c36df04db53a77da64e1bdea9459a8b8d1b56 tempo 126.05 duration 310.13 timbre -9.97 pitch 0.35 intensity -53.63 segments 43 frequency 217.82 key A3 name free-digital-original-god-x-angst-x-hellasketchy-type-beat-prod-loopy-g-m-g-m
free-ecco2k-x-deadmau5-x-crystal-castles-type-beat-sangang_899d3c266e228c33a7d73b78ca6574c86de02e89586bf299b2b4c09058e2dab2 tempo 123.05 duration 420.02 timbre -11.69 pitch 0.31 intensity -46.31 segments 96 frequency 432.17 key A4 name free-ecco2k-x-deadmau5-x-crystal-castles-type-beat-sangang
free-for-profit-hatred-part-2-lil-peep-x-xxxtentacion-type-beat-g-m-g-m_e411e9feb0927f5747028f079f9ea09e9c75326f0e2e8de1ace48739f0e3aaef tempo 123.05 duration 385.67 timbre -11.75 pitch 0.34 intensity -55.37 segments 57 frequency 218.3 key A3 name free-for-profit-hatred-part-2-lil-peep-x-xxxtentacion-type-beat-g-m-g-m
free-for-profit-hyperpop-x-glitchcore-x-lxner-type-beat-synth-prod-soft-clipper-pn_65c44a347f1e5a7509dbd36ac4b1466baad77f4717126a917a0924fe28b66334 tempo 132.51 duration 290.3 timbre -11.46 pitch 0.39 intensity -55.12 segments 41 frequency 314.03 key D#4 name free-for-profit-hyperpop-x-glitchcore-x-lxner-type-beat-synth-prod-soft-clipper-pn
free-for-profit-open-ended-alternative-rock-type-beat_b195caeabdaf42fb1044359add520fd01378da6389e2b92ed057f96572cc76c5 tempo 132.51 duration 306.04 timbre -11.54 pitch 0.46 intensity -48.55 segments 38 frequency 206.14 key G#3 name free-for-profit-open-ended-alternative-rock-type-beat
free-for-profit-witt-lowry-hurt-type-beat-longing-g-m-g-m_0210ef59a8fa64a0092a73e2ee4606449a8e01e3377baebdb7e84888f852168a tempo 129.2 duration 429.03 timbre -12.44 pitch 0.32 intensity -61.69 segments 67 frequency 366.1 key F#4 name free-for-profit-witt-lowry-hurt-type-beat-longing-g-m-g-m
free-guilt-alt-rock-lil-peep-x-nothing-nowhere-type-beat-prod-loopy-g-m-g-m_b3bd210d80f777cc2bbfcb9a2ec6f50750cbc5408dadb0208a4e48abbc0ca83a tempo 114.84 duration 310.13 timbre -15.54 pitch 0.36 intensity -64.17 segments 62 frequency 238.62 key A#3 name free-guilt-alt-rock-lil-peep-x-nothing-nowhere-type-beat-prod-loopy-g-m-g-m
free-gunna-x-lil-baby-type-beat-at-sea-trap-instrumental-2020_e2605169cc469fadde84792b0ce0c1946a782d299bd63b1a677f9295da101807 tempo 129.2 duration 396.22 timbre -11.13 pitch 0.4 intensity -56.62 segments 56 frequency 404.79 key G#4 name free-gunna-x-lil-baby-type-beat-at-sea-trap-instrumental-2020
free-juice-wrld-x-iann-dior-type-beat-reality_a27f934e1119b3679217b05dcd417f1e5a3ad3c8c1b2e63ab1a94ba6055fe391 tempo 129.2 duration 331.36 timbre -11.78 pitch 0.29 
intensity -57.32 segments 48 frequency 223.58 key A3 name free-juice-wrld-x-iann-dior-type-beat-reality
free-juice-wrld-x-iann-dior-type-beat-reborn-trap-instrumental-2020_9fa29fe52fba614133eaa8f04e95e96e4d03edff52b53af9e2ce46c3f9fb9db7 tempo 129.2 duration 336.03 timbre -10.76 pitch 0.37 intensity -54.59 segments 42 frequency 96.5 key G2 name free-juice-wrld-x-iann-dior-type-beat-reborn-trap-instrumental-2020
free-lil-peep-x-coldhart-x-horse-head-x-wicca-phase-type-beat-mistakes-prod-metlastmp3-g-m-g-m_d9694fe1ae9068e9900d8fb76e988e647105f2310e0f4210b2bb1f556c21b53a tempo 120.19 duration 330.08 timbre -12.99 pitch 0.29 intensity -58.87 segments 60 frequency 287.71 key D4 name free-lil-peep-x-coldhart-x-horse-head-x-wicca-phase-type-beat-mistakes-prod-metlastmp3-g-m-g-m
free-lil-peep-x-horse-head-x-lil-lotus-x-smrtdeath-type-beat-midnight-prod-metlast-b-135-00_54224408ed8149b51e9e48844ebf11b7768fa44bf90a69a191fc2f92ed1df2ce tempo 136.0 duration 320.16 timbre -12.25 pitch 0.29 intensity -63.89 segments 48 frequency 103.17 key G#2 name free-lil-peep-x-horse-head-x-lil-lotus-x-smrtdeath-type-beat-midnight-prod-metlast-b-135-00
free-lil-peep-x-lil-tracy-type-beat-heart-hurt-sad-guitar-instrumental-2019-g-m-g-m_2731d94a8c1c5ef18f2739493c886e8f1c7112e05ee70d0d16d93c4cec258c7d tempo 136.0 duration 455.25 timbre -14.12 pitch 0.27 intensity -65.04 segments 64 frequency 185.31 key F#3 name free-lil-peep-x-lil-tracy-type-beat-heart-hurt-sad-guitar-instrumental-2019-g-m-g-m
free-mac-miller-x-j-cole-type-beat-mirrors-2020_b89ce2151bae8d1fce643482e9857d6c8b4a6a9940440dc2925349aae1f8e898 tempo 120.19 duration 404.02 timbre -14.07 pitch 0.48 intensity -63.87 segments 87 frequency 322.16 key E4 name free-mac-miller-x-j-cole-type-beat-mirrors-2020
free-metalcore-x-melodic-post-hardcore-type-beat-dark-horse-melodic-metalcore-instrumental_5ea9250320d2b426a89330e14901d0fee31315cb2da5954c3b450fbb5233a961 tempo 132.51 duration 268.04 timbre -7.72 pitch 0.45 intensity -43.94 segments 33 frequency 238.74 key A#3 name free-metalcore-x-melodic-post-hardcore-type-beat-dark-horse-melodic-metalcore-instrumental
free-no-friends-juice-wrld-x-lil-mosey-x-lil-skies-type-beat-2019-prod-kcaaz-g-m-g-m_0e450b7477e21b8c76723e0fc075a0f57a69bb5dcaff6978d170160ec641de6a tempo 136.0 duration 362.62 timbre -11.49 pitch 0.27 intensity -59.82 segments 39 frequency 127.33 key C3 name free-no-friends-juice-wrld-x-lil-mosey-x-lil-skies-type-beat-2019-prod-kcaaz-g-m-g-m
free-nothing-nowhere-tothegood-lil-lotus-type-beat-i-can-t-leave-yet-prod-remghost-_e93134232c6187318d35e7f57e15c494115ae47be35229b00e96f84925f32421 tempo 120.19 duration 288.59 timbre -10.49 pitch 0.25 intensity -58.26 segments 38 frequency 76.53 key D#2 name free-nothing-nowhere-tothegood-lil-lotus-type-beat-i-can-t-leave-yet-prod-remghost-
free-nothing-nowhere-x-family-pet-x-shinigami-type-beat-keep-it-together-prod-suttee-_d9192fd92c08baa0dbd71822763e21fb0167269181b701373557411cbf44f0c8 tempo 120.19 
duration 324.1 timbre -9.98 pitch 0.38 intensity -51.83 segments 66 frequency 231.54 key A#3 name free-nothing-nowhere-x-family-pet-x-shinigami-type-beat-keep-it-together-prod-suttee-
free-phora-ft-post-malone-type-beat-diamonds-instrumental-2019-g-m-g-m_f20887d1167fb52b61004b77f148bfc2a9ef5800962cf9824ba11aa7061ad9be tempo 114.84 duration 474.12 timbre -14.12 pitch 0.28 intensity -67.4 segments 56 frequency 215.45 key A3 name free-phora-ft-post-malone-type-beat-diamonds-instrumental-2019-g-m-g-m
free-pnb-rock-x-lil-tjay-type-beat-2019-broke-me-prod-midlowbeats-g-m-g-m_dc8662cbb9ca2d845b37b026bfe324c2eba3dbc7ad713ae7fe02b1e1a144feae tempo 129.2 duration 480.22 timbre -10.89 pitch 0.27 intensity -61.51 segments 65 frequency 117.69 key A#2 name free-pnb-rock-x-lil-tjay-type-beat-2019-broke-me-prod-midlowbeats-g-m-g-m    
free-pop-punk-emo-scenecore-type-beat-almost-had-u-pn_feb7e9b184fddb4e920e4f3bd8adb91e9c1442cdf39d938798f405a19ab0941d tempo 129.2 duration 390.14 timbre -8.03 pitch 0.39 intensity -40.23 segments 57 frequency 249.77 key B3 name free-pop-punk-emo-scenecore-type-beat-almost-had-u-pn
free-pop-rock-mgk-x-jxdn-x-iann-dior-pop-punk-type-beat-still-here_73cf7504165037f75db1090e9b55f02e19b6809137fa825b11cacb915bec980f tempo 126.05 duration 372.59 timbre -8.58 pitch 0.45 intensity -49.6 segments 56 frequency 77.03 key D#2 name free-pop-rock-mgk-x-jxdn-x-iann-dior-pop-punk-type-beat-still-here
free-post-malone-guitar-type-beat-apologize-pop-instrumental-2019_a55e6f0ce28d3bcdcbfc31e8f1722a5b6aded62d0817ad43cb32c89f514a6e03 tempo 117.45 duration 460.09 timbre -12.14 pitch 0.24 intensity -63.71 segments 55 frequency 178.87 key F3 name free-post-malone-guitar-type-beat-apologize-pop-instrumental-2019
free-sad-chill-jazzy-type-beat-emma-prod-noria-beats-_e96d131ae2d8290b5f031c1702ea00c9fa6ed169e52103fa551e5e1151c45651 tempo 136.0 duration 458.64 timbre -12.81 pitch 0.29 intensity -63.12 segments 95 frequency 136.79 key C#3 name free-sad-chill-jazzy-type-beat-emma-prod-noria-beats-
free-sad-chill-lofi-type-beat-emotional-deep-piano-trap-2019-_15b9aac06093456ebc5dd245b46b270facf18d890e979bed55b6c17c2cfdb85f tempo 126.05 duration 434.17 timbre -13.58 pitch 0.26 intensity -66.62 segments 65 frequency 234.29 key A#3 name free-sad-chill-lofi-type-beat-emotional-deep-piano-trap-2019-
free-sad-guitar-xxxtentacion-x-lil-peep-type-beat-lakes-pn_ac78d876ffba367a63ff8196f326808ec1d40627ee25d5e229195b9704abe055 tempo 123.05 duration 567.31 timbre -12.0 pitch 0.24 intensity -56.68 segments 119 frequency 360.9 key F#4 name free-sad-guitar-xxxtentacion-x-lil-peep-type-beat-lakes-pn
free-sad-xxxtentacion-type-beat-fly-prod-xenshel-_3c8a2bcd3e39526ad308f4cf2b47acf16e7162a3180d85e15cd02b58cd482030 tempo 120.19 duration 212.15 timbre -10.41 pitch 
0.25 intensity -57.41 segments 31 frequency 227.17 key A#3 name free-sad-xxxtentacion-type-beat-fly-prod-xenshel-
free-scenecore-x-rave-x-hyperpop-type-beat-opals-prod-pro-z-_19431a48572226ddda07c68015a73371f08d41990ff56b919bd9698706a4f0ab tempo 136.0 duration 249.74 timbre -9.1 pitch 0.63 intensity -47.35 segments 41 frequency 318.81 key D#4 name free-scenecore-x-rave-x-hyperpop-type-beat-opals-prod-pro-z-
free-scenecore-x-rave-x-hyperpop-type-beat-unseen-forces-prod-pro-z-_fa186c820758c9380592cd777cfc69cabdcfe29018ad27702745cce1518a43c5 tempo 136.0 duration 239.53 timbre -9.31 pitch 0.53 intensity -46.55 segments 40 frequency 133.58 key C3 name free-scenecore-x-rave-x-hyperpop-type-beat-unseen-forces-prod-pro-z-
free-uicideboy-x-pouya-type-beat-other-body-prod-eykey-beats-x-phil-good-beats-g-m-g-m-g-m_46e33e55c61ca5f35dacef7d6b31136abff4d1f13842e83c8aa878bfc1c3b926 tempo 132.51 duration 294.67 timbre -8.97 pitch 0.31 intensity -50.94 segments 46 frequency 241.73 key B3 name free-uicideboy-x-pouya-type-beat-other-body-prod-eykey-beats-x-phil-good-beats-g-m-g-m-g-m
free-whitearmor-x-crystal-castles-x-thaiboy-digital-type-beat_9a4ac66e722140b5f910dc21e89eb63c9e756f82cb0bac3085ab80b4778eb990 tempo 129.2 duration 410.05 timbre -13.41 pitch 0.34 intensity -54.66 segments 56 frequency 267.09 key C4 name free-whitearmor-x-crystal-castles-x-thaiboy-digital-type-beat
free-witt-lowry-x-nf-type-beat-memories-hip-hop-rap-instrumental-2020-g-m-g-m-130-00_4b3907809b803b57b80b67fb80b24b6a14661199213d32c7acd91e0fd7dd58de tempo 129.2 duration 473.93 timbre -11.41 pitch 0.36 intensity -56.9 segments 74 frequency 81.64 key E2 name free-witt-lowry-x-nf-type-beat-memories-hip-hop-rap-instrumental-2020-g-m-g-m-130-00
free-xxxtentacion-type-beat-forever-emotional-sad-piano-rap-beat-2019_081bb9eb5de563a60d7bef01c36feed5758c200f5cac66dfbd5d70a88ecf4a2c tempo 129.2 duration 400.13 timbre -12.65 pitch 0.34 intensity -58.9 segments 75 frequency 393.56 key G4 name free-xxxtentacion-type-beat-forever-emotional-sad-piano-rap-beat-2019
free-xxxtentacion-x-lil-peep-type-beat-im-sorry-sad-guitar-instrumental-2019-g-m-g-m_cd260a84f796f76fff33e8911934cc6e4eaa7ec0d3bd0b890cb7e043e1832558 tempo 129.2 duration 343.37 timbre -10.5 pitch 0.39 intensity -57.59 segments 59 frequency 183.32 key F#3 name free-xxxtentacion-x-lil-peep-type-beat-im-sorry-sad-guitar-instrumental-2019-g-m-g-m
free-xxxtentacion-x-nf-type-beat-wishes-sad-rap-piano-instrumental-2019-g-m-g-m_55f306c8a95ac4bf7d90739449f0e27d31456cf4c696d4f3d9f4cb26798615cc tempo 126.05 duration 432.07 timbre -11.64 pitch 0.33 intensity -56.3 segments 93 frequency 156.68 key D#3 name free-xxxtentacion-x-nf-type-beat-wishes-sad-rap-piano-instrumental-2019-g-m-g-m
g-m-g-m-116-00_0789686c6614391ebb58d0b524b1cb472f2c81f6dd70bec447e319949638f173 tempo 114.84 duration 240.78 timbre -12.16 pitch 0.27 intensity -58.4 segments 47 frequency 175.32 key F3 name g-m-g-m-116-00
guccihighwaters-9tails-convolk-guardin-shinigami-lil-lotus-type-beat-sad-guitar_fee4136b71f10588c595e9d6c830637de01a5cf8359db292121112b2b4a0eabe tempo 129.2 duration 483.02 timbre -10.87 pitch 0.35 intensity -53.7 segments 82 frequency 304.4 key D#4 name guccihighwaters-9tails-convolk-guardin-shinigami-lil-lotus-type-beat-sad-guitar
gunner-prod-fantom-_e6b23d20b29b923d9951a3cdf006217003a9ab22d80cc18642db66581669bfe2 tempo 123.05 duration 302.79 timbre -10.2 pitch 0.39 intensity -57.58 segments 
30 frequency 70.31 key C#2 name gunner-prod-fantom-
hot-mulligan-tiny-moving-parts_b56d4e39828c3a73916074523c34b69a0bb9ae4d53630cd9d6893b42bb2b9914 tempo 123.05 duration 288.48 timbre -8.27 pitch 0.35 intensity -44.24 segments 49 frequency 212.55 key G#3 name hot-mulligan-tiny-moving-parts
i-miss-you-free-nf-x-ivan-b-type-beat-emotional-sad-instrumental-prod-starbeats-2019-g-m-g-m-125-00_f877bc649cb0a304f03fdbb965137b29b6844a5b5ed3abb68d7303f3c4722b09 tempo 126.05 duration 537.69 timbre -9.48 pitch 0.3 intensity -55.5 segments 81 frequency 153.23 key D#3 name i-miss-you-free-nf-x-ivan-b-type-beat-emotional-sad-instrumental-prod-starbeats-2019-g-m-g-m-125-00
i-miss-you-g-m-g-m_5888aa4efe963eca2694d28723c6ae2e2c7639caa3f842c2495eef85f0a9cf35 tempo 120.19 duration 357.28 timbre -12.12 pitch 0.3 intensity -54.9 segments 62 frequency 280.86 key C#4 name i-miss-you-g-m-g-m
ill-faded-prod-bassment-_b0b27b0cccae442b0f0f3bb13f3d8871c79210a8a2b4e590f544ce2079cf9a2d tempo 126.05 duration 320.16 timbre -12.08 pitch 0.39 intensity -56.05 segments 42 frequency 242.89 key B3 name ill-faded-prod-bassment-
illusions-soft-chill-rap-instrumental-atmospheric-trap-beat-2019-g-m-g-m_664a1b256bcd2f461d7d5b23526a696a2c7c46fdae2a24f93f67a3b2032bec3b tempo 136.0 duration 384.1 timbre -9.34 pitch 0.37 intensity -53.89 segments 54 frequency 72.87 key D2 name illusions-soft-chill-rap-instrumental-atmospheric-trap-beat-2019-g-m-g-m
is-love-bones-x-teamsesh-type-beat-prod-rareflowermp3-g-m-g-m_0936412db01ae4b1593bd0697ebf723552125152e2a10f4948c5cf0e9454584e tempo 129.2 duration 580.08 timbre -11.54 pitch 0.37 intensity -49.64 segments 76 frequency 241.86 key B3 name is-love-bones-x-teamsesh-type-beat-prod-rareflowermp3-g-m-g-m
ivan-b-x-witt-lowry-type-beat-shedding-my-tears-deep-storytelling-g-m-g-m_5e1ed52eff0e50d680e44d1d245c0ff3b873e75a0d0a319f9f21dfec3245a0ea tempo 126.05 duration 354.47 timbre -11.19 pitch 0.29 intensity -61.02 segments 58 frequency 142.89 key D3 name ivan-b-x-witt-lowry-type-beat-shedding-my-tears-deep-storytelling-g-m-g-m    
kevin-gates-x-future-type-beat-hate-me-iii-prod-by-mb13beatz-g-m-g-m_773c9df75276ea13fe03ba957fce3d360a5b802f7ec86191dfc3cb22560ab661 tempo 129.2 duration 540.04 timbre -12.12 pitch 0.29 intensity -57.73 segments 92 frequency 204.95 key G#3 name kevin-gates-x-future-type-beat-hate-me-iii-prod-by-mb13beatz-g-m-g-m
letter-2-the-weeknd_4d59a21756d8f88cbac9b330b347d1ca3abb2b05d67521108de4219f963a8dc4 tempo 126.05 duration 430.08 timbre -10.52 pitch 0.59 intensity -49.02 segments 54 frequency 245.85 key B3 name letter-2-the-weeknd
lipstick-prod-qb-trap-beat-for-singing_e38cbaabd562f84239d27034c28d10a1acea66f5a60c7b6ebd897dfeb1f48c5c tempo 132.51 duration 480.1 timbre -13.05 pitch 0.26 intensity -62.08 segments 69 frequency 99.02 key G2 name lipstick-prod-qb-trap-beat-for-singing
midwest-emo-type-beat_41e4cee0420bf1becfc09770dc95a4f2c6007f0cc768ec8dfd189c0419f36604 tempo 136.0 duration 406.08 timbre -11.64 pitch 0.27 intensity -59.74 segments 52 frequency 224.0 key A3 name midwest-emo-type-beat
new-year-prod-metlast-_2e06a190d773f0c2a8e1667f92969bcf0718cca2070c920a32b4bf0080107ff7 tempo 120.19 duration 288.25 timbre -11.9 pitch 0.28 intensity -60.38 segments 29 frequency 349.82 key F4 name new-year-prod-metlast-
nineteen_39d06763a0ff50d8553eba900b60c5ecc4a2f70b12083b98f546bccbcdbf333e tempo 136.0 duration 287.1 timbre -15.67 pitch 0.36 intensity -61.77 segments 33 frequency 256.04 key C4 name nineteen
nothing-nowhere-fats-e-iann-dior_259e5911ddd61c3faae1860d1bc8daaf97416ea805700edfbf6418823ea47227 tempo 136.0 duration 474.19 timbre -9.63 pitch 0.25 intensity -55.03 segments 63 frequency 121.45 key B2 name nothing-nowhere-fats-e-iann-dior
numb-g-m-g-m_185b1083d3ae30b7a0c539dc7dc7e5e20da4c5d9b11ce9a1b12ad8001c75d2b0 tempo 123.05 duration 504.12 timbre -12.14 pitch 0.31 intensity -57.66 segments 77 frequency 133.59 key C3 name numb-g-m-g-m
prod-capsctrl-silo-g-m-g-m_6c71eb80c1a8700ccd0ba117217e77c80fd2ee0007b470ffb9a71d23b729bbd8 tempo 120.19 duration 392.11 timbre -11.48 pitch 0.31 intensity -57.48 segments 63 frequency 268.18 key C4 name prod-capsctrl-silo-g-m-g-m
rain_cbf08b90a080cdec19295a666cf18eae5c913d88725e6cc9e76ed09a65766bfb tempo 129.2 duration 391.72 timbre -12.63 pitch 0.29 intensity -60.26 segments 61 frequency 77.21 key D#2 name rain
raptrap-beat-trapnew-school-instrumental-2019-prod-kyu-tracks-g-m-g-m_d2c06ebe76db5e6d0b6d02bda5a8a5ada73358d53ed3d4bb633358274fca67e6 tempo 126.05 duration 373.25 
timbre -9.86 pitch 0.27 intensity -53.4 segments 57 frequency 268.98 key C4 name raptrap-beat-trapnew-school-instrumental-2019-prod-kyu-tracks-g-m-g-m
ripsquad-x-nosgov-x-senses-x-bladee-type-beat-prod-ev333-_b3b015df97d837ef4b834c089d9b8e3545b360ba5c80e12214fc6756fe2ae739 tempo 123.05 duration 300.05 timbre -12.36 pitch 0.3 intensity -54.6 segments 46 frequency 457.15 key A#4 name ripsquad-x-nosgov-x-senses-x-bladee-type-beat-prod-ev333-
sad-ambient-piano-type-beat-piece-320-kbps-_643ca8237d17a55c06dad6aaaccd50882e348efa95cf88c1f049f8ffbafa20a6 tempo 120.19 duration 427.73 timbre -13.91 pitch 0.36 intensity -64.23 segments 69 frequency 281.38 key C#4 name sad-ambient-piano-type-beat-piece-320-kbps-
save-me-sad-piano-instrumental-2019_0f27a2faccd6dc111a74522a22572edebd975c726a23e8946ddd88d09d2a504d tempo 136.0 duration 427.34 timbre -12.84 pitch 0.3 intensity -60.38 segments 109 frequency 307.66 key D#4 name save-me-sad-piano-instrumental-2019
sold-dark-xxxtentacion-x-denzel-curry-type-beat-plague-trap-intrumental-2020_ed7882cdee3d26fe38ad55cac61ea079cd945c01484b0bf7918382fc6a857318 tempo 129.2 duration 304.08 timbre -10.23 pitch 0.44 intensity -54.77 segments 35 frequency 341.02 key F4 name sold-dark-xxxtentacion-x-denzel-curry-type-beat-plague-trap-intrumental-2020
sold-xxxtentacion-sad-lofi-type-beat-scars-ft-mishaal-g-m-g-m_e054b3218482c95fffbc2cc8c53c0c7a7f48fa4782c77393d3c0215800e67c55 tempo 120.19 duration 309.81 timbre -13.55 pitch 0.32 intensity -56.13 segments 43 frequency 285.71 key D4 name sold-xxxtentacion-sad-lofi-type-beat-scars-ft-mishaal-g-m-g-m
synth_d5637fa2aa32345a3792c1fa7c357cb31c2dd0e6b447340a5950c41b5dbd2b19 tempo 132.51 duration 290.19 timbre -11.68 pitch 0.4 intensity -56.12 segments 36 frequency 305.53 key D#4 name synth
time-free-nf-type-beat-emotional-sad-piano-instrumental-2019-prod-starbeats-g-m-g-m-g-m-135-00_da1fcece5188a3427a800a8a0191b14d2f67699293db80c5ea6b4e0c6f15f2f8 tempo 136.0 duration 551.19 timbre -11.44 pitch 0.43 intensity -54.57 segments 81 frequency 270.33 key C#4 name time-free-nf-type-beat-emotional-sad-piano-instrumental-2019-prod-starbeats-g-m-g-m-g-m-135-00
waifu_ca3105d05ff8fada0dbcd0a695cc40f8b2d3900175bf28c4a1cf75e8f95f17b1 tempo 126.05 duration 262.75 timbre -8.86 pitch 0.36 intensity -45.87 segments 45 frequency 187.13 key F#3 name waifu
zen_e88e86af4b2e47a4ea4e6d6a5f95455bc6b0acae99e117f644977ba71dac8bd2 tempo 114.84 duration 271.52 timbre -11.19 pitch 0.3 intensity -58.57 segments 60 frequency 173.46 key F3 name zen
--------------------------------------------------------------------------

C:\Users\Ninja\polymath>python polymath.py -a C:/Users/Ninja/polymath/input/tge/
2023-03-04 14:41:26.142923: W tensorflow/stream_executor/platform/default/dso_loader.cc:64] Could not load dynamic library 'cudart64_110.dll'; dlerror: cudart64_110.dll not found
2023-03-04 14:41:26.143930: I tensorflow/stream_executor/cuda/cudart_stub.cc:29] Ignore above cudart dlerror if you do not have a GPU set up on your machine.
---------------------------------------------------------------------------- 
--------------------------------- POLYMATH --------------------------------- 
----------------------------------------------------------------------------
add video: C:/Users/Ninja/polymath/input/tge/ to videos: 94
add directory with wav or mp3 files
Found 0 wav or mp3 files
------------------------------ Files in DB: 94 ------------------------------
a-letter-to-write_6efb86a5da47e3e7ad5c2a1242a080128b95e964f51f6efb22dce052c62df8af tempo 126.05 duration 472.14 timbre -7.86 pitch 0.35 intensity -40.98 segments 69 frequency 284.64 key C#4 name a-letter-to-write
cemeteries-and-greyhound-busses_68ee27932a358f0da40bed24e2d3d6c366056decb74299c7702fa431cdb96ac2 tempo 136.0 duration 551.14 timbre -8.21 pitch 0.48 intensity -42.58 segments 68 frequency 254.92 key C4 name cemeteries-and-greyhound-busses
diet-coke-and-mentos_2ebb90d50670d1153113d1314f640829bbeedfe9d0f35fd7bcf85ffc40c0a5cb tempo 120.19 duration 411.12 timbre -8.31 pitch 0.4 intensity -40.68 segments 
64 frequency 228.46 key A#3 name diet-coke-and-mentos
goodbye-mr-perfection_4ee19add8d0df6ac261b132da0163d67f94c1fa4c5145a0211bfb53f30968b37 tempo 143.55 duration 462.32 timbre -8.64 pitch 0.33 intensity -42.34 segments 68 frequency 263.09 key C4 name goodbye-mr-perfection
our-perfect-ending_7b949ba5a05cbb5030e6961a073dfbe6aeaabf62d8b8913fa2ad3c0e68eead68 tempo 139.67 duration 477.78 timbre -12.4 pitch 0.25 intensity -49.55 segments 76 frequency 235.66 key A#3 name our-perfect-ending
seven-days_dfd68b93e298ca6eeeba645e3e7eda8755fe3fc2436554821adbdca5da57d167 tempo 126.05 duration 370.31 timbre -7.79 pitch 0.44 intensity -38.7 segments 42 frequency 274.96 key C#4 name seven-days
the-great-escape_5f14bbc778ab78ebe0adff825fa96d0ea01c3385df3b5fdefce6ba8d3c15dec2 tempo 117.45 duration 416.97 timbre -7.65 pitch 0.41 intensity -42.24 segments 60 
frequency 258.09 key C4 name the-great-escape
view-of-coma_79fc23932086e9530542150c47857bb03b65b11d1fd7c455e2dd238eca100cfa tempo 107.67 duration 445.91 timbre -8.21 pitch 0.43 intensity -42.77 segments 64 frequency 222.6 key A3 name view-of-coma
when-open-air-becomes-a-battlefield_f922c336e1eefdb69496e4a2fb030652728be6ad7c99bc34be4d5a09960ffc11 tempo 152.0 duration 386.21 timbre -7.9 pitch 0.44 intensity -38.7 segments 45 frequency 293.47 key D4 name when-open-air-becomes-a-battlefield
100-free-xxxtentacion-type-beat-angel-raptrap-instrumental_b20fc5ffacc2737c7880e3ba9b79c3c74d82195151c93482c31169890ed1d330 tempo 120.19 duration 361.04 timbre -14.53 pitch 0.44 intensity -58.9 segments 50 frequency 334.44 key E4 name 100-free-xxxtentacion-type-beat-angel-raptrap-instrumental
130-01_f1c3e675d845fe1f825a670fbcfcf8810a504890da960574b434cca88e094104 tempo 129.2 duration 458.26 timbre -12.01 pitch 0.22 intensity -59.66 segments 66 frequency 
233.78 key A#3 name 130-01
be-yourself_37ad5163700b7faa927526b2e48a11b76835c4a5776a6664cb086f2bb33d5009 tempo 114.84 duration 496.87 timbre -8.2 pitch 0.39 intensity -46.33 segments 76 frequency 263.74 key C4 name be-yourself
breathe_c3916db375d4e9b22565ae65367646472770dcce0b494c92b26aa82d453511ce tempo 126.05 duration 390.02 timbre -9.68 pitch 0.42 intensity -50.33 segments 67 frequency 207.7 key G#3 name breathe
cold-trap-beat-instrumental-trap-type-beat-prod-by-gherah-g-m-g-m_a3737d5654ccd679e6407db611d58bd2aeeab6101bce49a870159d103e7a1355 tempo 120.19 duration 360.97 timbre -11.72 pitch 0.27 intensity -54.64 segments 39 frequency 662.82 key E5 name cold-trap-beat-instrumental-trap-type-beat-prod-by-gherah-g-m-g-m
diabla-trap-beat-emotional-bryant-mayers-mike-beatz-g-m-g-m_78ddf057fea8a69b45bb5b56cf9d978d6613722fcb1b2072f5b60b7edf9bfbbd tempo 86.13 duration 346.01 timbre -10.99 pitch 0.28 intensity -56.76 segments 48 frequency 215.0 key A3 name diabla-trap-beat-emotional-bryant-mayers-mike-beatz-g-m-g-m
disaster_590e25b9f3eb4ef3102e0f7e5887237886296dc6a162670b20b21ddbff983bdc tempo 132.51 duration 315.36 timbre -11.24 pitch 0.29 intensity -57.96 segments 45 frequency 153.13 key D#3 name disaster
drops_41baa90392281d60931ae009a0b2ad5727288707e94fab59c75033e04f1b8d61 tempo 120.19 duration 180.48 timbre -13.47 pitch 0.35 intensity -54.55 segments 29 frequency 
298.6 key D4 name drops
ea7-sad-lofi-piano-type-beat-320-kbps-_3e3261c31899b53111fdf6a38dc9a41163ad61948281f9e32c75887f3686ba28 tempo 129.2 duration 405.94 timbre -11.69 pitch 0.43 intensity -60.82 segments 55 frequency 186.59 key F#3 name ea7-sad-lofi-piano-type-beat-320-kbps-
enough_641750e90ad696c3c7da3ac8a6eb3c925e459b75a05cf4550ae81e11abeae479 tempo 132.51 duration 269.02 timbre -12.25 pitch 0.3 intensity -52.89 segments 46 frequency 
285.66 key D4 name enough
free-6lack-type-beat-piano-ambient-instrumental-no-connection-2019-g-m-g-m_ceaf5ecaa0314b5c6edf4b28829041dcfba2b05cb4ffdcc92b8f7f6f4ecd82c9 tempo 114.84 duration 432.39 timbre -13.62 pitch 0.25 intensity -59.58 segments 73 frequency 209.21 key G#3 name free-6lack-type-beat-piano-ambient-instrumental-no-connection-2019-g-m-g-m 
free-alternative-rock-type-beat-prod-useless-320-kbps-g-m-g-m_1121fdde50d6f160892868bc4f7894f240ce5ddbfb726cab9461d8b2db3bddb6 tempo 129.2 duration 295.73 timbre -10.47 pitch 0.31 intensity -52.05 segments 44 frequency 276.59 key C#4 name free-alternative-rock-type-beat-prod-useless-320-kbps-g-m-g-m
free-balcony-bones-x-6dogs-type-beat-prod-bleach-g-m-g-m_eb64a24bbaf033d57b0dfa05f80fd6b6fac24fc5b3a1715cb526cc3d857b071c tempo 136.0 duration 263.5 timbre -11.82 pitch 0.27 intensity -61.12 segments 29 frequency 177.36 key F3 name free-balcony-bones-x-6dogs-type-beat-prod-bleach-g-m-g-m
free-bladee-x-capoxxo-hyperpop-type-beat-redo-prod-pro-z-_faaa4050e487ad959a070f4dc25652223c920901d0c704cd5566f54de2bb7f86 tempo 129.2 duration 236.6 timbre -12.31 
pitch 0.26 intensity -57.95 segments 25 frequency 243.59 key B3 name free-bladee-x-capoxxo-hyperpop-type-beat-redo-prod-pro-z-
free-bones-type-beat-ashes-prod-ojhi_a3fdf5f3c06d1df2ae42b84f1cca986b5f98333897f183c5f2cb59118f69ecf7 tempo 129.2 duration 358.09 timbre -13.71 pitch 0.35 intensity -56.7 segments 50 frequency 508.62 key C5 name free-bones-type-beat-ashes-prod-ojhi
free-bones-type-beat-purple-trees-prod-seshtillirest-_05b2db8eff84808e0f1a44be508fa6027799143b62f576da0f5ad438e566618e tempo 120.19 duration 333.02 timbre -12.21 pitch 0.28 intensity -53.62 segments 57 frequency 317.79 key D#4 name free-bones-type-beat-purple-trees-prod-seshtillirest-
free-bones-x-lil-peep-type-beat-falling-asleep-prod-yago-g-m-g-m_ccf8a999b3cbe65745eedb25645954eaa1904365319462a04517d9f960104f6c tempo 120.19 duration 324.1 timbre -10.13 pitch 0.36 intensity -48.92 segments 40 frequency 238.82 key A#3 name free-bones-x-lil-peep-type-beat-falling-asleep-prod-yago-g-m-g-m
free-bones-x-lil-peep-x-greaf-type-beat-amazing-prod-seshtillirest-g-m-g-m_9285924f32bedae35254a1ae06c203f2b12067344bcb6ab46127b7ccc446af47 tempo 129.2 duration 360.23 timbre -13.32 pitch 0.38 intensity -60.22 segments 49 frequency 277.42 key C#4 name free-bones-x-lil-peep-x-greaf-type-beat-amazing-prod-seshtillirest-g-m-g-m  
free-capoxxo-x-syko-x-oaf1-hyperpop-type-beat-underworld-prod-pro-z-_8cef0bedf65434e7f1e76b5732a49708aae9881d3ee639e62418aa93cbda3e8f tempo 136.0 duration 249.47 timbre -10.13 pitch 0.45 intensity -47.49 segments 29 frequency 374.09 key F#4 name free-capoxxo-x-syko-x-oaf1-hyperpop-type-beat-underworld-prod-pro-z-
free-chill-x-sad-jhene-aiko-type-beat-rnb-instrumental-2019-early-in-the-morning-g-m-g-m_dd473358d39e95948044c7da1b151b88f3578396fa57cfc1557163a95f8a5a19 tempo 123.05 duration 533.03 timbre -14.65 pitch 0.36 intensity -62.15 segments 81 frequency 344.04 key F4 name free-chill-x-sad-jhene-aiko-type-beat-rnb-instrumental-2019-early-in-the-morning-g-m-g-m
free-digital-original-god-x-angst-x-hellasketchy-type-beat-prod-loopy-g-m-g-m_41580b40da8123f069aabaca336c36df04db53a77da64e1bdea9459a8b8d1b56 tempo 126.05 duration 310.13 timbre -9.97 pitch 0.35 intensity -53.63 segments 43 frequency 217.82 key A3 name free-digital-original-god-x-angst-x-hellasketchy-type-beat-prod-loopy-g-m-g-m
free-ecco2k-x-deadmau5-x-crystal-castles-type-beat-sangang_899d3c266e228c33a7d73b78ca6574c86de02e89586bf299b2b4c09058e2dab2 tempo 123.05 duration 420.02 timbre -11.69 pitch 0.31 intensity -46.31 segments 96 frequency 432.17 key A4 name free-ecco2k-x-deadmau5-x-crystal-castles-type-beat-sangang
free-for-profit-hatred-part-2-lil-peep-x-xxxtentacion-type-beat-g-m-g-m_e411e9feb0927f5747028f079f9ea09e9c75326f0e2e8de1ace48739f0e3aaef tempo 123.05 duration 385.67 timbre -11.75 pitch 0.34 intensity -55.37 segments 57 frequency 218.3 key A3 name free-for-profit-hatred-part-2-lil-peep-x-xxxtentacion-type-beat-g-m-g-m
free-for-profit-hyperpop-x-glitchcore-x-lxner-type-beat-synth-prod-soft-clipper-pn_65c44a347f1e5a7509dbd36ac4b1466baad77f4717126a917a0924fe28b66334 tempo 132.51 duration 290.3 timbre -11.46 pitch 0.39 intensity -55.12 segments 41 frequency 314.03 key D#4 name free-for-profit-hyperpop-x-glitchcore-x-lxner-type-beat-synth-prod-soft-clipper-pn
free-for-profit-open-ended-alternative-rock-type-beat_b195caeabdaf42fb1044359add520fd01378da6389e2b92ed057f96572cc76c5 tempo 132.51 duration 306.04 timbre -11.54 pitch 0.46 intensity -48.55 segments 38 frequency 206.14 key G#3 name free-for-profit-open-ended-alternative-rock-type-beat
free-for-profit-witt-lowry-hurt-type-beat-longing-g-m-g-m_0210ef59a8fa64a0092a73e2ee4606449a8e01e3377baebdb7e84888f852168a tempo 129.2 duration 429.03 timbre -12.44 pitch 0.32 intensity -61.69 segments 67 frequency 366.1 key F#4 name free-for-profit-witt-lowry-hurt-type-beat-longing-g-m-g-m
free-guilt-alt-rock-lil-peep-x-nothing-nowhere-type-beat-prod-loopy-g-m-g-m_b3bd210d80f777cc2bbfcb9a2ec6f50750cbc5408dadb0208a4e48abbc0ca83a tempo 114.84 duration 310.13 timbre -15.54 pitch 0.36 intensity -64.17 segments 62 frequency 238.62 key A#3 name free-guilt-alt-rock-lil-peep-x-nothing-nowhere-type-beat-prod-loopy-g-m-g-m
free-gunna-x-lil-baby-type-beat-at-sea-trap-instrumental-2020_e2605169cc469fadde84792b0ce0c1946a782d299bd63b1a677f9295da101807 tempo 129.2 duration 396.22 timbre -11.13 pitch 0.4 intensity -56.62 segments 56 frequency 404.79 key G#4 name free-gunna-x-lil-baby-type-beat-at-sea-trap-instrumental-2020
free-juice-wrld-x-iann-dior-type-beat-reality_a27f934e1119b3679217b05dcd417f1e5a3ad3c8c1b2e63ab1a94ba6055fe391 tempo 129.2 duration 331.36 timbre -11.78 pitch 0.29 
intensity -57.32 segments 48 frequency 223.58 key A3 name free-juice-wrld-x-iann-dior-type-beat-reality
free-juice-wrld-x-iann-dior-type-beat-reborn-trap-instrumental-2020_9fa29fe52fba614133eaa8f04e95e96e4d03edff52b53af9e2ce46c3f9fb9db7 tempo 129.2 duration 336.03 timbre -10.76 pitch 0.37 intensity -54.59 segments 42 frequency 96.5 key G2 name free-juice-wrld-x-iann-dior-type-beat-reborn-trap-instrumental-2020
free-lil-peep-x-coldhart-x-horse-head-x-wicca-phase-type-beat-mistakes-prod-metlastmp3-g-m-g-m_d9694fe1ae9068e9900d8fb76e988e647105f2310e0f4210b2bb1f556c21b53a tempo 120.19 duration 330.08 timbre -12.99 pitch 0.29 intensity -58.87 segments 60 frequency 287.71 key D4 name free-lil-peep-x-coldhart-x-horse-head-x-wicca-phase-type-beat-mistakes-prod-metlastmp3-g-m-g-m
free-lil-peep-x-horse-head-x-lil-lotus-x-smrtdeath-type-beat-midnight-prod-metlast-b-135-00_54224408ed8149b51e9e48844ebf11b7768fa44bf90a69a191fc2f92ed1df2ce tempo 136.0 duration 320.16 timbre -12.25 pitch 0.29 intensity -63.89 segments 48 frequency 103.17 key G#2 name free-lil-peep-x-horse-head-x-lil-lotus-x-smrtdeath-type-beat-midnight-prod-metlast-b-135-00
free-lil-peep-x-lil-tracy-type-beat-heart-hurt-sad-guitar-instrumental-2019-g-m-g-m_2731d94a8c1c5ef18f2739493c886e8f1c7112e05ee70d0d16d93c4cec258c7d tempo 136.0 duration 455.25 timbre -14.12 pitch 0.27 intensity -65.04 segments 64 frequency 185.31 key F#3 name free-lil-peep-x-lil-tracy-type-beat-heart-hurt-sad-guitar-instrumental-2019-g-m-g-m
free-mac-miller-x-j-cole-type-beat-mirrors-2020_b89ce2151bae8d1fce643482e9857d6c8b4a6a9940440dc2925349aae1f8e898 tempo 120.19 duration 404.02 timbre -14.07 pitch 0.48 intensity -63.87 segments 87 frequency 322.16 key E4 name free-mac-miller-x-j-cole-type-beat-mirrors-2020
free-metalcore-x-melodic-post-hardcore-type-beat-dark-horse-melodic-metalcore-instrumental_5ea9250320d2b426a89330e14901d0fee31315cb2da5954c3b450fbb5233a961 tempo 132.51 duration 268.04 timbre -7.72 pitch 0.45 intensity -43.94 segments 33 frequency 238.74 key A#3 name free-metalcore-x-melodic-post-hardcore-type-beat-dark-horse-melodic-metalcore-instrumental
free-no-friends-juice-wrld-x-lil-mosey-x-lil-skies-type-beat-2019-prod-kcaaz-g-m-g-m_0e450b7477e21b8c76723e0fc075a0f57a69bb5dcaff6978d170160ec641de6a tempo 136.0 duration 362.62 timbre -11.49 pitch 0.27 intensity -59.82 segments 39 frequency 127.33 key C3 name free-no-friends-juice-wrld-x-lil-mosey-x-lil-skies-type-beat-2019-prod-kcaaz-g-m-g-m
free-nothing-nowhere-tothegood-lil-lotus-type-beat-i-can-t-leave-yet-prod-remghost-_e93134232c6187318d35e7f57e15c494115ae47be35229b00e96f84925f32421 tempo 120.19 duration 288.59 timbre -10.49 pitch 0.25 intensity -58.26 segments 38 frequency 76.53 key D#2 name free-nothing-nowhere-tothegood-lil-lotus-type-beat-i-can-t-leave-yet-prod-remghost-
free-nothing-nowhere-x-family-pet-x-shinigami-type-beat-keep-it-together-prod-suttee-_d9192fd92c08baa0dbd71822763e21fb0167269181b701373557411cbf44f0c8 tempo 120.19 
duration 324.1 timbre -9.98 pitch 0.38 intensity -51.83 segments 66 frequency 231.54 key A#3 name free-nothing-nowhere-x-family-pet-x-shinigami-type-beat-keep-it-together-prod-suttee-
free-phora-ft-post-malone-type-beat-diamonds-instrumental-2019-g-m-g-m_f20887d1167fb52b61004b77f148bfc2a9ef5800962cf9824ba11aa7061ad9be tempo 114.84 duration 474.12 timbre -14.12 pitch 0.28 intensity -67.4 segments 56 frequency 215.45 key A3 name free-phora-ft-post-malone-type-beat-diamonds-instrumental-2019-g-m-g-m
free-pnb-rock-x-lil-tjay-type-beat-2019-broke-me-prod-midlowbeats-g-m-g-m_dc8662cbb9ca2d845b37b026bfe324c2eba3dbc7ad713ae7fe02b1e1a144feae tempo 129.2 duration 480.22 timbre -10.89 pitch 0.27 intensity -61.51 segments 65 frequency 117.69 key A#2 name free-pnb-rock-x-lil-tjay-type-beat-2019-broke-me-prod-midlowbeats-g-m-g-m    
free-pop-punk-emo-scenecore-type-beat-almost-had-u-pn_feb7e9b184fddb4e920e4f3bd8adb91e9c1442cdf39d938798f405a19ab0941d tempo 129.2 duration 390.14 timbre -8.03 pitch 0.39 intensity -40.23 segments 57 frequency 249.77 key B3 name free-pop-punk-emo-scenecore-type-beat-almost-had-u-pn
free-pop-rock-mgk-x-jxdn-x-iann-dior-pop-punk-type-beat-still-here_73cf7504165037f75db1090e9b55f02e19b6809137fa825b11cacb915bec980f tempo 126.05 duration 372.59 timbre -8.58 pitch 0.45 intensity -49.6 segments 56 frequency 77.03 key D#2 name free-pop-rock-mgk-x-jxdn-x-iann-dior-pop-punk-type-beat-still-here
free-post-malone-guitar-type-beat-apologize-pop-instrumental-2019_a55e6f0ce28d3bcdcbfc31e8f1722a5b6aded62d0817ad43cb32c89f514a6e03 tempo 117.45 duration 460.09 timbre -12.14 pitch 0.24 intensity -63.71 segments 55 frequency 178.87 key F3 name free-post-malone-guitar-type-beat-apologize-pop-instrumental-2019
free-sad-chill-jazzy-type-beat-emma-prod-noria-beats-_e96d131ae2d8290b5f031c1702ea00c9fa6ed169e52103fa551e5e1151c45651 tempo 136.0 duration 458.64 timbre -12.81 pitch 0.29 intensity -63.12 segments 95 frequency 136.79 key C#3 name free-sad-chill-jazzy-type-beat-emma-prod-noria-beats-
free-sad-chill-lofi-type-beat-emotional-deep-piano-trap-2019-_15b9aac06093456ebc5dd245b46b270facf18d890e979bed55b6c17c2cfdb85f tempo 126.05 duration 434.17 timbre -13.58 pitch 0.26 intensity -66.62 segments 65 frequency 234.29 key A#3 name free-sad-chill-lofi-type-beat-emotional-deep-piano-trap-2019-
free-sad-guitar-xxxtentacion-x-lil-peep-type-beat-lakes-pn_ac78d876ffba367a63ff8196f326808ec1d40627ee25d5e229195b9704abe055 tempo 123.05 duration 567.31 timbre -12.0 pitch 0.24 intensity -56.68 segments 119 frequency 360.9 key F#4 name free-sad-guitar-xxxtentacion-x-lil-peep-type-beat-lakes-pn
free-sad-xxxtentacion-type-beat-fly-prod-xenshel-_3c8a2bcd3e39526ad308f4cf2b47acf16e7162a3180d85e15cd02b58cd482030 tempo 120.19 duration 212.15 timbre -10.41 pitch 
0.25 intensity -57.41 segments 31 frequency 227.17 key A#3 name free-sad-xxxtentacion-type-beat-fly-prod-xenshel-
free-scenecore-x-rave-x-hyperpop-type-beat-opals-prod-pro-z-_19431a48572226ddda07c68015a73371f08d41990ff56b919bd9698706a4f0ab tempo 136.0 duration 249.74 timbre -9.1 pitch 0.63 intensity -47.35 segments 41 frequency 318.81 key D#4 name free-scenecore-x-rave-x-hyperpop-type-beat-opals-prod-pro-z-
free-scenecore-x-rave-x-hyperpop-type-beat-unseen-forces-prod-pro-z-_fa186c820758c9380592cd777cfc69cabdcfe29018ad27702745cce1518a43c5 tempo 136.0 duration 239.53 timbre -9.31 pitch 0.53 intensity -46.55 segments 40 frequency 133.58 key C3 name free-scenecore-x-rave-x-hyperpop-type-beat-unseen-forces-prod-pro-z-
free-uicideboy-x-pouya-type-beat-other-body-prod-eykey-beats-x-phil-good-beats-g-m-g-m-g-m_46e33e55c61ca5f35dacef7d6b31136abff4d1f13842e83c8aa878bfc1c3b926 tempo 132.51 duration 294.67 timbre -8.97 pitch 0.31 intensity -50.94 segments 46 frequency 241.73 key B3 name free-uicideboy-x-pouya-type-beat-other-body-prod-eykey-beats-x-phil-good-beats-g-m-g-m-g-m
free-whitearmor-x-crystal-castles-x-thaiboy-digital-type-beat_9a4ac66e722140b5f910dc21e89eb63c9e756f82cb0bac3085ab80b4778eb990 tempo 129.2 duration 410.05 timbre -13.41 pitch 0.34 intensity -54.66 segments 56 frequency 267.09 key C4 name free-whitearmor-x-crystal-castles-x-thaiboy-digital-type-beat
free-witt-lowry-x-nf-type-beat-memories-hip-hop-rap-instrumental-2020-g-m-g-m-130-00_4b3907809b803b57b80b67fb80b24b6a14661199213d32c7acd91e0fd7dd58de tempo 129.2 duration 473.93 timbre -11.41 pitch 0.36 intensity -56.9 segments 74 frequency 81.64 key E2 name free-witt-lowry-x-nf-type-beat-memories-hip-hop-rap-instrumental-2020-g-m-g-m-130-00
free-xxxtentacion-type-beat-forever-emotional-sad-piano-rap-beat-2019_081bb9eb5de563a60d7bef01c36feed5758c200f5cac66dfbd5d70a88ecf4a2c tempo 129.2 duration 400.13 timbre -12.65 pitch 0.34 intensity -58.9 segments 75 frequency 393.56 key G4 name free-xxxtentacion-type-beat-forever-emotional-sad-piano-rap-beat-2019
free-xxxtentacion-x-lil-peep-type-beat-im-sorry-sad-guitar-instrumental-2019-g-m-g-m_cd260a84f796f76fff33e8911934cc6e4eaa7ec0d3bd0b890cb7e043e1832558 tempo 129.2 duration 343.37 timbre -10.5 pitch 0.39 intensity -57.59 segments 59 frequency 183.32 key F#3 name free-xxxtentacion-x-lil-peep-type-beat-im-sorry-sad-guitar-instrumental-2019-g-m-g-m
free-xxxtentacion-x-nf-type-beat-wishes-sad-rap-piano-instrumental-2019-g-m-g-m_55f306c8a95ac4bf7d90739449f0e27d31456cf4c696d4f3d9f4cb26798615cc tempo 126.05 duration 432.07 timbre -11.64 pitch 0.33 intensity -56.3 segments 93 frequency 156.68 key D#3 name free-xxxtentacion-x-nf-type-beat-wishes-sad-rap-piano-instrumental-2019-g-m-g-m
g-m-g-m-116-00_0789686c6614391ebb58d0b524b1cb472f2c81f6dd70bec447e319949638f173 tempo 114.84 duration 240.78 timbre -12.16 pitch 0.27 intensity -58.4 segments 47 frequency 175.32 key F3 name g-m-g-m-116-00
guccihighwaters-9tails-convolk-guardin-shinigami-lil-lotus-type-beat-sad-guitar_fee4136b71f10588c595e9d6c830637de01a5cf8359db292121112b2b4a0eabe tempo 129.2 duration 483.02 timbre -10.87 pitch 0.35 intensity -53.7 segments 82 frequency 304.4 key D#4 name guccihighwaters-9tails-convolk-guardin-shinigami-lil-lotus-type-beat-sad-guitar
gunner-prod-fantom-_e6b23d20b29b923d9951a3cdf006217003a9ab22d80cc18642db66581669bfe2 tempo 123.05 duration 302.79 timbre -10.2 pitch 0.39 intensity -57.58 segments 
30 frequency 70.31 key C#2 name gunner-prod-fantom-
hot-mulligan-tiny-moving-parts_b56d4e39828c3a73916074523c34b69a0bb9ae4d53630cd9d6893b42bb2b9914 tempo 123.05 duration 288.48 timbre -8.27 pitch 0.35 intensity -44.24 segments 49 frequency 212.55 key G#3 name hot-mulligan-tiny-moving-parts
i-miss-you-free-nf-x-ivan-b-type-beat-emotional-sad-instrumental-prod-starbeats-2019-g-m-g-m-125-00_f877bc649cb0a304f03fdbb965137b29b6844a5b5ed3abb68d7303f3c4722b09 tempo 126.05 duration 537.69 timbre -9.48 pitch 0.3 intensity -55.5 segments 81 frequency 153.23 key D#3 name i-miss-you-free-nf-x-ivan-b-type-beat-emotional-sad-instrumental-prod-starbeats-2019-g-m-g-m-125-00
i-miss-you-g-m-g-m_5888aa4efe963eca2694d28723c6ae2e2c7639caa3f842c2495eef85f0a9cf35 tempo 120.19 duration 357.28 timbre -12.12 pitch 0.3 intensity -54.9 segments 62 frequency 280.86 key C#4 name i-miss-you-g-m-g-m
ill-faded-prod-bassment-_b0b27b0cccae442b0f0f3bb13f3d8871c79210a8a2b4e590f544ce2079cf9a2d tempo 126.05 duration 320.16 timbre -12.08 pitch 0.39 intensity -56.05 segments 42 frequency 242.89 key B3 name ill-faded-prod-bassment-
illusions-soft-chill-rap-instrumental-atmospheric-trap-beat-2019-g-m-g-m_664a1b256bcd2f461d7d5b23526a696a2c7c46fdae2a24f93f67a3b2032bec3b tempo 136.0 duration 384.1 timbre -9.34 pitch 0.37 intensity -53.89 segments 54 frequency 72.87 key D2 name illusions-soft-chill-rap-instrumental-atmospheric-trap-beat-2019-g-m-g-m
is-love-bones-x-teamsesh-type-beat-prod-rareflowermp3-g-m-g-m_0936412db01ae4b1593bd0697ebf723552125152e2a10f4948c5cf0e9454584e tempo 129.2 duration 580.08 timbre -11.54 pitch 0.37 intensity -49.64 segments 76 frequency 241.86 key B3 name is-love-bones-x-teamsesh-type-beat-prod-rareflowermp3-g-m-g-m
ivan-b-x-witt-lowry-type-beat-shedding-my-tears-deep-storytelling-g-m-g-m_5e1ed52eff0e50d680e44d1d245c0ff3b873e75a0d0a319f9f21dfec3245a0ea tempo 126.05 duration 354.47 timbre -11.19 pitch 0.29 intensity -61.02 segments 58 frequency 142.89 key D3 name ivan-b-x-witt-lowry-type-beat-shedding-my-tears-deep-storytelling-g-m-g-m    
kevin-gates-x-future-type-beat-hate-me-iii-prod-by-mb13beatz-g-m-g-m_773c9df75276ea13fe03ba957fce3d360a5b802f7ec86191dfc3cb22560ab661 tempo 129.2 duration 540.04 timbre -12.12 pitch 0.29 intensity -57.73 segments 92 frequency 204.95 key G#3 name kevin-gates-x-future-type-beat-hate-me-iii-prod-by-mb13beatz-g-m-g-m
letter-2-the-weeknd_4d59a21756d8f88cbac9b330b347d1ca3abb2b05d67521108de4219f963a8dc4 tempo 126.05 duration 430.08 timbre -10.52 pitch 0.59 intensity -49.02 segments 54 frequency 245.85 key B3 name letter-2-the-weeknd
lipstick-prod-qb-trap-beat-for-singing_e38cbaabd562f84239d27034c28d10a1acea66f5a60c7b6ebd897dfeb1f48c5c tempo 132.51 duration 480.1 timbre -13.05 pitch 0.26 intensity -62.08 segments 69 frequency 99.02 key G2 name lipstick-prod-qb-trap-beat-for-singing
midwest-emo-type-beat_41e4cee0420bf1becfc09770dc95a4f2c6007f0cc768ec8dfd189c0419f36604 tempo 136.0 duration 406.08 timbre -11.64 pitch 0.27 intensity -59.74 segments 52 frequency 224.0 key A3 name midwest-emo-type-beat
new-year-prod-metlast-_2e06a190d773f0c2a8e1667f92969bcf0718cca2070c920a32b4bf0080107ff7 tempo 120.19 duration 288.25 timbre -11.9 pitch 0.28 intensity -60.38 segments 29 frequency 349.82 key F4 name new-year-prod-metlast-
nineteen_39d06763a0ff50d8553eba900b60c5ecc4a2f70b12083b98f546bccbcdbf333e tempo 136.0 duration 287.1 timbre -15.67 pitch 0.36 intensity -61.77 segments 33 frequency 256.04 key C4 name nineteen
nothing-nowhere-fats-e-iann-dior_259e5911ddd61c3faae1860d1bc8daaf97416ea805700edfbf6418823ea47227 tempo 136.0 duration 474.19 timbre -9.63 pitch 0.25 intensity -55.03 segments 63 frequency 121.45 key B2 name nothing-nowhere-fats-e-iann-dior
numb-g-m-g-m_185b1083d3ae30b7a0c539dc7dc7e5e20da4c5d9b11ce9a1b12ad8001c75d2b0 tempo 123.05 duration 504.12 timbre -12.14 pitch 0.31 intensity -57.66 segments 77 frequency 133.59 key C3 name numb-g-m-g-m
prod-capsctrl-silo-g-m-g-m_6c71eb80c1a8700ccd0ba117217e77c80fd2ee0007b470ffb9a71d23b729bbd8 tempo 120.19 duration 392.11 timbre -11.48 pitch 0.31 intensity -57.48 segments 63 frequency 268.18 key C4 name prod-capsctrl-silo-g-m-g-m
rain_cbf08b90a080cdec19295a666cf18eae5c913d88725e6cc9e76ed09a65766bfb tempo 129.2 duration 391.72 timbre -12.63 pitch 0.29 intensity -60.26 segments 61 frequency 77.21 key D#2 name rain
raptrap-beat-trapnew-school-instrumental-2019-prod-kyu-tracks-g-m-g-m_d2c06ebe76db5e6d0b6d02bda5a8a5ada73358d53ed3d4bb633358274fca67e6 tempo 126.05 duration 373.25 
timbre -9.86 pitch 0.27 intensity -53.4 segments 57 frequency 268.98 key C4 name raptrap-beat-trapnew-school-instrumental-2019-prod-kyu-tracks-g-m-g-m
ripsquad-x-nosgov-x-senses-x-bladee-type-beat-prod-ev333-_b3b015df97d837ef4b834c089d9b8e3545b360ba5c80e12214fc6756fe2ae739 tempo 123.05 duration 300.05 timbre -12.36 pitch 0.3 intensity -54.6 segments 46 frequency 457.15 key A#4 name ripsquad-x-nosgov-x-senses-x-bladee-type-beat-prod-ev333-
sad-ambient-piano-type-beat-piece-320-kbps-_643ca8237d17a55c06dad6aaaccd50882e348efa95cf88c1f049f8ffbafa20a6 tempo 120.19 duration 427.73 timbre -13.91 pitch 0.36 intensity -64.23 segments 69 frequency 281.38 key C#4 name sad-ambient-piano-type-beat-piece-320-kbps-
save-me-sad-piano-instrumental-2019_0f27a2faccd6dc111a74522a22572edebd975c726a23e8946ddd88d09d2a504d tempo 136.0 duration 427.34 timbre -12.84 pitch 0.3 intensity -60.38 segments 109 frequency 307.66 key D#4 name save-me-sad-piano-instrumental-2019
sold-dark-xxxtentacion-x-denzel-curry-type-beat-plague-trap-intrumental-2020_ed7882cdee3d26fe38ad55cac61ea079cd945c01484b0bf7918382fc6a857318 tempo 129.2 duration 304.08 timbre -10.23 pitch 0.44 intensity -54.77 segments 35 frequency 341.02 key F4 name sold-dark-xxxtentacion-x-denzel-curry-type-beat-plague-trap-intrumental-2020
sold-xxxtentacion-sad-lofi-type-beat-scars-ft-mishaal-g-m-g-m_e054b3218482c95fffbc2cc8c53c0c7a7f48fa4782c77393d3c0215800e67c55 tempo 120.19 duration 309.81 timbre -13.55 pitch 0.32 intensity -56.13 segments 43 frequency 285.71 key D4 name sold-xxxtentacion-sad-lofi-type-beat-scars-ft-mishaal-g-m-g-m
synth_d5637fa2aa32345a3792c1fa7c357cb31c2dd0e6b447340a5950c41b5dbd2b19 tempo 132.51 duration 290.19 timbre -11.68 pitch 0.4 intensity -56.12 segments 36 frequency 305.53 key D#4 name synth
time-free-nf-type-beat-emotional-sad-piano-instrumental-2019-prod-starbeats-g-m-g-m-g-m-135-00_da1fcece5188a3427a800a8a0191b14d2f67699293db80c5ea6b4e0c6f15f2f8 tempo 136.0 duration 551.19 timbre -11.44 pitch 0.43 intensity -54.57 segments 81 frequency 270.33 key C#4 name time-free-nf-type-beat-emotional-sad-piano-instrumental-2019-prod-starbeats-g-m-g-m-g-m-135-00
waifu_ca3105d05ff8fada0dbcd0a695cc40f8b2d3900175bf28c4a1cf75e8f95f17b1 tempo 126.05 duration 262.75 timbre -8.86 pitch 0.36 intensity -45.87 segments 45 frequency 187.13 key F#3 name waifu
zen_e88e86af4b2e47a4ea4e6d6a5f95455bc6b0acae99e117f644977ba71dac8bd2 tempo 114.84 duration 271.52 timbre -11.19 pitch 0.3 intensity -58.57 segments 60 frequency 173.46 key F3 name zen
--------------------------------------------------------------------------

C:\Users\Ninja\polymath>    

```
