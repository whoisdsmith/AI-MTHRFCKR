# Plugin Development Frameworks

A List Of Software Stacks/frameworks Used To Make Audio Plugins, Along With Their Pros And Cons.

- Please Note That You Must Have A Licensing Agreement With Steinberg To *Distribute* Any VST2 And Any Non-GPLv3 VST3 Plugins As Per [`Steinberg's VST3 License`]. If You Don't Already Have A VST2 License, You're Out Of Luck Since Steinberg Doesn't Support It Anymore (Yeah It Stinks). Target VST3 Instead In That Case. Or Better Yet, Target The New [`CLAP`] Standard ;).

## [`Nih-plug`]

  - Full-stack And Modular Framework With GUI In [`Rust`].
  - Fully Open-source Using A Permissive License.
  - Targets CLAP And VST3 Plugin Formats.
  - Targets Linux, Mac, And Windows Platforms.
  - Has Several Different Options For GUI Such As [`Vizia`], [`Iced`], And [`Egui`].
  - Very New And Still Somewhat A Work In Progress, But The Essential Features You Need To Get Started Are There.
  - There Is Now A [`Cookiecutter Template`] To Help Get You Started Faster.

## [`DISTRHO Plugin Framework`]

  - Full-stack Framework With GUI In C++.
  - Fully Open-source Using A Permissive License.
  - Targets LADSPA, DSSI, LV2, VST2, And Jack Plugin Formats.
  - Targets Linux, Mac, And Windows Platforms.

## [`Dplug`]

  - Full-stack Framework With GUI In Te D Programming Language.
  - Fully Open-source Using A Permissive License.
  - The GUI Framework Has Fancy Physically-modeled Rendering Inspired By Game Engines.
  - Targets VST2, VST3, AUv2, AAX, And LV2 Plugin Formats.
  - Targets Linux, Mac, Windows, And Raspberry Pi Platforms.
  - Used By Several Commercial Plugins.

## [`JUCE`]

  - Full-stack Framework With GUI In C++.
  - Open Source, But Some Of Its Modules Require A Hefty Commercial License To Distribute Any Non-GPLv3 Plugins.
  - Targets VST2, VST3, AUv2, AUv3, RTAS, And AAX Plugin Formats. Unofficial Support For The CLAP Standard Is Also In The Works [`Here`](https://github.com/free-audio/clap-juce-extensions).
  - Targets Linux, Mac, Windows, IOS, Android, And Raspberry Pi Platforms.
  - Well Known In The Industry, And Many Commercial Plugins Are Built With It.

## [`Tracktion Engine`]

  - Full-stack Framework In C++ With GUI. It Is Built On Top Of [`JUCE`].
  - Same Licensing As [`JUCE`] Since It's Built On Top Of It.
  - Targeted Formats And Platforms Are The Same As [`JUCE`].
  - Made And Used By The Commercial Company Tracktion.

## [`IPlug2`]

  - Full-stack Framework In C++ With GUI.
  - Fully Open-source Using A Permissive License.
  - Targets VST2, VST3, AUv2, AUv3, AAX And The Web Audio Module (WAM) Plugin Formats (Also Support For CLAP Is In The Works).
  - Targets Mac, Windows, IOS, And Web. It Does Not Target Linux, So I'm Personally Not A Fan Of This One.

[`Steinberg's VST3 License`]: Https://developer.steinberg.help/display/VST/VST+3+Licensing

[`Rust`]: Https://www.rust-lang.org/
[`CLAP`]: Https://github.com/free-audio/clap

[`DISTRHO Plugin Framework`]: Https://github.com/DISTRHO/DPF
[`Dplug`]: Https://github.com/AuburnSounds/Dplug
[`JUCE`]: Https://github.com/juce-framework/JUCE
[`Tracktion Engine`]: Https://github.com/Tracktion/tracktion_engine/
[`IPlug2`]: Https://github.com/iPlug2/iPlug2
[`Nih-plug`]: Https://github.com/robbert-vdh/nih-plug
[`Vizia`]: Https://github.com/vizia/vizia
[`Iced`]: Https://github.com/iced-rs/iced
[`Egui`]: Https://github.com/emilk/egui
[`Cookiecutter Template`]: Https://github.com/robbert-vdh/nih-plug-template
