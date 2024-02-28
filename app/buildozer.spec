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

# requirements = Cython,kivy,tornado,htbulma,htag>=0.64.0
#--------------------------------------------------------- https://github.com/ArtemSBulgakov/buildozer-action/issues/34
requirements = Cython==0.29.33,kivy==2.2.0,tornado,htbulma,htag<0.90.0
#---------------------------------------------------------

orientation = portrait
fullscreen = 0
android.archs = arm64-v8a
# android.archs = armeabi-v7a


# (list) Permissions
android.permissions = INTERNET

android.accept_sdk_license = True

# (str) Filename to the hook for p4a
p4a.hook = p4a/hook.py

#--------------------------------------------------------- https://github.com/ArtemSBulgakov/buildozer-action/issues/34
# p4a.branch = release-2022.12.20
p4a.branch = v2023.09.16
#---------------------------------------------------------

# iOS specific
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master
ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
ios.ios_deploy_branch = 1.7.0

[buildozer]
log_level = 2
