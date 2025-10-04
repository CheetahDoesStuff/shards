# Shards
*A nice small collection of handy tools*

**Changelog:** [changelog.md](https://github.com/CheetahDoesStuff/shards/blob/release/changelog.md)

**Note:** This is a temporary README, documentation will be availble soon after the first PyPi release

### What is this?
Shards is a small library made for a single reason, in smaller projects you
maybe dont need an big library like numpy, but a single func from it, something simple like an multidimensional array etc. This is made to 
give some simple features to you, that you probably reimplement yourself
every time.

### What is a shard?
A shard is a feature, class or sublibrary containing one or more functions/classes for a single usecase, for example multidimensional arrays is a shard.

### Features
*An up to date list of all shards*
* Logger Shard (`from shards import sLogger`) - Docs coming soon

    A simple logging shard with coloured output and file saving based on timestamps

* (Planned) YaCfg Shard (`from shards import yacfg`) - Docs coming soon

    YaCfg is a simple shard for converting config files (YAML / TOML) into python objects. Has support for Logging trough the logger shard

* MDL Shard (`from shards.math import mdl`) - Docs coming soon

    MDL (standing for MultiDimensional Lists) is a small shard containing classes for creating multidimensional lists and using them (similar to other lower level languages)