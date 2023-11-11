[app]

title = Test htag App
package.name = testhtagapk
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg

# (str) Presplash of the application
presplash.filename = %(source.dir)s/htag.png

# (str) Icon of the application
icon.filename = %(source.dir)s/htag.png

version = 0.1
requirements = python3,kivy,tornado,htbulma,htag

orientation = portrait
fullscreen = 0
# android.archs = arm64-v8a
android.archs = armeabi-v7a


# (list) Permissions
android.permissions = INTERNET

# (str) Filename to the hook for p4a
p4a.hook = p4a/hook.py

# iOS specific
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master
ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
ios.ios_deploy_branch = 1.7.0

[buildozer]
log_level = 2
