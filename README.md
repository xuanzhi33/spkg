# SPKG by xuanzhi33
    
## name: SPAG = Simple Packager

## Usage

spkg [COMMAND]

Options:

-        help, -h: show this help message and exit (default)
-        upload, -u: upload the package to pypi (equals to 'twine upload dist/*')
-        setup, -s: setup the package (equals to 'python3 setup.py sdist')
-        clear, -c: delete all .tar.gz files in 'dist' folder
-        pkg, -p: clear, setup, and upload the package
-        info, -i: show package info
-        pkgver, -pv: show package version
-        setver, -sv: set package version

-        The commands below can change package version quickly and then run 'pkg' command:
-        (They will modify the version in 'setup.py')
-        patch, -pa: Release patch update (e.g. 1.0.1 -> 1.0.2)
-        minor, -mi : Release minor update (e.g. 1.0.3 -> 1.1.0)
-        major, -ma: Release major update (e.g. 1.1.1 -> 2.0.0)