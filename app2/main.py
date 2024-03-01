# -*- coding: utf-8 -*-

from htag import Tag,expose

def start_intent( url ):
    print(f"Try to start_intent {url}")
    try:
        ###################################################################
        # https://github.com/adywizard/car-locator/blob/master/main.py#L1088
        from jnius import autoclass
        PythonActivity = autoclass('org.kivy.android.PythonActivity')
        Intent = autoclass('android.content.Intent')
        Uri = autoclass('android.net.Uri')
        mActivity = PythonActivity.mActivity

        uri = Uri.parse(url)
        intent = Intent(Intent.ACTION_VIEW, uri)
        intent.setDataAndType(uri, "video/*");  # ???
        intent.setPackage("org.videolan.vlc")
        mActivity.startActivity(intent)
        return "ok"
        ###################################################################
    except Exception as e:
        return f"ko: {e}"


class FocusablePanel(Tag.div):
    """ propose une navigation via keys cursor dans les childs @class=".focusable" """
    statics="""
.focusable:focus {
  color: red;
  outline: none;
}
"""
    def init(self):
        self.js = """
document.onkeydown = function(e) {
    var ll = [...document.querySelectorAll(".focusable")];
    var current=document.activeElement;
    if(e['key']=="ArrowLeft" || e['key']=="ArrowUp") {
        let idx=ll.indexOf(current);
        idx=( ll.length + idx - 1) % ll.length;
        ll[idx].focus();
        e.preventDefault();
    }
    else if(e['key']=="ArrowRight" || e['key']=="ArrowDown") {
        let idx=ll.indexOf(current);
        idx=( ll.length + idx + 1) % ll.length;
        ll[idx].focus();
        e.preventDefault();
    }
}
        """



class App(Tag.body):
    imports=[FocusablePanel]
    statics="""body {background:black;color:white}"""

    def init(self):

        self.log = Tag.div()

        with FocusablePanel() as d:
            d += Tag.button("play1",_class="focusable", _onclick=self.play,js="self.focus()",
                url="https://avtshare01.rz.tu-ilmenau.de/avt-vqdb-uhd-1/test_1/segments/bigbuck_bunny_8bit_15000kbps_1080p_60.0fps_h264.mp4"
            )
            d += Tag.button("play2",_class="focusable", _onclick=self.play, 
                url="https://avtshare01.rz.tu-ilmenau.de/avt-vqdb-uhd-1/test_1/segments/water_netflix_7500kbps_2160p_59.94fps_h264.mp4"
            )
            d += Tag.button("play3",_class="focusable", _onclick=self.play, 
                url="https://avtshare01.rz.tu-ilmenau.de/avt-vqdb-uhd-1/test_1/segments/vegetables_tuil_15000kbps_1080p_59.94fps_h264.mp4"
            )
        
        # build ui
        self+=d
        self+=self.log
        
    def play(self,o):
        self.log.set( start_intent(o.url) )



#=================================================================================
if __name__=="__main__":
    PORT = 12459    #!!! IMPORTANT !!! same as in buildozer.spec (see key "p4a.port") 

    from htag.runners import Runner
    Runner( App, port=PORT, interface=0 ).run()