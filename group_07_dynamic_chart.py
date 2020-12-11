from tkinter import Tk, Canvas, Frame, BOTH, W
from tkinter import ttk
from tkinter import *
import random
import collections,threading,time
from group_07_data_generator import mimicData

class DynamicChart(Frame):
    def __init__(self,canvas,canvasCol,canvasRow,canColSpan,canRowSpan,maxTemp,minTemp):
        super().__init__()
        self.initUI(canvas,canvasCol,canvasRow,canColSpan,canRowSpan,maxTemp,minTemp)
    
    def initUI(self,canvas,canvasCol,canvasRow,canColSpan,canRowSpan,maxTemp,minTemp):
        self.count_addData=0
        self.count_readData=0
        self.recIncreaseUnit=50
        self.rect_horizon_x_unit=30
        self.rect_horizon_x_gap=10
        self.rect_start_x_start=70
        self.rect_start_y_start=400
        self.rect_start_x=self.rect_start_x_start
        self.rect_start_y=self.rect_start_y_start
        self.fillColor='#90D695'

        self.maxTempGraph=maxTemp+2
        self.minTempGraph=minTemp-2
        self.data_minTemp=minTemp
        self.data_maxTemp=maxTemp
        self.timeStamp=""
        
        self.data=collections.deque()
        self.canvas=canvas

        self.canvas.grid(column=canvasCol,row=canvasRow,columnspan=canColSpan,rowspan=canRowSpan)
    
    def setTimeStamp(self,timeStamp):
        self.timeStamp=timeStamp
        
    def setFillColor(self,fillColorCode):
        self.fillColor=fillColorCode
    
    def drawColumnAndLine(self,data):
        self.canvas.delete('all')
        num=data.popleft()
        lineStartPoint_x=self.rect_start_x
        lineStartPoint_y=self.rect_start_y-(num-self.minTempGraph)*self.recIncreaseUnit
        data.appendleft(num)
        self.canvas.create_text(100,self.rect_start_y_start-(self.maxTempGraph-self.minTempGraph)*self.recIncreaseUnit-20,fill="black",
                        text=f"Random Temperature {self.data_minTemp} - {self.data_maxTemp}")
        self.canvas.create_text(400,self.rect_start_y_start-(self.maxTempGraph-self.minTempGraph)*self.recIncreaseUnit-20,fill="black",
                        text=f"Data TimeStamp {self.timeStamp}")

        # draw y-axis
        self.canvas.create_line(self.rect_start_x_start-5, self.rect_start_y_start,     #start x,y
                self.rect_start_x_start-5, self.rect_start_y_start-(self.maxTempGraph-self.minTempGraph)*self.recIncreaseUnit)  
            # graph min range
        self.canvas.create_line(self.rect_start_x_start-5, self.rect_start_y_start,     #start x,y
                self.rect_start_x_start-10, self.rect_start_y_start)                       #end x,y

        self.canvas.create_text(self.rect_start_x_start-40, self.rect_start_y_start, 
                anchor=W, font='Purisa',  text=self.minTempGraph)
            # data min range
        self.canvas.create_line(self.rect_start_x_start-5, self.rect_start_y_start-(self.data_minTemp-self.minTempGraph)*self.recIncreaseUnit,     #start x,y
                self.rect_start_x_start-10, self.rect_start_y_start-(self.data_minTemp-self.minTempGraph)*self.recIncreaseUnit)                       #end x,y

        self.canvas.create_text(self.rect_start_x_start-40, self.rect_start_y_start-(self.data_minTemp-self.minTempGraph)*self.recIncreaseUnit, 
                anchor=W, font='Purisa',  text=self.data_minTemp)
            # graph max range
        self.canvas.create_line(self.rect_start_x_start-5, self.rect_start_y_start-(self.maxTempGraph-self.minTempGraph)*self.recIncreaseUnit,     #start x,y
                self.rect_start_x_start-10, self.rect_start_y_start-(self.maxTempGraph-self.minTempGraph)*self.recIncreaseUnit)                       #end x,y

        self.canvas.create_text(self.rect_start_x_start-40, self.rect_start_y_start-(self.maxTempGraph-self.minTempGraph)*self.recIncreaseUnit, 
                anchor=W, font='Purisa',  text=self.maxTempGraph)
            # data max range
        self.canvas.create_line(self.rect_start_x_start-5, self.rect_start_y_start-(self.data_maxTemp-self.minTempGraph)*self.recIncreaseUnit,     #start x,y
                self.rect_start_x_start-10, self.rect_start_y_start-(self.data_maxTemp-self.minTempGraph)*self.recIncreaseUnit)                       #end x,y

        self.canvas.create_text(self.rect_start_x_start-40, self.rect_start_y_start-(self.data_maxTemp-self.minTempGraph)*self.recIncreaseUnit, 
                anchor=W, font='Purisa',  text=self.data_maxTemp)

# draw bar and lines
        for num in data:
            self.canvas.create_rectangle(self.rect_start_x+self.rect_horizon_x_unit, self.rect_start_y-(num-self.minTempGraph)*self.recIncreaseUnit,    #top left
            self.rect_start_x, self.rect_start_y,                      #bottom right
            outline='#618963',fill=self.fillColor)

            if self.count_readData!=range:
                self.canvas.create_line(self.rect_start_x+self.rect_horizon_x_unit-15, self.rect_start_y-(num-self.minTempGraph)*self.recIncreaseUnit,     #start x,y
                lineStartPoint_x+15, lineStartPoint_y)                       #end x,y

            lineStartPoint_x=self.rect_start_x
            lineStartPoint_y=self.rect_start_y-(num-self.minTempGraph)*self.recIncreaseUnit
            self.count_readData+=1

            self.rect_start_x+=(self.rect_horizon_x_unit+self.rect_horizon_x_gap)
        self.rect_start_x=self.rect_start_x_start
        self.rect_start_y=self.rect_start_y_start
        self.canvas.update()
    

    def dataGenerate(self,displayColumnSize,singleData):

        if len(self.data)<displayColumnSize:
            num=singleData
            self.data.append(num)
        else:
            self.data.popleft()
            self.data.append(singleData)
        return self.data

    
    def drawGraph(self):    
            self.drawColumnAndLine(self.data)

# root=Tk()
# root.geometry('550x400')
# frame = ttk.Frame(
#     root,
#     width=500,
#     height=400)

# frame.pack()
# display_btn = Button(frame, text="Go", command=lambda: DrawChart())
# display_btn.grid(
#     column=0,
#     row=3
# )
# root.mainloop()


        