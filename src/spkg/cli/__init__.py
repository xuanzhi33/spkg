# SPDX-FileCopyrightText: 2024-present xuanzhi33 <xuanzhi33@qq.com>
#
# SPDX-License-Identifier: GPL-3.0-only

import click

from spkg.__about__ import __version__
from spkg.hatch import Hatch_cli
from spkg.ci import CI
from spkg.log import Log
from spkg.action import Action

log = Log()
hatch = Hatch_cli()
ci = CI()
action = Action(log=log, hatch=hatch, ci=ci)


EPILOG = f"{click.style(' SPKG ', bg='blue')} by xuanzhi33 {click.style('v' + __version__, fg='green')}"


@click.group(context_settings={"help_option_names": ["-h", "--help"]},
             epilog=EPILOG)
@click.version_option(version=__version__, prog_name="spkg")
def spkg():
    """
    SPKG (Simple Packager) - A command line tools for building and uploading python packages.
    """
    pass

@spkg.command()
@click.option("-s", "--simple", is_flag=True, help="Using simple config: no tests, GPL-3.0 license.")
@click.option("-r", "--restore", is_flag=True, help="Restore to default config.")
def config(simple, restore):
    """
    Configure spkg.
    """
    if simple:
        action.simple_config()
    elif restore:
        action.restore_config()
    else:
        action.need_option("config")

@spkg.command()
def patch():
    """
    Release patch update (1.0.1 -> 1.0.2) and publish to pypi.

    If GitHub Actions (publish.yml) is enabled, it will only modify the version number.
    """
    action.version("patch")

@spkg.command()
def minor():
    """
    Release minor update (1.0.1 -> 1.1.0) and publish to pypi.

    If GitHub Actions (publish.yml) is enabled, it will only modify the version number.
    """
    action.version("minor")

@spkg.command()
def major():
    """
    Release major update (1.0.1 -> 2.0.0) and publish to pypi.

    If GitHub Actions (publish.yml) is enabled, it will only modify the version number.
    """
    action.version("major")

@spkg.command()
@click.option("--clean/--no-clean", " /-c", default=True, help="Clean dist folder before building.")
def build(clean):
    """
    Build package.
    """
    action.build(clean)

@spkg.command()
def publish():
    """
    Publish to pypi.
    """
    action.release()

@spkg.command()
@click.argument("name")
@click.option("--cli/--no-cli", "-c", default=False, help="Create package with Command Line Interface.")
@click.option("--ci/--no-ci", "-i", default=False, help="Create Publish Workflow for GitHub Actions.")
@click.option("--open/--no-open", "-o", default=False, help="Open in Visual Studio Code when finished.")
def new(name, cli, ci, open):
    """
    Create a new package.
    """

    action.new(name, is_cli=cli, create_ci=ci, open_vscode=open)

@spkg.command()
def info():
    """
    Show package information.
    """
    log.info(hatch.info())


if __name__ == "__main__":
    spkg()