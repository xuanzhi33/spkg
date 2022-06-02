import os
import sys
def help():
    print("""
    SPKG by xuanzhi33
    Usage: spkg [COMMAND]
    
    Options:
        help, -h: show this help message and exit (default)
        upload, -u: upload the package to pypi (equals to 'twine upload dist/*')
        setup, -s: setup the package (equals to 'python3 setup.py sdist')
        clear, -c: delete all .tar.gz files in 'dist' folder
        pkg, -p: clear, setup, and upload the package
        info, -i: show package info
        pkgver, -pv: show package version
        setver, -sv: set package version

        The commands below can change package version quickly and then run 'pkg' command:
        (They will modify the version in 'setup.py')
        patch, -pa: Release patch update (e.g. 1.0.1 -> 1.0.2)
        minor, -mi : Release minor update (e.g. 1.0.3 -> 1.1.0)
        major, -ma: Release major update (e.g. 1.1.1 -> 2.0.0)

    """)

def upload():
    print("\033[1;34mUploading package to pypi...\033[0m")
    print("\033[1;30mRunning 'twine upload dist/*'...\033[0m")

    os.system("twine upload dist/*")

    print("\033[1;32mDone.\033[0m")

def setup():
    print("Setting up package")
    print("Running 'python3 setup.py sdist'...")
    os.system("python3 setup.py sdist")
    print("Done.")
    
def clear():
    print("Deleting all .tar.gz files in 'dist' folder...")
    if os.path.exists("dist"):
        files = os.listdir("dist")
        for file in files:
            if file.endswith(".tar.gz"):
                os.remove("dist/" + file)
                print("Removed:", file)
    else:
        print("No dist folder found.")

def getAttrs(attrlist):
    valList = []
    with open("setup.py", "r") as f:
        lines = f.readlines()
        for attr in attrlist:
            flag = False
            for i in range(len(lines)):
                if attr in lines[i] and "=" in lines[i] and "\"" in lines[i]:
                    valstr = lines[i].split("=")[1].strip()
                    val = valstr.split("\"")[1]
                    valList.append(val)
                    flag = True
                    break
            if not flag:
                valList.append("")

    return valList

def setAttr(attr, new):
    flag = False
    with open("setup.py", "r") as f:
        lines = f.readlines()
        for i in range(len(lines)):
            if attr in lines[i] and "=" in lines[i] and "\"" in lines[i]:
                lines[i] = "    " + attr + "=\"" + new + "\",\n"
                flag = True
                break
    if flag:
        with open("setup.py", "w") as f:
            f.writelines(lines)
        return True
    else:
        return False

def setver(ver):
    info = getAttrs(["name", "version"])
    if info[0] == "":
        print("Package name not found in setup.py")
    elif info[1] == "":
        print("Package version not found in setup.py")
    else:
        if setAttr("version", ver):
            print("Verson of package '" + info[0] + "' changed from '" + info[1] + "' to '" + ver + "'")
        else:
            print("Failed to set package version.")

def getver():
    info = getAttrs(["name", "version"])
    if info[0] == "":
        print("Package name not found in setup.py")
    elif info[1] == "":
        print("Package version not found in setup.py")
    else:
        print("Package name:", info[0])
        print("Package version:", info[1])

def pkg():
    clear()
    setup()
    upload()

def patch():
    info = getAttrs(["name", "version"])
    if info[0] == "":
        print("Package name not found in setup.py")
    elif info[1] == "":
        print("Package version not found in setup.py")
    else:
        ver = info[1].split(".")
        ver[-1] = str(int(ver[-1]) + 1)
        ver = ".".join(ver)
        setver(ver)
        pkg()
        
def minor():
    info = getAttrs(["name", "version"])
    if info[0] == "":
        print("Package name not found in setup.py")
    elif info[1] == "":
        print("Package version not found in setup.py")
    else:
        ver = info[1].split(".")
        ver[-2] = str(int(ver[-2]) + 1)
        ver[-1] = "0"
        ver = ".".join(ver)
        setver(ver)
        pkg()

def major():
    info = getAttrs(["name", "version"])
    if info[0] == "":
        print("Package name not found in setup.py")
    elif info[1] == "":
        print("Package version not found in setup.py")
    else:
        ver = info[1].split(".")
        ver[-3] = str(int(ver[-3]) + 1)
        ver[-2] = "0"
        ver[-1] = "0"
        ver = ".".join(ver)
        setver(ver)
        pkg()

def main():
    argv = sys.argv
    if len(argv) == 1:
        help()
    elif argv[1] == "-h" or argv[1] == "help":
        help()
    elif argv[1] == "-u" or argv[1] == "upload":
        upload()
    elif argv[1] == "-s" or argv[1] == "setup":
        setup()
    elif argv[1] == "-c" or argv[1] == "clear":
        clear()
    elif argv[1] == "-p" or argv[1] == "pkg":
        pkg()
    elif argv[1] == "-i" or argv[1] == "info":
        print("spkg by xuanzhi33")
    elif argv[1] == "-pv" or argv[1] == "pkgver":
        getver()
    elif argv[1] == "-sv" or argv[1] == "setver":
        if len(argv) == 3:
            setver(argv[2])
        else:
            ver = input("new version: ")
            setver(ver)
    elif argv[1] == "-mi" or argv[1] == "minor":
        minor()
    elif argv[1] == "-ma" or argv[1] == "major":
        major()
    elif argv[1] == "-pa" or argv[1] == "patch":
        patch()
    else:
        print("Unknown command:", argv[1])
        help()

if __name__ == "__main__":
    main()

