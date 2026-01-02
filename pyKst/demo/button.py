#!/usr/bin/env python3

# pressing a button makes random circles appear.

import sys

try:
    import pykst as kst
except ImportError:
    import os
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    import pykst as kst
import random
from PyQt5 import QtCore, QtNetwork
from PyQt5.QtWidgets import QApplication

class Magic:
  def __init__(self,client):
    self.client=client
  def test(self):
    self.client.new_circle((random.random(),random.random()), random.random()/10.0,
                      "#"+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9)))
                      
client=kst.Client("testbutton")
app=QApplication(sys.argv)
m=Magic(client)

s=QtNetwork.QLocalSocket()
s.readyRead.connect(m.test)
b=kst.Button(client,"Click Here",s,0.5,0.5,0.2,0.1)
app.exec_()
