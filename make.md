# make.py : a command line to build/install the apk

It's a command line for the full process ! You will need a linux host (or a windows/wsl2) where **docker**, **git**, **adb** & **pidcat** are availables. (you'll need to install them)

Give the "execution" rights to make.py :
```bash 
chmod +x ./make.py
```

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
