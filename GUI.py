import Tkinter as tk
import xlrd
import xlwt
import sys
import csv
import numpy as np
import re
import tkFileDialog
from simulate import *
from FileDialog import *
from file_operation import *
import tkMessageBox
import matplotlib
import PIL
import PIL.ImageTk
import os
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.pyplot import savefig


#! /usr/bin/python

class interface:
    def __init__(self, root):
        self.Agentset = []
        self.root = root
        self.root.title("AgentTest")
        self.root.geometry('1100x500')
        self.count = []
        self.nbAgent = 0
        self.nbBreedC = 0
        self.nbBreedNc = 0
        self.widgets()
        self.Brand_Factor()  # obtain Brand Factor
        self.statisticdata()

    ### Create window
    def widgets(self):

        self.path = StringVar()
        self.years = StringVar()
        self.years.set("15")
        self.BFscale = tk.Label(self.root, text='')
        self.BFscale.place(x=20, y=120)
        tk.Label(self.root, text="Initialization").place(x=20, y=40)
        Entry(self.root, textvariable=self.path).place(x=20, y=70)
        button_import = tk.Button(self.root, text='Import file', width=10, height=1, command=self.importdata)
        button_import.place(x=220, y=70)
        self.yearsEntry = Entry(self.root,textvariable=self.years)
        self.yearsEntry.place(x=20, y=200)
        tk.Label(self.root, text="years").place(x=220, y=200)
        button_launche = tk.Button(self.root, text='Launche', width=10, height=1, command=self.launche)
        button_launche.place(x=20, y=250)
        button_export = tk.Button(self.root, text='Export', width=10, height=1, command = self.exportdata)
        button_export.place(x=150, y=250)


    ### Methods

    # Import excel file to initialize data
    def importdata(self):
        opts = {}
        opts['filetypes'] = [('Excel files', '.xlsx'), ('all files', '.*'),('CSV files', '.csv')]
        filename = tkFileDialog.askopenfilename(**opts)  # path by default
        if filename:
            self.path.set('%s' % filename)
            type = re.findall(r"\..*", filename)
            if type[0] == ".xlsx" :
                create_csv(filename)
                self.Agentset = data_initialize()
            else: self.Agentset = data_initialize()
        return

    # Export data as a CSV file
    def exportdata(self):
        opts = {}
        opts['filetypes'] = [('CSV files', '.csv'), ('all files', '.*')]
        filename = tkFileDialog.asksaveasfilename(**opts)
        if filename:
            export(filename, self.Agentset)

    # Dispaly Brand_Factor selected
    def print_br(self, brand_factor):
        self.BFscale.config(text='Brand factor selected:  ' + brand_factor)
        return

    # Scale of Brand_Factor
    def Brand_Factor(self):
        self.s = tk.Scale(self.root, from_=0.1, to_=2.9, orient=tk.HORIZONTAL, length=200, tickinterval=2.8, showvalue=0,
                     resolution=0.01, command=self.print_br)
        self.s.place(x=20, y=140)

    # Launche
    def launche(self):
        try:
            years = int(self.yearsEntry.get())
        except:
            tkMessageBox.showerror("Error", "Check the value of year !")
        else:
            if years > 0:
                self.years = years
                self.BF = self.s.get()
                self.statisticdata()
                simulate(self.Agentset, self.BF, self.years)
                self.statistic_new()
                self.chartpie()
                self.chartbar()


    # Statistic of original data

    def statisticdata(self):
        self.count = statistic(self.Agentset)
        title2 = tk.Label(self.root, text="Original data:").place(x=20, y=300)
        self.nbAgents = tk.Label(self.root, text=str(self.count[0]) + " agents")
        self.nbAgents.place(x=20, y=320)
        self.nbAgents_C = tk.Label(self.root, text=str(self.count[1]) + " Breed_C")
        self.nbAgents_C.place(x=20, y=340)
        self.nbAgents_NC = tk.Label(self.root, text=str(self.count[2]) + " Breed_NC")
        self.nbAgents_NC.place(x=20, y=360)

    # Statistic of new data
    def statistic_new(self):
        self.countnew = statistic(self.Agentset)
        title3 = tk.Label(self.root, text="New data:").place(x=150, y=300)
        self.nbAgents1 = tk.Label(self.root, text=str(len(self.Agentset)) + " agents")
        self.nbAgents1.place(x=150, y=320)
        self.nbAgents_C1 = tk.Label(self.root, text=str(self.countnew[1]) + " Breed_C")
        self.nbAgents_C1.place(x=150, y=340)
        self.nbAgents_NC1 = tk.Label(self.root, text=str(self.countnew[2]) + " Breed_NC")
        self.nbAgents_NC1.place(x=150, y=360)
        self.nbAgents_Lost = tk.Label(self.root, text=str(self.countnew[3]) + " Lost")
        self.nbAgents_Lost.place(x=150, y=380)
        self.nbAgents_Gained = tk.Label(self.root, text=str(self.countnew[4]) + " Gained")
        self.nbAgents_Gained.place(x=150, y=400)
        self.nbAgents_Regained = tk.Label(self.root, text=str(self.countnew[5]) + " Regained")
        self.nbAgents_Regained.place(x=150, y=420)
        self.nbAgents_Regained = tk.Label(self.root, text=str(self.countnew[6]) + " Unaltered")
        self.nbAgents_Regained.place(x=150, y=440)

    #Drawing charts
    def chartpie(self):
        plt.figure(figsize=(6, 9))
        labels = ['Lost', 'Gained', 'Regained','Unaltered']
        self.lost_percent = float(self.countnew[3])/float(self.countnew[0])
        self.gained_percent = float(self.countnew[4]) / float(self.countnew[0])
        self.regained_percent = float(self.countnew[5]) /float(self.countnew[0])
        self.unaltered_percent = float(self.countnew[6]) / float(self.countnew[0])
        percent =[self.lost_percent,self.gained_percent, self.regained_percent,self.unaltered_percent]
        colors = ['pink', 'yellowgreen', 'lightskyblue','red']
        explode = (0.05, 0, 0, 0)
        patches, l_text, p_text = plt.pie(percent, explode=explode, labels=labels, colors=colors,
                                          labeldistance = 0.8, autopct='%3.1f%%', shadow =True,
                                          startangle= 90, pctdistance=0.6)
        for t in l_text:
            t.set_size = (30)
        for t in p_text:
            t.set_size = (20)
        plt.axis('equal')
        plt.legend()

        ### Prefer putting the figure in the main windows to getting a popup of figure
        #Using regular expression to obtain the path for saving the figure
        path = self.path.get()
        dataname = re.findall(r"\w*\.", path)
        dataname = re.findall(r"\w*", dataname[0])
        path = re.sub("\w*\.[xlsx]?[csv]?.*", "Figure/" + dataname[0], path)
        self.mkdir(path)
        path = path + '/pie_' + str(self.years) + '_' + str(self.BF)  + '.png'
        savefig(path)
        #Display
        piepng = PIL.Image.open(path)
        (x, y) = piepng.size
        piepng = piepng.resize((300,450),PIL.Image.ANTIALIAS)
        photo =  PIL.ImageTk.PhotoImage(piepng)
        pielabel = Label(self.root, image=photo)
        pielabel.image = photo  # keep a reference!
        pielabel.place(x = 500, y = 300, anchor = CENTER)
        tk.Label(self.root, text="Pie chart(after simulation)").place(x=420, y=40)

    def chartbar(self):
        n_groups = 2

        Breed_C = (self.count[1],self.countnew[1])
        Breed_NC = (self.count[2],self.countnew[2])
        plt.subplots()
        index = np.arange(n_groups)
        bar_width = 0.2
        opacity = 0.4
        error_config = {'ecolor': '0.3'}
        plt.bar(index, Breed_C, bar_width,
                alpha=opacity,color='b', error_kw=error_config,
                label='Breed_C')
        plt.bar(index + bar_width, Breed_NC, bar_width,
                alpha=opacity,color='r',error_kw=error_config,
                label='Breed_NC')
        plt.xlabel('Breed Type')
        plt.ylabel('Number')
        plt.title('Comparision')
        plt.xticks(index + bar_width, ('Breed_C', 'Breed_NC'))
        plt.legend()
        # Save
        path = self.path.get()
        dataname = re.findall(r"\w*\.", path)
        dataname = re.findall(r"\w*", dataname[0])
        path = re.sub("\w*\.[xlsx]?[csv]?.*", "Figure/" + dataname[0], path)
        self.mkdir(path)
        path = path + '/bar_' + str(self.years) + '_' +str(self.BF) + '.png'
        savefig(path)
        # Display
        barpng = PIL.Image.open(path)
        barpng = barpng.resize((370, 350), PIL.Image.ANTIALIAS)
        photobar = PIL.ImageTk.PhotoImage(barpng)
        barlabel = Label(self.root, image=photobar)
        barlabel.image = photobar  # keep a reference!
        barlabel.place(x=900, y=300, anchor=CENTER)
        tk.Label(self.root, text="Bar chart(comparision)").place(x=820, y=40)

    def mkdir(self,path):
        path = path.strip()
        isExists = os.path.exists(path)
        if not isExists:
            os.makedirs(path)
            return True

