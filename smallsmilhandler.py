#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILHandler(ContentHandler):

    def __init__ (self):
        self.width = ""
        self.height = ""
        self.backgroundcolor = ""
        self.id = ""
        self.top = ""
        self.bottom = ""
        self.left = ""
        self.right = ""
        self.src = ""
        self.region = ""
        self.begin = ""
        self.dur = ""
        self.lista = []
        self.atributos = {}

    def startElement(self, name, attrs):
        if name == 'root-layout':
            self.width = attrs.get('width',"")
            self.height = attrs.get('height',"")
            self.backgroundcolor = attrs.get('background-color',"")
            
            self.atributos['width'] = self.width
            self.atributos['height'] = self.height
            self.atributos['background-color'] = self.backgroundcolor
            self.lista.append(self.atributos)
            self.atributos = {}
        
        elif name == 'region':
            self.id = attrs.get('id',"")
            self.top = attrs.get('top',"")
            self.bottom = attrs.get('bottom',"")
            self.left = attrs.get('left',"")
            self.right = attrs.get('right',"")
            
            self.atributos['id'] = self.id
            self.atributos['top'] = self.top
            self.atributos['bottom'] = self.bottom
            self.atributos['left'] = self.left
            self.atributos['right'] = self.right
            self.lista.append(self.atributos)
            self.atributos = {}
            
        elif name == 'img':
            self.src = attrs.get('src',"")
            self.region = attrs.get('region',"")
            self.begin = attrs.get('begin',"")
            self.dur = attrs.get('dur',"")
            
            self.atributos['src'] = self.src
            self.atributos['region'] = self.region
            self.atributos['begin'] = self.begin
            self.atributos['dur'] = self.dur
            self.lista.append(self.atributos)
            self.atributos = {}
            
        elif name == 'audio':
            self.src = attrs.get('src',"")
            self.begin = attrs.get('begin',"")
            self.dur = attrs.get('dur',"")
            
            self.atributos['src'] = self.src
            self.atributos['begin'] = self.begin
            self.atributos['dur'] = self.dur
            self.lista.append(self.atributos)
            self.atributos = {}
            
        elif name == 'textstream':
            self.src = attrs.get('src',"")
            self.region = attrs.get('region',"")
            
            self.atributos['src'] = self.src
            self.atributos['region'] = self.region
            self.lista.append(self.atributos)
            self.atributos = {}
        
        #self.etiquetas.append(name)
        
        

    def get_tags(self):
        return self.lista
            
if __name__ == "__main__":
    parser = make_parser()
    Handler = SmallSMILHandler()
    parser.setContentHandler(Handler)
    parser.parse(open('karaoke.smil'))
    print(Handler.get_tags())
