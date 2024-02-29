# make.py : a command line to build/install the apk

It's a command line for the full process ! You will need a linux host (or a windows/wsl2) where **python3**, **docker**, **git**, **adb** & **pidcat** are availables. (you'll need to install them)

If you have an unique folder/project : it will use this unique folder/project.

If you have multiple folder (ex: 'app1', 'app2' folders) : you must provide the folder name
(ex: `./make.py app1 test`, `./make.py app1 build`, ... etc ...)


# `./make.py test`
Test your app in your current browser (good practice before building ;-))

# `./make.py build`
Build the apk in `app/bin` folder ! (debug mode)

# `./make.py install`
**[need plugged device]** Plug you device (with usb cable), and it will install & run the apk in the device

# `./make.py debug`
**[need plugged device]** Follow the logs from your app running in the device

# `./make.py clean`
clean all (delete apks and app/.buildozer on your computer)
