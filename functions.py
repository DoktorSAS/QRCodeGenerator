import re
import os
from importlib_metadata import version
import qrcode
import qrcode.image.svg


VALID_COLORS = ['blue', 'red', 'white', 'black', 'yellow', 'green', 'purple', 'orange']
HEX_COLOR_REGEX = r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$'

def is_hex_color(input_string):
    regexp = re.compile(HEX_COLOR_REGEX)
    if regexp.search(input_string):
        return True
    return False

def is_color(input_string):
    for color in VALID_COLORS:
        if color in input_string or is_hex_color(input_string):
            return True
    return False

def validate_url(str):
    regex = ("((http|https)://)(www.)?" +
            "[a-zA-Z0-9@:%._\\+~#?&//=]" +
            "{2,256}\\.[a-z]" +
            "{2,6}\\b([-a-zA-Z0-9@:%" +
            "._\\+~#?&//=]*)")

    p = re.compile(regex)
    if (str == None):
        return False
 
    if(re.search(p, str)):
        return True
    else:
        return False


def generate_html(url, method):
    if method == 'basic':
        factory = qrcode.image.svg.SvgImage
    elif method == 'fragment':
        factory = qrcode.image.svg.SvgFragmentImage
    elif method == 'path':
        factory = qrcode.image.svg.SvgPathImage

    img = qrcode.make(url, image_factory = factory, version=10)

    img.save("tmp.svg")

    with open("qrcode.html", "w+") as f:
        with open("tmp.svg", "r") as s:
            f.write('<!DOCTYPE html> <html lang=\"en\"> <head> <meta charset=\"UTF-8\"> <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\"> <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"> <link href=\"https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css\" rel=\"stylesheet\"> <script src=\"https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js\"></script> <script src=\"https://code.jquery.com/jquery-3.5.0.js\"></script> <title>qrcode</title> </head> <body> <div class=\"card\"> <div class=\"text-center\"> <div class=\"d-flex flex-row text-center\"> <div class=\"d-flex flex-column ml-1\">'+ str(s.read()) +'</div> </div> </div> <hr class=\"line\"> <span class=\"text-secondary\">QRCode Generator developed by <a href=\"https://www.patreon.com/DoktorSAS\">DoktorSAS</a></span> </div> </body> </html> <style> body { background-color: #F0EDE5; height: 100vh; display: flex; justify-content: center; align-items: center } .card { align-items: center; width: 300px; border: none; height: 350px; border-radius: 15px; padding: 20px; background-color: #fff } .percent { font-size: 56px; color: #fff } .discount { font-size: 27px; color: #fff } .line { color: #fff } .form-check-input:checked { background-color: #F44336; border-color: #F44336 } .form-check-input:focus { border-color: #d50000; outline: 0; box-shadow: none } .form-check { display: block; min-height: 1.5rem; padding-left: 1.75em; margin-bottom: -5px } </style>')
    os.remove("tmp.svg")

def generate_svg(url, method):

    if method == 'basic':
        factory = qrcode.image.svg.SvgImage
    elif method == 'fragment':
        factory = qrcode.image.svg.SvgFragmentImage
    elif method == 'path':
        factory = qrcode.image.svg.SvgPathImage

    img = qrcode.make(url, image_factory = factory, version=10)

    img.save("qrcode.svg")
    
def generate_png(url):
    img = qrcode.make(url)
    img.save("qrcode.png", version=10)

def generate_jpg(url):
    img = qrcode.make(url)
    img.save("qrcode.jpg", version=10)

class funcs:

    def generate(self, url):
        print(url)
        if validate_url( url ):
            print("Start!")
            if ( not is_hex_color(self.ui.bgcolor.get()) or not is_color(self.ui.bgcolor.get()) ):
                self.ui.set_issue_text("Invalid bg color")
            if ( not is_hex_color(self.ui.fgcolor.get()) or not is_color(self.ui.fgcolor.get()) ):
                self.ui.set_issue_text("Invalid fg color")
            else:
                if(self.ui.svg_type.get() == 1):
                    generate_svg(url, "basic")
                if(self.ui.png_type.get() == 1):
                    print("Generating png")
                if(self.ui.jpg_type.get() == 1):
                    print("Generating jpg")
                if(self.ui.html_type.get() == 1):
                    generate_html(url, "basic")
        else:
            self.ui.set_issue_text("Invalid URL")
            


            
            


    def __init__(self, view):
        super().__init__()
        self.ui = view
    