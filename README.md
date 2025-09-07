# vscode-python-opt
Simple examples of running discrete optimization solvers in Python

## Quick start
If needed, [install uv](https://docs.astral.sh/uv/getting-started/installation/). You can then run the examples with `uv run manage.py`.

## Environment Setup

### Dev Container (VS Code, VSCodium)
You can [open this repo in a Visual Studio Code Dev Container](https://code.visualstudio.com/docs/devcontainers/containers?originUrl=%2Fdocs%2Fdevcontainers%2Ftutorial#_quick-start-open-an-existing-folder-in-a-container) with all the required packages automatically installed.
You will need to install Visual Studio Code, and a containerization platform like Docker or Podman (see [Dev Containers tutorial](https://code.visualstudio.com/docs/devcontainers/tutorial)).

Alternatively, you can create a [DevPod Workspace](https://devpod.sh/docs/what-is-devpod) if you want to use other IDEs like [VSCodium](https://vscodium.com/).

### Docker / Docker Compose
You can open this repo in a container with command-line access using Docker Compose (included in [Docker Desktop](https://docs.docker.com/desktop/)) or Podman Compose ([setup from Podman Desktop](https://podman-desktop.io/docs/compose/setting-up-compose)), by running the following command in the repo's root directory:
```
docker compose run --rm devbox
```
Since the repo directory is mounted into the container as a volume, any changes to the files will be reflected immediately.

If you make any changes to the package requirements, you can rebuild the container with
```
docker compose build devbox
```

### Virtual environment (conda)
If needed, install a conda environment manager (recommend a local user installation of either [miniconda](https://www.anaconda.com/docs/getting-started/miniconda/install) or [micromamba](https://mamba.readthedocs.io/en/latest/installation/micromamba-installation.html), but [mamba](https://mamba.readthedocs.io/en/latest/user_guide/mamba.html), [conda](https://docs.conda.io/en/latest/), or the [Anaconda Distribution](https://www.anaconda.com/docs/getting-started/anaconda/install) will also work).

Then, you can build and activate a [conda environment](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file) / [mamba environment](https://mamba.readthedocs.io/en/latest/user_guide/mamba.html#id2) with all the necessary packages by running the following commands in the repo's root directory:
```
# Replace `conda` with `micromamba` or `mamba` as needed.
conda env create -n vscode-python-opt -f environment.yml
conda activate vscode-python-opt
```

### Virtual environment (Python)
If needed, [install and setup a Python environment for your platform](https://docs.python.org/3/using/index.html).

Then, you can build and activate a [Python virtual environment](https://docs.python.org/3/library/venv.html) with all the necessary packages by running the following commands in the repo's root directory:
```
# Windows PowerShell / cmd
# You may need to use `python` instead of `py` if you installed Python via the Microsoft Store app.
py -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt

# Linux / OSX
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Alternatively, if you are using [uv](https://docs.astral.sh/uv/), you can run `uv sync` to update the virtual environment, and/or run the examples with `uv run manage.py`.

## Running the examples
To run the examples, you can use the `manage.py` script.

To run a specific example, specify the name of the solver and the name of the example:
```
python manage.py gurobi simple
```

You can also call `manage.py` with no arguments to get a CLI showing the possible options:
```
# Show available solvers
python manage.py

# Show available examples for the solver Gurobi
python manage.py gurobi
```

## Development

### Updating versions

When updating package versions, remember to update:
 1. pyproject.toml
 2. requirements.txt
 3. environment.yml
 4. uv.lock

When updating Python version, remember to update:
 1. pyproject.toml
 2. environment.yml
 3. .python-version
 4. Dockerfile
 5. devcontainer.json
 6. uv.lock
