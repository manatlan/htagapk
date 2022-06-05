# Recipes to build an android/apk from an HTag app

This is the **build apk method** for an [HTag app](https://github.com/manatlan/htag)

It uses the [AndroidApp runner](https://manatlan.github.io/htag/runners/#androidapp), based on [kivy](https://kivy.org/) and [tornado](https://www.tornadoweb.org/en/stable/).

Your application must use the **AndroidApp** like this :

```python
from htag.runners import AndroidApp
AndroidApp( Page ).run()
```

There are 2 recipes, to build the apk : **locally** or using **github action**

## Locally

You'll need to have a linux host, and you will need to install [kivy](https://kivy.org/) and [buildozer](https://buildozer.readthedocs.io/en/latest/), and [adb tools](https://www.xda-developers.com/install-adb-windows-macos-linux/).

Download the repo, plug your phone (with a good usb cable), and in console:

```
cd app
buildozer android debug deploy run
```

The app should start on your phone ...


## Github action

The simplest one ! Any changes to the repo will run a **Github Action**, which will produce a "package" (zip containing the apk) in the [github action](actions) > artifacts panel. (after 10 to 12 minutes)

(thanks to the marvellous github action : https://github.com/ArtemSBulgakov/buildozer-action !)

**`**NEXTSOON**`**

## Test the apk/online

[You can test the generated apk here !](https://appetize.io/app/70yxx4a32qcq1v0m00b12fm68w?device=pixel6&osVersion=12.0&scale=75)

<details>
  <summary>Urls inspirations</summary>
  
  help for modify androidmanifest : https://github.com/ArtemSBulgakov/buildozer-action/issues/20
  
  github actions doc : https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idstepsuses

  P4A docs : https://github.com/Android-for-Python/Android-for-Python-Users#changing-buildozerspec

  Buidozer-action: https://github.com/ArtemSBulgakov/buildozer-action

  example : https://github.com/kaustubhgupta/KivyMLApp

  clear text trouble : https://manatlan.github.io/guy/howto_build_apk_android/#authorize-clear-text-traffic-in-your-apk

  main ideas: https://towardsdatascience.com/3-ways-to-convert-python-app-into-apk-77f4c9cd55af
</details>
