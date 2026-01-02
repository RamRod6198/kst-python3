#!/usr/bin/env python3

# demonstrate buttons and line inputs:
# plot an equation the user inputs

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

class KsNspire:
  text=""
  def __init__(self,client):
    self.client=client
    self.s=QtNetwork.QLocalSocket()
    self.s.readyRead.connect(self.create)
    self.s2=QtNetwork.QLocalSocket()
    self.s2.readyRead.connect(self.changeValue)
    self.l=kst.LineEdit(client,"",self.s2,0.47,0.975,0.93,0.025)
    self.b=kst.Button(client,"Go!",self.s,0.97,0.975,0.05,0.025)
    self.plot=client.new_plot((0.5,0.4885),(0.9,0.8))
    self.genVec=client.new_generated_vector(-100,100,1000)
    
  def create(self):
    eq = self.client.new_equation(self.genVec, self.text)
    c = self.client.new_curve(eq.x(), eq.y())
    self.plot.add(c)

  def changeValue(self):
    data = self.s2.read(8000)
    strx = bytes(data).decode('utf-8')
    if "valueSet:" in strx:
      strx = strx.replace("valueSet:", "")
      self.text = strx

client=kst.Client()
app=QApplication(sys.argv)
m=KsNspire(client)

app.exec_()
