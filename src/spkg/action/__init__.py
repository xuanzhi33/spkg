from spkg.hatch import Hatch_cli
from spkg.ci import CI
from spkg.log import Log
from click import style
from subprocess import run

class Action:
    def __init__(self, log: Log, hatch: Hatch_cli, ci: CI):
        self.log = log
        self.ci = ci
        self.hatch = hatch

    def version(self, option):
        if self.ci.is_exist():
            self.log.info("CI detected, only modifying the version number.")
            self.hatch.version(option)
        else:
            self.log.info(f"Releasing {option} update and publishing to pypi.")
            self.hatch.version(option)
            self.build()
            self.release()

    def build(self, clean=True):
        if clean:
            self.hatch.clean()
            self.log.done("Cleaned dist folder.")
        self.hatch.build()
        self.log.done("Built package.")

    def release(self):
        self.hatch.publish()
        self.log.done("Published to pypi.")

    def simple_config(self):
        self.log.info("Using simple config.")
        self.hatch.simple_config()
        self.log.done("Configured successfully: no tests, GPL-3.0 license.")
    def restore_config(self):
        self.log.info("Restoring to default config.")
        self.hatch.config_restore()
    def need_option(self, cmd):
        self.log.error(f"Please specify a valid option for {cmd}.")
        self.log.info(f'Use {style(f"spkg {cmd} --help", fg="green")} for more information.')
    def new(self, name, is_cli, create_ci, open_vscode):
        if is_cli:
            self.log.info(f"Creating a new package {name} with Command Line Interface.")
            self.hatch.new_cli(name)
        else:
            self.log.info(f"Creating a new package {name}.")
            self.hatch.new(name)

        if create_ci:
            self.log.info("Creating Publish Workflow for GitHub Actions.")
            self.ci.create(name, in_project=False)

        self.log.done(f"Created package {name} successfully.")
        
        if open_vscode:
            self.log.info("Opening in Visual Studio Code.")
            run(["code", "."])
