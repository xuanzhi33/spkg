# SPKG

Language: [English](https://github.com/xuanzhi33/spkg/blob/master/README.md) |
[中文文档](https://github.com/xuanzhi33/spkg/blob/master/README_cn.md)


## Introduction

SPKG (Simple Packager) - A command line tools for setting up and uploading python packages.

一个简单的命令行工具，用于快速的打包和上传python包到pypi。

## Install

```
pip3 install spkg
```

## Usage

Make sure you are in **the directory of your package** and run the following command:

```
spkg [command]
```

### Commands

- `help`, `-h`: show this help message and exit (default)
- `upload`, `-u`: upload the package to pypi (equals to 'twine upload dist/*')
- `setup`, `-s`: setup the package (equals to 'python3 setup.py sdist')
- `clear`, `-c`: delete all .tar.gz files in 'dist' folder
- `pkg`, `-p`: clear, setup, and upload the package
- `info`, `-in`: show package info
- `setver`, `-sv`: set package version
- `install`, `-i`: install a package from pypi using 'pip3 install --upgrade [package]'

The commands below can change package version quickly and then run 'pkg' command:
(They will modify the version in 'setup.py')
- `patch`, `-pa`: Release patch update (e.g. 1.0.1 -> 1.0.2)
- `minor`, `-mi` : Release minor update (e.g. 1.0.3 -> 1.1.0)
- `major`, `-ma`: Release major update (e.g. 1.1.1 -> 2.0.0)

### Examples

- To upload all files in 'dist' folder to pypi:

```
spkg upload
```

- To setup and upload the package:

```
spkg pkg
```

- If your package's version is 1.4.2, you can run the following command to change the `version` in 'setup.py' to 1.4.3 and upload the package to pypi:

```
spkg patch
```

- To install or update a package from pypi:

```
spkg install [package]
```
