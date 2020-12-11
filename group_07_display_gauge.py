from tkinter import *
from tkinter import ttk
from tkinter import DoubleVar
from tkinter.ttk import *
from tkinter import messagebox
from group_07_showBar import ShowBar
from group_07_showGauge import ShowGauge
from functools import partial

class displayGauge(Frame):
    def __init__(self,canvas,canvasCol,canvasRow,canColSpan,canRowSpan):
        super().__init__()
        self.max_temperature=60
        self.min_temperature=-20
        self.initUI(canvas,canvasCol,canvasRow,canColSpan,canRowSpan)
        self.timeStamp=""
        self.fillColor='#f11'
    
    def initUI(self,canvas,canvasCol,canvasRow,canColSpan,canRowSpan):
        self.canvas=canvas
        self.canvas.grid(column=canvasCol,row=canvasRow,columnspan=canColSpan,rowspan=canRowSpan)

    def displayValue(self,inputValue):

        self.canvas.delete("all")
        self.canvas.create_text(100,10,fill="black",
                        text=f"Value obtained: {inputValue}")
        self.canvas.create_text(400,10,fill="black",
                        text=f"Data TimeStamp {self.timeStamp}")
        ShowBar(inputValue,self.canvas,self.fillColor)
        ShowGauge(inputValue,self.canvas,self.fillColor)
        self.canvas.update()

    def setTimeStamp(self,timeStamp):
        self.timeStamp=timeStamp

    def setFillColor(self,fillColorCode):
        self.fillColor=fillColorCode
        