# Performance Notes

Notes on various programming performance improvements methods I learned. This will generally contain topic, brief description and may have links for detailed exploration.

This needs to improved as it may have mistakes and some texts needs to separated to appropriate categories to be more meaningful. Also need to fix duplicates of same text in multiple categories.

# Language Independent Concepts

- Todo.

# Python

- Use python 3.11+ as there are [reported improvement](https://docs.python.org/3/whatsnew/3.11.html) in speed.
- Use [dis module](https://docs.python.org/3/library/dis.html) of python to disassemble and inspect bytecode.

# C++

- Use compiler optimization flags. In gcc compiler there are [flags](https://www.rapidtables.com/code/linux/gcc/gcc-o.html) like `-O2`, `-O3` and others. There is tradeoff between compile time, memory usage, code size vs execution time.

# Pytorch 

### Pytorch Low Memory Training and Inference

Good resources, [huggingface performance](https://huggingface.co/docs/transformers/performance), [single gpu guide](https://huggingface.co/docs/transformers/perf_train_gpu_one) and [deepspeed guide](https://huggingface.co/docs/transformers/main_classes/deepspeed).

- Gradient checkpointing selected modules lowering vram requirement at the cost of speed. 
- During training set batch size to 1 and accumulate gradient in loop N times at the cost of training speed.
- During inference set batch size to 1.
- Set torch to eval mode during inference.
- Use torch.no_grad() during inference.
- Delete models or other memory intersive calculated variables with del, then garbage collect and cuda empty cache. Often deleting a variable will not release memory. Like deleting a dict `output` variable then garbage collect and empty cache may still retain memory and cause cuda memory error. In this case using `del output['predictions']` and following rest of the process will work.

  `output` variable,
  ```
  {'predictions': tensor([[ 0.6208, -0.7106],
           [ 0.6987, -0.7888],
           [ 1.3222, -1.4706]], device='cuda:0'),
   'targets': tensor([0, 1, 1], device='cuda:0')}
  ```

  releasing memory,
  ```
  del output['predictions']
  import gc
  gc.collect()
  torch.cuda.empty_cache()
  ``` 
- A single model may contain parts which are not all used at the same time. Discard or not loading those keys will save memory for training and inference.
- During inference optimizer states, scheduler etc. are not needed, only loading the (multiple if applicable) state_dict will reduce memory.
- Prunning to compress model and reduce memory.
- Knowledge distillation to distill from large teacher model to a small student model. It will speed up and reduce memory size at the cost of some accuracy.
- Model quantization from FP32 to FP16, INT8 will speedup processing. It will also reduce memory size (not sure yet!!!).
- Using low memory requirement alternative of various modules like self attention. There are alternatives that are equally good but requires lot less memory.
- Use deepspeed (TODO).

### Pytorch Faster Inference

Some of the things described above for reducing gpu memory requirement is also applicable to improve speed.

- Convert model to onnx for inference.
- Prune model with pytorch, [NNI](https://github.com/microsoft/nni) etc.
- Quantize model.
- Distillation.
- TensorRT.
- Jit model.
- Avoid custom python functions, loops and use native functions.
- Use numba, cython if applicable.
- Custom cpp cuda extensions.

# Running ML Models in Real Time

- Try INT8, FP16 quantization.
- Use ONNX runtime, OpenCV DNN, TFLite, openvino.
- Use model compression, prunning.
- Run drawing, other operations on separate threads.
- In OpenCV use threaded non blocking webcam, file video capture.   
- Detect in a frame and in next N frames run tracking only then again detect. Frame dropping and skipping.
- Empty frame buffer/queue to always get the latest frame.
- Do cpu specific compilation of code take advantage of cpu architectures such as AVX2, AVX512 etc.
- Compile with oneDNN, oneMKL, CUDA, oneTBB, gstreamer etc.
- Use vectorized implementations instead of naive approaches. Try Numba jit for cpu/gpu, CuPy.
- Use C++ instead of python for whole code.
- Move slower part of python code to C++ and call as library.
- Use a smaller input resolution for the model at the cost of accuracy/result quality.
- Use better data structures and algorithms, tweak code to speedup.
