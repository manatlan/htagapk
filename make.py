#!/usr/local/bin/python3.7 -u
import os,sys,subprocess,json,glob
CWD=os.path.realpath(os.path.dirname(__file__) or os.path.dirname(sys.argv[0]))

DOCKER="mybuildozer"

def read_spec():
    return dict([ [j.strip() for j in i.split("=",1)] for i in open(f"{CWD}/app/buildozer.spec").read().splitlines() if i.strip() and "=" in i])

def is_docker_image_exists():
    try:
        x=json.loads(subprocess.run(f"docker images {DOCKER} --format json",capture_output=True,shell=True).stdout)
    except:
        x={}
    return "ID" in x

def build(mode="debug"):
    if not is_docker_image_exists():
        assert subprocess.call("which git",shell=True)==0,"install git !"
        assert subprocess.call("which docker",shell=True)==0,"install docker !"
        os.system(f"""
cd /tmp
git clone https://github.com/kivy/buildozer.git
cd buildozer
docker build --tag={DOCKER} .
""")

    os.system(f"""
cd {CWD}/app
mkdir .buildozer
docker run -v $(pwd)/.buildozer:/home/user/.buildozer -v $(pwd):/home/user/hostcwd {DOCKER} android {mode}
""")

def install():
    assert subprocess.call("which adb",shell=True)==0,"install adb !"

    x=read_spec()
    package=x["package.domain"]+"."+x["package.name"]
    name = x["package.name"]

    apks=glob.glob(f"{CWD}/app/bin/{name}-*.apk")
    if apks:
        print("install",package,apks[0])
        os.system(f"""
adb uninstall {package}
adb install -r -g {apks[0]}
""")
        
        activity="org.kivy.android.PythonActivity"
        os.system(f"adb shell am start -W -n {package}/{activity}")
    else:
        print("no apk in app/bin ?!")

def clean():
    os.system(f"rm -rf {CWD}/app/bin")
    os.system(f"rm -rf {CWD}/app/.buildozer")

def test():
    os.system(f"{sys.executable} app/main.py")

def debug():
    assert subprocess.call("which pidcat",shell=True)==0,"install pidcat !"

    x=read_spec()
    package=x["package.domain"]+"."+x["package.name"]

    os.system(f"pidcat {package}")


if __name__=="__main__":
    assert os.path.isfile(f"{CWD}/app/buildozer.spec"),"wtf?"
    _,*args = sys.argv
    if args==["build"]:
        build()
    elif args==["install"]:
        install()
    elif args==["debug"]:
        debug()
    elif args==["clean"]:
        clean()
    elif args==["test"]:
        test()
    else:
        print("USAGE: $./make.py <option>")
        print("'test/build/install' apk from an htag app")
        print("Where <option> is:")
        print(" - test    : test you app locally")
        print(" - build   : to build the apk")
        print(" - install : to install/run the apk in plugged device")
        print(" - debug   : watch log from your app in plugged device")
        print(" - clean   : delete apks and app/.buildozer")
