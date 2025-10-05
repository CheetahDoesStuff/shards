# Welcome!

Everyone is welcome to contribute, but to keep the repo organized we have to follow the documentation!

# Things to note

## Everything through uv

All commands related to the python enviorment or developement must be ran through uv using the `uv run` command, eg `uv run myfile.py`, `uv run pytest` or `uv run pip install -e .`

# Getting started

## Installing dependencies

No, the python packages does not have to be installed manually, here we instead install the tools we need for the development process.

The tools you need are:
* Python (of course), to install, check out their [downloads page](https://www.python.org/downloads/)
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
uv venv install
```

If you cloned the repository correctly, this will use the uv.lock and pyproject.toml files to create the python enviorment and install the dependencies! Then, well need to set up pre-commit for formatting and linting, dont worry, its easy! Ruff already installed it for us, now we just have to run:

```sh
uv run pre-commit install
uv run pre-commit run --all-files
```

The first command installs the pre-commit hooks, the seconds command then runs pre-commit once manually to ensure everything is formatted! Now youre all set and pre-commit will run every time you create a new git commit!
