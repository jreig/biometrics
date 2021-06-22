# Build and run

## Requirements

The project runs inside a docker container that need access to the gpu. In order to work (tested in Ubuntu 20.04) you need to install in your local machine the following requirements:

- **docker v19.03.0+**. You can read an installation guide [here](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04).
- **nvidia-container-runtime**. Follow [this instructions](https://nvidia.github.io/nvidia-container-runtime/) and then run this command:
```
$ sudo apt install nvidia-container-runtime

// Ensure after the installation that nvidia-container-runtime-hook is accessible from $PATH
$ which nvidia-container-runtime-hook
```
- **docker-compose v1.28.0+**. Docker-compose allow for easy container managment. Ensure you install the [latest version](https://github.com/docker/compose/releases/latest) (only v1.28.0+ has gpu support):
```
// Remove previous installation (if any)
$ sudo apt remove docker-compose

// Set up installation destination and version
$ VERSION=1.28.5
$ DESTINATION=/usr/local/bin/docker-compose

// Download and set up permisions
$ sudo curl -L https://github.com/docker/compose/releases/download/${VERSION}/docker-compose-$(uname -s)-$(uname -m) -o $DESTINATION
$ sudo chmod 755 $DESTINATION

// Check installation
$ docker-compose --version
```
## Work with notebooks

The project is configured to mount `dataset/` and `notebooks/` directories so you can work while the container is running. To work with jupyter notebooks just run the following commands:
```
$ docker-compose build
$ docker-compose up
```

You can visualize and run the notebooks on http://localhost:8888 with the access token.

### Work on VSCode

You can edit and run the notebooks on VSCode on the host by installing the Python extension and adding the container jupyter server as a remote server.

## Run scripts

If you want to execute a script inside the container just run:
```
$ docker-compose run notebookserver python scripts/script.py
$ docker-compose run notebookserver sh scripts/script.sh
```

If you want to execute the script inside a container multiple times or want to edit it
without stoping the container execute:
```
$ docker-compose run notebookserver bash

// [Inside container]
# python scripts/script.py
# ./scripts/scripts.sh
```

## Tensorboard

To use tensorboar inside the container you must launch it in a way that accepts outside connections:
```
# Load the TensorBoard notebook extension
%load_ext tensorboard

# Run tensorboard
%tensorboard --logdir logs --host 0.0.0.0

# List open TensorBoard instances
from tensorboard import notebook
notebook.list()
```

Then you can access to http://localhost:6006 to see tensorwboard