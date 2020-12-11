
import paho.mqtt.client as mqtt
import paho
import json
import time
import collections,random
from random import randrange
from group_07_dynamic_chart import DynamicChart
from group_07_display_gauge import displayGauge
from group_07_data_generator import mimicData

from tkinter import Tk, Canvas, Frame, BOTH, W
from tkinter import ttk
from tkinter import *

class publisher():
    def __init__(self,client_id,topic,canvas,canvasCol,canvasRow,canColSpan,canRowSpan,maxTem,minTemp):
        self.client = mqtt.Client(client_id=client_id, clean_session=True, userdata=None, protocol=mqtt.MQTTv31, transport="tcp")
        self.generatedData=0
        self.dynamicChart=DynamicChart(canvas,canvasCol,canvasRow,canColSpan,canRowSpan,maxTem,minTemp)
        self.topic=topic
        self.currentTopic=topic
        self.canvas=canvas
        self.singleData=mimicData(maxTem,minTemp)
        self.displayGauge=displayGauge(canvas,canvasCol,canvasRow,canColSpan,canRowSpan)
        self.goodDataCount=0
        self.corrputDataCount=0
        self.missTransmissionDetermineNum=0

    def setTopic(self,topic):
        self.currentTopic=topic
    
    def generateData(self,maxContinueGoodDataNumber):
        # determine if corrupt data will be generated
        if self.goodDataCount<maxContinueGoodDataNumber:
            self.generatedData=self.singleData.singleDataGenerater()
            self.goodDataCount+=1
        else:
            self.generatedData=self.singleData.singleDataGenerater()
            if self.generatedData>19.5:
               self.generatedData+=random.choice([-3.5,2])
            else:
                self.generatedData+=random.choice([-1,4])
            self.goodDataCount=0
            self.corrputDataCount+=1

        if self.topic=='Dynamic Chart':
            self.dynamicChart.dataGenerate(10,self.generatedData)
        else:
            time.sleep(0.5)



    def drawGraph(self,obj):
        if self.topic=='Dynamic Chart':
            self.dynamicChart.drawGraph()
            self.dynamicChart.setTimeStamp(obj["TimeStamp"])
        else:
            self.displayGauge.displayValue(self.generatedData)
            self.displayGauge.setTimeStamp(obj["TimeStamp"])
    
    # def getCorruptDataCount(self):
    #     return self.corrputDataCount
        
    def connectPublisher(self,maxContinueGoodDataNumber):
        systemTime=""

        while(True):
            if self.currentTopic != self.topic:
                self.currentTopic = self.topic
                break

            self.missTransmissionDetermineNum=randrange(100)
            self.generateData(maxContinueGoodDataNumber)
            print(self.generatedData)

            systemTime=time.asctime()
            self.dynamicChart.setTimeStamp(systemTime)

            data={'TimeStamp':systemTime,
            'GeneratedData':self.generatedData}
        # The possibility of miss transmission will be 3%
            if self.missTransmissionDetermineNum!=1 and self.missTransmissionDetermineNum!=2 and self.missTransmissionDetermineNum!=3:
                self.client.connect('localhost', 1883) 
                self.client.publish(self.topic, json.dumps(data))
                self.client.disconnect()
                self.dynamicChart.setFillColor('#90D695')
            else:
                self.dynamicChart.setFillColor('#808080')
                self.displayGauge.setFillColor('#808080')
            self.drawGraph(data)
            time.sleep(0.5)
        # for better testing experience, data including miss transmission data will be draw in publisher
            # self.drawGraph(data)


# root=Tk()
# root.title('Publisher')
# root.geometry('550x400')
# frame = ttk.Frame(
#         root,
#         width=500,
#         height=400)
# frame.pack()
# canvas=Canvas(frame,width=500,height=300)
# canvasCol=0
# canvasRow=4
# canColSpan=3
# canRowSpan=5
# ex=publisher('topic01', canvas,canvasCol,canvasRow,canColSpan,canRowSpan)
# ex.connectPublisher()


# root.mainloop()