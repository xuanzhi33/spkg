from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="spkg",
    version="0.4.0",
    author="xuanzhi33",
    author_email="xuanzhi33@qq.com",
    url="https://github.com/xuanzhi33/spkg",
    description="Simple Packager - A command line tools for setuping and uploading python packages",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    license="GPL-3.0",
    install_requires=["twine"],
    packages=find_packages(),
    python_requires=">=3.6",
    entry_points = {
        "console_scripts": [
            "spkg = spkg.__main__:main"
        ]
    }
)
