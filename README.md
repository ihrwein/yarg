# Yet Another RSync GUI

## Installation

### Linux

You can install the required dependencies with the following commands on Ubuntu 14.04:
```
apt-get install qtdeclarative5-quicklayouts-plugin qtdeclarative5-controls-plugin python3 python3-pyqt5 python3-pyqt5.qtquick python3-setuptools
easy_install3 PyYAML
```

Clone the source code into a directory:
```
git clone https://github.com/ihrwein/yarg.git
```

Then, you can install YARG:
```
python3 setup.py install
```

## Configuration

You have to copy a configuration file into your HOME directory (from the clones git repo):
```
cp tests/yarg.conf ~/.yarg.conf
```
Now, you are ready to use YARG!
