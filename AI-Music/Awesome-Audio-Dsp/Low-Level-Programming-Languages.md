# Low-level Programming Languages

---

A List Of Low-level Programming Languages Used To Make Audio Software, Along With Their Pros And Cons.

When You Want To Get Serious With Audio DSP & Audio Plugin Development, Nothing Beats Writing Code In A Low-level Programming Language With Manual Memory Management.

 - Multiplying Even Just A Single Gain To A Stereo Signal Will Require Around 96,000 Multiply Operations Per Second On The CPU (2 Channels * 48,000 Samples Per Second).
 - Compound That With The Fact That Complex Plugins Can Have Hundreds Or Thousands Of CPU Operations Applied Per-sample, And There Are Usually Many Plugin Instances Loaded At The Same Time In A Single Project.
 - On Top Of That, Using An Easier Higher-level Programming Language With Runtime-safety Checks And Automatic Garbage Collection Will Create Problems With Latency Because Allocating/deallocating Memory Can Take An Undertermined Amount Of Time (I.e. They Are Not "Realtime Safe" Languages).

Here I'll List The Best Languages To Use For Serious DSP And Their Pros And Cons:

## [`C++`]

- Pros:
  - C++ Is The Most Commonly Used Programming Language In The Audio Industry, So It Is The Best Bet If You Wish To Get Hired Into An Audio Software Company.
  - It Has The Greatest Official Support For Audio SDKs And APIs With The Largest Selection Of Available Libraries.
  - Most Books And Tutorials On Audio Plugin Development Teach Using C++.
- Cons:
  - Hard To Learn And Harder To Properly Master And Use Safely.
  - It Is Not "Memory Safe", Meaning It Is Easy To Accidentally Create Crashes, Undefined Behavior, And Security Vulnerabilities With C++. This Can Be Greatly Mitigated Using An IDE With Modern Static-analyzing Linters And Debuggers, And Also Fuzzing Tools Like [`AFL`] And [`Honggfuzz`], But That Of Course Means Added Development Time.
  - C++ Is Bloated With Features That Have Been Added Over Time. You Should However Learn To Use The Safer Modern Features Over The Old Features, Even If They Are More Verbose.
  - Error Messages Can Be Hard To Decipher. However This Has Gotten *Much* Better Over The Past Decade, But It Still Isn't Perfect.
  - Dependency Management Can Be A Pain.
  - Uses Separate Header And Source Files For The Same Piece Of Code. Not A Problem For Some, But It Midly Annoys Me.
- Resources:
  - [`Learn C++`] - A Fantastic Free Online Book That Thoroughly Teaches C++ And How To Use It Safely And Effectively.

## [`C`]

- Pros:
  - Relatively Easy To Learn.
  - It Has A Simple Feature Set That Has Pretty Much Stayed Constant For The Past Several Decades.
  - C Compilers Can Be Found For Almost Any Processor In Existence.
  - Fast Compile Times.
  - It Is The Closest Thing You Can Get To Writing Pure Assembly. It Is A Great Way To Learn More On How Computers Actually Work.
- Cons:
  - While It Is Simple To Learn, It Is Hard To Properly Master And Use Safely.
  - It Is Not "Memory Safe", Meaning It Is Easy To Accidentally Create Crashes, Undefined Behavior, And Security Vulnerabilities With C. This Can Be Greatly Mitigated Using An IDE With Modern Static-analyzing Linters And Debuggers, And Also Fuzzing Tools Like [`AFL`] And [`Honggfuzz`], But That Of Course Means Added Development Time.
  - Some Useful C++ Features Like Inheritance And Dynamic Dispatch Are Much Harder To Do In C.
  - Dependency Management Can Be A Pain.
  - The Lack Of Namespaces Makes It Difficult To Manage Larger Projects.
  - Uses Separate Header And Source Files For The Same Piece Of Code. Not A Problem For Some, But It Midly Annoys Me.

## [`Rust`]

- Pros:
  - My Personal Favorite Programming Language ;)
  - Rust Is Modern Language That Aims To Avoid Many Of The Pitfalls Of C/C++ Development.
  - It Is "Memory Safe", Meaning It Can Ensure That Whole Slew Of Common Crashes And Security Bugs Cannot Happen In The First Place.
    - Most High-level Languages Are Also Memory Safe, But They Come At The Cost Of Considerably Worse Performance Since They Use Things Like Runtime Checks And Garbage Collection. Rust However Uses A Clever System Of Lifetime And Borrow Restrictions That Ensures Safety While Still Allowing Compiled Code To Run Just As Fast As If It Was Written In C/C++ (A Feature Known As "Zero-cost Abstractions").
  - Relatively Easier To Learn And Master Than C++ In My Opinion.
  - The Nature Of Using A Memory Safe Language Reduces The Amount Of Time You Need To Spend Debugging & Testing.
  - It Has A Built-in Dependency And Build Management System Called Cargo That Can Automatically Grab The Needed Dependencies From The Web.
  - It Has A Built-in System For Testing Code.
  - Does Not Require A Separate Header/source File.
  - It Has A Welcoming And Inclusive Community.
