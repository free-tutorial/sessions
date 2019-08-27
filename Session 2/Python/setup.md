# Python Setup

## Anaconda
Anaconda is a free and open-source distribution of the Python and R programming languages for scientific computing, that aims to simplify package management and deployment. Package versions are managed by the package management system conda.

### Installation
```bash
$ cd /tmp
$ curl -O https://repo.anaconda.com/archive/Anaconda3-2019.03-Linux-x86_64.sh
```

```bash
$ sha256sum Anaconda3-2019.03-Linux-x86_64.sh
45c851b7497cc14d5ca060064394569f724b67d9b5f98a926ed49b834a6bb73a  Anaconda3-2019.03-Linux-x86_64.sh

$ bash Anaconda3-2019.03-Linux-x86_64.sh
$ source ~/.bashrc
```


### Commands

|Command|Description|
|--|--|
|`conda list`|list of available packages|
|`conda create --name my_env python=3.6`|create a new environment named `my_env` with python 3.6|
|`conda create -n myenv python=3.4 scipy=0.15.0 astroid babel`|create an environment with a specific version of Python and multiple packages|
|`conda activate my_env`|activate an environment|
|`conda env create -f environment.yml`|Creating an environment from an `environment.yml` file|
|`conda env remove --name myenv`|remove environment|
|`conda info --envs`|list environments|

### Creating an Environment File Manually

```yml
name: stats
dependencies:
  - python=3.6
  - bokeh=0.9.2
  - numpy=1.9.*
  - nodejs=0.10.*
  - flask
```

### Cloning an Environment
You can make an exact copy of an environment by creating a clone of it.

```bash
conda create --name myclone --clone myenv
```

### Building Identical Conda Environments
You can use explicit specification files to build an identical conda environment on the same operating system platform, either on the same machine or on a different machine.

```bash
$ conda list --explicit > spec-file.txt
$ conda create --name myenv --file spec-file.txt
```

You can use spec-file to install its listed packages into an existing environment:
```bash
$ conda install --name myenv --file spec-file.txt
```