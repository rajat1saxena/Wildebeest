# Author: Rajat Saxena<rajat.saxena.work@gmail.com>
# License: GNU GPL v3

import pygtk
pygtk.require("2.0")
from BeautifulSoup import BeautifulSoup
import sys
import gtk

class editor:
    def __init__(self):
        self.filename = "./interface.glade"
        self.builder = gtk.Builder()
        self.builder.add_from_file(self.filename)

        #getting objects from glade file
        self.win = self.builder.get_object("mainwin")
        self.html = self.builder.get_object("html")
        self.css = self.builder.get_object("css")
        self.js = self.builder.get_object("js")
        self.check_js = self.builder.get_object("check_js")
        self.do = self.builder.get_object("do")
        self.status = self.builder.get_object("status")

        #main window's settings
        self.win.set_size_request(900,450)
        self.win.connect("destroy",self.destroy)

        #setting do button's properties
        self.do.set_size_request(50,20)
        self.check_js.set_size_request(50,20)
        self.html.set_size_request(300,370)
        self.css.set_size_request(300,370)
        self.js.set_size_request(300,370)
        self.status.set_size_request(900,2)
        self.do.connect("clicked",self.process)

        #enabling wrap mode
        self.html.set_wrap_mode(gtk.WRAP_WORD)

        #other settings
        self.status.set_text("Editing...")

        #reading data and filling text boxes
        self.prefill() 

        #window
        self.win.set_title("Wildebeest Editor")
        self.win.show_all()

    def destroy(self,widget):
        gtk.main_quit()

    def prefill(self):
        try:
                #filling html textview
                prehtml = open("webfile.html","r")
                string = ""
                for each in prehtml:
                        string = string+each
                #print(string)
                soup = BeautifulSoup(string)
                prehtmltext = soup.body
                print(prehtmltext.renderContents())
                prehtml.close()

                html_buffer = self.html.get_buffer()
                html_buffer.set_text(prehtmltext.renderContents())

                #filling css textview
                precss = open("style.css","r")
                string = ""
                for each in precss:
                        string = string+each
                print(string)
                precss.close()

                css_buffer = self.css.get_buffer()
                css_buffer.set_text(string)

                #filling css textview
                prejs = open("script.js","r")
                string = ""
                for each in prejs:
                        string = string+each
                print(string)
                prejs.close()

                js_buffer = self.js.get_buffer()
                js_buffer.set_text(string)

        except:
                pass


    def process(self,widget):

        #Getting text from all the textview widgets
        html_buffer = self.html.get_buffer()
        css_buffer = self.css.get_buffer()
        js_buffer = self.js.get_buffer()
        texthtml = html_buffer.get_text(html_buffer.get_start_iter(),html_buffer.get_end_iter())
        textcss = css_buffer.get_text(css_buffer.get_start_iter(),css_buffer.get_end_iter())
        textjs = js_buffer.get_text(js_buffer.get_start_iter(),js_buffer.get_end_iter())

        #This is the module for auto refreshing the page 
        script = '''
        /* Just remove this function.It was introduced by Wildebeest editor */
        
                function refresh(){
                        window.location.reload(true);
                }
                setTimeout(refresh,1000)
        
        /* End of wildebeest editor's auto reloading function */
        '''

        if self.check_js.get_active():
                script = ""
        #if texthtml == "":
        #        sys.exit(0)

        #Formatting the template
        self.htmltemplate = "<!DOCTYPE html>\n<html>\n<head>\n<title>From Editor</title>\n<script type='text/javascript' src='autoreload.js'>\n<script type='text/javascript' src='script.js'></script>\n<link rel='stylesheet' href='style.css'>\n"+"</head>\n<body>\n"+texthtml+"\n</body>\n</html>"
        
        #Saving data to script.js
        jsfile = open("script.js","w")
        for each in textjs:
                jsfile.write(each)
        jsfile.close()

        #Saving data to style.css
        cssfile = open("style.css","w")
        for each in textcss:
                cssfile.write(each)
        cssfile.close()

        #Saving data to autoreload.js
        reloadfile = open("autoreload.js","w")
        for each in script:
                reloadfile.write(each)
        reloadfile.close()

        #Saving data to html page named "webfile.html"
        webfile = open("webfile.html","w")
        for each in self.htmltemplate:
            webfile.write(each)
        webfile.close()

        

if __name__ == "__main__":
    editor = editor()
    gtk.main()
        
