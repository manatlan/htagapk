
[app]

title = Test htag App
package.name = testhtagapk
package.domain = org.test
version = 1.0

source.dir = .
source.include_exts = py,png,jpg

#--------------------------------------------------------- https://github.com/ArtemSBulgakov/buildozer-action/issues/34
requirements = android,htag>=0.90.0,htbulma
#---------------------------------------------------------

#=================================== # smartphone
orientation = portrait
fullscreen = 0
android.archs = arm64-v8a
## android.archs = x86_64
icon.filename = %(source.dir)s/htag.png
#=================================== # android tv
#~ orientation = landscape
#~ fullscreen = 1
#~ android.archs = armeabi-v7a
#~ presplash.filename = %(source.dir)s/banner.png
#~ icon.filename = %(source.dir)s/icontv.png
#===================================


home_app = 1
android.permissions = INTERNET
android.accept_sdk_license = True

# (str) Filename to the hook for p4a
p4a.hook = p4a/hook.py

# this PORT should be the same as in Runner part !!!!
p4a.port = 12458
p4a.bootstrap = webview
#--------------------------------------------------------- by default it's "master"
p4a.branch = v2023.09.16
#---------------------------------------------------------

[buildozer]
log_level = 2
