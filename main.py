import tkinter
import tkinter.filedialog
from tkinter import messagebox
import math
import random
import string
import numpy as np
from os import listdir
from os.path import isfile, join
import numpy
from array import array
from numpy import linalg as LA
import time
from tkinter import filedialog
import tkinter.messagebox
from PyQt4 import QtCore, QtGui
import pickle
import itertools
import numpy as np
import numpy as np
import numpy
import os
from os import listdir
from os.path import isfile, join

visualise = 1
import numpy as np
import argparse
import imutils
import time
from time import sleep
import sys
from time import sleep
import numpy as np
import urllib.request as urllib2, json
import cv2
from scipy import stats

confidence_TH = 0.5
threshold_TH = 0.1
labelsPath = os.path.sep.join(['YOLO', "YOLO.names"])
LABELS = open(labelsPath).read().strip().split("\n")
np.random.seed(42)
COLORS = np.random.randint(0, 255, size=(len(LABELS), 3), dtype="uint8")
weightsPath = os.path.sep.join(['YOLO', "YOLO.weights"])
configPath = os.path.sep.join(['YOLO', "YOLO.cfg"])
print("loading Model")
net = cv2.dnn.readNetFromDarknet(configPath, weightsPath)
ln = net.getLayerNames()
ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]

global VidRes

