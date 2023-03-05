# Audio Analysis With Machine Learning: Building AI-Fueled Sound Detection App | AltexSoft

---

![Wave,File,Of,Sound,On,Monitor,/,Record,Sound,In](https://content.altexsoft.com/media/2022/05/shutterstock_1131853538-scaled.jpg)

---

CONTENTS

- [What Is Audio Analysis?](https://www.altexsoft.com/blog/audio-analysis//#what-is-audio-analysis)
    - [Speech Recognition](https://www.altexsoft.com/blog/audio-analysis//#speech-recognition)
    - [Voice Recognition](https://www.altexsoft.com/blog/audio-analysis//#voice-recognition)
    - [Music Recognition](https://www.altexsoft.com/blog/audio-analysis//#music-recognition)
    - [Environmental Sound Recognition](https://www.altexsoft.com/blog/audio-analysis//#environmental-sound-recognition)
- [What Is Audio Data?](https://www.altexsoft.com/blog/audio-analysis//#what-is-audio-data)
    - [Audio Data File Formats](https://www.altexsoft.com/blog/audio-analysis//#audio-data-file-formats)
    - [Audio Data Transformation Basics To Know](https://www.altexsoft.com/blog/audio-analysis//#audio-data-transformation-basics-to-know)
    - [Audio Analysis Software](https://www.altexsoft.com/blog/audio-analysis//#audio-analysis-software)
    - [Audio Data Analysis Steps](https://www.altexsoft.com/blog/audio-analysis//#audio-data-analysis-steps)
- [Voice And Sound Data Acquisition](https://www.altexsoft.com/blog/audio-analysis//#voice-and-sound-data-acquisition)
    - [Free Data Sources](https://www.altexsoft.com/blog/audio-analysis//#free-data-sources)
    - [Commercial Datasets](https://www.altexsoft.com/blog/audio-analysis//#commercial-datasets)
    - [Expert Datasets](https://www.altexsoft.com/blog/audio-analysis//#expert-datasets)
- [Audio Data Preparation](https://www.altexsoft.com/blog/audio-analysis//#audio-data-preparation)
    - [Audio Data Labeling](https://www.altexsoft.com/blog/audio-analysis//#audio-data-labeling)
    - [Audio Data Preprocessing](https://www.altexsoft.com/blog/audio-analysis//#audio-data-preprocessing)
- [Feature Extraction](https://www.altexsoft.com/blog/audio-analysis//#feature-extraction)
    - [Time-domain Features](https://www.altexsoft.com/blog/audio-analysis//#time-domain-features)
    - [Frequency Domain Features](https://www.altexsoft.com/blog/audio-analysis//#frequency-domain-features)
    - [Time-frequency Domain Features](https://www.altexsoft.com/blog/audio-analysis//#time-frequency-domain-features)
- [Selecting And Training Machine Learning Models](https://www.altexsoft.com/blog/audio-analysis//#selecting-and-training-machine-learning-models)
    - [Long Short-term Memory Networks (LSTMs)](https://www.altexsoft.com/blog/audio-analysis//#long-short-term-memory-networks-lstms)
    - [Convolutional Neural Networks (CNNs)](https://www.altexsoft.com/blog/audio-analysis//#convolutional-neural-networks-cnns)
- [Building An App For Snore And Teeth Grinding Detection](https://www.altexsoft.com/blog/audio-analysis//#building-an-app-for-snore-and-teeth-grinding-detection)

---

We Live In The World Of Sounds: Pleasant And Annoying, Low And High, Quiet And Loud, They Impact Our Mood And Our Decisions. Our Brains Are Constantly Processing Sounds To Give Us Important Information About Our Environment. But Acoustic Signals Can Tell Us Even More If Analyze Them Using Modern Technologies.  

Today, We Have AI And [Machine Learning](https://www.altexsoft.com/whitepapers/machine-learning-bridging-between-business-and-data-science/) To Extract Insights, Inaudible To Human Beings, From Speech, Voices, Snoring, Music, Industrial And Traffic Noise, And Other Types Of Acoustic Signals. In This Article, We’ll Share What We’ve Learned When Creating AI-based Sound Recognition Solutions For Healthcare Projects.  

Particularly, We’ll Explain How To Obtain Audio Data, Prepare It For Analysis, And Choose The Right ML Model To Achieve The Highest Prediction Accuracy. But First, Let’s Go Over The Basics: What Is The Audio Analysis, And What Makes Audio Data So Challenging To Deal With.  

## What Is Audio Analysis?

Audio Analysis Is A Process Of Transforming, Exploring, And Interpreting Audio Signals Recorded By Digital Devices. Aiming At Understanding Sound Data, It Applies A Range Of Technologies, Including State-of-the-art [Deep Learning](https://www.altexsoft.com/blog/deep-learning/) Algorithms. Audio Analysis Has Already Gained Broad Adoption In Various Industries, From Entertainment To Healthcare To Manufacturing. Below We’ll Give The Most Popular Use Cases.

### Speech Recognition

**Speech Recognition** Is About The Ability Of Computers To Distinguish Spoken Words With [Natural Language Processing](https://www.altexsoft.com/blog/natural-language-processing/) Techniques. It Allows Us To Control PCs, Smartphones, And Other Devices Via Voice Commands And Dictate Texts To Machines Instead Of Manual Entering. Siri By Apple, Alexa By Amazon, Google Assistant, And Cortana By Microsoft Are Popular Examples Of How Deeply The Technology Has Penetrated Into Our Daily Lives.

### Voice Recognition

**Voice Recognition** Is Meant To Identify People By The Unique Characteristics Of Their Voices Rather Than To Isolate Separate Words. The Approach Finds Applications In Security Systems For User Authentication. For Instance, [Nuance Gatekeeper](https://www.nuance.com/omni-channel-customer-engagement/authentication-and-fraud-prevention/biometric-authentication.html) Biometric Engine Verifies Employees And Customers By Their Voices In The Banking Sector.

### Music Recognition

**Music Recognition** Is A Popular Feature Of Such Apps As [Shazam](https://www.shazam.com/gb/home) That Helps You Identify Unknown Songs From A Short Sample. Another Application Of Musical Audio Analysis Is Genre Classification: Say, [Spotify](https://www.spotify.com/ua-en/) Runs Its Proprietary Algorithm To Group Tracks Into Categories (Their Database Holds More Than [5,000 Genres](https://crimsonnews.org/7630/entertainment/spotifys-newest-non-genre/))

### Environmental Sound Recognition

**Environmental Sound Recognition** Focuses On The Identification Of Noises Around Us, Promising A Bunch Of Advantages To Automotive And Manufacturing Industries. It’s Vital For Understanding Surroundings In [IoT Applications](https://www.altexsoft.com/blog/iot-architecture-layers-components/).

Systems Like [Audio Analytic](https://www.audioanalytic.com/) ‘Listen’ To The Events Inside And Outside Your Car, Enabling The Vehicle To Make Adjustments In Order To Increase A Driver’s Safety. Another Example Is [SoundSee](https://www.bosch.com/research/know-how/success-stories/audio-ai/) Technology By Bosch That Can Analyze Machine Noises And Facilitate [Predictive Maintenance](https://www.altexsoft.com/blog/predictive-maintenance/) To Monitor Equipment Health And Prevent Costly Failures.

Healthcare Is Another Field Where Environmental Sound Recognition Comes In Handy. It Offers A Non-invasive Type Of [Remote Patient Monitoring](https://www.altexsoft.com/blog/remote-patient-monitoring-systems/) To Detect Events Like Falling. Besides That, Analysis Of Coughing, Sneezing, Snoring, And Other Sounds Can Facilitate Pre-screening, Identifying A Patient’s Status, Assessing The Infection Level In Public Spaces, And So On.

A Real-life Use Case Of Such Analysis Is [Sleep.ai](https://sleep.ai/) Which Detects Teeth Grinding And Snoring Sounds During Sleep. The Solution Created By AltexSoft For A Dutch Healthcare Startup Helps Dentists Identify And Monitor Bruxism To Eventually Understand The Causes Of This Abnormality And Treat It.

No Matter What Type Of Sounds You Analyze, It All Starts With An Understanding Of Audio Data And Its Specific Characteristics.

## What Is Audio Data?

Audio Data Represents Analog Sounds In A Digital Form, Preserving The Main Properties Of The Original. As We Know From School Lessons In Physics, A Sound Is A Wave Of Vibrations Traveling Through A Medium Like Air Or Water And Finally Reaching Our Ears. It Has Three Key Characteristics To Be Considered When Analyzing Audio Data—time Period, Amplitude, And Frequency.

**Time** **Period** Is How Long A Certain Sound Lasts Or, In Other Words, How Many Seconds It Takes To Complete One Cycle Of Vibrations.

**Amplitude** Is The Sound Intensity Measured In Decibels (DB) Which We Perceive As Loudness.

**Frequency** Measured In Hertz (Hz) Indicates How Many Sound Vibrations Happen Per Second. People Interpret Frequency As Low Or High **Pitch.**

While Frequency Is An Objective Parameter, The Pitch Is Subjective. The Human [Hearing Range](https://en.wikipedia.org/wiki/Hearing_range) Lies Between 20 And 20,000 Hz. Scientists Claim That Most People Perceive As Low Pitch All Sounds Below 500 Hz—like The Plane Engine Roar. In Turn, High Pitch For Us Is Everything Beyond 2,000 Hz (For Example, A Whistle.)

### Audio Data File Formats

Similar To Texts And Images, Audio Is [Unstructured Data](https://www.altexsoft.com/blog/structured-unstructured-data/) Meaning That It’s Not Arranged In Tables With Connected Rows And Columns. Instead, You Can Store Audio In Various File Formats Like

- WAV Or WAVE (Waveform Audio File Format) Developed By Microsoft And IBM. It’s A Lossless Or Raw File Format Meaning That It Doesn’t Compress The Original Sound Recording;
- AIFF (Audio Interchange File Format) Developed By Apple. Like WAV, It Works With Uncompressed Audio;
- FLAC (Free Lossless Audio Codec) Developed By Xiph.Org Foundation That Offers Free Multimedia Formats And Software Tools. FLAC Files Are Compressed Without Losing Sound Quality.
- MP3 (Mpeg-1 Audio Layer 3) Developed By The Fraunhofer Society In Germany And Supported Globally. It’s The Most Common File Format Since It Makes Music Easy To Store On Portable Devices And Send Back And Forth Via The Internet. Though Mp3 Compresses Audio, It Still Offers An Acceptable Sound Quality.

We Recommend Using Aiff And Wav Files For Analysis As They Don’t Miss Any Information Present In Analog Sounds. At The Same Time, Keep In Mind That Neither Of Those And Other Audio Files Can Be Fed Directly To Machine Learning Models. To Make Audio Understandable For Computers, Data Must Undergo A Transformation.

### Audio Data Transformation Basics To Know

Before Diving Deeper Into The Processing Of Audio Files, We Need To Introduce Specific Terms, That You Will Encounter At Almost Every Step Of Our Journey From Sound Data Collection To Getting ML Predictions. It’s Worth Noting That Audio Analysis Involves Working With Images Rather Than Listening.

A **Waveform** Is A Basic Visual Representation Of An Audio Signal That Reflects How An Amplitude Changes Over Time. The Graph Displays The Time On The Horizontal (X) Axis And The Amplitude On The Vertical (Y) Axis But It Doesn’t Tell Us What’s Happening To Frequencies.

![](Https://content.altexsoft.com/media/2022/05/word-image-6.png.webp)

![](Https://content.altexsoft.com/media/2022/05/word-image-6.png)

*An Example Of A Waveform. Source:* [*Audio Singal Processing For Machine Learning*](https://www.youtube.com/watch?v=bnHHVo3j124&list=PL-wATfeyAMNqIee7cH3q1bh4QJFAaeNv0&index=2&ab_channel=ValerioVelardo-TheSoundofAI)

A **Spectrum Or Spectral Plot** Is A Graph Where The X-axis Shows The Frequency Of The Sound Wave While The Y-axis Represents Its Amplitude. This Type Of Sound [Data Visualization](https://www.altexsoft.com/blog/data-visualization-tools-types-techniques/) Helps You Analyze Frequency Content But Misses The Time Component.

**![](Https://content.altexsoft.com/media/2022/05/word-image-7.png.webp)

![](Https://content.altexsoft.com/media/2022/05/word-image-7.png)

**

*An Example Of A Spectrum Plot. Source:* [*Analytics Vidhya*](https://medium.com/analytics-vidhya/understanding-the-mel-spectrogram-fca2afa2ce53)

A **Spectrogram** Is A Detailed View Of A Signal That Covers All Three Characteristics Of Sound. You Can Learn About Time From The X-axis, Frequencies From The Y-axis, And Amplitude From Color. The Louder The Event The Brighter The Color, While Silence Is Represented By Black. Having Three Dimensions On One Graph Is Very Convenient: It Allows You To Track How Frequencies Change Over Time, Examine The Sound In All Its Fullness, And Spot Various Problem Areas (Like Noises) And Patterns By Sight.

![](Https://content.altexsoft.com/media/2022/05/word-image-8.png.webp)

![](Https://content.altexsoft.com/media/2022/05/word-image-8.png)

*An Example Of A Spectrogram. Source:* [*IZotope*](https://www.izotope.com/en/learn/understanding-spectrograms.html)

A **Mel Spectrogram** Where Mel Stands For Melody Is A Type Of Spectrogram Based On The Mel Scale That Describes How People Perceive Sound Characteristics. Our Ear Can Distinguish Low Frequencies Better Than High Frequencies. You Can Check It Yourself: Try To [Play Tones](https://www.youtube.com/watch?v=el-n-GdTjL8&ab_channel=HCSCARAUDIO) From 500 To 1000 Hz And Then From 10,000 To 10,500 Hz. The Former Frequency Range Would Seem Much Broader Than The Latter, Though, In Fact, They Are The Same. The Mel Spectrogram Incorporates This Unique Feature Of Human Hearing, Converting The Values In Hertz Into The Mel Scale. This Approach Is Widely Used For Genre Classification, Instrument Detection In Songs, And Speech Emotion Recognition.

![](Https://content.altexsoft.com/media/2022/05/word-image.jpeg.webp)

![](Https://content.altexsoft.com/media/2022/05/word-image.jpeg)

*An Example Of A Mel Spectrogram. Source:* [*Devopedia*](https://devopedia.org/audio-feature-extraction)

The **Fourier Transform (FT)** Is A Mathematical Function That Breaks A Signal Into Spikes Of Different Amplitudes And Frequencies. We Use It To Convert Waveforms Into Corresponding Spectrum Plots To Look At The Same Signal From A Different Angle And Perform Frequency Analysis. It’s A Powerful Instrument To Understand Signals And Troubleshooting Errors In Them.

The **Fast Fourier Transform (FFT)** Is The Algorithm Computing The Fourier Transform.

![](Https://content.altexsoft.com/media/2022/05/word-image-9.png.webp)

![](Https://content.altexsoft.com/media/2022/05/word-image-9.png)

*Applying FFT To View The Same Signal From Time And Frequency Perspectives. Source:* [*NTi Audio*](https://www.nti-audio.com/en/support/know-how/fast-fourier-transform-fft)

The **Short-time Fourier Transform (STFT)** Is A Sequence Of Fourier Transforms Converting A Waveform Into A Spectrogram.

### Audio Analysis Software

Of Course, You Don’t Need To Perform Transformations Manually. Neither Need You To Understand The Complex Mathematics Behind FT, STFT, And Other Techniques Used In Audio Analysis. All These And Many Other Tasks Are Done Automatically By Audio Analysis Software That In Most Cases Supports The Following Operations:

- Import Audio Data
- Add Annotations (Labels),
- Edit Recordings And Split Them Into Pieces,
- Remove Noise,
- Convert Signals Into Corresponding Visual Representations (Waveforms, Spectrum Plots, Spectrograms, Mel Spectrograms),
- Do Preprocessing Operations,
- Analyze Time And Frequency Content,
- Extract Audio Features And More.

The Most Advanced Platforms Also Allow You To Train Machine Learning Models And Even Provide You With Pre-trained Algorithms.

Here Is The List Of The Most Popular Tools Used In Audio Analysis.

[Audacity](https://www.audacityteam.org/) Is A Free And Open-source Audio Editor To Split Recordings, Remove Noise, Transform Waveforms To Spectrograms, And Label Them. Audacity Doesn’t Require Coding Skills. Yet, Its Toolset For Audio Analysis Is Not Very Sophisticated. For Further Steps, You Need To Load Your Dataset To [Python](https://www.altexsoft.com/blog/python-pros-and-cons/) Or Switch To A Platform Specifically Focusing On Analysis And/or Machine Learning.

![](Https://content.altexsoft.com/media/2022/05/word-image-1.jpeg.webp)

![](Https://content.altexsoft.com/media/2022/05/word-image-1.jpeg)

*Labeling Of Audio Data In Audacity. Source:* [*Towards Data Science*](https://towardsdatascience.com/how-to-label-audio-for-deep-learning-in-4-simple-steps-6a2c33b343e6)

[Tensorflow-io Package](https://www.tensorflow.org/io/tutorials/audio) For Preparation And Augmentation Of Audio Data Lets You Perform A Wide Range Of Operations—noise Removal, Converting Waveforms To Spectrograms, Frequency, And Time Masking To Make The Sound Clearly Audible, And More. The Tool Belongs To The Open-source TensorFlow Ecosystem, Covering End-to-end Machine Learning Workflow. So, After Preprocessing You Can Train An ML Model On The Same Platform.

[Librosa](https://librosa.org/doc/latest/index.html) Is An Open-source Python Library That Has Almost Everything You Need For Audio And Music Analysis. It Enables Displaying Characteristics Of Audio Files, Creating All Types Of Audio Data Visualizations, And Extracting Features From Them, To Name Just A Few Capabilities.

[Audio Toolbox By MathWorks](https://www.mathworks.com/help/audio/) Offers Numerous Instruments For Audio Data Processing And Analysis, From Labeling To Estimating Signal Metrics To Extracting Certain Features. It Also Comes With Pre-trained Machine Learning And Deep Learning Models That Can Be Used For Speech Analysis And Sound Recognition.

### Audio Data Analysis Steps

Now That We Have A Basic Understanding Of Sound Data, Let’s Take A Glance At The Key Stages Of The End-to-end Audio Analysis Project.

1. **Obtain** Project-specific Audio Data Stored In Standard File Formats.
2. **Prepare Data** For Your Machine Learning Project, Using Software Tools
3. **Extract** Audio Features From Visual Representations Of Sound Data.
4. **Select** The Machine Learning Model And **Train** It On Audio Features.

![](Https://content.altexsoft.com/media/2022/05/word-image-10.png.webp)

![](Https://content.altexsoft.com/media/2022/05/word-image-10.png)

*Steps Of Audio Analysis With Machine Learning*

## Voice And Sound Data Acquisition

You Have Three Options To Obtain Data To Train Machine Learning Models: Use Free Sound Libraries Or Audio Datasets, Purchase It From Data Providers, Or Collect It Involving Domain Experts.

### Free Data Sources

There Are A Lot Of Such Sources Out There On The Web. But What We Do Not Control In This Case Is [Data Quality](https://www.altexsoft.com/blog/data-quality-management-and-tools/) And Quantity, And The General Approach To Recording.

**Sound Libraries** Are Free Audio Pieces Grouped By Theme. Sources Like [Freesound](https://freesound.org/browse/packs/?order=-last_updated) And [BigSoundBank](https://bigsoundbank.com/search) Offer Voice Recordings, Environment Sounds, Noises, And Honestly All Kinds Of Stuff. For Example, You Can Find The Soundscape Of The [Applause](https://bigsoundbank.com/detail-2479-applause-concert-bar-1.html), And The Set With [Skateboard](https://freesound.org/people/Rbrtbiehl/packs/34912/) Sounds.

The Most Important Thing Is That Sound Libraries Are Not Specifically Prepared For Machine Learning Projects. So, We Need To Perform Extra Work On Set Completion, Labeling, And Quality Control.

**Audio Datasets** Are, On The Contrary, Created With Particular Machine Learning Tasks In Mind. For Instance, The [Bird Audio Detection](https://dagshub.com/kingabzpro/Bird-Audio-Detection-challenge) Dataset By The [Machine Listening Lab](http://machine-listening.eecs.qmul.ac.uk/#:~:text=In%20the%20Machine%20Listening%20Lab,extract%20useful%20information%20from%20sound.) Has More Than 7,000 Excerpts Collected During Bio-acoustics Monitoring Projects. Another Example Is The [ESC-50: Environmental Sound Classification](https://dagshub.com/kinkusuma/esc50-dataset) Dataset, Containing 2,000 Labeled Audio Recordings. Each File Is 5 Seconds Long And Belongs To One Of The 50 Semantical Classes Organized In Five Categories.

One Of The Largest Audio Data Collections Is [AudioSet](https://research.google.com/audioset/index.html) By Google. It Includes Over 2 Million Human-labeled 10-second Sound Clips, Extracted From YouTube Videos. The Dataset Covers 632 Classes, From Music And Speech To Splinter And Toothbrush Sounds.

### Commercial Datasets

Commercial Audio Sets For Machine Learning Are Definitely More Reliable In Terms Of [Data Integrity](https://www.altexsoft.com/blog/data-integrity/) Than Free Ones. We Can Recommend [ProSoundEffects](https://www.prosoundeffects.com/machine-learning-audio-research-datasets/) Selling Datasets To Train Models For Speech Recognition, Environmental Sound Classification, Audio Source Separation, And Other Applications. In Total, The Company Has 357,000 Files Recorded By Experts In Film Sound And Classified Into 500+ Categories.

But What If The Sound Data You’re Looking For Is Way Too Specific Or Rare? What If You Need Full Control Of The Recording And Labeling? Well, Then Better Do It In A Partnership With Reliable Specialists From The Same Industry As Your Machine Learning Project.

### Expert Datasets

When Working With Sleep.ai, Our Task Was To Create A Model Capable Of Identifying Grinding Sounds That People With Bruxism Typically Make During Sleep. Clearly, We Needed Special Data, Not Available Through Open Sources. Also, The Data Reliability And Quality Had To Be The Best So We Could Get Trustworthy Results.

To Obtain Such A Dataset, The Startup Partnered With Sleep Laboratories, Where Scientists Monitor People While They Are Sleeping To Define Healthy Sleep Patterns And Diagnose Sleep Disorders. Experts Use Various Devices To Record Brain Activity, Movements, And Other Events. For Us, They Prepared A Labeled Data Set With About 12,000 Samples Of Grinding And Snoring Sounds.

## Audio Data Preparation

In The Case Of Sleep.io, Our Team Skipped This Step Entrusting Sleep Experts With The Task Of Data Preparation For Our Project. The Same Relates To Those Who Buy Annotated Sound Collections From Data Providers. But If You Have Only Raw Data Meaning Recordings Saved In One Of The Audio File Formats You Need To Get Them Ready For Machine Learning.

### Audio Data Labeling

[Data Labeling](https://www.altexsoft.com/blog/data-labeling/) Or Annotation Is About Tagging Raw Data With Correct Answers To Run [Supervised Machine Learning](https://www.altexsoft.com/blog/business/supervised-learning-use-cases-low-hanging-fruit-in-data-science-for-businesses/). In The Process Of Training, Your Model Will Learn To Recognize Patterns In New Data And Make The Right Predictions, Based On The Labels. So, Their Quality And Accuracy Are Critical For The Success Of ML Projects.

Though Labeling Suggests Assistance From Software Tools And Some Degree Of Automation, For The Most Part, It’s Still Performed Manually, By Professional Annotators And/or Domain Experts. In Our Bruxism Detection Project, Sleep Experts Listened To Audio Recordings And Mark Them With Grinding Or Snoring Labels.

*Learn More About Approaches To Annotation From Our Article* [*How To Organize Data Labeling For Machine Learning*](https://www.altexsoft.com/blog/datascience/how-to-organize-data-labeling-for-machine-learning-approaches-and-tools/)

### Audio Data Preprocessing

Besides Enriching Data With Meaningful Tags, We Have To Preprocess Sound Data To Achieve Better Prediction Accuracy. Here Are The Most Basic Steps For Speech Recognition And Sound Classification Projects.

**Framing** Means Cutting The Continuous Stream Of Sound Into Short Pieces (Frames) Of The Same Length (Typically, Of 20-40 Ms) For Further Segment-wise Processing.

**Windowing** Is A Fundamental Audio Processing Technique To Minimize Spectral Leakage—the Common Error That Results In Smearing The Frequency And Degrading The Amplitude Accuracy. There Are Several Window Functions (Hamming, Hanning, Flat Top, Etc) Applied To Different Types Of Signals, Though The Hanning Variation Works Well For [95 Percent](https://download.ni.com/evaluation/pxi/Understanding%20FFTs%20and%20Windowing.pdf) Of Cases.

Basically, All Windows Do The Same Thing: Reduce Or Smooth The Amplitude At The Start And The End Of Each Frame While Increasing It At The Center To Preserve The Average Value.

![](Https://content.altexsoft.com/media/2022/05/word-image-11.png.webp)

![](Https://content.altexsoft.com/media/2022/05/word-image-11.png)

*The Signal Waveform Before And After Windowing. Source:* [*National Instruments*](https://zone.ni.com/reference/en-XX/help/371361R-01/lvanlsconcepts/windowing_signals/).

**Overlap-add (OLA)** Method Prevents Losing Vital Information That Can Be Caused By Windowing**.** OLA Provides 30-50 Percent Overlap Between Adjacent Frames, Allowing To Modify Them Without The Risk Of Distortion. In This Case, The Original Signal Can Be Accurately Reconstructed From Windows.

![](Https://content.altexsoft.com/media/2022/05/word-image-12.png.webp)

![](Https://content.altexsoft.com/media/2022/05/word-image-12.png)

*An Example Of Windowing With Overlapping. Source:* [*Aalto University Wiki*](https://wiki.aalto.fi/display/ITSP/Windowing)

*Learn More About The Preprocessing Stage And Techniques It Uses From Our Article* [*Preparing Your Data For Machine Learning*](https://www.altexsoft.com/blog/datascience/preparing-your-dataset-for-machine-learning-8-basic-techniques-that-make-your-data-better/) *And The Video Below.*

[*Https://youtu.be/P8ERBy91Y90*](https://youtu.be/P8ERBy91Y90)

## Feature Extraction

Audio Features Or Descriptors Are Properties Of Signals, Computed From Visualizations Of Preprocessed Audio Data. They Can Belong To One Of Three Domains

- Time Domain Represented By Waveforms,
- Frequency Domain Represented By Spectrum Plots, And
- Time And Frequency Domain Represented By Spectrograms.

![](Https://content.altexsoft.com/media/2022/05/word-image-13.png.webp)

![](Https://content.altexsoft.com/media/2022/05/word-image-13.png)

*Audio Data Visualization: Waveform For Time Domain, Spectrum For Frequency Domain, And Spectrogram For Time-and-frequency Domain. Source:* [*Types Of Audio Features For ML.*](https://www.youtube.com/watch?v=ZZ9u1vUtcIA&list=PL-wATfeyAMNqIee7cH3q1bh4QJFAaeNv0&index=7)

### Time-domain Features

As We Mentioned Before, Time Domain Or Temporal Features Are Extracted Directly From Original Waveforms. Notice That Waveforms Don’t Contain Much Information On How The Piece Would Really Sound. They Indicate Only How The Amplitude Changes With Time. In The Image Below We Can See That The Air Condition And Siren Waveforms Look Alike, But Surely Those Sounds Would Not Be Similar.

![](Https://content.altexsoft.com/media/2022/05/word-image-14.png.webp)

![](Https://content.altexsoft.com/media/2022/05/word-image-14.png)

*Waveforms Examples. Source:* [*Towards Data Science*](https://towardsdatascience.com/how-to-apply-machine-learning-and-deep-learning-methods-to-audio-analysis-615e286fcbbc)

Now Let’s Move To Some Key Features We Can Draw From Waveforms.

**Amplitude Envelope (AE)** Traces Amplitude Peaks Within The Frame And Shows How They Change Over Time. With AE, You Can Automatically Measure The Duration Of Distinct Parts Of A Sound (As Shown In The Picture Below). AE Is Widely Used For The Onset Detection To Indicate When A Certain Signal Starts, And For Music Genre Classification.

![](Https://content.altexsoft.com/media/2022/05/word-image-15.png.webp)

![](Https://content.altexsoft.com/media/2022/05/word-image-15.png)

*The Amplitude Envelope Of A Tico-tico Bird Singing. Source:* [*Seewave: Sound Anaysis Principles*](https://cran.r-project.org/web/packages/seewave/vignettes/seewave_analysis.pdf)

**Short-time Energy (STE)** Shows The Energy Variation Within A Short Speech Frame.

It’s A Powerful Tool To Separate Voiced And Unvoiced Segments.

**Root Mean Square Energy** (RMSE) Gives You An Understanding Of The Average Energy Of The Signal. It Can Be Computed From A Waveform Or A Spectrogram. In The First Case, You’ll Get Results Faster. Yet, A Spectrogram Provides A More Accurate Representation Of Energy Over Time. RMSE Is Particularly Useful For Audio Segmentation And Music Genre Classification.

**Zero-crossing Rate (ZCR)** Counts How Many Times The Signal Wave Crosses The Horizontal Axis Within A Frame. It’s One Of The Most Important Acoustic Features, Widely Used To Detect The Presence Or Absence Of Speech, And Differentiate Noise From Silence And Music From Speech.

### Frequency Domain Features

Frequency-domain Features Are More Difficult To Extract Than Temporal Ones As The Process Involves Converting Waveforms Into Spectrum Plots Or Spectrograms Using FT Or STFT. Yet, It’s The Frequency Content That Reveals Many Important Sound Characteristics Invisible Or Hard To See In The Time Domain.

The Most Common Frequency Domain Features Include

- Mean Or Average Frequency,
- Median Frequency When The Spectrum Is Divided Into Two Regions With Equal Amplitude,
- Signal-to-noise Ratio (SNR) Comparing The Strength Of Desired Sound Against The Background Nose,
- Band Energy Ratio (BER) Depicting Relations Between Higher And Lower Frequency Bands. In Other Words. It Measures How Low Frequencies Are Dominant Over High Ones.

Of Course, There Are Numerous Other Properties To Look At In This Domain. To Recap, It Tells Us How The Sound Energy Spreads Across Frequencies While The Time Domain Shows How A Signal Change Over Time.

### Time-frequency Domain Features

This Domain Combines Both Time And Frequency Components And Uses Various Types Of Spectrograms As A Visual Representation Of A Sound. You Can Get A Spectrogram From A Waveform Applying The Short-time Fourier Transform.

One Of The Most Popular Groups Of Time-frequency Domain Features Is **Mel-frequency Cepstral Coefficients (MFCCs)**. They Work Within The Human Hearing Range And As Such Are Based On The Mel Scale And Mel Spectrograms We Discussed Earlier.

No Surprise That The Initial Application Of MFCCs Is Speech And Voice Recognition. But They Also Proved To Be Effective For Music Processing And [Acoustic Diagnostics](https://www.researchgate.net/figure/a-Mel-frequency-cepstral-coefficients-MFCC-deformed-male-speech-laryngean-polypus_fig1_5766666) For Medical Purposes, Including Snoring Detection. For Example, One Of The Recent [Deep Learning Models](https://www.mdpi.com/2079-9292/8/9/987) Developed By The School Of Engineering (Eastern Michigan University) Was Trained On 1000 MFCC Images (Spectrograms) Of Snoring Sounds.

![](Https://content.altexsoft.com/media/2022/05/word-image-16.png.webp)

![](Https://content.altexsoft.com/media/2022/05/word-image-16.png)

*The Waveform Of Snoring Sound (A) And Its MFCC Spectrogram (B) Compared With The Waveform Of The Toilet Flush Sound (C) And Corresponding MFCC Image (D). Source: A Deep Learning Model For Snoring Detection (*[*Electronic Journal, Vol.8, Issue 9*](https://www.mdpi.com/2079-9292/8/9/987)*)*

To Train A Model For The Sleep.ai Project, Our Data Scientists Selected A Set Of Most Relevant Features From Both The Time And Frequency Domains. In Combination, They Created Rich Profiles Of Grinding And Snoring Sounds.

## Selecting And Training Machine Learning Models

Since Audio Features Come In The Visual Form (Mostly As Spectrograms), It Makes Them An Object Of [Image Recognition](https://www.altexsoft.com/blog/image-recognition-neural-networks-use-cases/) That Relies On Deep Neural Networks. There Are Several Popular Architectures Showing Good Results In Sound Detection And Classification. Here, We Only Focus On Two Commonly Used To Identify Sleep Problems By Sound.

### Long Short-term Memory Networks (LSTMs)

**Long Short-term Memory Networks (LSTMs)** Are Known For Their Ability To Spot Long-term Dependencies In Data And Remember Information From Numerous Prior Steps. According To Sleep Apnea Detection Research, LSTMs Can Achieve An Accuracy Of [87 Percent](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7787852/) When Using MFCC Features As Input To Separate Normal Snoring Sounds From Abnormal Ones.

Another Study Shows Even Better Results: The LSTM Classified Normal And Abnormal Snoring Events With An Accuracy Of [95.3 Percent](https://www.sciencedirect.com/science/article/abs/pii/S1746809421008351). The Neural Network Was Trained Using Five Types Of Features Including MFCCs And Short-time Energy From The Time Domain. Together, They Represent Different Characteristics Of Snoring.

### Convolutional Neural Networks (CNNs)

Convolutional Neural Networks Lead The Pack In [Computer Vision In Healthcare](https://www.altexsoft.com/blog/computer-vision-healthcare/) And Other Industries. They Are Often Referred To As *A Natural Choice For Image Recognition Tasks*. The Efficiency Of CNN Architecture In Spectrogram Processing Proves The Validity Of This Statement One More Time.

In The Above-mentioned Project By The School Of Engineering (Eastern Michigan University) A CNN-based Deep Learning Model Hit An Accuracy Of [96 Percent](https://www.mdpi.com/2079-9292/8/9/987) In The Classification Of Snoring Vs Non-snoring Sounds.

Almost The Same Results Are Reported For The Combination Of CNN And LSTM Architectures. The Group Of Scientists From The Eindhoven University Of Technology Applied The CNN Model To Extract Features From Spectrograms And Then Run The LSTM To Classify The CNN Output Into Snore And Non-snore Events. The Accuracy Values Range From [94.4 To 95.9 Percent](https://www.sciencedirect.com/science/article/pii/S0169260720317508#!) Depending On The Location Of The Microphone Used For Recording Snoring Sounds.

For Sleep.io Project, The AltexSoft Data Science Team Used Two CNNs (For Snoring And Grinding Detection) And Trained It On The TensorFlow Platform. After Models Achieved An Accuracy Of Over 80 Percent, They Were Launched To Production. Their Results Have Been Constantly Getting Better With The Growing Number Of Inputs Collected From Real Users.
