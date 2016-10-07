#!/usr/bin/python3
# -*- encoding: utf-8 -*-

from xml.sax.handler import ContentHandler
from xml.sax import make_parser
from smallsmilhandler import SmallSMILHandler
import sys


if __name__ == "__main__":
    try:
        ficherosmil = sys.argv[1]
        parser = make_parser()
        sHandler = SmallSMILHandler()
        parser.setContentHandler(sHandler)
        parser.parse(open(ficherosmil))
        #obtengo las etiquetas del anterior ejercicio
        mis_etiquetas = sHandler.get_tags()
   
        salida = "" 
        for elemento in mis_etiquetas:
            etiqueta = elemento[0]
            atributos = elemento[1]
            mis_atributos = ""
            
            #devuelvo la lista de claves del diccionario
            for atributo in atributos:
                mis_atributos = mis_atributos + '\t' + atributo + '="' + atributos[atributo] + '"'
            
            salida += etiqueta + mis_atributos + "\n"

        print(salida)
    except IndexError:
        print("Usage: python3 karaoke.py file.smil")
        

