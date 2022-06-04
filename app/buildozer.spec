[app]

title = Test htag App                                 # <- adapt here
package.name = testhtagapk                            # <- adapt here
package.domain = org.test                             # <- adapt here

source.dir = .
source.include_exts = py,png,jpg                      # <- adapt here

version = 0.1
requirements = python3,kivy,tornado,htbulma,htag      # <- adapt here

orientation = portrait
fullscreen = 0
android.arch = arm64-v8a

# (list) Permissions
android.permissions = INTERNET                        # <- adapt here

# (str) Filename to the hook for p4a
p4a.hook = p4a/hook.py

# iOS specific
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master
ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
ios.ios_deploy_branch = 1.7.0

[buildozer]
log_level = 2
