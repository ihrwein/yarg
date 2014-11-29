import subprocess
from subprocess import Popen

from yarg.rsync import CLIOptions


class RSyncClient:
    def __init__(self, profile):
        self.profile = profile
        cli = CLIOptions(profile)
        self._command = cli.get_command_and_options()

    def start_sync(self):
        joined = ' '.join(self._command)
        print('RSync CLI options:', joined)
        #popen = Popen(self._command, stderr=subprocess.STDOUT)
        popen = Popen(['rsync.bat'], stderr=subprocess.STDOUT)
        return popen

    def _abort_sync(self):
        pass