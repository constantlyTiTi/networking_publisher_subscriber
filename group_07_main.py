from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from group_07_publisher import publisher
from tkinter import Tk, Canvas, Frame, BOTH, W
from tkinter import messagebox
from group_07_subscriber import subscriber
import threading,collections

 ########################################## Main ##########################################
class MainWindow:
    def __init__(self, root, topic):
        self.root = root
        self.pubId=0
        self.publisherClientId=f"pubID_{self.pubId}"

        self.root.geometry("400x300")
        self.frame = Frame(root,width=400,height=300)
        self.frame.pack()
        
        self.publisher_btn = Button(self.frame, text = "Publisher",
        command= lambda: self.new_window_pub(PublisherWindow))
        self.publisher_btn.grid(
        column=2,
        row=3,    
        padx=10,
        pady=10)

        self.subscriber_btn = Button(self.frame, text = "Subscriber",
        command= lambda: self.new_window_sub(SubscriberWindow))
        self.subscriber_btn.grid(
        column=2,
        row=4,    
        padx=10,
        pady=10)
    
    def new_window_pub(self, _class):
        self.pubId+=1
        self.new = Toplevel(self.root)
        _class(self.new,self.publisherClientId)
    def new_window_sub(self, _class):
        self.new = Toplevel(self.root)
        _class(self.new)
        
    
 
 ########################################## Publisher ##########################################
class PublisherWindow:
    def __init__(self,root,publisherClientId):
        self.root = root
        self.root.geometry("550x500")
        self.root.title("Publisher")
        self.frame = Frame(root,width=550,height=500)
        self.frame.pack()
        self.threads=collections.deque()

        self.topic_lbl = Label(self.frame, text='Topic:')
        self.topic_lbl.grid(column=0, row=1)
        self.topic_combobx = Combobox(self.frame)
        self.topic_combobx['values'] = topicTuple
        self.topic_combobx.grid(
        column=1,
        row=1,    
        padx=10,
        pady=10)
        self.topic_combobx.current(0)

        self.maxContinueGoodDataNumber=20
        self.publisherClientId=publisherClientId

        self.canvas=Canvas(self.frame,width=550,height=450)
        self.canvasCol=0
        self.canvasRow=4
        self.canColSpan=3
        self.canRowSpan=5
        self.topicChangeCount=0
        self.previousThread=""


        publish_topic_btn = Button(self.frame,width = 10, text="Publish", command=lambda:self.connectPub())
        publish_topic_btn.grid(
        column=2,
        row=1)
    def connectPub(self):
        self.topic = self.topic_combobx.get()
        self.topic_combobx['state']="disabled"
        # if len(self.threads)>0:
        #     prevThread=self.threads.pop()
        #     # prevThread.join()
        # else:
        pubThread=threading.Thread(target=self.threadCreate)
        pubThread.setDaemon(True)
            # self.threads.append(pubThread)
        pubThread.start()
        # self.previousThread=pubThread.getName()
        
    # def callback(self,sv):
    #     return self.publisher.getCorruptDataCount()
    def threadCreate(self):
        self.publisher=publisher(self.publisherClientId,self.topic, self.canvas,self.canvasCol,self.canvasRow,self.canColSpan,self.canRowSpan,maxTem,minTemp)
        self.publisher.connectPublisher(self.maxContinueGoodDataNumber)



 
########################################## Subscriber  ##########################################
class SubscriberWindow:
    def __init__(self, root):
        
        self.root = root
        self.root.geometry("550x500")
        self.root.title("Subscriber")
        self.frame = Frame(root,width=550,height=500)
        self.frame.pack()

        self.topic_lbl = Label(self.frame, text='Topics')
        self.topic_lbl.grid(column=0, row=1, )
      
        self.topic_combobx = Combobox(self.frame)
        self.topic_combobx['values'] = topicTuple
        self.topic_combobx.grid(
        column=1,
        row=1,    
        padx=10,
        pady=10)

        self.canvas=Canvas(self.frame,width=550,height=450)
        self.canvasCol=0
        self.canvasRow=4
        self.canColSpan=3
        self.canRowSpan=5

        connect_btn = Button(self.frame,width = 10, text="Connect", command=lambda: self.connectSub())
        connect_btn.grid(
        column=2,
        row=1)

    def connectSub(self):
        self.topic_combobx['state']="disabled"
        self.subscriber=subscriber(self.topic_combobx.get(), self.canvas,self.canvasCol,self.canvasRow,self.canColSpan,self.canRowSpan,maxTem,minTemp)
        subThread=threading.Thread(target=self.threadCreate)
        subThread.setDaemon(True)
        subThread.start()

    def threadCreate(self):
        self.subscriber.connectSubscriber()

####################################################################################
####################################################################################
topicTuple = ("Dynamic Chart", "Gauge")
maxTem=21
minTemp=18
if __name__ == "__main__":
    root = Tk()
    app = MainWindow(root, topicTuple)
    app.root.title("Group 7 Final Project")
    root.mainloop()