# Neural Style Transfer Series

## Papers

| Paper | Year | Conference |
| --- | --- | --- |
| [Perceptual Losses for Real-Time Style Transfer and Super-Resolution](https://arxiv.org/abs/1603.08155) <br> [Supplementary](https://cs.stanford.edu/people/jcjohns/papers/fast-style/fast-style-supp.pdf) | 2016 |  |

# Perceptual Losses for Real-Time Style Transfer and Super-Resolution

Proposed method is orders of magnitude faster than previous and result is generated in single forward pass without explicit optimization on output image at test time. Instead of using pixel wise loss they use perceptual loss. Perceptual loss uses intermediate layers features of pretrained network to calculate loss between various input images.
