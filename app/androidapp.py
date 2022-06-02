# -*- coding: utf-8 -*-
# # #############################################################################
# Copyright (C) 2022 manatlan manatlan[at]gmail(dot)com
#
# MIT licence
#
# https://github.com/manatlan/htag
# #############################################################################


from htag import Tag
from htag.render import HRenderer

import os
import threading

import uvicorn
from starlette.applications import Starlette
from starlette.responses import HTMLResponse,JSONResponse
from starlette.routing import Route


class AndroidApp:
    """
    An "Android Runner", for an HTag App. Which will only work on android/platform
    
    BTW : it uses Starlette/uvicorn/http as backend server
    """
    def __init__(self,tagClass:type):
        assert issubclass(tagClass,Tag)

        js = """
async function interact( o ) {
    action( await (await window.fetch("/",{method:"POST", body:JSON.stringify(o)})).json() )
}

window.addEventListener('DOMContentLoaded', start );
"""

        host,port= "127.0.0.1", 8707
        self.urlStartPage = f"http://{host}:{port}"
        
        self.renderer=HRenderer(tagClass, js, lambda: os._exit(0) )

        asgi=Starlette(debug=True, routes=[
            Route('/', self.GET, methods=["GET"]),
            Route('/', self.POST, methods=["POST"]),
        ])

        self._server = threading.Thread(name='ChromeAppServer', target=uvicorn.run,args=(asgi,),kwargs=dict(host=host, port=port))

    async def GET(self,request) -> HTMLResponse:
        return HTMLResponse( str(self.renderer) )

    async def POST(self,request) -> JSONResponse:
        data = await request.json()
        dico = await self.renderer.interact(data["id"],data["method"],data["args"],data["kargs"])
        return JSONResponse(dico)

    def run(self): # basically, the same code as guy.runAndroid()
        import kivy
        from kivy.app import App
        from kivy.utils import platform
        from kivy.uix.widget import Widget
        from kivy.clock import Clock
        from kivy.logger import Logger

        def run_on_ui_thread(arg):
            pass

        webView       = None
        webViewClient = None
        #~ webChromeClient = None
        activity      = None
        if platform == 'android':
            from jnius import autoclass
            from android.runnable import run_on_ui_thread
            webView       = autoclass('android.webkit.WebView')
            webViewClient = autoclass('android.webkit.WebViewClient')
            #~ webChromeClient = autoclass('android.webkit.WebChromeClient')
            activity      = autoclass('org.kivy.android.PythonActivity').mActivity
        else:
            print("Can only work on android, you are on '%s' !!!" % platform)
            os._exit(-1)



        class Wv(Widget):
            def __init__(self, aa ):
                self.f2 = self.create_webview # important
                super(Wv, self).__init__()
                self.visible = False

                def exit(v):
                    activity.finish()
                    App.get_running_app().stop()
                    os._exit(0)

                self.aa=aa
                aa._server.start()                                              # !important

                Clock.schedule_once(self.create_webview, 0)

            @run_on_ui_thread
            def create_webview(self, *args):
                webview = webView(activity)
                webview.getSettings().setJavaScriptEnabled(True)
                webview.getSettings().setDomStorageEnabled(True)
                webview.setWebViewClient(webViewClient())
                #~ webview.setWebChromeClient(webChromeClient())
                activity.setContentView(webview)
                webview.loadUrl(self.aa.urlStartPage)                           # !important

        class ServiceApp(App):
            def build(this):
                return Wv( self )

        ServiceApp().run()
