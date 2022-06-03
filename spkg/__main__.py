import os
import sys

def output(text):
    print("\033[44m SPKG \033[0m " + text)

def print_done(text):
    output("\033[42m DONE \033[0m " + text)

def print_error(text):
    output("\033[41m ERROR \033[0m " + text)

def run_cmd(cmd):
    output("\033[45m RUNNING \033[0m " + cmd)
    os.system(cmd)

def help():
    print("""\033[44m SPKG \033[0m by \033[1;92mxuanzhi33\033[0m
Usage: spkg [COMMAND]

Commands:
    help, -h: show this help message and exit (default)
    upload, -u: upload the package to pypi (equals to 'twine upload dist/*')
    setup, -s: setup the package (equals to 'python3 setup.py sdist')
    clear, -c: delete all .tar.gz files in 'dist' folder
    pkg, -p: clear, setup, and upload the package
    info, -in: show package info
    setver [version] , -sv [version]: set package version
    install [package] , -i [package]: install a package from pypi using 'pip3 install --upgrade [package]'
    
    The commands below can change package version quickly and then run 'pkg' command:
    (They will modify the version in 'setup.py')
    patch, -pa: Release patch update (e.g. 1.0.1 -> 1.0.2)
    minor, -mi : Release minor update (e.g. 1.0.3 -> 1.1.0)
    major, -ma: Release major update (e.g. 1.1.1 -> 2.0.0)""")

def upload():
    output("Uploading package to \033[34mpypi\033[0m...")
    run_cmd("twine upload dist/*")
    print_done("Package uploaded.")
    

def setup():
    output("Setting up package...")
    run_cmd("python3 setup.py sdist")
    print_done("Setup successfully.")

def clear():
    output("Deleting all .tar.gz files in 'dist' folder...")
    if os.path.exists("dist"):
        files = os.listdir("dist")
        for file in files:
            if file.endswith(".tar.gz"):
                os.remove("dist/" + file)
                output("\033[41m REMOVED \033[0m " + file)
    else:
        output("No dist folder found.")

    print_done("All .tar.gz files in 'dist' folder deleted.")


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

def setver(ver, info):
    if setAttr("version", ver):
        print_done("Verson of package '" + info[0] + "' changed from '" + info[1] + "' to '" + ver + "'")
    else:
        print_error("Failed to set package version.")

def pkg_info(info):
    output("Package name:", info[0])
    output("Package version:", info[1])

def pkg():
    clear()
    setup()
    upload()

def patch(info):
    ver = info[1].split(".")
    ver[-1] = str(int(ver[-1]) + 1)
    ver = ".".join(ver)
    setver(ver, info)
    pkg()
        
def minor(info):
    ver = info[1].split(".")
    ver[-2] = str(int(ver[-2]) + 1)
    ver[-1] = "0"
    ver = ".".join(ver)
    setver(ver, info)
    pkg()

def major(info):
    ver = info[1].split(".")
    ver[-3] = str(int(ver[-3]) + 1)
    ver[-2] = "0"
    ver[-1] = "0"
    ver = ".".join(ver)
    setver(ver, info)
    pkg()

def check_pkg():
    if not os.path.exists("setup.py"):
        print_error("No setup.py found in current folder.")        
        return None

    info = getAttrs(["name", "version"])
    if info[0] == "":
        print_error("Package name not found in setup.py")
        return None
    if info[1] == "":
        print_error("Package version not found in setup.py")
        return None
    
    return info

def install_pkg(pkg):
    run_cmd("pip3 install --upgrade " + pkg)

def main():
    argv = sys.argv
    if len(argv) == 1:
        help()
    elif argv[1] == "-h" or argv[1] == "help":
        help()
    else:
        pkginfo = check_pkg()
        if pkginfo is not None:
            if argv[1] == "-u" or argv[1] == "upload":
                upload()
            elif argv[1] == "-s" or argv[1] == "setup":
                setup()
            elif argv[1] == "-c" or argv[1] == "clear":
                clear()
            elif argv[1] == "-p" or argv[1] == "pkg":
                pkg()
            elif argv[1] == "-in" or argv[1] == "info":
                pkg_info(pkginfo)
            elif argv[1] == "-sv" or argv[1] == "setver":
                if len(argv) == 3:
                    setver(argv[2], pkginfo)
                else:
                    ver = input("new version: ")
                    setver(ver, pkginfo)

            elif argv[1] == "-mi" or argv[1] == "minor":
                minor(pkginfo)
            elif argv[1] == "-ma" or argv[1] == "major":
                major(pkginfo)
            elif argv[1] == "-pa" or argv[1] == "patch":
                patch(pkginfo)
            elif argv[1] == "-i" or argv[1] == "install":
                if len(argv) == 3:
                    install_pkg(argv[2])
                else:
                    pkg = input("package name: ")
                    install_pkg(pkg)
            else:
                print_error("Unknown command: " + argv[1])
                help()

if __name__ == "__main__":
    main()
