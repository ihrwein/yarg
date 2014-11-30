# Yet Another RSync GUI

## Installation

### Linux

You have to install the following dependencies on Ubuntu 14.04:
```
python3-pyqt5.qtquick
python3-pyqt5
libglu1-mesa-dev
```

Then, you can install YARG:
```
python3 setup.py install --user
```

## Configuration

A simple config file:

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
     ssh_remote: destination
     ssh:
       port: 10022
       identity_file: ~/.ssh/id_rsa
       host: jimmy.sch.bme.hu
```
