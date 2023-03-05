# Plugin APIs

There Are Quite A Few Audio Plugin API Standards Which Allow Your Plugin Be Compatible With Certain DAWs And Hosts. I'll List The Most Relevant Ones Today And Their Advantages/disadvantages.

(If You Just Want One Recommendation From Me, Go For The CLAP Plugin Standard.)

## CLAP

  - Why?: A Brand New Fully Free And Open-source Plugin Standard With No Licensing Restrictions. It Was Started By An Employee Of The Bitwig DAW And Has Since Gotten Development Support From Several Key Players In The Audio Industry. It Is Built From The Ground Up By People With Real-world Experience Developing Audio Software, And Such It Is Designed To Fit The Needs Of Actual Developers As Much As Possible. It Is Written In A Stable Header-only C API, Making It Easy To Create Bindings To It In Any Programming Language.
  - Why Not?: It Is Still Kind-of Young, And Only A Handful Of DAWs Support This Standard. But This Is Changing Pretty Quick, And Expect Many More DAWs To Adpot This Standard!
  - License: [`MIT`]
  - Platforms: Linux, Mac, Windows, Android, IOS
  - Support: Currently Only Supported By A Handful Of DAWs Such As Bitwig, MultitrackStudio, And QTractor, But More DAWs Are Currently In The Works To Adopt This Standard.
  - Distribution - You Can Distribute Open Source And Close Sourced Versions Of Your Plugins (And Host CLAP Plugins) Freely Without Restriction.
  - SDK Source: [`CLAP SDK`] (Also Includes Links To Examples)

