import sys
import subprocess
import json
from click import style

PYTHON_PATH = sys.executable

class Hatch_cli:
    def hatch(self, args):
        cmd_list = [PYTHON_PATH, "-m", "hatch"] + args
        subprocess.run(cmd_list)

    def config(self, key, value):
        self.hatch(["config", "set", key, value])
    def config_restore(self):
        self.hatch(["config", "restore"])
    def simple_config(self):
        self.config_restore()
        self.config("template.licenses.default", "['GPL-3.0-only']")
        self.config("template.plugins.default.tests", "false")
    def clean(self):
        self.hatch(["clean"])
    def build(self):
        self.hatch(["build"])
    def publish(self):
        self.hatch(["publish"])
    def release(self):
        self.hatch(["release"])
    def version(self, version):
        self.hatch(["version", version])
    def new(self, name):
        self.hatch(["new", name])
    def new_cli(self, name):
        self.hatch(["new", "--cli", name])
    def info(self):
        result = subprocess.run([PYTHON_PATH, "-m", "hatch", "project", "metadata"], capture_output=True, text=True)
        info_dict = json.loads(result.stdout)
        deps = info_dict['dependencies']
        output = f"""{info_dict['name']}
Description:
{info_dict['description']}
Version: {style(info_dict['version'], fg='green')}
License: {style(info_dict['license'], fg='blue')}
Dependencies: """
        for dep in deps:
            output += f"{style(dep, fg='magenta')} "
        return output
