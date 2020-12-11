from tkinter import Tk, Canvas, Frame, BOTH, W
from tkinter import ttk
from math import pi, cos, sin,radians
class ShowGauge(Frame):

    def __init__(self, value,canvas,fillColor):
        super().__init__()
        self.initUI(value,canvas,fillColor)


    def initUI(self,value,canvas,fillColor):
        self.master.title('Final Project')
        self.pack(fill=BOTH, expand=1)
        self.minTemperature=0
        self.maxTemperature=30
        self.value=value
        self.fillColor=fillColor

        self.oval_top_x=200*0.5+300   
        self.oval_top_y=100*0.5+100  
        self.oval_bot_x=400*0.5+300       
        self.oval_bot_y=300*0.5+100    
        self.x_start=300*0.5+300     
        self.y_start=200*0.5+100  
        self.x_endLarge=150*0.5     
        self.x_endSmall=150*0.5  

        ratioDegree=240/self.maxTemperature
        startTemper=0
        startDegree=-30

        while(startDegree<=210):
            bot_y=sin(radians(startDegree)).__round__(2)
            bot_x=cos(radians(startDegree)).__round__(2)
            if startDegree%30==0:
                canvas.create_line(self.x_start, self.y_start,     #start x,y
                self.x_start-bot_x*self.x_endLarge, self.y_start-bot_y*self.x_endLarge)
                if startDegree<=90 and  startTemper>0:
                    canvas.create_text(self.x_start-bot_x*self.x_endLarge-20, self.y_start-bot_y*self.x_endLarge-10, 
                    anchor=W, font='Purisa',  text=startTemper)
                elif startDegree==0:
                    canvas.create_text(self.x_start-bot_x*self.x_endLarge-30, self.y_start-bot_y*self.x_endLarge, 
                    anchor=W, font='Purisa',  text=startTemper)
                elif startDegree<=90 and  startDegree<0:
                    canvas.create_text(self.x_start-bot_x*self.x_endLarge-20, self.y_start-bot_y*self.x_endLarge+10, 
                    anchor=W, font='Purisa',  text=startTemper)
                elif startDegree>90 and startDegree<180:
                    canvas.create_text(self.x_start-bot_x*self.x_endLarge+10, self.y_start-bot_y*self.x_endLarge-10, 
                    anchor=W, font='Purisa',  text=startTemper)
                else:
                    canvas.create_text(self.x_start-bot_x*self.x_endLarge+10, self.y_start-bot_y*self.x_endLarge, 
                    anchor=W, font='Purisa',  text=startTemper)
                
            else:
                canvas.create_line(self.x_start, self.y_start,     #start x,y
                self.x_start-bot_x*(self.x_endLarge-20), self.y_start-bot_y*(self.x_endLarge-20))
            
            startDegree+=ratioDegree
            startTemper+=1
        
        canvas.create_oval(self.oval_top_x, self.oval_top_y,    #top left
        self.oval_bot_x, self.oval_bot_y,                      #bottom right
        outline='#f11',fill='#77f')

        canvas.create_arc(self.oval_top_x, self.oval_top_y,    #top left
        self.oval_bot_x, self.oval_bot_y, 
        start=210, extent=-1*(self.value*ratioDegree),         
        outline='#77f', fill=self.fillColor, width=2)
