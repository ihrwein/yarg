# Yet Another RSync GUI

Maybe YARG is not the best Rsync GUI out there,
maybe it has flaws, bugs or it's not easy to use. BUT!
It demonstrates some technologies which may come in handy
in some cases. These are:
 * PyQT5,
 * `distutils` installation with resource files.

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
Now, you are ready to use YARG:
```
$ yarg
```
## Useful stuffs
### distutils with resource files

I struggled with our `setup.py` until I found a way to
accomplish my goal: I wanted to use resource files (`*.qml`)
in this project and reference them with their relative path to
the project's root directory in my runner script.

You can check the layout of this project:
 * all python files are under `yarg/` package
 * all QML files are under `yarg/resource/`
 * a main program is a script called `runner.py` (in the repo's root dir), which references a QML with path: `yarg/resource/main.qml`

The problem is, that when I install this little program, the runner script ends up
in a `bin` directory somewhere on my computer. It will import the `yarg` package,
but it won't find the `*.qml` files. I worked around this with the following solution:
 * in `setup.py`, I use `data_files` to tell distutils, what are my resource files:
 ```
 ...
 data_files=[('resource', ['yarg/resource/main.qml'])],
 ...
 ```
 * in my runner script, I use the `pkg_resources` module, to access to the resource files
  bundled in a single EGG file, which is a simple compressed file with a specific directory and file
  layout and some meta files. When you use `pkg_resouces`, it will decompress your resources in a temporary
  directory and tells you the location of this place:
  ```
  import pkg_resources
  ...
  # This will decompress the whole yarg/resource directory into a temp. dir. and returns
  # the path of that dir.
  # I need this, because my root QML file (main.qml) imports the others next to it.
  pkg_resources.resource_filename('yarg', 'resource')
  ...
  # This function returns the path of the yarg/resource/main.qml files.
  pkg_resources.resource_filename('yarg.resource', 'main.qml')
  ```
And now, I'm able to use the same code in development and after installation. `pkg_resources` will
find the most appropriate locations.
