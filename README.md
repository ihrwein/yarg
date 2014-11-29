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
     credentials: public_key
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
