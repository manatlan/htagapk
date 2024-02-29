#!/usr/local/bin/python3.7 -u
import os,sys,subprocess,json,glob
CWD=os.path.realpath(os.path.dirname(__file__) or os.path.dirname(sys.argv[0]))
KNOWNAPPS=[i[2:].split("/")[-2] for i in glob.glob(CWD+"/*/buildozer.spec")]

DOCKER="mybuildozer"

def help(error=None):
    
    
    if error:
        print("**",error,"**")
        print()
    
    print("USAGE: $ make.py [project] <option>")
    print("Commandline to test/build/install apk from an htag app")
    print()
    print(f"Existings project(s) : {','.join(KNOWNAPPS)}")
    print()
    print("Where <option> is:")
    print(" - test    : to test you app locally")
    print(" - build   : to build the apk")
    print(" - install : to install/run the apk in plugged device")
    print(" - debug   : to watch log from your app in plugged device")
    print(" - clean   : to delete apks and app/.buildozer")
    sys.exit(-1)

def read_spec(app:str):
    return dict([ [j.strip() for j in i.split("=",1)] for i in open(f"{CWD}/{app}/buildozer.spec").read().splitlines() if i.strip() and "=" in i])

def is_docker_image_exists():
    try:
        x=json.loads(subprocess.run(f"docker images {DOCKER} --format json",capture_output=True,shell=True).stdout)
    except:
        x={}
    return "ID" in x

############################################################
def build(app:str, mode="debug"):
############################################################
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
cd {CWD}/{app}
mkdir .buildozer
docker run -v $(pwd)/.buildozer:/home/user/.buildozer -v $(pwd):/home/user/hostcwd {DOCKER} android {mode}
""")

############################################################
def install(app:str):
############################################################
    assert subprocess.call("which adb",shell=True)==0,"install adb !"

    x=read_spec(app)
    package=x["package.domain"]+"."+x["package.name"]
    name = x["package.name"]

    apks=glob.glob(f"{CWD}/{app}/bin/{name}-*.apk")
    if apks:
        if len(apks)>1:
            help("GOT MULTIPLE APK ?! AMBIGUS !!!")
        print("install",package,apks[0])
        os.system(f"""
adb uninstall {package}
adb install -r -g {apks[0]}
""")
        
        activity="org.kivy.android.PythonActivity"
        os.system(f"adb shell am start -W -n {package}/{activity}")
    else:
        print(f"no apk in {app}/bin ?!")

############################################################
def clean(app:str):
############################################################
    os.system(f"rm -rf {CWD}/{app}/bin")
    os.system(f"rm -rf {CWD}/{app}/.buildozer")

############################################################
def test(app:str):
############################################################
    os.system(f"{sys.executable} {app}/main.py")

############################################################
def debug(app:str):
############################################################
    assert subprocess.call("which pidcat",shell=True)==0,"install pidcat !"

    x=read_spec(app)
    package=x["package.domain"]+"."+x["package.name"]

    os.system(f"pidcat {package}")


if __name__=="__main__":
    
    _,*args = sys.argv
    if not args:
        help()
    else:
        if len(args)==1:
            if len(KNOWNAPPS)==1:
                # auto define/select app (coz only one)
                app=KNOWNAPPS[0]
                cmd=args[0]
                print("USE PROJECT:",app)
            else:
                help("YOU SHOULD SPECIFY ONE !")
        elif len(args)==2:
            app=args[0]
            cmd=args[1]
            if not app in KNOWNAPPS:
                help("YOU SHOULD SPECIFY AN APP WHICH EXISTS !")
        else:
            help()
            
        if cmd in ["build","install","debug","clean","test"]:
            if cmd=="build":
                build(app)
            elif cmd=="install":
                install(app)
            elif cmd=="debug":
                debug(app)
            elif cmd=="clean":
                clean(app)
            elif cmd=="test":
                test(app)
        else:
            help(f"UNKNWON COMMAND '{cmd}'" )
