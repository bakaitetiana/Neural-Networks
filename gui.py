# -*- coding: utf-8 -*-
from tkinter import *
import untitled0

class App(Frame):

    def __init__(self, master):
        super(App, self).__init__(master)
        self.grid()
        self.create_widgets()
    
    def create_widgets(self):
        Label(self, text = "Choose dataset:").grid(row = 0, column = 0)
        self.var = IntVar()
        self.var.set(0)
        self.file = Radiobutton(self, text = "CNAE-9", variable=self.var, value=0)
        self.file.grid(columnspan = 2)
        self.gui = Radiobutton(self, text = "SPECT", width=3, height=3, variable=self.var, value=1) 
        self.gui.grid(columnspan = 2)
        self.gui2 = Radiobutton(self, text = "haberman", variable=self.var, value=2) 
        self.gui2.grid(columnspan = 2)
        Label(self, text = "Choose number of hidden layers:").grid(row = 4, column = 0)
        self.v = IntVar()
        self.v.set(0)
        self.file = Radiobutton(self, text = "1", variable=self.varr, value=0)
        self.file.grid(columnspan = 2)
        self.gui4 = Radiobutton(self, text = "2", width=3, height=3, variable=self.varr, value=1) 
        self.gui4.grid(columnspan = 2)
        Label(self, text = "Choose number of neurons in hidden layers:").grid(row = 7, column = 0)
        Label(self, text = "1").grid(row = 8, column = 0)
        self.user_input = Entry(self)
        self.user_input.grid(row = 8, column = 1, sticky = W)
        Label(self, text = "2").grid(row = 9, column = 0) 
        self.us_input = Entry(self)
        self.us_input.grid(row = 9, column = 1, sticky = W)
        self.b2 = Button(self, text="Work", command= self.clicked)
        self.b2.grid(row = 13, column = 1)
        self.b3 = Button(self, text = 'Exit', command = self.quit)
        self.b3.grid(row = 14, column = 1)
        Label(self, text = "Result").grid(row = 16, column = 0) 
        self.c = Text(self, width=30, height=8, wrap = WORD)
        self.c.grid(row = 16, column = 1)
        
        
        
    # training  
    def clicked(self):
        p = self.user_input.get("1.0", END)
        if (self.var.get() == 0):
            f = open("C:/AI2/NN/CNAE-9.data","r")
            fl = f.readlines()
            input_list = []
            target_list = []
            model = NeuralNetwork(input_nodes=856,hidden_nodes=p,output_nodes=9)
            for x in fl:
                input_list.append(list(map(int,x.split(',')[1:])))
                exptd = [0 for i in range(9)]
                exptd[int(x.split(',')[0])-1] = 1
                target_list.append(exptd)
                model.train(input_list[-1],target_list[-1])
            res = untitled0.explore_nn(input_list,target_list, model)
        elif (self.var.get() == 1):
            f = open("C:/AI2/NN/CNAE-9.data","r")
            fl = f.readlines()
            input_list = []
            target_list = []
            model = NeuralNetwork(input_nodes=856,hidden_nodes=p,output_nodes=9)
            for x in fl:
                input_list.append(list(map(int,x.split(',')[1:])))
                exptd = [0 for i in range(9)]
                exptd[int(x.split(',')[0])-1] = 1
                target_list.append(exptd)
                model.train(input_list[-1],target_list[-1])
            res = untitled0.explore_nn(input_list,target_list, model)
        elif (self.var.get() == 2):
            f = open("C:/AI2/NN/haberman.data","r")
            fl = f.readlines()
            input_list = []
            target_list = []
            model = NeuralNetwork(input_nodes=3,hidden_nodes=p,output_nodes=2)
            for x in fl:
                input_list.append(list(map(int,x.split(',')[:-1])))
                exptd = [0 for i in range(2)]
                exptd[int(x.split(',')[-1])-1] = 1
                target_list.append(exptd)
                model.train(input_list[-1],target_list[-1])
            res = untitled0.explore_nn(input_list,target_list, model)
        else:
            results = None
        self.c.insert(END, res)


root = Tk()
root.title('GUI')
root.geometry('550x550')
app = App(root)
root.mainloop()
  
