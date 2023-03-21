<Img Align="right" Src="fig/logo.png">

# Deep Learning For Music (DL4M) [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

By [Yann Bayle](http://yannbayle.fr/english/index.php) ([Website](http://yannbayle.fr/english/index.php), [GitHub](https://github.com/ybayle)) From LaBRI ([Website](http://www.labri.fr/), [Twitter](https://twitter.com/labriOfficial/)), Univ. Bordeaux ([Website](https://www.u-bordeaux.fr/), [Twitter](https://twitter.com/univbordeaux)), CNRS ([Website](http://www.cnrs.fr/), [Twitter](https://twitter.com/CNRS)) And SCRIME ([Website](https://scrime.u-bordeaux.fr/)).

**TL;DR** Non-exhaustive List Of Scientific Articles On Deep Learning For Music: [Summary](#dl4m-summary) (Article Title, Pdf Link And Code), [Details](AI-Music/awesome-deep-learning-music-master/dl4m.tsv) (Table - More Info), [Details](AI-Music/awesome-deep-learning-music-master/dl4m.bib) (Bib - All Info)

The Role Of This Curated List Is To Gather Scientific Articles, Thesis And Reports That Use Deep Learning Approaches Applied To Music.  
The List Is Currently Under Construction But Feel Free To Contribute To The Missing Fields And To Add Other Resources! To Do So, Please Refer To The [How To Contribute](#how-to-contribute) Section.  
The Resources Provided Here Come From My Review Of The State-of-the-art For My PhD Thesis For Which An Article Is Being Written.  
There Are Already Surveys On Deep Learning For [Music Generation](https://arxiv.org/pdf/1709.01620.pdf), [Speech Separation](https://arxiv.org/ftp/arxiv/papers/1708/1708.07524.pdf) And [Speaker Identification](https://www.researchgate.net/profile/Seyed_Reza_Shahamiri/publication/319158024_Speaker_Identification_Features_Extraction_Methods_A_Systematic_Review/links/599e2816aca272dff12fdef1/Speaker-Identification-Features-Extraction-Methods-A-Systematic-Review.pdf).  
However, These Surveys Do Not Cover Music Information Retrieval Tasks That Are Included In This Repository.

## Table Of Contents

- [DL4M Summary](#dl4m-summary)
- [DL4M Details](#dl4m-details)
- [Code Without Articles](#code-without-articles)
- [Statistics And Visualisations](#statistics-and-visualisations)
- [Advices For Reviewers Of Dl4m Articles](#advices-for-reviewers-of-dl4m-articles)
- [How To Contribute](#how-to-contribute)
- [FAQ](#faq)
- [Acronyms Used](#acronyms-used)
- [Sources](#sources)
- [Contributors](#contributors)
- [Other Useful Related Lists](#other-useful-related-lists-and-resources)
- [Cited By](#cited-by)
- [License](#license)

## DL4M Summary

| Year |  Articles, Thesis And Reports | Code |
|------|-------------------------------|------|
| 1988 | Neural Net Modeling Of Music | No |
| 1988 | [Creation By Refinement: A Creativity Paradigm For Gradient Descent Learning Networks](http://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=23933) | No |
| 1988 | A Sequential Network Design For Musical Applications | No |
| 1989 | [The Representation Of Pitch In A Neural Net Model Of Chord Classification](http://www.jstor.org/stable/3679550) | No |
| 1989 | [Algorithms For Music Composition By Neural Nets: Improved CBR Paradigms](https://quod.lib.umich.edu/cgi/p/pod/dod-idx/algorithms-for-music-composition.pdf?c=icmc;idno=bbp2372.1989.044;format=pdf) | No |
| 1989 | [A Connectionist Approach To Algorithmic Composition](http://www.jstor.org/stable/3679551) | No |
| 1994 | [Neural Network Music Composition By Prediction: Exploring The Benefits Of Psychoacoustic Constraints And Multi-scale Processing](http://www-labs.iro.umontreal.ca/~pift6080/H09/documents/papers/mozer-music.pdf) | No |
| 1995 | [Automatic Source Identification Of Monophonic Musical Instrument Sounds](https://www.researchgate.net/publication/3622871_Automatic_source_identification_of_monophonic_musical_instrument_sounds) | No |
| 1995 | [Neural Network Based Model For Classification Of Music Type](http://ieeexplore.ieee.org/abstract/document/514161/) | No |
| 1997 | [A Machine Learning Approach To Musical Style Recognition](http://repository.cmu.edu/cgi/viewcontent.cgi?article=1496&context=compsci) | No |
| 1998 | [Recognition Of Music Types](https://www.ri.cmu.edu/pub_files/pub1/soltau_hagen_1998_2/soltau_hagen_1998_2.pdf) | No |
| 1999 | [Musical Networks: Parallel Distributed Perception And Performance](https://s3.amazonaws.com/academia.edu.documents/3551783/10.1.1.39.6248.pdf?AWSAccessKeyId=AKIAIWOWYYGZ2Y53UL3A&Expires=1507055806&Signature=5mGzQc7bvJgUZYfXOmCX8eeNQOs%3D&response-content-disposition=inline%3B%20filename%3DMusical_networks_Parallel_distributed_pe.pdf) | No |
| 2001 | [Multi-phase Learning For Jazz Improvisation And Interaction](http://www.cs.smith.edu/~jfrankli/papers/CtColl01.pdf) | No |
| 2002 | [A Supervised Learning Approach To Musical Style Recognition](https://www.researchgate.net/profile/Giuseppe_Buzzanca/publication/228588086_A_supervised_learning_approach_to_musical_style_recognition/links/54b43ee90cf26833efd0109f.pdf) | No |
| 2002 | [Finding Temporal Structure In Music: Blues Improvisation With LSTM Recurrent Networks](http://www-perso.iro.umontreal.ca/~eckdoug/papers/2002_ieee.pdf) | No |
| 2002 | [Neural Networks For Note Onset Detection In Piano Music](https://www.researchgate.net/profile/Matija_Marolt/publication/2473938_Neural_Networks_for_Note_Onset_Detection_in_Piano_Music/links/00b49525efccc79fed000000.pdf) | No |
| 2004 | [A Convolutional-kernel Based Approach For Note Onset Detection In Piano-solo Audio Signals](http://www.murase.nuie.nagoya-u.ac.jp/~ide/res/paper/E04-conference-pablo-1.pdf) | No |
| 2009 | [Unsupervised Feature Learning For Audio Classification Using Convolutional Deep Belief Networks](http://papers.nips.cc/paper/3674-unsupervised-feature-learning-for-audio-classification-using-convolutional-deep-belief-networks.pdf) | No |
| 2010 | [Audio Musical Genre Classification Using Convolutional Neural Networks And Pitch And Tempo Transformations](http://lbms03.cityu.edu.hk/theses/c_ftt/mphil-cs-b39478026f.pdf) | No |
| 2010 | [Automatic Musical Pattern Feature Extraction Using Convolutional Neural Network](https://www.researchgate.net/profile/Antoni_Chan2/publication/44260643_Automatic_Musical_Pattern_Feature_Extraction_Using_Convolutional_Neural_Network/links/02e7e523dac6bb86b0000000.pdf) | No |
| 2011 | [Audio-based Music Classification With A Pretrained Convolutional Network](http://www.ismir2011.ismir.net/papers/PS6-3.pdf) | No |
| 2012 | [Rethinking Automatic Chord Recognition With Convolutional Neural Networks](http://ieeexplore.ieee.org/abstract/document/6406762/) | No |
| 2012 | [Moving Beyond Feature Design: Deep Architectures And Automatic Feature Learning In Music Informatics](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.294.2304&rep=rep1&type=pdf) | No |
| 2012 | [Local-feature-map Integration Using Convolutional Neural Networks For Music Genre Classification](http://liris.cnrs.fr/Documents/Liris-5602.pdf) | No |
| 2012 | [Learning Sparse Feature Representations For Music Annotation And Retrieval](https://pdfs.semanticscholar.org/099d/85f25e9336f48ff64287a4b53ee5fb64ab51.pdf) | No |
| 2012 | [Unsupervised Learning Of Local Features For Music Classification](http://www.ismir2012.ismir.net/event/papers/139_ISMIR_2012.pdf) | No |
| 2013 | [Multiscale Approaches To Music Audio Feature Learning](http://ismir2013.ismir.net/wp-content/uploads/2013/09/69_Paper.pdf) | No |
| 2013 | [Musical Onset Detection With Convolutional Neural Networks](http://phenicx.upf.edu/system/files/publications/Schlueter_MML13.pdf) | No |
| 2013 | [Deep Content-based Music Recommendation](http://papers.nips.cc/paper/5004-deep-content-based-music-recommendation.pdf) | No |
| 2014 | [The Munich LSTM-RNN Approach To The MediaEval 2014 Emotion In Music Task](https://pdfs.semanticscholar.org/8a24/c5131d5a28165f719697028c34b00e6d3f60.pdf) | No |
| 2014 | [End-to-end Learning For Music Audio](http://ieeexplore.ieee.org/abstract/document/6854950/) | No |
| 2014 | [Deep Learning For Music Genre Classification](https://courses.engr.illinois.edu/ece544na/fa2014/Tao_Feng.pdf) | No |
| 2014 | [Recognition Of Acoustic Events Using Deep Neural Networks](https://www.cs.tut.fi/sgn/arg/music/tuomasv/dnn_eusipco2014.pdf) | No |
| 2014 | [Deep Image Features In Music Information Retrieval](https://www.degruyter.com/downloadpdf/j/eletel.2014.60.issue-4/eletel-2014-0042/eletel-2014-0042.pdf) | No |
| 2014 | [From Music Audio To Chord Tablature: Teaching Deep Convolutional Networks To Play Guitar](https://ejhumphrey.com/assets/pdf/humphrey2014music.pdf) | No |
| 2014 | [Improved Musical Onset Detection With Convolutional Neural Networks](http://www.mirlab.org/conference_papers/International_Conference/ICASSP%202014/papers/p7029-schluter.pdf) | No |
| 2014 | [Boundary Detection In Music Structure Analysis Using Convolutional Neural Networks](https://dav.grrrr.org/public/pub/ullrich_schlueter_grill-2014-ismir.pdf) | No |
| 2014 | [Improving Content-based And Hybrid Music Recommendation Using Deep Learning](http://www.smcnus.org/wp-content/uploads/2014/08/reco_MM14.pdf) | No |
| 2014 | [A Deep Representation For Invariance And Music Classification](http://www.mirlab.org/conference_papers/International_Conference/ICASSP%202014/papers/p7034-zhang.pdf) | No |
| 2015 | [Auralisation Of Deep Convolutional Neural Networks: Listening To Learned Features](http://ismir2015.uma.es/LBD/LBD24.pdf) | [GitHub](https://github.com/keunwoochoi/Auralisation) |
| 2015 | [Downbeat Tracking With Multiple Features And Deep Neural Networks](http://perso.telecom-paristech.fr/~grichard/Publications/2015-durand-icassp.pdf) | No |
| 2015 | [Music Boundary Detection Using Neural Networks On Spectrograms And Self-similarity Lag Matrices](http://www.ofai.at/~jan.schlueter/pubs/2015_eusipco.pdf) | No |
| 2015 | [Classification Of Spatial Audio Location And Content Using Convolutional Neural Networks](https://www.researchgate.net/profile/Toni_Hirvonen/publication/276061831_Classification_of_Spatial_Audio_Location_and_Content_Using_Convolutional_Neural_Networks/links/5550665908ae12808b37fe5a/Classification-of-Spatial-Audio-Location-and-Content-Using-Convolutional-Neural-Networks.pdf) | No |
| 2015 | [Deep Learning, Audio Adversaries, And Music Content Analysis](http://www2.imm.dtu.dk/pubdb/views/edoc_download.php/6905/pdf/imm6905.pdf) | No |
| 2015 | [Deep Learning And Music Adversaries](https://arxiv.org/pdf/1507.04761.pdf) | [GitHub](https://github.com/coreyker/dnn-mgr) |
| 2015 | [Singing Voice Detection With Deep Recurrent Neural Networks](https://hal-imt.archives-ouvertes.fr/hal-01110035/) | No |
| 2015 | [Automatic Instrument Recognition In Polyphonic Music Using Convolutional Neural Networks](https://arxiv.org/pdf/1511.05520.pdf) | No |
| 2015 | [A Software Framework For Musical Data Augmentation](https://bmcfee.github.io/papers/ismir2015_augmentation.pdf) | No |
| 2015 | [A Deep Bag-of-features Model For Music Auto-tagging](https://arxiv.org/pdf/1508.04999v1.pdf) | No |
| 2015 | [Music-noise Segmentation In Spectrotemporal Domain Using Convolutional Neural Networks](http://ismir2015.uma.es/LBD/LBD27.pdf) | No |
| 2015 | [Musical Instrument Sound Classification With Deep Convolutional Neural Network Using Feature Fusion Approach](https://arxiv.org/ftp/arxiv/papers/1512/1512.07370.pdf) | No |
| 2015 | [Environmental Sound Classification With Convolutional Neural Networks](http://karol.piczak.com/papers/Piczak2015-ESC-ConvNet.pdf) | No |
| 2015 | [Exploring Data Augmentation For Improved Singing Voice Detection With Neural Networks](https://grrrr.org/pub/schlueter-2015-ismir.pdf) | [GitHub](https://github.com/f0k/ismir2015) |
| 2015 | [Singer Traits Identification Using Deep Neural Network](https://cs224d.stanford.edu/reports/SkiZhengshan.pdf) | No |
| 2015 | [A Hybrid Recurrent Neural Network For Music Transcription](https://arxiv.org/pdf/1411.1623.pdf) | No |
| 2015 | [An End-to-end Neural Network For Polyphonic Music Transcription](https://arxiv.org/pdf/1508.01774.pdf) | No |
| 2015 | [Deep Karaoke: Extracting Vocals From Musical Mixtures Using A Convolutional Deep Neural Network](https://link.springer.com/chapter/10.1007/978-3-319-22482-4_50) | No |
| 2015 | [Folk Music Style Modelling By Recurrent Neural Networks With Long Short Term Memory Units](http://ismir2015.uma.es/LBD/LBD13.pdf) | [GitHub](https://github.com/IraKorshunova/folk-rnn) |
| 2015 | [Deep Neural Network Based Instrument Extraction From Music](https://www.researchgate.net/profile/Stefan_Uhlich/publication/282001406_Deep_neural_network_based_instrument_extraction_from_music/links/5600eeda08ae07629e52b397/Deep-neural-network-based-instrument-extraction-from-music.pdf) | No |
| 2015 | [A Deep Neural Network For Modeling Music](https://www.researchgate.net/profile/Xiaoqing_Zheng3/publication/275347034_A_Deep_Neural_Network_for_Modeling_Music/links/5539d2060cf2239f4e7dad0d/A-Deep-Neural-Network-for-Modeling-Music.pdf) | No |
| 2016 | [An Efficient Approach For Segmentation, Feature Extraction And Classification Of Audio Signals](http://file.scirp.org/pdf/CS_2016042615054817.pdf) | No |
| 2016 | [Text-based LSTM Networks For Automatic Music Composition](https://drive.google.com/file/d/0B1OooSxEtl0FcG9MYnY2Ylh5c0U/view) | No |
| 2016 | [Towards Playlist Generation Algorithms Using RNNs Trained On Within-track Transitions](https://arxiv.org/pdf/1606.02096.pdf) | No |
| 2016 | [Automatic Tagging Using Deep Convolutional Neural Networks](https://arxiv.org/pdf/1606.00298.pdf) | No |
| 2016 | [Automatic Chord Estimation On Seventhsbass Chord Vocabulary Using Deep Neural Network](http://ieeexplore.ieee.org/abstract/document/7471677/) | No |
| 2016 | [DeepBach: A Steerable Model For Bach Chorales Generation](https://arxiv.org/pdf/1612.01010.pdf) | [GitHub](https://github.com/Ghadjeres/DeepBach) |
| 2016 | [Bayesian Meter Tracking On Learned Signal Representations](http://www.rhythmos.org/MMILab-Andre_files/ISMIR2016_CNNDBNbeats_camready.pdf) | No |
| 2016 | [Deep Learning For Music](https://arxiv.org/pdf/1606.04930.pdf) | No |
| 2016 | [Learning Temporal Features Using A Deep Neural Network And Its Application To Music Genre Classification](https://www.researchgate.net/profile/Il_Young_Jeong/publication/305683876_Learning_temporal_features_using_a_deep_neural_network_and_its_application_to_music_genre_classification/links/5799a27c08aec89db7bb9f92.pdf) | No |
| 2016 | [On The Potential Of Simple Framewise Approaches To Piano Transcription](https://arxiv.org/pdf/1612.05153.pdf) | No |
| 2016 | [Feature Learning For Chord Recognition: The Deep Chroma Extractor](https://arxiv.org/pdf/1612.05065.pdf) | [GitHub](https://github.com/fdlm/chordrec/tree/master/experiments/ismir2016) |
| 2016 | [A Fully Convolutional Deep Auditory Model For Musical Chord Recognition](https://www.researchgate.net/profile/Filip_Korzeniowski/publication/305590295_A_Fully_Convolutional_Deep_Auditory_Model_for_Musical_Chord_Recognition/links/579486ba08aed51475cc6958/A-Fully-Convolutional-Deep-Auditory-Model-for-Musical-Chord-Recognition.pdf?_iepl%5BhomeFeedViewId%5D=HTzFFmKPia2YminQ4psHT5at&_iepl%5Bcontexts%5D%5B0%5D=pcfhf&_iepl%5BinteractionType%5D=publicationDownload&origin=publication_detail&ev=pub_int_prw_xdl&msrp=Dz_6LKHzYcPyP-LmgZPF-m63ayZ6k0entFEntooiu_e32zfETNQXKPQSTFOI87NONIIQuUQdnUtwORdomTXfteTrb09KiAIdDtBJnw_02P6JeRr5zu2eyaCG.2Uxsi_eENxtbYL39lvorIK8LofRYhkgpUHzpzmVzkIEiyHc0wUY87rEa4PH1qbXi4k4RyagHUsA2IsZtewnprglORjx2v9Cwbk9ZfQ.cd67BaqtHul_hE6SX6vUFKuldz81aH6dWq-cYMkq5vQKCHcvB8l9zgeM694Efb_r2wBB5GT9idt3OLeME0UxVHI6ROxamgK3LMNlSw.JtZXAo9HhR9t-8Wl3gxJgnoM4--rtmDEUDbXSWezbFyU-CoB_nyfxbRQ4kdoN4-5aJ3Tgx4YHdikicqAhc_cezB2ZntjxkB4rEDx1A) | No |
| 2016 | [A Deep Bidirectional Long Short-term Memory Based Multi-scale Approach For Music Dynamic Emotion Prediction](http://ieeexplore.ieee.org/document/7471734/) | No |
| 2016 | [Event Localization In Music Auto-tagging](http://mac.citi.sinica.edu.tw/~yang/pub/liu16mm.pdf) | [GitHub](https://github.com/ciaua/clip2frame) |
| 2016 | [Deep Convolutional Networks On The Pitch Spiral For Musical Instrument Recognition](https://github.com/lostanlen/ismir2016/blob/master/paper/lostanlen_ismir2016.pdf) | [GitHub](https://github.com/lostanlen/ismir2016) |
| 2016 | [SampleRNN: An Unconditional End-to-end Neural Audio Generation Model](https://openreview.net/pdf?id=SkxKPDv5xl) | [GitHub](https://github.com/soroushmehr/sampleRNN_ICLR2017) |
| 2016 | [Robust Audio Event Recognition With 1-max Pooling Convolutional Neural Networks](https://arxiv.org/pdf/1604.06338.pdf) | No |
| 2016 | [Experimenting With Musically Motivated Convolutional Neural Networks](http://jordipons.me/media/CBMI16.pdf) | [GitHub](https://github.com/jordipons/) |
| 2016 | [Singing Voice Melody Transcription Using Deep Neural Networks](https://wp.nyu.edu/ismir2016/wp-content/uploads/sites/2294/2016/07/163_Paper.pdf) | No |
| 2016 | [Singing Voice Separation Using Deep Neural Networks And F0 Estimation](http://www.music-ir.org/mirex/abstracts/2016/RSGP1.pdf) | [Website](http://cvssp.org/projects/maruss/mirex2016/) |
| 2016 | [Learning To Pinpoint Singing Voice From Weakly Labeled Examples](http://www.ofai.at/~jan.schlueter/pubs/2016_ismir.pdf) | No |
| 2016 | [Analysis Of Time-frequency Representations For Musical Onset Detection With Convolutional Neural Network](http://ieeexplore.ieee.org/abstract/document/7733228/) | No |
| 2016 | [Note Onset Detection In Musical Signals Via Neural-network-based Multi-ODF Fusion](https://www.degruyter.com/downloadpdf/j/amcs.2016.26.issue-1/amcs-2016-0014/amcs-2016-0014.pdf) | No |
| 2016 | [Music Transcription Modelling And Composition Using Deep Learning](https://drive.google.com/file/d/0B1OooSxEtl0FcTBiOGdvSTBmWnc/view) | [GitHub](https://github.com/IraKorshunova/folk-rnn) |
| 2016 | [Convolutional Neural Network For Robust Pitch Determination](http://www.mirlab.org/conference_papers/International_Conference/ICASSP%202016/pdfs/0000579.pdf) | No |
| 2016 | [Deep Convolutional Neural Networks And Data Augmentation For Acoustic Event Detection](https://arxiv.org/pdf/1604.07160.pdf) | [Website](https://bitbucket.org/naoya1/aenet_release) |
| 2017 | [Gabor Frames And Deep Scattering Networks In Audio Processing](https://arxiv.org/pdf/1706.08818.pdf) | No |
| 2017 | [Vision-based Detection Of Acoustic Timed Events: A Case Study On Clarinet Note Onsets](http://dorienherremans.com/dlm2017/papers/bazzica2017clarinet.pdf) | No |
| 2017 | [Deep Learning Techniques For Music Generation - A Survey](https://arxiv.org/pdf/1709.01620.pdf) | No |
| 2017 | [JamBot: Music Theory Aware Chord Based Generation Of Polyphonic Music With LSTMs](https://arxiv.org/pdf/1711.07682.pdf) | [GitHub](https://github.com/brunnergino/JamBot) |
| 2017 | [XFlow: 1D <-> 2D Cross-modal Deep Neural Networks For Audiovisual Classification](https://arxiv.org/pdf/1709.00572.pdf) | No |
| 2017 | [Machine Listening Intelligence](http://dorienherremans.com/dlm2017/papers/cella2017mli.pdf) | No |
| 2017 | [Monoaural Audio Source Separation Using Deep Convolutional Neural Networks](http://mtg.upf.edu/system/files/publications/monoaural-audio-source_0.pdf) | [GitHub](https://github.com/MTG/DeepConvSep) |
| 2017 | [Deep Multimodal Network For Multi-label Classification](http://ieeexplore.ieee.org/abstract/document/8019322/) | No |
| 2017 | [A Tutorial On Deep Learning For Music Information Retrieval](https://arxiv.org/pdf/1709.04396.pdf) | [GitHub](https://github.com/keunwoochoi/dl4mir) |
| 2017 | [A Comparison On Audio Signal Preprocessing Methods For Deep Neural Networks On Music Tagging](https://arxiv.org/pdf/1709.01922.pdf) | [GitHub](https://github.com/keunwoochoi/transfer_learning_music) |
| 2017 | [Transfer Learning For Music Classification And Regression Tasks](https://arxiv.org/pdf/1703.09179v3.pdf) | [GitHub](https://github.com/keunwoochoi/transfer_learning_music) |
| 2017 | [Convolutional Recurrent Neural Networks For Music Classification](http://ieeexplore.ieee.org/abstract/document/7952585/) | [GitHub](https://github.com/keunwoochoi/icassp_2017) |
| 2017 | [An Evaluation Of Convolutional Neural Networks For Music Classification Using Spectrograms](http://www.inf.ufpr.br/lesoliveira/download/ASOC2017.pdf) | No |
| 2017 | [Large Vocabulary Automatic Chord Estimation Using Deep Neural Nets: Design Framework, System Variations And Limitations](https://arxiv.org/pdf/1709.07153.pdf) | No |
| 2017 | [Basic Filters For Convolutional Neural Networks: Training Or Design?](https://arxiv.org/pdf/1709.02291.pdf) | No |
| 2017 | [Ensemble Of Deep Neural Networks For Acoustic Scene Classification](https://arxiv.org/pdf/1708.05826.pdf) | No |
| 2017 | [Robust Downbeat Tracking Using An Ensemble Of Convolutional Networks](http://ieeexplore.ieee.org/abstract/document/7728057/) | No |
| 2017 | [Music Signal Processing Using Vector Product Neural Networks](http://dorienherremans.com/dlm2017/papers/fan2017vector.pdf) | No |
| 2017 | [Transforming Musical Signals Through A Genre Classifying Convolutional Neural Network](http://dorienherremans.com/dlm2017/papers/geng2017genre.pdf) | No |
| 2017 | [Audio To Score Matching By Combining Phonetic And Duration Information](https://arxiv.org/pdf/1707.03547.pdf) | [GitHub](https://github.com/ronggong/jingjuSingingPhraseMatching/tree/v0.1.0) |
| 2017 | [Interactive Music Generation With Positional Constraints Using Anticipation-RNNs](https://arxiv.org/pdf/1709.06404.pdf) | No |
| 2017 | [Deep Rank-based Transposition-invariant Distances On Musical Sequences](https://arxiv.org/pdf/1709.00740.pdf) | No |
| 2017 | [GLSR-VAE: Geodesic Latent Space Regularization For Variational Autoencoder Architectures](https://arxiv.org/pdf/1707.04588.pdf) | No |
| 2017 | [Deep Convolutional Neural Networks For Predominant Instrument Recognition In Polyphonic Music](http://dl.acm.org/citation.cfm?id=3068697) | No |
| 2017 | [CNN Architectures For Large-scale Audio Classification](https://arxiv.org/pdf/1609.09430v2.pdf) | No |
| 2017 | [DeepSheet: A Sheet Music Generator Based On Deep Learning](http://ieeexplore.ieee.org/abstract/document/8026272/) | No |
| 2017 | [Talking Drums: Generating Drum Grooves With Neural Networks](http://dorienherremans.com/dlm2017/papers/hutchings2017drums.pdf) | No |
| 2017 | [Singing Voice Separation With Deep U-Net Convolutional Networks](https://ismir2017.smcnus.org/wp-content/uploads/2017/10/171_Paper.pdf) | [GitHub](https://github.com/Xiao-Ming/UNet-VocalSeparation-Chainer) |
| 2017 | [Music Emotion Recognition Via End-to-end Multimodal Neural Networks](http://ceur-ws.org/Vol-1905/recsys2017_poster18.pdf) | No |
| 2017 | [Chord Label Personalization Through Deep Learning Of Integrated Harmonic Interval-based Representations](http://dorienherremans.com/dlm2017/papers/koops2017pers.pdf) | No |
| 2017 | [End-to-end Musical Key Estimation Using A Convolutional Neural Network](https://arxiv.org/pdf/1706.02921.pdf) | No |
| 2017 | [MediaEval 2017 AcousticBrainz Genre Task: Multilayer Perceptron Approach](http://www.cp.jku.at/research/papers/Koutini_2017_mediaeval-acousticbrainz.pdf) | No |
| 2017 | [Classification-based Singing Melody Extraction Using Deep Convolutional Neural Networks](https://www.preprints.org/manuscript/201711.0027/v1) | No |
| 2017 | [Multi-level And Multi-scale Feature Aggregation Using Pre-trained Convolutional Neural Networks For Music Auto-tagging](https://arxiv.org/pdf/1703.01793v2.pdf) | No |
| 2017 | [Multi-level And Multi-scale Feature Aggregation Using Sample-level Deep Convolutional Neural Networks For Music Classification](https://arxiv.org/pdf/1706.06810.pdf) | [GitHub](https://github.com/jongpillee/musicTagging_MSD) |
| 2017 | [Sample-level Deep Convolutional Neural Networks For Music Auto-tagging Using Raw Waveforms](https://arxiv.org/pdf/1703.01789v2.pdf) | No |
| 2017 | [A SeqGAN For Polyphonic Music Generation](https://arxiv.org/pdf/1710.11418.pdf) | [GitHub](https://github.com/L0SG/seqgan-music) |
| 2017 | [Harmonic And Percussive Source Separation Using A Convolutional Auto Encoder](http://www.eurasip.org/Proceedings/Eusipco/Eusipco2017/papers/1570346835.pdf) | No |
| 2017 | [Stacked Convolutional And Recurrent Neural Networks For Music Emotion Recognition](https://arxiv.org/pdf/1706.02292.pdf) | No |
| 2017 | [A Deep Learning Approach To Source Separation And Remixing Of Hiphop Music](https://repositori.upf.edu/bitstream/handle/10230/32919/Martel_2017.pdf?sequence=1&isAllowed=y) | No |
| 2017 | [Music Genre Classification Using Masked Conditional Neural Networks](https://link.springer.com/chapter/10.1007%2F978-3-319-70096-0_49) | No |
| 2017 | [Monaural Singing Voice Separation With Skip-Filtering Connections And Recurrent Inference Of Time-Frequency Mask](https://arxiv.org/pdf/1711.01437.pdf) | [GitHub](https://github.com/Js-Mim/mss_pytorch) |
| 2017 | [Generating Data To Train Convolutional Neural Networks For Classical Music Source Separation](https://www.researchgate.net/profile/Marius_Miron/publication/318322107_Generating_data_to_train_convolutional_neural_networks_for_classical_music_source_separation/links/59637cc3458515a3575b93c6/Generating-data-to-train-convolutional-neural-networks-for-classical-music-source-separation.pdf?_iepl%5BhomeFeedViewId%5D=WchoMnlUL1Hk9hBLVTeR8Amh&_iepl%5Bcontexts%5D%5B0%5D=pcfhf&_iepl%5BinteractionType%5D=publicationDownload&origin=publication_detail&ev=pub_int_prw_xdl&msrp=p3lQ8M4uZlb4TF5Hv9a2U3P2y4wW7ant5KWj4E5-OcD1Mg53p1ykTKHMG9_zVTB9n6mI8fvZOCL2Xhpru186pCEY-2ZxiYR-CB8_QvwHc1kUG-QE4SHdProR.LoJb2BDOiiQth3iR9xgZUxxCWEJgtTBF4whFrFa01OD49-3YYRxA0WQVN--zhtQU_7C2Pt0rKdwoFxT1pfxFvnKXSXmy2eT1Jpz-pw.U1QLoFO_Uc6aQVr2Nm2FcAi6BqAUfngH2Or5__6wegbCgVvTYoIGt22tmCkYbGTOQ_4PxBgt1LrvsFQiL0oMyogP8Yk8myTj0gs9jw.fGpkufGqAI4R2v8Hfe0ThcXL7M7yN2PuAlx974BGVn50SdUWvNhhIPWBD-zWTn8NKtVJx3XrjKXFrMgi9Cx7qGrNP8tBWpha6Srf6g) | [GitHub](https://github.com/MTG/DeepConvSep) |
| 2017 | [Monaural Score-informed Source Separation For Classical Music Using Convolutional Neural Networks](https://www.researchgate.net/profile/Marius_Miron/publication/318637038_Monaural_score-informed_source_separation_for_classical_music_using_convolutional_neural_networks/links/597327c6458515e26dfdb007/Monaural-score-informed-source-separation-for-classical-music-using-convolutional-neural-networks.pdf?_iepl%5BhomeFeedViewId%5D=WchoMnlUL1Hk9hBLVTeR8Amh&_iepl%5Bcontexts%5D%5B0%5D=pcfhf&_iepl%5BinteractionType%5D=publicationDownload&origin=publication_detail&ev=pub_int_prw_xdl&msrp=Hp6dDqMepEiRZ5E6WkreaqyjFkFkwMxPFoJvr14etVJsoKZBc5qb99fBnJjVUZrRHLFRhaXvNY9k1sMvYPOouuGbQP0YhEGm28zLw_55Zewu86WGnHck1Tqi.93HH2WqXfTedn6IaZRjjhQGYZVDHBz1X6nr4ABBgMAVv584gvGN3sW5IyBAY-4MBWf5DJFPBGm8zsaC2dKz8G-odZPfosWoXY0afAQ.KoCP2mO9l31lCER0oMZMZBrbuRGvb6ZzeBwHb88pL8AhMfJk03Hj1eLrohQIjPDETBj4hhqb0gniDGJgtZ9GnW64ZNjh9GbQDrIl5A.egNQTyC7t8P26zCQWrbEhf51Pxy2JRBZoTkH6SpRHHhRhFl1_AT_AT481lMcFI34-JbeRq-5oTQR7DpvAuw7iUIivd78ltuxpI9syg) | [GitHub](https://github.com/MTG/DeepConvSep) |
| 2017 | [Multi-label Music Genre Classification From Audio, Text, And Images Using Deep Features](https://ismir2017.smcnus.org/wp-content/uploads/2017/10/126_Paper.pdf) | [GitHub](https://github.com/sergiooramas/tartarus) |
| 2017 | [A Deep Multimodal Approach For Cold-start Music Recommendation](https://arxiv.org/pdf/1706.09739.pdf) | [GitHub](https://github.com/sergiooramas/tartarus) |
| 2017 | [Melody Extraction And Detection Through LSTM-RNN With Harmonic Sum Loss](http://ieeexplore.ieee.org/abstract/document/7952660/) | No |
| 2017 | [Representation Learning Of Music Using Artist Labels](https://arxiv.org/pdf/1710.06648.pdf) | No |
| 2017 | [Toward Inverse Control Of Physics-based Sound Synthesis](http://dorienherremans.com/dlm2017/papers/pfalz2017synthesis.pdf) | [Website](https://www.cct.lsu.edu/~apfalz/inverse_control.html) |
| 2017 | [DNN And CNN With Weighted And Multi-task Loss Functions For Audio Event Detection](https://arxiv.org/pdf/1708.03211.pdf) | No |
| 2017 | [Score-informed Syllable Segmentation For A Cappella Singing Voice With Convolutional Neural Networks](https://ismir2017.smcnus.org/wp-content/uploads/2017/10/46_Paper.pdf) | [GitHub](https://github.com/ronggong/jingjuSyllabicSegmentaion/tree/v0.1.0) |
| 2017 | [End-to-end Learning For Music Audio Tagging At Scale](https://arxiv.org/pdf/1711.02520.pdf) | [GitHub](https://github.com/jordipons/music-audio-tagging-at-scale-models) |
| 2017 | [Designing Efficient Architectures For Modeling Temporal Features With Convolutional Neural Networks](http://ieeexplore.ieee.org/document/7952601/) | [GitHub](https://github.com/jordipons/ICASSP2017) |
| 2017 | [Timbre Analysis Of Music Audio Signals With Convolutional Neural Networks](https://github.com/ronggong/EUSIPCO2017) | [GitHub](https://github.com/jordipons/EUSIPCO2017) |
| 2017 | [Deep Learning And Intelligent Audio Mixing](http://www.semanticaudio.co.uk/wp-content/uploads/2017/09/WIMP2017_Martinez-RamirezReiss.pdf) | No |
| 2017 | [Deep Learning For Event Detection, Sequence Labelling And Similarity Estimation In Music Signals](http://ofai.at/~jan.schlueter/pubs/phd/phd.pdf) | No |
| 2017 | [Music Feature Maps With Convolutional Neural Networks For Music Genre Classification](https://www.researchgate.net/profile/Thomas_Pellegrini/publication/319326354_Music_Feature_Maps_with_Convolutional_Neural_Networks_for_Music_Genre_Classification/links/59ba5ae3458515bb9c4c6724/Music-Feature-Maps-with-Convolutional-Neural-Networks-for-Music-Genre-Classification.pdf?origin=publication_detail&ev=pub_int_prw_xdl&msrp=wzXuHZAa5zAnqEmErYyZwIRr2H0q01LnNEd4Wd7A15CQfdVLwdy98pmE-AdnrDvoc3-bVENSFrHt0yhaOiE2mQrYllVS9CJZOk-c9R0j_R1rbgcZugS6RtQ_.AUjPuJSF5P_DMngf-woH7W-7jdnQlbNQziR4_h6NnCHfR_zGcEa8vOyyOz5gx5nc4azqKTPQ5ZgGGLUxkLj1qCQLEQ5ThkhGlWHLyA.s6MBZE20-EO_RjRGCOCV4wk0WSFdN56Aloiraxz9hKCbJwRM2Et27RHVUA8jj9H8qvXIB6f7zSIrQgjXGrL2yCpyQlLffuf57rzSwg.KMMXbZrHsihV8DJM53xkHAWf3VebCJESi4KU4btNv9nQsyK2KnkhSQaTILKv0DSZY3c70a61LzywCBuoHtIhVOFhW5hVZN2n5O9uKQ) | No |
| 2017 | [Automatic Drum Transcription For Polyphonic Recordings Using Soft Attention Mechanisms And Convolutional Neural Networks](https://carlsouthall.files.wordpress.com/2017/12/ismir2017adt.pdf) | [GitHub](https://github.com/CarlSouthall/ADTLib) |
| 2017 | [Adversarial Semi-supervised Audio Source Separation Applied To Singing Voice Extraction](https://arxiv.org/pdf/1711.00048.pdf) | No |
| 2017 | [Taking The Models Back To Music Practice: Evaluating Generative Transcription Models Built Using Deep Learning](http://jcms.org.uk/issues/Vol2Issue1/taking-models-back-to-music-practice/Taking%20the%20Models%20back%20to%20Music%20Practice:%20Evaluating%20Generative%20Transcription%20Models%20built%20using%20Deep%20Learning.pdf) | [GitHub](https://github.com/IraKorshunova/folk-rnn) |
| 2017 | [Generating Nontrivial Melodies For Music As A Service](https://ismir2017.smcnus.org/wp-content/uploads/2017/10/178_Paper.pdf) | No |
| 2017 | [Invariances And Data Augmentation For Supervised Music Transcription](https://arxiv.org/pdf/1711.04845.pdf) | [GitHub](https://github.com/jthickstun/thickstun2018invariances/) |
| 2017 | [Lyrics-based Music Genre Classification Using A Hierarchical Attention Network](https://ismir2017.smcnus.org/wp-content/uploads/2017/10/43_Paper.pdf) | [GitHub](https://github.com/alexTsaptsinos/lyricsHAN) |
| 2017 | [A Hybrid DSP/deep Learning Approach To Real-time Full-band Speech Enhancement](https://arxiv.org/pdf/1709.08243.pdf) | [GitHub](https://github.com/xiph/rnnoise/) |
| 2017 | [Convolutional Methods For Music Analysis](http://vbn.aau.dk/files/260308151/PHD_Gissel_Velarde_E_pdf.pdf) | No |
| 2017 | [Extending Temporal Feature Integration For Semantic Audio Analysis](http://www.aes.org/e-lib/browse.cfm?elib=18682) | No |
| 2017 | [Recognition And Retrieval Of Sound Events Using Sparse Coding Convolutional Neural Network](http://ieeexplore.ieee.org/abstract/document/8019552/) | No |
| 2017 | [A Two-stage Approach To Note-level Transcription Of A Specific Piano](http://www.mdpi.com/2076-3417/7/9/901/htm) | No |
| 2017 | [Reducing Model Complexity For DNN Based Large-scale Audio Classification](https://arxiv.org/pdf/1711.00229.pdf) | No |
| 2017 | [Audio Spectrogram Representations For Processing With Convolutional Neural Networks](http://dorienherremans.com/dlm2017/papers/wyse2017spect.pdf) | [Website](http://lonce.org/research/audioST/) |
| 2017 | [Unsupervised Feature Learning Based On Deep Models For Environmental Audio Tagging](https://arxiv.org/pdf/1607.03681.pdf) | No |
| 2017 | [Attention And Localization Based On A Deep Convolutional Recurrent Model For Weakly Supervised Audio Tagging](https://arxiv.org/pdf/1703.06052.pdf) | [GitHub](https://github.com/yongxuUSTC/att_loc_cgrnn) |
| 2017 | [Surrey-CVSSP System For DCASE2017 Challenge Task4](https://www.cs.tut.fi/sgn/arg/dcase2017/documents/challenge_technical_reports/DCASE2017_Xu_146.pdf) | [GitHub](https://github.com/yongxuUSTC/dcase2017_task4_cvssp) |
| 2017 | [A Study On LSTM Networks For Polyphonic Music Sequence Modelling](https://qmro.qmul.ac.uk/xmlui/handle/123456789/24946) | [Website](http://www.eecs.qmul.ac.uk/~ay304/code/ismir17) |
| 2018 | [MuseGAN: Multi-track Sequential Generative Adversarial Networks For Symbolic Music Generation And Accompaniment](https://arxiv.org/pdf/1709.06298.pdf) | [GitHub](https://github.com/salu133445/musegan) |
| 2018 | [Music Transformer: Generating Music With Long-term Structure](https://arxiv.org/pdf/1809.04281.pdf) | No |
| 2018 | [Music Theory Inspired Policy Gradient Method For Piano Music Transcription](https://nips2018creativity.github.io/doc/music_theory_inspired_policy_gradient.pdf) | No |
| 2019 | [Enabling Factorized Piano Music Modeling And Generation With The MAESTRO Dataset](https://arxiv.org/abs/1810.12247) | [GitHub](https://github.com/magenta/magenta/tree/master/magenta/models/onsets_frames_transcription) |
| 2019 | [Generating Long Sequences With Sparse Transformers](https://arxiv.org/pdf/1904.10509.pdf) | [GitHub](https://github.com/openai/sparse_attention) |

[Go Back To Top](https://github.com/ybayle/awesome-deep-learning-music#deep-learning-for-music-dl4m-)

## DL4M Details

A Human-readable Table Summarized Version If Displayed In The File [Dl4m.tsv](AI-Music/awesome-deep-learning-music-master/dl4m.tsv). All Details For Each Article Are Stored In The Corresponding Bib Entry In [Dl4m.bib](AI-Music/awesome-deep-learning-music-master/dl4m.bib). Each Entry Has The Regular Bib Field:

- `Author`
- `Year`
- `Title`
- `Journal` Or `Booktitle`

Each Entry In [Dl4m.bib](AI-Music/awesome-deep-learning-music-master/dl4m.bib) Also Displays Additional Information:

- `Link` - HTML Link To The PDF File
- `Code` - Link To The Source Code If Available
- `Archi` - Neural Network Architecture
- `Layer` - Number Of Layers
- `Task` - The Proposed Tasks Studied In The Article
- `Dataset` - The Names Of The Dataset Used
- `Dataaugmentation` - The Type Of Data Augmentation Technique Used
- `Time` - The Computation Time
- `Hardware` - The Hardware Used
- `Note` - Additional Notes And Information
- `Repro` - Indication To What Extent The Experiments Are Reproducible

[Go Back To Top](https://github.com/ybayle/awesome-deep-learning-music#deep-learning-for-music-dl4m-)

## Code Without Articles

- [Audio Classifier In Keras Using Convolutional Neural Network](https://github.com/drscotthawley/audio-classifier-keras-cnn)
- [Deep Learning Driven Jazz Generation Using Keras & Theano](https://github.com/jisungk/deepjazz)
- [End-to-end Learning For Music Audio Tagging At Scale](https://github.com/jordipons/music-audio-tagging-at-scale-models)
- [Music Genre Classification On GTZAN Dataset Using CNNs](https://github.com/Hguimaraes/gtzan.keras)
- [Pitch Estimation Of Choir Music Using Deep Learning Strategies: From Solo To Unison Recordings](https://github.com/helenacuesta/choir-pitch-estimation)
- [Music Genre Classification With LSTMs](https://github.com/ruohoruotsi/LSTM-Music-Genre-Classification)
- [CNN Based Music Emotion Classification Using TensorFlow](https://github.com/rickiepark/cnn_mer)
- [Separating Singing Voice From Music Based On Deep Neural Networks In Tensorflow](https://github.com/andabi/music-source-separation)
- [Music Tag Classification Model Using CRNN](https://github.com/kristijanbartol/Deep-Music-Tagger)
- [Finding The Genre Of A Song With Deep Learning](https://github.com/despoisj/DeepAudioClassification)
- [Composing Music Using Neural Nets](https://github.com/fephsun/neuralnetmusic)
- [Performance-RNN-PyTorch](https://github.com/djosix/Performance-RNN-PyTorch)

[Go Back To Top](https://github.com/ybayle/awesome-deep-learning-music#deep-learning-for-music-dl4m-)

## Statistics And Visualisations

- 165 Papers Referenced. See The Details In [Dl4m.bib](AI-Music/awesome-deep-learning-music-master/dl4m.bib).  
There Are More Papers From 2017 Than Any Other Years Combined.  
Number Of Articles Per Year:  
![Number Of Articles Per Year](articles_per_year.png)
- If You Are Applying DL To Music, There Are [356 Other Researchers](AI-Music/awesome-deep-learning-music-master/authors.md) In Your Field.
- 34 Tasks Investigated. See The List Of [Tasks](AI-Music/awesome-deep-learning-music-master/tasks.md).  
Tasks Pie Chart:  
![Tasks Pie Chart](pie_chart_task.png)
- 53 Datasets Used. See The List Of [Datasets](AI-Music/awesome-deep-learning-music-master/datasets.md).  
Datasets Pie Chart:  
![Datasets Pie Chart](pie_chart_dataset.png)
- 30 Architectures Used. See The List Of [Architectures](AI-Music/awesome-deep-learning-music-master/architectures.md).  
Architectures Pie Chart:  
![Architectures Pie Chart](pie_chart_architecture.png)
- 9 Frameworks Used. See The List Of [Frameworks](AI-Music/awesome-deep-learning-music-master/frameworks.md).  
Frameworks Pie Chart:  
![Frameworks Pie Chart](pie_chart_framework.png)
- Only 45 Articles (27%) Provide Their Source Code.  
Repeatability Is The Key To Good Science, So Check Out The [List Of Useful Resources On Reproducibility For MIR And ML](AI-Music/awesome-deep-learning-music-master/reproducibility.md).

[Go Back To Top](https://github.com/ybayle/awesome-deep-learning-music#deep-learning-for-music-dl4m-)

## Advices For Reviewers Of Dl4m Articles

Please Refer To The [Advice_review.md](AI-Music/awesome-deep-learning-music-master/advice_review.md) File.

## How To Contribute

Contributions Are Welcome!  
Please Refer To The [CONTRIBUTING.md](CONTRIBUTING.md) File.

[Go Back To Top](https://github.com/ybayle/awesome-deep-learning-music#deep-learning-for-music-dl4m-)

## FAQ

> How Are The Articles Sorted?

The Articles Are First Sorted By Decreasing Year (To Keep Up With The Latest News) And Then Alphabetically By The Main Author's Family Name.

> Why Are Preprint From ArXiv Included In The List?

I Want To Have Exhaustive Research And The Latest News On DL4M. However, One Should Take Care Of The Information Provided In The Articles Currently In Review. If Possible You Should Wait For The Final Accepted And Peer-reviewed Version Before Citing An ArXiv Paper. I Regularly Update The ArXiv Links To The Corresponding Published Papers When Available.

> How Much Can I Trust The Results Published In An Article?

The List Provided Here Does Not Guarantee The Quality Of The Articles. You Should Either Try To Reproduce The Experiments Described Or Submit A Request To [ReScience](https://github.com/ReScience/ReScience). Use One Article's Conclusion At Your Own Risks.

[Go Back To Top](https://github.com/ybayle/awesome-deep-learning-music#deep-learning-for-music-dl4m-)

## Acronyms Used

A List Of Useful Acronyms Used In Deep Learning And Music Is Stored In [Acronyms.md](AI-Music/awesome-deep-learning-music-master/acronyms.md).

[Go Back To Top](https://github.com/ybayle/awesome-deep-learning-music#deep-learning-for-music-dl4m-)

## Sources

The List Of Conferences, Journals And Aggregators Used To Gather The Proposed Materials Is Stored In [Sources.md](AI-Music/awesome-deep-learning-music-master/sources.md).

[Go Back To Top](https://github.com/ybayle/awesome-deep-learning-music#deep-learning-for-music-dl4m-)

## Contributors

- [Yann Bayle](http://yannbayle.fr/english/index.php) ([GitHub](https://github.com/ybayle)) - Instigator And Principal Maintainer
- Vincent Lostanlen ([GitHub](https://github.com/lostanlen))
- [Keunwoo Choi](https://keunwoochoi.wordpress.com/) ([GitHub](https://github.com/keunwoochoi))
- [Bob L. Sturm](http://www.eecs.qmul.ac.uk/~sturm/) ([GitHub](https://github.com/boblsturm))
- [Stefan Balke](https://www.audiolabs-erlangen.de/fau/assistant/balke) ([GitHub](https://github.com/stefan-balke))
- [Jordi Pons](http://www.jordipons.me/) ([GitHub](https://github.com/jordipons))
- Mirza Zulfan ([GitHub](https://github.com/mirzazulfan)) For The Logo
- [Devin Walters](https://github.com/devn)
- Https://github.com/LegendJ

[Go Back To Top](https://github.com/ybayle/awesome-deep-learning-music#deep-learning-for-music-dl4m-)

## Other Useful Related Lists And Resources

### Audio

- [DL4MIR Tutorial With Keras](https://github.com/tuwien-musicir/DL_MIR_Tutorial) - Tutorial For Deep Learning On Music Information Retrieval By [Thomas Lidy](http://ifs.tuwien.ac.at/~lidy/)
- [Video Talk From Ron Weiss](https://www.youtube.com/watch?v=sI_8EA0_ha8) - Ron Weiss (Google) Talk On Training Neural Network Acoustic Models On Waveforms
- [Slides On DL4M](http://www.jordipons.me/media/DL4Music_Pons.pdf) - A Personal (Re)view Of The State-of-the-art By [Jordi Pons](http://www.jordipons.me/)
- [DL4MIR Tutorial](https://github.com/marl/dl4mir-tutorial) - Python Tutorials For Learning To Solve MIR Tasks With DL
- [Awesome Python Scientific Audio](https://github.com/faroit/awesome-python-scientific-audio) - Python Resources For Audio And Machine Learning
- [ISMIR Resources](http://ismir.net/resources.php) - Community Maintained List
- [ISMIR Google Group](https://groups.google.com/a/ismir.net/forum/#!forum/community) - Daily Dose Of General MIR
- [Awesome Python](https://github.com/vinta/awesome-python#audio) - Audio Section Of Python Resources
- [Awesome Web Audio](https://github.com/notthetup/awesome-webaudio) - WebAudio Packages And Resources
- [Awesome Music](https://github.com/ciconia/awesome-music) - Music Software
- [Awesome Music Production](https://github.com/adius/awesome-music-production) - Music Creation
- [The Asimov Institute](http://www.asimovinstitute.org/analyzing-deep-learning-tools-music/) - 6 Deep Learning Tools For Music Generation
- [DLM Google Group](https://groups.google.com/forum/#!forum/icdlm) - Deep Learning In Music Group
- [MIR Community On Slack](https://slackpass.io/mircommunity) - Link To Subscribe To The MIR Community's Slack
- [Unclassified List Of MIR-related Links](http://www.music.mcgill.ca/~cmckay/links_academic.html) - [Cory McKay](http://www.music.mcgill.ca/~cmckay/)'s List Of Various Links On DL, MIR, …
- [MIRDL](http://jordipons.me/wiki/index.php/MIRDL) - Unmaintained List Of DL Articles For MIR From [Jordi Pons](http://www.jordipons.me/)
- [WWW 2018 Challenge](https://www.crowdai.org/challenges/www-2018-challenge-learning-to-recognize-musical-genre) - Learning To Recognize Musical Genre On The [FMA](https://github.com/mdeff/fma) Dataset
- [Music Generation With DL](https://github.com/umbrellabeach/music-generation-with-DL) - List Of Resources On Music Generation With Deep Learning
- [Auditory Scene Analysis](https://mitpress.mit.edu/books/auditory-scene-analysis) - Book About The Perceptual Organization Of Sound By [Albert Bregman](https://en.wikipedia.org/wiki/Albert_Bregman), The "Father Of [Auditory Scene Analysis](https://en.wikipedia.org/wiki/Auditory_scene_analysis)".
  - [Demonstrations Of Auditory Scene Analysis](http://webpages.mcgill.ca/staff/Group2/abregm1/web/downloadstoc.htm) - Audio Demonstrations, Which Illustrate Examples Of Auditory Perceptual Organization.

[Go Back To Top](https://github.com/ybayle/awesome-deep-learning-music#deep-learning-for-music-dl4m-)

### Music Datasets

- [AudioContentAnalysis Nearly Exhaustive List Of Music-related Datasets](http://www.audiocontentanalysis.org/data-sets/)
- [Teaching MIR](https://teachingmir.wikispaces.com/Datasets)
- [Wikipedia's List Of Datasets For Machine Learning Research](https://en.wikipedia.org/wiki/List_of_datasets_for_machine_learning_research#cite_ref-215)
- [Datasets For Deep Learning](http://deeplearning.net/datasets/)
- [Awesome Public Datasets](https://github.com/caesar0301/awesome-public-datasets)
- [Awesome Music Listening](https://github.com/ybayle/awesome-music-listening)

[Go Back To Top](https://github.com/ybayle/awesome-deep-learning-music#deep-learning-for-music-dl4m-)

### Deep Learning

- [DLPaper2Code: Auto-generation Of Code From Deep Learning Research Papers](https://arxiv.org/abs/1711.03543) -
- [Model Convertors](https://github.com/ysh329/deep-learning-model-convertor) - Convertors For DL Frameworks And Backend
- [Deep Architecture Genealogy](https://github.com/hunkim/deep_architecture_genealogy) - Genealogy Of DL Architectures
- [Deep Learning As An Engineer](http://www.univie.ac.at/nuhag-php/dateien/talks/3358_schlueter.pdf) - Slides From Jan Schlüter
- [Awesome Deep Learning](https://github.com/ChristosChristofidis/awesome-deep-learning) - General Deep Learning Resources
- [Awesome Deep Learning Resources](https://github.com/endymecy/awesome-deeplearning-resources) - Papers Regarding Deep Learning And Deep Reinforcement Learning
- [Awesome RNNs](https://github.com/kjw0612/awesome-rnn) - RNNs Code, Theory And Applications
- [Cheatsheets AI](https://github.com/kailashahirwar/cheatsheets-ai) - Cheat Sheets For Keras, Neural Networks, Scikit-learn,…
- [DL PaperNotes](https://github.com/dennybritz/deeplearning-papernotes) - Summaries And Notes On General Deep Learning Research Papers
- General [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome) Lists
- [Echo State Network](http://minds.jacobs-university.de/sites/default/files/uploads/papers/PracticalESN.pdf)
- [DL In NLP](http://ruder.io/deep-learning-nlp-best-practices/index.html#introduction) - Best Practices For Using Neural Networks By [Sebastian Ruder](http://ruder.io/)
- [CNN Overview](http://cs231n.github.io/convolutional-networks/) - Stanford Course
- [Dilated Recurrent Neural Networks](https://arxiv.org/pdf/1710.02224.pdf) - How To Improve RNNs?
- [Encoder-Decoder In RNNs](https://machinelearningmastery.com/how-does-attention-work-in-encoder-decoder-recurrent-neural-networks/?utm_content=buffer0d2a7&utm_medium=social&utm_source=twitter.com&utm_campaign=bufferhttps://blog.recast.ai/ml-spotlight-rnn/?utm_content=bufferf19d3&utm_medium=social&utm_source=twitter.com&utm_campaign=buffer) - How Does Attention Work In Encoder-Decoder Recurrent Neural Networks
- [On The Use Of DL](https://twitter.com/randal_olson/status/927157485240311808/photo/1) - Misc Fun Around DL
- [ML From Scratch](https://github.com/eriklindernoren/ML-From-Scratch) - Python Implementations Of ML Models And Algorithms From Scratch From Data Mining To DL
- [Comparison Of DL Frameworks](https://project.inria.fr/deeplearning/files/2016/05/DLFrameworks.pdf) - Presentation Describing The Different Existing Frameworks For DL
- [ELU > ReLU](https://arxiv.org/pdf/1511.07289.pdf) - Article Describing The Differences Between ELU And ReLU
- [Reinforcement Learning: An Introduction](http://incompleteideas.net/sutton/book/bookdraft2017nov5.pdf) - Book About Reinforcement Learning
- [Estimating Optimal Learning Rate](https://towardsdatascience.com/estimating-optimal-learning-rate-for-a-deep-neural-network-ce32f2556ce0) - Blog Post On The Learning Rate Optimisation
- [GitHub Repo For Sklearn Add-on For Imbalanced Learning](https://github.com/scikit-learn-contrib/imbalanced-learn) - ML In Uneven Datasets
- [Video On DL From Nando De Freitas, Scott Reed And Oriol Vinyals](https://www.youtube.com/watch?v=YJnddoa8sHk) - Deep Learning: Practice And Trends (NIPS 2017 Tutorial, Parts I & II)
- [Article "Are GANs Created Equal? A Large-Scale Study"](https://arxiv.org/abs/1711.10337) - Actually Comparing DL Algorithms
- [Battle Of The Deep Learning Frameworks](https://towardsdatascience.com/battle-of-the-deep-learning-frameworks-part-i-cff0e3841750) - DL Frameworks Comparison And Evolution
- [Black-box Optimization](http://timvieira.github.io/blog/post/2018/03/16/black-box-optimization/) - There Are Other Optimization Algorithms Than Just Gradient Descent

[Go Back To Top](https://github.com/ybayle/awesome-deep-learning-music#deep-learning-for-music-dl4m-)

## Cited By

If You Use The Information Contained In This Repository, Please Let Us Know! This Repository Is Cited By:

- [Alexander Schindler](https://twitter.com/Slychief/status/915218386421997568)
- [Meinard Müller, Christof Weiss, Stefan Balke](https://www.audiolabs-erlangen.de/resources/MIR/2017-GI-Tutorial-Musik/2017_MuellerWeissBalke_GI_DeepLearningMIR.pdf)
- [WWW 2018 Challenge: Learning To Recognize Musical Genre](https://www.crowdai.org/challenges/www-2018-challenge-learning-to-recognize-musical-genre)
- [Awesome Deep Learning](https://github.com/ChristosChristofidis/awesome-deep-learning)
- [AINewsFeed](https://twitter.com/AINewsFeed/status/897832912351105025)

[Go Back To Top](https://github.com/ybayle/awesome-deep-learning-music#deep-learning-for-music-dl4m-)
