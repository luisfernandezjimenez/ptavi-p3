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
            self.atributos['width'] = attrs.get('width',"")
            self.atributos['height'] = attrs.get('height',"")
            self.atributos['background-color'] = attrs.get('background-color',"")
            self.atributos['etiqueta'] = name
            self.lista.append(self.atributos)
            self.atributos = {}
        
        elif name == 'region':
            self.atributos['id'] = attrs.get('id',"")
            self.atributos['top'] = attrs.get('top',"")
            self.atributos['bottom'] = attrs.get('bottom',"")
            self.atributos['left'] = attrs.get('left',"")
            self.atributos['right'] = attrs.get('right',"")
            self.atributos['etiqueta'] = name
            self.lista.append(self.atributos)
            self.atributos = {}
            
        elif name == 'img':
            self.atributos['src'] = attrs.get('src',"")
            self.atributos['region'] = attrs.get('region',"")
            self.atributos['begin'] = attrs.get('begin',"")
            self.atributos['dur'] = attrs.get('dur',"")
            self.atributos['etiqueta'] = name
            self.lista.append(self.atributos)
            self.atributos = {}
            
        elif name == 'audio':
            self.atributos['src'] = attrs.get('src',"")
            self.atributos['begin'] = attrs.get('begin',"")
            self.atributos['dur'] = attrs.get('dur',"")
            self.atributos['etiqueta'] = name
            self.lista.append(self.atributos)
            self.atributos = {}
            
        elif name == 'textstream':
            self.atributos['src'] = attrs.get('src',"")
            self.atributos['region'] = attrs.get('region',"")
            self.atributos['etiqueta'] = name
            self.lista.append(self.atributos)
            self.atributos = {}

    def get_tags(self):
        return self.lista
            
if __name__ == "__main__":
    parser = make_parser()
    Handler = SmallSMILHandler()
    parser.setContentHandler(Handler)
    parser.parse(open('karaoke.smil'))
    print(Handler.get_tags())
