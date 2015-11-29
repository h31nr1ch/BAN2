#!/usr/bin/python2.7
from __future__ import division
from PyQt4 import *
from imageEditor import *
from copy import *
from banco import *
import MySQLdb
import sys


"""
htmlPrefix = "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">"
htmlSuffix = "</p></body></html>"
"""

class gui(QtGui.QMainWindow, Ui_MainWindow,QtGui.QDialog,krl,passt):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self)

        self.setupUi(self)
	self.insert1.clicked.connect(self.insereModelos)
	self.insert2.clicked.connect(self.insereSindicatos)
	self.insert3.clicked.connect(self.insereTestes)
	self.insert4.clicked.connect(self.insereAvia)
	self.insert5.clicked.connect(self.insertFuncionario)
	self.insert6.clicked.connect(self.insertTecnicos)
	self.insert7.clicked.connect(self.insertControladores)
	self.insert8.clicked.connect(self.insertManutencao)
	self.insert9.clicked.connect(self.insertAfiliacao)
	self.insert10.clicked.connect(self.insertPericia)

    def insereModelos(self):
		tabelas='modelos'
		what='('+self.line1.text()+','+self.line2.text()+','+self.line3.text()+')'
		print what
		print tabelas
		self.insert(c,tabelas,what)
		#con.commit()
	
    def insereSindicatos(self):
		tabelas = 'sindicatos'
		what = '('+self.line4.text()+ ',' + self.line5.text()+')'
		self.insert(c,tabelas,what)
		con.commit()

    def insereTestes(self):
		tabelas = 'testes'
		what = '('+self.line6.text() + ',' + self.line7.text() + ',' + self.line8+')'
		self.insert(c,tabelas,what)
		con.commit()

    def insereAvia(self):
		tabelas = 'aviao' 
		what = '('+self.line9.text() + ',' + self.line10.text() +')'
		self.insert(c,tabelas,what)
		con.commit()


    def insertFuncionario(self):
		tabelas = 'funcionarios'
		what = '('+self.line11.text() + ',' + self.line12.text+')'
		self.insert(c,tabelas,what)
		con.commit()


    def insertTecnicos(self):
		tabelas = 'tecnicos'
		what = '('+self.line13.text() + ',' + self.line14.text() + ',' + self.line15.text() + ',' +self.line16.text()+')'
		self.insert(c,tabelas,what)
		con.commit()


    def insertControladores(self):
		tabelas = 'controladores'
		what = '('+self.line17.text() + ',' +self.line18.text()+')'
		self.insert(c,tabelas,what)
		con.commit()


    def insertManutencao(self):
		tabelas = 'manutencao'
		what = '('+self.line19.text() + ',' + self.line20.text() + ',' +self.line21.text() + ',' + self.line22.text() + ',' + self.line23.text() + ',' +self.line24.text()+')'
		self.insert(c,tabelas,what)
		con.commit()


    def insertAfiliacao(self): 
		tabelas = 'afiliacao'
		what = '('+self.line25.text() + ',' + self.line26.text() + ',' + self.line27.text()+')'
		self.insert(c,tabelas,what)
		con.commit()


    def insertPericia(self):
		tabelas = 'pericia'
		what = '('+self.line28.text()+ ',' +self.line29.text()+')'
		self.insert(c,tabelas,what)
		con.commit()


"""
    def setSecondaryBar(self):
        try:
            value = int(self.SecondaryValue.text())
        except ValueError:
            diag = dialogBox()
            diag.text.setHtml(htmlPrefix + 'Valor Invalido' + htmlSuffix)
            diag.exec_()
            self.SecondaryValue.setText(str(self.lastSecondaryValue))
            return
        if value > 255:
            diag = dialogBox()
            diag.text.setHtml(htmlPrefix + 'O valor dos limites precisa estar\nentre 0 e 255' + htmlSuffix)
            diag.exec_()
            self.SecondaryValue.setText(str(self.lastSecondaryValue))
            return
        self.scribbler.secondThresh = value
        self.SecondaryBar.setSliderPosition(value)
        self.lastSecondaryValue = value

    def secondThresholdToggle(self):
        self.scribbler.secondToggle = not self.scribbler.secondToggle
"""



class dialogBox(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setAttribute(QtCore.Qt.WA_StaticContents)
        self.setGeometry(500,500,450,250)
        self.text = QtGui.QTextEdit(self)
        self.text.setGeometry(QtCore.QRect(10, 10, 431, 171))
        self.text.setReadOnly(True)
        self.ok = QtGui.QPushButton(self)
        self.ok.setGeometry(QtCore.QRect(170, 190, 98, 27))
        self.ok.setText("OK")
        QtCore.QObject.connect(self.ok, QtCore.SIGNAL(("clicked()")), self.close)
