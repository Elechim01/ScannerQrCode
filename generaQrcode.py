# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
" generazione qrcode"
import pyqrcode
import png
from pyqrcode import QRCode 
QRstr = "https://www.google.it/"
url = pyqrcode.create(QRstr)
"url.png('/Users/michelemanniello/Desktop/qr.png',scale = 8)"

