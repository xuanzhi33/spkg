from os import path, makedirs

WORKFLOW = """\
name: publish

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:
  build-and-publish:
    runs-on: ubuntu-latest
    environment:
      name: pypi
      url: https://pypi.org/p/{name}
    permissions:
      id-token: write
    steps:
    - uses: actions/checkout@v4
    - name: Set up Python 
      uses: actions/setup-python@v5
      with:
        python-version: '3.8'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade hatch
    - name: Build package
      run: |
        hatch build

    - name: Publish package distributions to PyPI
      uses: pypa/gh-action-pypi-publish@release/v1
"""

CI_DIR = path.join(".github", "workflows")
CI_NAME = "publish.yml"

class CI:
    def is_exist(self):
        return path.exists(path.join(CI_DIR, CI_NAME))
    def create(self, name, in_project):
        cur_ci_dir = CI_DIR
        if not in_project:
            cur_ci_dir = path.join(name, cur_ci_dir)
        makedirs(cur_ci_dir, exist_ok=True)
        ci_file = path.join(cur_ci_dir, CI_NAME)

        with open(ci_file, "w", encoding="utf-8") as f:
            f.write(WORKFLOW.format(name=name))

