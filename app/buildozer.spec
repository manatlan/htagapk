[app]

title = Test htag App
package.name = testhtagapk
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1
requirements = python3,kivy,tornado,htbulma,htag

orientation = portrait
fullscreen = 0
android.arch = armeabi-v7a

# (str) Filename to the hook for p4a
p4a.hook = p4a/hook.py

# iOS specific
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master
ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
ios.ios_deploy_branch = 1.7.0

[buildozer]
log_level = 2
