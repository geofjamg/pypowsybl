# PyPowSyBl

[![MPL-2.0 License](https://img.shields.io/badge/license-MPL_2.0-blue.svg)](https://www.mozilla.org/en-US/MPL/2.0/)
[![Join the community on Spectrum](https://withspectrum.github.io/badge/badge.svg)](https://spectrum.chat/powsybl)

The PyPowSyBl project gives access to PowSyBl Java framework to Python developers. This Python integration relies on [JPype](https://github.com/jpype-project/jpype). This is not a **native** implementation of PowSyBl features: internally a JVM is started to run the java code, and the Python code access to the Java objects through JNI. 

## Table of contents
- [Requirements](#requirements)
    - [Ubuntu](#ubuntu-2004)
    - [CentOS](#centos)
- [Install](#install)
    - [Install from the binaries](#install-from-the-binaries)
    - [Install from the sources](#install-from-the-sources)
- [Demo](#demo)
- [Contributing](#contributing)

## Requirements
This project contains both Java and Python source files. To build the project, you need to install:
- Java Development Kit (1.8 or later)
- [Maven](https://maven.apache.org/)
- [python3](https://www.python.org)
- [python3-jpype](https://pypi.org/project/JPype1/)
- [python3-pip](https://pypi.org/project/pip/)
- [python3-wheel](https://pypi.org/project/wheel/)

### Ubuntu
```
$> sudo apt install python3 python3-jpype python3-pip python3-wheel
```

### CentOS
```
$> sudo yum install python3 python3-jpype python3-pip python3-wheel
```

## Install
To install PyPowSyBl, you can either use the binary package or build the project from the sources.

### Install from the binaries
Download the latest version of the PyPowSyBl and install the package with `pip`:
```
$> pip3 install pypowsybl-1.0.0-py3-none-any.whl
```

This command requires privileges but you can also install the package for the current user only:
```
$> pip3 install --user pypowsybl-1.0.0-py3-none-any.whl
```
This will require to update your `PYTHONPATH` environment variable to make the package accessible in your scripts:
```
export PYTHONPATH=$PYTHONPATH:$HOME/.local/lib/python3.8/site-packages
```

### Install from the sources
To build and install PyPowSyBl from the sources, you need to clone this repository using `git`.
```
$> git clone https://github.com/powsybl/pypowsybl
```

All the build is managed by Maven. It will compile the Java classes and package them in `powsybl-pypowsybl-<VERSION>.jar` file, download all the Java dependencies declared in the `pom.xml` file and create an python wheel package.
```
$> mvn package
```

Once it's done, you simply have to install the package:
```
$> pip3 install target/dist/pypowsybl-1.0.0-py3-none-any.whl
```

*Note:* in case of any change from the binaries or from the sources (either from Java code or from Python code), you have to reinstall the package either by uninstalling and reinstalling the package or by passing the `-I` option to `pip3`:
```
$> pip3 install target/dist/pypowsybl-1.0.0-py3-none-any.whl
```

### Demo
A small demo is provided in the `demo` folder. It shows how to load a case-file, run a load-flow and export the updated network to another case file to the temporary directory.
```
$> python3 demo.py
```

## Contributing
If you are interested in the PyPowSyBl project, feel free to contribute. All the information you need are available on our [website](https://www.powsybl.org/pages/contributing/).
