# Yet Another RSync GUI

## Installation

### Linux

You can install the dependencies with the following command on Ubuntu 14.04:
```
apt-get install qtdeclarative5-quicklayouts-plugin qtdeclarative5-controls-plugin python3 python3-pyqt5 python3-pyqt5.qtquick python3-setuptools
easy_install3 PyYAML
```

Then, you can install YARG:
```
python3 setup.py install --user
```

## Configuration

A sample config file:

```yaml
default_rsync_options:
  verbose: false
  info: FLAGS
  debug: FLAGS
  msgs2stderr: false

profiles:
   - name: local
     source:
       path:
       - /tmp/source/
     destination:
       path:
       - /tmp/target/
     last_sync: 1417030174.658952
     rsync_options:
       partial: true
       force: true
       chmod: "600"
   - name: Backup server 1
     source:
       path:
       - /tmp/source/
     destination:
       path:
       - /tmp/target/
       remote: true
     last_sync: 1417030174.658952
     rsync_options:
       partial: true
       force: true
       chmod: "600"
       rsh: ssh
     ssh:
       port: 10022
       identity_file: ~/.ssh/id_rsa
       host: jimmy.sch.bme.hu
```
