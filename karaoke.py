#!/usr/bin/python3
# -*- encoding: utf-8 -*-

from xml.sax.handler import ContentHandler
from xml.sax import make_parser
from smallsmilhandler import SmallSMILHandler
import sys
import json
import urllib


class KaraokeLocal():
    def __init__(self, fichero):
        parser = make_parser()
        sHandler = SmallSMILHandler()
        parser.setContentHandler(sHandler)
        parser.parse(open(ficherosmil))
        # obtengo las etiquetas del anterior ejercicio
        self.mi_lista = sHandler.get_tags()

    def __str__(self):
        salida = ''
        for sublista in self.mi_lista:
            etiqueta = sublista[0]
            atributos = sublista[1]
            for valor in atributos:
                if atributos[valor] != '':  # los campos vacios no los quiero
                    etiqueta += '\t' + valor + '="' + atributos[valor] + '"'
            salida += etiqueta + '\n'
        return salida

    def to_json(self, fichero=''):
        if not fichero:
            fichero = 'local.json'
        else:
            fichero = fichero.split('.')[0] + '.json'

        json.dump(self.mi_lista, open(fichero, 'w'))

    def do_local(self):
        for sublista in self.mi_lista:
            atributos = sublista[1]
            for clave in atributos:
                if clave == 'src' and atributos[clave][:7] == 'http://':
                    # descargo el contenido de src y
                    # recorto el string por el final
                    urllib.request.urlretrieve(atributos[clave],
                                               atributos[clave].split('/')[-1])
                    atributos[clave] = atributos[clave].split('/')[-1]

if __name__ == "__main__":
    try:
        ficherosmil = sys.argv[1]
        lista = KaraokeLocal(ficherosmil)
        print(lista)
        lista.to_json(ficherosmil)
        lista.do_local()
        lista.to_json()
        print(lista)
    except IndexError:
        print("Usage: python3 karaoke.py file.smil")
