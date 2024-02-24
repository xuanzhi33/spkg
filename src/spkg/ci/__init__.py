from os import path

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

class CI:
    def is_exist(self):
        return path.exists(".github/workflows/publish.yml")

    def create(self, name, in_project):
        ci_path = path.join(".github", "workflows", "publish.yml")
        if not in_project:
            ci_path = path.join(name, ci_path)

        with open(ci_path, "w", encoding="utf-8") as f:
            f.write(WORKFLOW.format(name=name))

