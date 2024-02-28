# Recipes to build an android/apk from an HTag app

<img src="app/htag.png" width="100" height="100">

**IMPORTANT 2024/02/28**
All theses recipes will only work for htag < 0.90.0 !!!
The new recipe, for htag>=0.90.0 will come soon (and will use the buildozer/p4a "webview" bootstrap, in place of the old bootstrap sdl2/kivy). Because it works a lot better, and a lot simpler !
**IMPORTANT 2024/02/28**



This is the **build apk method** for an [HTag app](https://github.com/manatlan/htag)

It uses the [AndroidApp runner](https://manatlan.github.io/htag/runners/#androidapp), based on [kivy](https://kivy.org/) and [tornado](https://www.tornadoweb.org/en/stable/).

Your application must use the **AndroidApp** like this :

```python
from htag.runners import AndroidApp
AndroidApp( App ).run()
```

There are 2 recipes, to build the apk : **locally** or using **github action**

## Locally

You should use [make.py](make.md) !

## Github action

The simplest one ! Click the "Run workflow" button on this [Github Action](https://github.com/manatlan/htagapk/actions/workflows/build.yml). It will produce a "package" (zip containing the apk) in the "github action" > artifacts panel. (after 10 to 12 minutes)

(thanks to the marvellous github action : https://github.com/ArtemSBulgakov/buildozer-action !)


## Test the apk/online

  * [You can test the generated apk on appetize.io !](https://appetize.io/app/e8wmjett21ewfb737x152c9bfr?device=pixel6&osVersion=12.0&scale=75). Or you can download the apk (find it in a "package.zip", downloadable from github action builds), and test on your phone.
  * You can test, the same app, in a web context : https://htag.glitch.me/?app=c99
  * And, you can test it, in a pyscript context (with **PyScript runner**) : https://raw.githack.com/manatlan/htag/main/examples/pyscript_htbulma.html (just pure html !(no server side))

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

## IRL apps

 - [TriApp](https://github.com/manatlan/TriApp): a freely android clone of TriCount
 - [MAAR](https://github.com/manatlan/maar) : a POC of a music player for android autoradio
 - ...

