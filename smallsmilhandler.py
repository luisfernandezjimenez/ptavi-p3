#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):
    def __init__(self):
        self.root = ['width', 'height', 'background-color']
        self.region = ['id', 'top', 'bottom', 'left', 'right']
        self.img = ['src', 'region', 'begin', 'dur']
        self.audio = ['src', 'begin', 'dur']
        self.text = ['src', 'region']

        self.etiquetas = {'root-layout': self.root, 'region': self.region,
                          'img': self.img, 'audio': self.audio,
                          'textstream': self.text}
        self.lista = []

    def startElement(self, name, attrs):
        if name in self.etiquetas:
            self.dicc = {}
            for atributo in self.etiquetas[name]:
                self.dicc[atributo] = attrs.get(atributo, "")
            self.lista.append(name)
            self.lista.append(self.dicc)

    def get_tags(self):
        return self.lista

if __name__ == "__main__":
    parser = make_parser()
    Handler = SmallSMILHandler()
    parser.setContentHandler(Handler)
    parser.parse(open('karaoke.smil'))
    print(Handler.get_tags())
