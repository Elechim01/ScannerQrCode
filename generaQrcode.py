# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
"""
from covid  import Covid
covid = Covid()
print(covid.get_total_active_cases())
print(covid.get_total_deaths())
print(covid.get_total_confirmed_cases())

import socket 
hostin = socket.gethostname()
IPAd = socket.gethostbyname(hostin)
print("IP ADDRESs IS "+ IPAd)
"""
" generazione qrcode"
import pyqrcode
import png
from pyqrcode import QRCode 
QRstr = "https://www.google.it/"
url = pyqrcode.create(QRstr)
"url.png('/Users/michelemanniello/Desktop/qr.png',scale = 8)"