## VST2 (Aka VST, Version 2)

  - Why?: It Is The Most Well-known And Mature Format, Supported By Almost Every DAW.
  - Why Not?: Unless You Already Have A Signed License Agreement From Steinberg, You're Not Even Allowed To Distribute Your VST2 Plugins Or Create A Host For VST2 Plugins.
  - License: Proprietary
  - Platforms: Linux, Mac, Windows
  - Support: Supported By Pretty Much Every Commercial DAW (With Notable Exception Of Apple's DAW Logic) And By Most Open Source DAWs.
  - Distribution: Must Have A Signed License Agreement To Distribute Any VST2 Plugin. If You Don't Already Have A VST2 License, You're Out Of Luck Since Steinberg Doesn't Support It Anymore (Yeah It Stinks).
  - SDK Source: (Not Available Anymore).

## Vestige (Reversed Engineered VST2)

  - Why?: If You Still *Really* Need To Distribute Or Host VST2 Plugins Without A Signed License Agreement, This Is Another Option.
  - Why Not?: Gray Legal Area.
  - License: *Technically* [`GPLv2`]/[`GPLv3`], But Again This Is A Gray Legal Area. It Is Technically Legal Since The Author Claims It To Be Cleanly And Legally Reverse Engineered Without Reference To The Official VST2 SDK. However, I Don't Believe This Has Been Tested In Court, So I Wouldn't Rely On It.
  - Platforms: Same As VST2 Above.
  - Support: Same As VST2 Above.
  - Distribution: You Can Only Distribute Your Plugins Or Host As Open Source Under Either The [`GPLv2`] Or [`GPLv3`] License. Though Again, This Is A Gray Legal Area So I Would Be Weary.
  - SDK Source: [`Vestige Header File`]

## VST3 (Aka VST Version 3)

  - Why?: This Plugin Standard Is Widely Used And Has Excellent Support In Most Modern Commercial DAWs.
  - Why Not?: Requires A Signed License Agreement With Steinberg In Order To Distribute Commercial (Closed Source) VST3 Plugins (Or To Host VST3 Plugins In A Closed Source Host). Also, The Standard Is Based On A Large And Complicated C++ Codebase, And Steinberg Is Not On-board With People Distributing Bindings To Other Languages (Like [`Rust`]).
  - License: Proprietary / [`GPLv3`]
  - Platforms: Linux, Mac, Windows
  - Support: Supported By Most Modern Commercial DAWs (With Notable Exception Of Apple's DAW Logic) And A Few Open Source DAWs.
  - Distribution - If You Are Distributing Your Plugin With The [`GPLv3`] Open Source License (Or Host VST3 Plugins With Your Own [`GPLv3`] Host), Then You Do Not Need To Have A Signed License Agreement With Steinberg. However, If You Want To Distribute Your Plugin Closed Source (For Commercial Purposes) Or Create A Closed-source Host, Then You Need To Get A Signed [`VST3 License Agreement`].
    - Also Note That Steinberg Has A History Of Changing Their License Agreements For However They See Fit (Like They Did When They Stopped Giving Out VST2 Licenses). If You Want To Ever Distribute Plugins Commercially, I Would Advise To Get A License Agreement As Soon As Possible Before Steinberg Changes Their Mind.
  - SDK Download: [`VST3 SDK`]

## AUv2/AUv3 (Aka AU Or Audio Units, Version 2 And 3)

  - License: [`Apache 2.0`]
  - Platforms: Mac, IOS
  - Support: Main Support Is For Apple's Own Logic DAW, But A Few Other DAWs That Run On Mac Support It As Well. AU Is The Only Plugin Standard Supported By Logic.
  - Distribution - You Can Distribute Open Source And Close Sourced Versions Of Your Plugins (And Host AU Plugins) Freely Without Restriction.
  - SDK Source: [`AU SDK`]

## AAX

This Is A Proprietary Plugin Standard For Use Exclusively With Avid's DAW Pro Tools.

  - Why?: Pro Tools Is Pretty Standard In The Professional/corporate Recording/mixing/mastering Industry. Pro Tools Only Supports AAX Plugins.
  - Why Not?: No Other DAW Supports It. Also, It Requires A Signed License Agreement With Avid, And Also Requires Joining Avid's Developer Program.
  - License: Proprietary
  - Platforms: Mac, Windows
  - Support: Only Pro Tools
  - Distribution: Requires A Signed License Agreement With Avid, And Also Requires Joining Avid's Developer Program.
  - SDK Source: (Must Register To Download)

## LV2

 LV2 Is A Free And Open Source Plugin Standard Created For Use Within The Linux Ecosystem.

  - Why?: Even Though Support On Mac And Windows Is Rare, Linux Has By Far The Best Development Ecosystem In My Opinion. There Is Also A Growing Community Of Music Producers Using Linux.
  - Why Not?: Lack Of Support In Most Major Commercial DAWs, And The New CLAP Spec Makes This Standard Obsolete In My Opinion.
  - License: [`MIT`]
  - Platforms: Linux, Mac, Windows (Although Support For Mac And Windows Is Rare.)
  - Support: Supported By Most Open-source DAWs, But Hardly Any Commercial DAWs Support It (Maybe Even None Of Them Do).
  - Distribution - You Can Distribute Open Source And Close Sourced Versions Of Your Plugins (And Host LV2 Plugins) Freely Without Restriction.
  - SDK Source: [`LV2 SDK`]
  - [`Sjaehn's LV2 Tutorial`] - A Nice Tutorial On Developing LV2 Plugins.

## LADSPA

LADSPA Is The Precursor To LV2.

  - Why?: It Is Dead Simple To Work With.
  - Why Not?: Lack Of Support In Most Major Commercial DAWs. Also, LADSPA Only Supports GUI-less Plugins. Again, The New CLAP Spec Makes This Standard Obsolete In My Opinion.
  - License: [`LGPLv2.1`]/[`LGPLv3`]
  - Platforms: Same As LV2 Above
  - Support: Same As LV2 Above
  - Distribution: Same As LV2 Above
  - SDK Source: [`LADSPA Header File`]

## WAP (Web Audio Plugins)

An Open Source Audio Plugin Standard For Use With Web Browsers Using WebAudio.

  - Why?: If You Want To Target Web-based DAWs.
  - Why Not?: Only Works In A Web Browser, So All Native DAWs Don't Support It.
  - License: [`MIT`]
  - Platforms: Web
  - Support: Only Web-browser Based DAWs
  - Distribution: You Can Distribute Open Source And Close Sourced Versions Of Your Plugins (And Host WAP Plugins) Freely Without Restriction.
  - SDK Source: [`WAP SDK`]

## VCV Rack / Cardinal Plugin

The Audio Plugin Standard For Use With The Open Source [`VCV Rack`] Or [`Cardinal`] Virtual Synthesizer.

  - Why?: If You Want To Create Plugins For [`VCV Rack`] / [`Cardinal`].
  - License: [`GPLv3`]
  - Distribution: You Can Distribute Freely If Your Plugin Is [`GPLv3`] Or A Multitude Of Other Accepted Open Source Licenses. You Are Allowed To Sell Closed-source Versions If You Get Special Permission From The Author Via Email. See [`VCV Rack Licensing`] For More Details.
  - SDK Source: [`VCV Rack Plugin SDK`]
  - [`VCV Rack Plugin Tutorial`] - The Official Tutorial On Making VCV Rack Plugins.

[`Vestige Header File`]: Https://github.com/x42/lv2vst/blob/master/include/vestige.h

[`VST3 License Agreement`]: Https://developer.steinberg.help/pages/viewpage.action?pageId=9797944
[`VST3 SDK`]: Https://github.com/steinbergmedia/vst3sdk
[`Rust`]: Https://www.rust-lang.org/

[`AU SDK`]: Https://github.com/apple/AudioUnitSDK

[`LV2 SDK`]: Https://gitlab.com/lv2/lv2
[`Sjaehn's LV2 Tutorial`]: Https://github.com/sjaehn/lv2tutorial

[`LADSPA Header File`]: Https://www.ladspa.org/ladspa_sdk/ladspa.h.txt

[`CLAP SDK`]: Https://github.com/free-audio/clap

[`WAP SDK`]: Https://github.com/micbuffa/WebAudioPlugins

[`VCV Rack`]: Https://vcvrack.com/
[`Cardinal`]: Https://github.com/DISTRHO/Cardinal
[`VCV Rack Licensing`]: Https://vcvrack.com/manual/PluginLicensing
[`VCV Rack Plugin SDK`]: Https://vcvrack.com/downloads/
[`VCV Rack Plugin Tutorial`]: Https://vcvrack.com/manual/PluginDevelopmentTutorial

[`GPLv2`]: Https://opensource.org/licenses/gpl-2.0.php
[`GPLv3`]: Https://choosealicense.com/licenses/gpl-3.0/
[`MIT`]: Https://choosealicense.com/licenses/mit/
[`Apache 2.0`]: Https://choosealicense.com/licenses/apache-2.0/
[`LGPLv2.1`]: Https://opensource.org/licenses/lgpl-2.1.php
[`LGPLv3`]: Https://choosealicense.com/licenses/lgpl-3.0/
