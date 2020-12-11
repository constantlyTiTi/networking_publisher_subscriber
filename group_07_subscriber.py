# Wk12a_subscriber.py
# This file will have the following:
# 1.	Create a client.
# 2.	Assign the on_messege delegate to the function in Step 7.
# 3.	Connect to the server.
# 4.	Subscribe to the required topic.
# 5.	Print a message.
# 6.	Invoke the client loop_forever() method.
# 7.	Create a function to do the following: (see signature in text or ppt slide)
# o	Decode the message.
# o	Convert the decoded string to a dict. Use the json.loads() function.
# o	Call the function in the first file to print the dictionary.

import paho.mqtt.client as mqtt
import json
from group_07_dynamic_chart import DynamicChart
from tkinter import Tk, Canvas, Frame, BOTH, W
from tkinter import ttk
from tkinter import *
import collections
from group_07_display_gauge import displayGauge

class subscriber():
    def __init__(self,topic,canvas,canvasCol,canvasRow,canColSpan,canRowSpan,maxTem,minTemp):
        super().__init__()
        self.dynamicChart=DynamicChart(canvas,canvasCol,canvasRow,canColSpan,canRowSpan,maxTem,minTemp)
        self.displayGauge=displayGauge(canvas,canvasCol,canvasRow,canColSpan,canRowSpan)
        self.topic=topic
# 7.	Create a function to do the following: (see signature in text or ppt slide)
    def setTopic(self,topic):
        self.topic=topic
    
    def connectSubscriber(self):
        # 1.	Create a client.
        self.client = mqtt.Client()

        # 2.	Assign the on_messege delegate to the function in Step 7.
        self.client.on_message = lambda client, userdata, msg: self.on_message(client, userdata, msg)

        # 3.	Connect to the server.
        self.client.connect('localhost', 1883)

        # 4.	Subscribe to the required topic.
        self.client.subscribe(self.topic)

        # 5.	Print a message.
        print('Message received')

        # 6.	Invoke the client loop_forever() method.
        # while True:
        self.client.loop_start()

    def drawGraph(self,obj):
        if obj['GeneratedData']>21 or obj['GeneratedData']<18:
            self.dynamicChart.setFillColor('#FFFF00')
            self.displayGauge.setFillColor('#FFFF00')
        else:
            self.dynamicChart.setFillColor('#90D695')
            self.displayGauge.setFillColor('#f11')

        if self.topic=='Dynamic Chart':
            self.dynamicChart.dataGenerate(10, obj['GeneratedData'])
            self.dynamicChart.drawGraph()
            self.dynamicChart.setTimeStamp(obj["TimeStamp"])
        else:
            self.displayGauge.displayValue(obj['GeneratedData'])
            self.displayGauge.setTimeStamp(obj["TimeStamp"])
            

    def on_message(self, client, userdata,message):
        print('Subscriber connecting')
        # Decode the message.
        data = message.payload.decode('utf-8')
        #Convert the decoded string to a dict. Use the json.loads() function.
        obj = json.loads(data)
        
        print(obj['GeneratedData'])
        self.drawGraph(obj)

# root=Tk()
# root.title('Subscriber')
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
# ex=subscriber('topic01', canvas,canvasCol,canvasRow,canColSpan,canRowSpan)
# ex.connectSubscriber()

# root.mainloop()

