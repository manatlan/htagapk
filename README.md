# Recipes to build an android/apk from an HTag app

<img src="app/htag.png" width="100" height="100">

This is the **build apk method** for an [HTag app](https://github.com/manatlan/htag) (using htag >= 0.90.0)

Don't be afraid, it's really simple (thanks to buildozer docker system !!)

**Note** : 

 - Since htag>=0.90, this recipe has changed (no more github action), and no more `AndroidApp`'htag special runner ! **htag** is the only dependancy !!!
 - The previous mechanim used the 'sdl2' bootstrap with kivy (so kivy was needed). Now it uses the 'webview' bootstrap (no more kivy needed!), and it's a lot more natural (apk is smaller, speedier, simpler and 'back' button is supported OOTB)


## Recipe :

You should use [make.py](make.md), which is a script/commandline to help you in the build/install/debug process (using the buildozer tool).

First of all, ensure that theses tools are installed on your computer :
**python3**, **docker**, **git**, **adb** & **pidcat** (depending on your distribution, it's just `sudo apt-get install python3 docker git adb pidcat`)

You'll have to know basics adb commmands (`adb connect`, `adb devices`, ...)

Open a console and do :
```bash
$ git clone https://github.com/manatlan/htagapk.git
$ cd htagapk
```

Give execution permission to `make.py`
```bash
$ chmod +x ./make.py
```

See if it works ;-)
```bash
$ ./make.py
```
It will show you that you have 2 project/folders (app & app2)

- "app" is an android smartphone app
- "app2" is an android tv app

(More to come)

So you'll have to define which one you want to test (in the folowing, we will take 'app" )

Build the apk
```bash
$ ./make.py app build
```

Plug your device, and ensure that it's connected (using `adb` tool)
```bash
$ adb devices
```
(no trouble to connect a wifi android device, it works the same (if the device accept incoming connexion))

You can install the apk, and run it, using :
```bash
$ ./make.py app install
```

If you want to see the live log
```bash
$ ./make.py app debug
```



## IRL others htag (<0.90) apps repo

Deprecated, coz using the old way, with htag < 0.90 !!!

 - [TriApp](https://github.com/manatlan/TriApp): a freely android clone of TriCount **(htag < 0.90)**
 - [MAAR](https://github.com/manatlan/maar) : a POC of a music player for android autoradio **(htag < 0.90)**
 - ...

