from htag import Tag
import htbulma as b
import html

"""
And here : the ultimate goal of htag ...

You can develop your own htag's components, and create your own UI Toolkit.
And start to build complex app, here is an example using "htbulma"
(a set of components, I use/develop on an other side )

NOTE : this project use a lot a deprecated htbulma components ;-) TODO: fix that ;-)
"""

class App(Tag.body):
    """Build and use your own UI components"""
    
    imports = b.ALL  # IRL, you don't need this line
    
    def init(self):
        self["style"]="overflow-y:auto !important"
        self.mbox = b.MBox(self) # declare the 'service' mbox
        self.toast = b.Toaster(self) # declare the 'service' toaster
        self.code = Tag.pre("select a file")
        
        nav = b.Nav("MyApp")    # declare the nav bar
        nav.addEntry("mbox",    lambda: self.mbox.show("hello"))  # declare an entry in the nav bar
        nav.addEntry("confirm", lambda: self.mbox.confirm("Sure ?",ok=self.action))  # declare an entry in the nav bar
        nav.addEntry("prompt",  lambda: self.mbox.prompt("What is your name ?","",ok=self.action))  # declare an entry in the nav bar
        nav.addEntry("EXIT",    lambda: self.exit())    # an entry, to be able to quit the android app ;-)

        self.select=1
        fields=b.Fields()
        options=[1,2,3]
        fields.addField("radio",      b.Radio(self.select, options, onchange=self.showvalue))
        fields.addField("sb",         b.SelectButtons(self.select, options, onchange=self.showvalue) )
        fields.addField("select",     b.Select(self.select, options, onchange=self.showvalue) )
        fields.addField("cb",         b.Checkbox( False, "Just do it", onchange=self.showvalue))
        fields.addField("input",      b.Input("hello", onchange=self.showvalue))
        fields.addField("input date", b.Input(None,_type="date", onchange=self.showvalue) )
        fields.addField("text area",  b.Textarea("world",_rows=2, onchange=self.showvalue) )
        fields.addField("range",      b.Range(42,_min=0,_max=100, onchange=self.showvalue) )

        filer = b.HSplit( 
            b.FileSelect("./", self.load, pattern="*.py"),
            self.code ,
            sizes=[30,70],
          )
        
        tab = b.Tabs()
        tab.addTab("Tab one",fields)
        tab.addTab("Tab two",filer)
        tab.addTab("Tab Three","I'm working in background"+b.Progress())
        
        main = b.Box()
        main <= b.Button("Push",_onclick=lambda o: self.action("button!") )
        main <= Tag.a("See htbulma",_href="https://github.com/manatlan/htbulma", _target="_blank", _style="float:right")
        main <= tab
        
        self <= nav + b.Section( main )
        
    def action(self,o=None):
        self.toast.show(o or ";-)")
    def showvalue(self,object):
        self.toast.show(object.value)
    def load(self,filename):
        self.action(filename)
        self.code.set( html.escape(open(filename).read()) )
        
if __name__=="__main__":
    PORT = 12458    #!!! IMPORTANT !!! same as in buildozer.spec (see key "p4a.port") 

    from htag.runners import Runner
    Runner( App, port=PORT, interface=0 ).run()
