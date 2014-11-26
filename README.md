# Yet Another RSync GUI

## Installation

### Linux

```
python3 setup.py install --user
```

## Configuration

A simple config file:

```yaml
credentials:
  - name: username
    type: username_password
    username: test
    password: secret

profiles:
   - name: local
     source:
       path: /tmp/source/
     destination:
       path: /tmp/target/
     last_sync: '2014-11-17 12:12:56.000'
     rsync_options:
       partial: true
       force: true
       chmod: "600"
       rsh: ssh
   - name: Backup server 1
     source:
       path: /tmp/source/
     destination:
       path: /tmp/target/
       host: backup.example.org
       port: 10022
       credential: username
     last_sync: '2014-11-17 12:12:56.000'
     rsync_options:
       partial: true
       force: true
       chmod: "600"
       rsh: ssh
```
