# Developement

Everyone is welcome to contribute, but to keep the repo organized we have to follow the documentation!

## Installing dependencies

No, the python packages does not have to be installed manually, here we instead install the tools we need for the development process.

The tools you need are:
* Git, to install, check out their [downloads page](https://git-scm.com/downloads)
* Uv, to install, check out their [installation guide](https://docs.astral.sh/uv/getting-started/installation/)

**Note:** these tools are NOT optional and are required for contributing to the repo!

## Dowloading the repo

Now that we have the tools we need, we need to get the actual repository, do this by running (run in the directory where you want to get the repo folder in):

```sh
git clone https://github.com/CheetahDoesStuff/shards
cd shards
```

This will download the repo, into a new directory, the seconds command moves our shell into that new repo. Now you have aqquired the repo!

## Setting up the enviorment

To ensure a developement process with full cross platform compatability we use the popular tool **uv** to manage the python enviorment and packages, to set up your enviorment simply run:

```sh
uv sync
```

If you cloned the repository correctly, 