root = tkinter.Tk()
print('******Start*****')
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_MainWindow1(object):
    def __init__(self):
        VidRes = [];

    def setupUii(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1200, 800)
        MainWindow.setStyleSheet(_fromUtf8("background-image: url(bg1.jpg)"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(750, 180, 111, 27))
        self.pushButton.clicked.connect(self.quit)
        self.pushButton.setStyleSheet(_fromUtf8("background-color: rgb(255,0, 0);\n"
                                                "color: rgb(0, 0, 0);"))

        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        #################################################################

        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(550, 180, 131, 27))
        self.pushButton_2.clicked.connect(self.show1)
        self.pushButton_2.setStyleSheet(_fromUtf8("background-color: rgb(255, 128, 0);\n"
                                                  "color: rgb(0, 0, 0);"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(550, 220, 131, 27))
        self.pushButton_4.clicked.connect(self.show2)
        self.pushButton_4.setStyleSheet(_fromUtf8("background-color: rgb(255, 128, 0);\n"
                                                  "color: rgb(0, 0, 0);"))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))

        ##        self.pushButton_5 = QtGui.QPushButton(self.centralwidget)
        ##        self.pushButton_5.setGeometry(QtCore.QRect(550, 260, 131, 27))
        ##        self.pushButton_5.clicked.connect(self.show3)
        ##        self.pushButton_5.setStyleSheet(_fromUtf8("background-color: rgb(255, 128, 0);\n"
        ##"color: rgb(0, 0, 0);"))
        ##        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "VIDEO TAGGINGING", None))
        self.pushButton_2.setText(_translate("MainWindow", "BROWSE VIDEO", None))
        self.pushButton_4.setText(_translate("MainWindow", "DOWNLOAD TAG", None))
        # self.pushButton_5.setText(_translate("MainWindow", "ACCURACY", None))
        self.pushButton.setText(_translate("MainWindow", "Exit", None))

    def quit(self):
        print('Process end')
        print('******End******')
        quit()

    def show1(self):
        print('EMPTY')
        # Code Start
        from tkinter.filedialog import askopenfilename
        filename = askopenfilename()
        FNum = 0;
        vs = cv2.VideoCapture(filename)
        Timesinsec = 0
        VidRes = [];
        while True:
            (grabbed, frame) = vs.read()
            FNum = FNum + 1

            (H, W) = frame.shape[:2]
            blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (416, 416),
                                         swapRB=True, crop=False)
            net.setInput(blob)
            start = time.time()
            layerOutputs = net.forward(ln)
            end = time.time()
            boxes = []
            confidences = []
            classIDs = []
            for output in layerOutputs:
                for detection in output:
                    scores = detection[5:]
                    classID = np.argmax(scores)
                    confidence = scores[classID]
                    if confidence > confidence_TH:
                        box = detection[0:4] * np.array([W, H, W, H])
                        (centerX, centerY, width, height) = box.astype("int")
                        x = int(centerX - (width / 2))
                        y = int(centerY - (height / 2))
                        boxes.append([x, y, int(width), int(height)])
                        confidences.append(float(confidence))
                        classIDs.append(classID)
            idxs = cv2.dnn.NMSBoxes(boxes, confidences, confidence_TH, threshold_TH)
            substrings = [];
            RES_25 = []
            if len(idxs) > 0:
                for i in idxs.flatten():
                    (x, y) = (boxes[i][0], boxes[i][1])
                    (w, h) = (boxes[i][2], boxes[i][3])
                    color = [int(c) for c in COLORS[classIDs[i]]]
                    cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
                    text = "{}".format(LABELS[classIDs[i]])
                    substrings.append(text)
                    # print(text,type(text))
                    cv2.putText(frame, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
                TT = frame
                # cv2.waitKey(1000);cv2.destroyAllWindows()
                # print(substrings,len(substrings),type(substrings))
                # print('----------Recognizing Environment--------------\n')
                # Recognizing Environment
                # Checking for office
                results = [];
                TF = 0;
                FF = 0
                a_string = ['chair', 'mouse', 'laptop']
                for substring in substrings:
                    results.append(substring in a_string)
                    output = any(results)
                    if output:
                        TF = TF + 1
                    else:
                        FF = FF + 1
                OFC = int((TF / (TF + FF)) * 100)

                # Checking for Road Traffic
                results = [];
                TF = 0;
                FF = 0
                a_string = ['car', 'bike', 'bicycle']
                for substring in substrings:
                    results.append(substring in a_string)
                    output = any(results)
                    if output:
                        TF = TF + 1
                    else:
                        FF = FF + 1
                ROD = int((TF / (TF + FF)) * 100)

                # Checking for RAILWAY STATION
                results = [];
                TF = 0;
                FF = 0
                a_string = ['train']
                for substring in substrings:
                    results.append(substring in a_string)
                    output = any(results)
                    if output:
                        TF = TF + 1
                    else:
                        FF = FF + 1
                RLWSTN = int((TF / (TF + FF)) * 100)

                # Checking for RAILWAY STATION
                results = [];
                TF = 0;
                FF = 0
                a_string = ['horse']
                for substring in substrings:
                    results.append(substring in a_string)
                    output = any(results)
                    if output:
                        TF = TF + 1
                    else:
                        FF = FF + 1
                HORSERID = int((TF / (TF + FF)) * 100)

                # Checking for Fruit
                results = [];
                TF = 0;
                FF = 0
                a_string = ['apple', 'banana', 'orange']
                for substring in substrings:
                    results.append(substring in a_string)
                    output = any(results)
                    if output:
                        TF = TF + 1
                    else:
                        FF = FF + 1
                FRTMRKT = int((TF / (TF + FF)) * 100)

                # Checking for Fruit
                results = [];
                TF = 0;
                FF = 0
                a_string = ['bat']
                for substring in substrings:
                    results.append(substring in a_string)
                    output = any(results)
                    if output:
                        TF = TF + 1
                    else:
                        FF = FF + 1
                CRKT = int((TF / (TF + FF)) * 100)

                TFPrb = [OFC, ROD, RLWSTN, HORSERID, FRTMRKT]

                if int(np.max(TFPrb)) >= 50:
                    IND = int(np.argmax(TFPrb))
                    RES_25.append(IND)
                else:
                    FINALRES = 'UNKNOWN'

                if IND == 0:
                    VidRes.append('OFFICE')
                elif IND == 1:
                    VidRes.append('ROAD')
                elif IND == 2:
                    VidRes.append('RAILWAY_STATION')
                elif IND == 3:
                    VidRes.append('HORSE_RIDING')
                elif IND == 4:
                    VidRes.append('FRUIT_MARKET')
                elif IND == 5:
                    VidRes.append('CRICKET')

            else:
                FINALRES = 'UNKNOWN'

            if (FNum % (25)) == 0:
                print('----------Recognizing Environment Per Sec Duration--------------\n')
                Timesinsec = Timesinsec + 1
                INDs = stats.mode(RES_25)
                INDs = int(INDs[0])
                # print(INDs)

                if INDs == 0:
                    FINALRES = 'Interval' + str(Timesinsec) + ' second Is OFFICE\n'
                    # messagebox.showinfo("CLASS", "OFFICE")
                elif INDs == 1:
                    FINALRES = 'Interval ' + str(Timesinsec) + ' second Is ROAD\n'
                    # messagebox.showinfo("CLASS", "ROAD")
                elif INDs == 2:
                    FINALRES = 'Interval ' + str(Timesinsec) + ' second Is RAILWAY STATION\n'
                    # messagebox.showinfo("CLASS", "RAILWAY STATION")
                elif INDs == 3:
                    FINALRES = 'Interval ' + str(Timesinsec) + ' second Is HORSE RIDING \n'
                    # messagebox.showinfo("CLASS", "HORSE RIDING")
                elif INDs == 4:
                    FINALRES = 'Interval ' + str(Timesinsec) + ' second Is FRUIT MARKET \n'
                    # messagebox.showinfo("CLASS", "FRUIT MARKET")
                elif INDs == 5:
                    FINALRES = 'Interval ' + str(Timesinsec) + ' second Is CRICKET MATCH \n'
                    # messagebox.showinfo("CLASS", "CRICKET")
                RES_25 = []
                print(FINALRES, '\n')
                print('----------------------------------------------------------\n')

            cv2.imshow('IMAGE', frame);
            cv2.waitKey(1000);
            cv2.destroyAllWindows()
            frame = [];
        print('Total frame wise Results\n')
        print(VidRes)
        oi = 0
        # for mi in VidRes:
        #   oi=oi+1
        #  print('Object found in Frame is: ',substrings,'\n')
        # print('Frame ', oi ,'Contain',mi,'\n')

        substrings = []
        # End of code

    def show2(self):
        for mi in VidRes:
            oi = oi + 1
            print('Object found in Frame is: ', substrings, '\n')
            print('Frame ', oi, 'Contain', mi, '\n')

    def show3(self):
        print('EMPTY')


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow1()
    ui.setupUii(MainWindow)
    MainWindow.move(550, 170)
    MainWindow.show()
    sys.exit(app.exec_())

