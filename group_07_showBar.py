from tkinter import Tk, Canvas, Frame, BOTH, W
from tkinter import ttk

class ShowBar(Frame):

    def __init__(self,value, canvas,fillColor):
        super().__init__()
        self.initUI(value,canvas,fillColor)

    def initUI(self,value,canvas,fillColor):
        self.master.title('Final Project')
        self.pack(fill=BOTH, expand=1)
        self.scale=0.5
        self.x_start=295*self.scale
        self.x_endSmall=250*self.scale
        self.x_endLarge=200*self.scale
        self.y_start=700*self.scale
        self.minTemperature=10
        self.maxTemperature=30
        self.value=value
        self.dataChangeScale=10
        self.topleft_border_outRec_x=100*self.scale
        self.topleft_border_outRec_y=40*self.scale
        self.botRight_border_outRec_x=450*self.scale
        self.botRight_border_outRec_y=600*self.scale
        self.topLeft_oval_x=275*self.scale
        self.topLeft_oval_y=540*self.scale
        self.botRight_oval_x=325*self.scale
        self.botRight_oval_y=590*self.scale
        self.topLeft_therom_background_x=295*self.scale
        self.topLeft_therom_background_y=50*self.scale
        self.botRight_therom_background_x=305*self.scale
        self.botRight_therom_background_y=542*self.scale
        self.topLeft_therom_unit_text_x=350*self.scale
        self.fillColor=fillColor

        canvas.create_rectangle(
            self.topleft_border_outRec_x, self.topleft_border_outRec_y,                 
            self.botRight_border_outRec_x, self.botRight_border_outRec_y,                  
        )

        canvas.create_oval(self.topLeft_oval_x, self.topLeft_oval_y,    #top left
        self.botRight_oval_x, self.botRight_oval_y,                      #bottom right
        outline='#f11',fill=self.fillColor)
        
        canvas.create_rectangle(
            self.topLeft_therom_background_x, self.topLeft_therom_background_y,                  #top left
            self.botRight_therom_background_x, self.botRight_therom_background_y,                  #bottom right
            outline='#f11'
        )

        canvas.create_rectangle(self.topLeft_therom_background_x, self.y_start-self.value*self.dataChangeScale,    #top left
        self.botRight_therom_background_x, self.botRight_therom_background_y,                      #bottom right
        outline='#f11',fill=self.fillColor)

        canvas.create_text(self.topLeft_therom_unit_text_x, self.topLeft_therom_background_y+10, 
                           anchor=W, font=('Purisa', 12), 
        text='°C')

        while(self.minTemperature<=self.maxTemperature):
            if self.minTemperature%10==0:
                canvas.create_line(self.x_start, self.y_start-self.minTemperature*self.dataChangeScale,     #start x,y
                self.x_endLarge, self.y_start-self.minTemperature*self.dataChangeScale)                       #end x,y

                canvas.create_text(self.x_endLarge-30, self.y_start-self.minTemperature*self.dataChangeScale-2, 
                anchor=W, font='Purisa',  text=self.minTemperature)


            elif self.minTemperature%10!=0:
                canvas.create_line(self.x_start, self.y_start-self.minTemperature*self.dataChangeScale,     #start x,y
                self.x_endSmall, self.y_start-self.minTemperature*self.dataChangeScale)                       #end x,y

            self.minTemperature+=0.5