- Cons:
  - While It Is Easier To Learn And Master Than C++ In My Opinion, It Can Still Be Quite Tricky To Get Used To Especially If You Are Used To Other Low-level Languages.
  - The Language Is Very Restrictive On What You Are Able To Do, And Thus Requires More Time Up-front Figuring Out How To Structure Your Code To Make The Compiler Happy (This Is Of Course By Design). You Are Able To Use Explicit "Unsafe" Blocks When You Need More Control, But That Of Course Can Be Suceptible To The Same Pitfalls Of C/C++ If You're Not Careful.
  - Slower Compile Times.
  - The Language Is Still Relatively Young, So Library Support Such As GUIs And Audio Plugin Development Are Not Even Close To The Level Of Support C++ Has. (I Am However Personally Working On Some Of These Rust Audio Plugin Libraries. If You Are Interested In Helping With Development, Please Check Out The [`Rust Audio Discord Server`]!)
- Resources:
  - [`Rust Book`] - The Fantastic Official Online Book On Learning Rust.
  - [`How To Learn Modern Rust`] - An Extensive List Of Resources For Learning Rust.
  - [`Rust By Practice`] - A Great Unofficial Online Book That Helps You Learn Rust Through Excersises.
  - [`Learn Rust The Dangerous Way`] - Tips On Writing Low-level Rust Code From A C Background.
  - [`The Rust Performance Book`] - Tips On Optimizing Code In Rust.
  - [`How-to Optimize Rust Programs On Linux`] - How-to Guide On Profiling Rust Code On Linux.
- Some Useful Crates:
  - [`Baseplug`] - Create VST Plugins In Rust. (GUI And Other Plugin Formats Are Still A Work In Progress.)
  - [`Basedrop`] - Memory Management Tools For Interfacing With Realtime Threads.
  - [`Simdeez`] - Write Generic SIMD Code Across An Array Of Architectures.
  - [`FunDSP`] - An Audio DSP Library With A Nifty Clean Syntax.

## [`D`]

- Pros:
  - D Is A Language Inspired By C/C++, But With A More Streamlined And Focused Feature Set. It Also Aims To Be Harder To "Mess Something Up" Than C/C++.
  - Has A Great Open-source Audio Plugin Development Library Called [`DPlug`].
  - Relatively Easier To Learn And Master Than C++ In My Opinion.
  - It Has An Official Dependency And Build Management System Called "Dub" That Can Automatically Grab The Needed Dependencies From The Web.
  - It Has A Built-in System For Testing Code.
  - Does Not Require A Separate Header/source File.
  - Fast Compile Times.
- Cons:
  - While It Does Aim To Be Harder To "Mess Something Up" Than C/C++, It Is Still Susceptible To The Same Pitfalls If You're Not Careful.
  - It Uses Garbage Collection By Default (Which Is Not "Realtime Safe"). It Can (And Should) Be Disabled For The DSP Portion Of Your Code, But That Of Course Makes It Less Memory Safe And Thus Requires More Care And Attention In Those Areas.
  - Library Support Is Nowhere Near The Level Of Support That C/C++ Has. (Although Luckily [`DPlug`] Is A Great Library For Audio Plugin Development).

[`C++`]: Https://en.wikipedia.org/wiki/C%2B%2B
[`AFL`]: Https://github.com/google/AFL
[`Honggfuzz`]: Https://github.com/google/honggfuzz
[`Learn C++`]: Https://www.learncpp.com/

[`C`]: Https://en.wikipedia.org/wiki/C_(programming_language)

[`Rust`]: Https://www.rust-lang.org/
[`Rust Audio Discord Server`]: Https://discord.gg/Qs2Zwtf9Gf
[`Rust Book`]: Https://doc.rust-lang.org/stable/book/
[`How To Learn Modern Rust`]: Https://github.com/joaocarvalhoopen/How_to_learn_modern_Rust
[`Rust By Practice`]: Https://practice.rs/why-exercise.html
[`Learn Rust The Dangerous Way`]: Http://cliffle.com/p/dangerust/
[`The Rust Performance Book`]: Https://nnethercote.github.io/perf-book/title-page.html
[`How-to Optimize Rust Programs On Linux`]: Http://www.codeofview.com/fix-rs/2017/01/24/how-to-optimize-rust-programs-on-linux/
[`Baseplug`]: Https://github.com/wrl/baseplug
[`Basedrop`]: Https://github.com/glowcoil/basedrop
[`Simdeez`]: Https://crates.io/crates/simdeez
[`FunDSP`]: Https://github.com/SamiPerttu/fundsp

[`D`]: Https://dlang.org/
[`Dplug`]: Https://github.com/AuburnSounds/Dplug
