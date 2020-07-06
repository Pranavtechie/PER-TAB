from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg
import sqlite3 as m
from PIL import ImageTk, Image
import random as r
from itertools import permutations
from tkinter import scrolledtext
import os

win = Tk()
win.title("PERTAB")
win.resizable(False, False)
win.geometry('1100x620')
win.configure(bg = '#f7e7ff')
win.iconbitmap('periodic-table.ico')

def pic():

    os.startfile('P_table.pdf')


heading = Button(win, text="The Modern Periodic Table", width = 30, font = ("Georgia", 23, "bold"), bg = "maroon", fg = "white", command = pic)
heading.pack()    

def Button_Click(Atomic_Number):

    mydb = m.connect("element.db")
    mycursor = mydb.cursor()
    
    ran = r.randint(1,102)
    
    mycursor.execute("select fact from facts where no = '%d'"%(ran))
    res = mycursor.fetchall()
    
    msg.showinfo('Interesting Facts from Science', str(res[0][0]))

    root = Toplevel()
    root.title('Element Discription')
    root.configure(bg = 'white')    
    root.resizable(False, False)
    root.geometry('1020x620')
    root.iconbitmap('periodic-table.ico')        
       
    mycursor.execute("SELECT * FROM elements where Atomic_Number = '%d'" %(Atomic_Number))
    result = mycursor.fetchall()   

    heading =  Label(root, text="Element Description", width = 30, font = ("Georgia", 23, "bold"), bg = "maroon", fg = "white" )
    heading.pack()

    Element_Sym = ImageTk.PhotoImage(Image.open("Element_Pics/"+ str(Atomic_Number)  + ".jpg"))
    panel_Sym = Label(root, image = Element_Sym)
    panel_Sym.place(x = 60, y = 50)
     
    Basic_info = LabelFrame(root, text = 'Basic Info',bd = 10, font = ('cambria',20,'italic'), bg = '#c9f3a8')
    Basic_info.place(x = 250, y = 50)

    Atomic_number =  Label(Basic_info, text = 'Atomic Number',relief = 'sunken', font = ('Imprint MT Shadow', 15), bg = '#abd0ff')
    Atomic_number.grid(column = 0, row = 0, padx = 3)

    Atomic_number_text =  Label (Basic_info, width = 13,text = str(result[0][0]), font  = ('baskeville old face',15, 'bold'), bg = 'white', relief = 'ridge')
    Atomic_number_text.grid(column = 1, row = 0, padx = 10, pady = 10)

    Symbol = Label (Basic_info, text = 'Symbol',relief = 'sunken', font = ('Imprint MT Shadow', 15), bg = '#abd0ff' )
    Symbol.grid(column = 0, row = 1, pady = 5)

    Symbol_text =  Label (Basic_info, width = 13,text = str(result[0][1]), font  = ('baskeville old face',15, 'bold'),relief = 'ridge' ,bg = 'white')
    Symbol_text.grid(column = 1, row = 1, pady = 5)

    Element_Name = Label (Basic_info, text = 'Element Name',relief = 'sunken', font = ('Imprint MT Shadow', 15), bg = '#abd0ff' )
    Element_Name.grid(column = 0, row = 2, pady = 5)

    Element_Name_text =  Label (Basic_info, width = 13,text = str(result[0][2]), relief = 'ridge',font  = ('baskeville old face',15, 'bold'), bg = 'white')
    Element_Name_text.grid(column = 1,row = 2, pady = 5)

    Atomic_Weight = Label (Basic_info, text = 'Atomic Weight (u)',relief = 'sunken', font = ('Imprint MT Shadow', 15), bg = '#abd0ff' )
    Atomic_Weight.grid(column = 0, row = 3, pady = 5)

    Atomic_Weight_Text =Label (Basic_info, width = 13,text = str(result[0][3]), relief = 'ridge',font  = ('baskeville old face',15, 'bold'), bg = 'white')
    Atomic_Weight_Text.grid(column = 1, row = 3, pady = 5)

    Discovery = LabelFrame(root, text = 'Discovery',bd = 10, font = ('cambria',20,'italic'), bg = '#c9f3a8')
    Discovery.place(x = 630, y = 50)    

    Discoverer = Label (Discovery, text = 'Discoverer',relief = 'sunken', font = ('Imprint MT Shadow', 15), bg = '#abd0ff' )
    Discoverer.grid(column = 0, row = 0, padx = 5, pady = 5)

    Discoverer_text =  Text (Discovery, width = 16,relief = 'groove', height = 2,font  = ('baskeville old face',12, 'bold'), bg = 'white')
    Discoverer_text.grid(column = 1, row = 0, padx = 5, pady = 5)
    Discoverer_text.insert(INSERT, str(result[0][4]))

    Year_of_Discovery = Label (Discovery, text = 'Year of Discovery',relief = 'sunken', font = ('Imprint MT Shadow', 15), bg = '#abd0ff' )
    Year_of_Discovery.grid(column = 0, row = 1, padx = 5, pady = 5)

    Year_of_Discovery_text =   Label(Discovery,text = str(result[0][5]),width = 10, relief = 'ridge', font  = ('baskeville old face',15, 'bold'), bg = 'white')
    Year_of_Discovery_text.grid(column = 1, row = 1, padx = 5, pady = 5)

    Temperature = LabelFrame(root, text = 'Temperature',bd = 10, font = ('cambria',20,'italic'), bg = '#c9f3a8')
    Temperature.place(x = 630, y = 320)
    
    Melting_Point = Label (Temperature, text = 'Melting Point',relief = 'sunken', font = ('Imprint MT Shadow', 15), bg = '#abd0ff' )
    Melting_Point.grid(column = 0, row = 0, padx = 5, pady = 5)

    Melting_point_text =  Label (Temperature, width = 10,text = str(result[0][6]),relief = 'ridge', font  = ('baskeville old face',15, 'bold'), bg = 'white')
    Melting_point_text.grid(column = 1, row = 0, padx = 5, pady = 5)

    Boiling_Point = Label (Temperature, text = 'Boiling Point',relief = 'sunken', font = ('Imprint MT Shadow', 15), bg = '#abd0ff' )
    Boiling_Point.grid(column = 0, row = 1, padx = 5, pady = 5)

    Boiling_Point_text =  Label (Temperature, width = 10,text = str(result[0][7]),relief = 'ridge', font  = ('baskeville old face',15, 'bold'), bg = 'white')
    Boiling_Point_text.grid(column = 1, row = 1, padx = 5, pady = 5)

    Position = LabelFrame(root, text = 'Position',bd = 10, font = ('cambria',20,'italic'), bg = '#c9f3a8')
    Position.place(x = 630, y = 190)

    Group = Label (Position, text = 'Group',relief = 'sunken', font = ('Imprint MT Shadow', 15), bg = '#abd0ff' )
    Group.grid(column = 0, row = 0, padx = 5, pady = 5)

    Group_text =  Label (Position, width = 10,text = str(result[0][8]),relief = 'ridge', font  = ('baskeville old face',15, 'bold'), bg = 'white')
    Group_text.grid(column = 1, row = 0, padx = 5, pady = 5)

    Period = Label (Position, text = 'Period',relief = 'sunken', font = ('Imprint MT Shadow', 15), bg = '#abd0ff' )
    Period.grid(column = 0, row = 1, padx = 5, pady = 5)

    Period_text =  Label (Position, width = 10,text = str(result[0][9]),relief = 'ridge', font  = ('baskeville old face',15, 'bold'), bg = 'white')
    Period_text.grid(column = 1, row = 1, padx = 5, pady = 5)

    Others = LabelFrame(root, text = 'Others', bd = 10, font = ('cambria',20,'italic'), bg = '#c9f3a8' )
    Others.place(x = 260, y = 270)    

    Abundance = Label (Others, text = 'Abundance', relief = 'sunken', font = ('Imprint MT Shadow', 15), bg = '#abd0ff' )
    Abundance.grid(column = 0, row = 0, padx = 5, pady = 5)

    Abundance_text =  Label (Others, width = 10,text = str(result[0][10]), relief = 'ridge', font  = ('baskeville old face',15, 'bold'), bg = 'white')
    Abundance_text.grid(column = 1, row = 0, padx = 5, pady = 5)

    Heat = Label (Others, text = 'Heat(J/gK)', relief = 'sunken',font = ('Imprint MT Shadow', 15), bg = '#abd0ff' )
    Heat.grid(column = 0, row = 1, padx = 5, pady = 5)

    Heat_text =  Label (Others, width = 10,text = str(result[0][11]),relief = 'ridge', font  = ('baskeville old face',15, 'bold'), bg = 'white')
    Heat_text.grid(column = 1, row = 1, padx = 5, pady = 5)

    Density = Label (Others, text = 'Density', relief = 'sunken',font = ('Imprint MT Shadow', 15), bg = '#abd0ff' )
    Density.grid(column = 0, row = 2, padx = 5, pady = 5)

    Density_text =  Label (Others, width = 10,text = str(result[0][12]),relief = 'ridge', font  = ('baskeville old face',15, 'bold'), bg = 'white')
    Density_text.grid(column = 1, row = 2, padx = 5, pady = 5)
    
    Radius_Info=  LabelFrame(root, text = 'Radius(Angstorm) / Valency', bd = 10, font = ('cambria',20,'italic'), bg = '#c9f3a8' )
    Radius_Info.place(x = 260, y = 450)
    
    At_radius = Label (Radius_Info, text = 'Atomic Radius', relief = 'sunken',font = ('Imprint MT Shadow', 15), bg = '#abd0ff' )
    At_radius.grid(column = 0, row = 0, padx = 5, pady = 5)
    
    At_radius_text =  Label (Radius_Info, width = 10,text = str(result[0][14]),relief = 'ridge', font  = ('baskeville old face',15, 'bold'), bg = 'white')
    At_radius_text.grid(column = 1, row = 0, padx = 5, pady = 5)
    
    Io_radius = Label (Radius_Info, text = 'Ionic Radius', relief = 'sunken',font = ('Imprint MT Shadow', 15), bg = '#abd0ff' )
    Io_radius.grid(column = 0, row = 1, padx = 5, pady = 5)
    
    Io_radius_text =  Label (Radius_Info, width = 10,text = str(result[0][15]),relief = 'ridge', font  = ('baskeville old face',15, 'bold'), bg = 'white')
    Io_radius_text.grid(column = 1, row = 1, padx = 5, pady = 5)
    
    Co_radius = Label (Radius_Info, text = 'Covalent Radius', relief = 'sunken',font = ('Imprint MT Shadow', 15), bg = '#abd0ff' )
    Co_radius.grid(column = 0, row = 2, padx = 5, pady = 5)
    
    Co_radius_text =  Label (Radius_Info, width = 10,text = str(result[0][16]),relief = 'ridge', font  = ('baskeville old face',15, 'bold'), bg = 'white')
    Co_radius_text.grid(column = 1, row = 2, padx = 10, pady = 5)
    
    Vw_radius = Label (Radius_Info, text = 'Vander waal Radius', relief = 'sunken',font = ('Imprint MT Shadow', 15), bg = '#abd0ff' )
    Vw_radius.grid(column = 3, row = 0, padx = 15, pady = 5)
    
    Vw_radius_text =  Label (Radius_Info, width = 10,text = str(result[0][17]),relief = 'ridge', font  = ('baskeville old face',15, 'bold'), bg = 'white')
    Vw_radius_text.grid(column = 4, row = 0, padx = 5, pady = 5)
    
    Cr_radius = Label (Radius_Info, text = 'Crystal Radius', relief = 'sunken',font = ('Imprint MT Shadow', 15), bg = '#abd0ff' )
    Cr_radius.grid(column = 3, row = 1, padx = 15, pady = 5)
    
    Cr_radius_text =  Label (Radius_Info, width = 10,text = str(result[0][18]),relief = 'ridge', font  = ('baskeville old face',15, 'bold'), bg = 'white')
    Cr_radius_text.grid(column = 4, row = 1, padx = 5, pady = 5)
    
    valency = Label (Radius_Info, text = 'Valency', relief = 'sunken',font = ('Imprint MT Shadow', 15), bg = '#abd0ff' )
    valency.grid(column = 3, row = 2, padx = 15, pady = 5)
    
    valency_text =  Label (Radius_Info, width = 13,text = str(result[0][13]),relief = 'ridge', font  = ('baskeville old face',15, 'bold'), bg = 'white')
    valency_text.grid(column = 4, row = 2, padx = 5, pady = 5)
   

    Configuration =  LabelFrame(root, text = 'Configuration', bd = 10, font = ('cambria',20,'italic'), bg = '#c9f3a8' )
    Configuration.place(x = 5, y = 270)
        
    Element_Config = ImageTk.PhotoImage(Image.open("Electronic_Configuration/"+ str(Atomic_Number)  + ".jpg"))
    panel_config = Label(Configuration, image = Element_Config)
    panel_config.grid(row = 0, column = 0, padx = 10, pady = 10)
    
    root.mainloop()

def entered1(event):
    at1.configure(bg = 'black', fg = 'white')    
def left1(event):
    at1.configure(bg = '#f13800', fg = 'black')    

def entered2(event):
    at2.configure(bg = 'black', fg = 'white')
def left2(event):
    at2.configure(bg = '#af7ffb', fg = 'black')

def entered3(event):
    at3.configure(bg = 'black', fg = 'white')
def left3(event):
    at3.configure(bg = "#49c9ff", fg = 'black')

def entered4(event):
    at4.configure(bg = 'black', fg = 'white')
def left4(event):
    at4.configure(bg = '#adaeb0', fg = 'black')
    
def entered5(event):
    at5.configure(bg = 'black', fg = 'white')
def left5(event):
    at5.configure(bg = '#1aff40', fg = 'black')
    
def entered6(event):
    at6.configure(bg = 'black', fg = 'white')
def left6(event):
    at6.configure(bg = '#1aff40', fg = 'black')
    
def entered7(event):
    at7.configure(bg = 'black', fg = 'white')
def left7(event):
    at7.configure(bg = '#1aff40', fg = 'black')
    
def entered8(event):
    at8.configure(bg = 'black', fg = 'white')
def left8(event):
    at8.configure(bg = '#1aff40', fg = 'black')
    
def entered9(event):
    at9.configure(bg = 'black', fg = 'white')
def left9(event):
    at9.configure(bg = '#1aff40', fg = 'black')
    
def entered10(event):
    at10.configure(bg = 'black', fg = 'white')
def left10(event):
    at10.configure(bg = '#af7ffb', fg = 'black')

def entered11(event):
    at11.configure(bg = 'black', fg = 'white')
def left11(event):
    at11.configure(bg = '#49c9ff', fg = 'black')

def entered12(event):
    at12.configure(bg = 'black', fg = 'white')
def left12(event):
    at12.configure(bg = '#adaeb0', fg = 'black')
    
def entered13(event):
    at13.configure(bg = 'black', fg = 'white')
def left13(event):
    at13.configure(bg = '#ff5500', fg = 'black')

def entered14(event):
    at14.configure(bg = 'black', fg = 'white')
def left14(event):
    at14.configure(bg = '#ff55ff', fg = 'black')

def entered15(event):
    at15.configure(bg = 'black', fg = 'white')
def left15(event):
    at15.configure(bg = '#1aff40', fg = 'black')
    
def entered16(event):
    at16.configure(bg = 'black', fg = 'white')
def left16(event):
    at16.configure(bg = '#1aff40', fg = 'black')
    
def entered17(event):
    at17.configure(bg = 'black', fg = 'white')
def left17(event):
    at17.configure(bg = '#1aff40', fg = 'black')
    
def entered18(event):
    at18.configure(bg = 'black', fg = 'white')
def left18(event):
    at18.configure(bg = '#af7ffb', fg = 'black')

def entered19(event):
    at19.configure(bg = 'black', fg = 'white')
def left19(event):
    at19.configure(bg = '#49c9ff', fg = 'black')

def entered20(event):
    at20.configure(bg = 'black', fg = 'white')
def left20(event):
    at20.configure(bg = '#adaeb0', fg = 'black')

def entered21(event):
    at21.configure(bg = 'black', fg = 'white')
def left21(event):
    at21.configure(bg = 'yellow', fg = 'black')

def entered22(event):
    at22.configure(bg = 'black', fg = 'white')
def left22(event):
    at22.configure(bg = 'yellow', fg = 'black')

def entered23(event):
    at23.configure(bg = 'black', fg = 'white')
def left23(event):
    at23.configure(bg = 'yellow', fg = 'black')

def entered24(event):
    at24.configure(bg = 'black', fg = 'white')
def left24(event):
    at24.configure(bg = 'yellow', fg = 'black')

def entered25(event):
    at25.configure(bg = 'black', fg = 'white')
def left25(event):
    at25.configure(bg = 'yellow', fg = 'black')

def entered26(event):
    at26.configure(bg = 'black', fg = 'white')
def left26(event):
    at26.configure(bg = 'yellow', fg = 'black')

def entered27(event):
    at27.configure(bg = 'black', fg = 'white')
def left27(event):
    at27.configure(bg = 'yellow', fg = 'black')

def entered28(event):
    at28.configure(bg = 'black', fg = 'white')
def left28(event):
    at28.configure(bg = 'yellow', fg = 'black')

def entered29(event):
    at29.configure(bg = 'black', fg = 'white')
def left29(event):
    at29.configure(bg = 'yellow', fg = 'black')
    
def entered30(event):
    at30.configure(bg = 'black', fg = 'white')
def left30(event):
    at30.configure(bg = 'yellow', fg = 'black')

def entered31(event):
    at31.configure(bg = 'black', fg = 'white')
def left31(event):
    at31.configure(bg = '#ff5500', fg = 'black')

def entered32(event):
    at32.configure(bg = 'black', fg = 'white')
def left32(event):
    at32.configure(bg = '#ff55ff', fg = 'black')

def entered33(event):
    at33.configure(bg = 'black', fg = 'white')
def left33(event):
    at33.configure(bg = '#ff55ff', fg = 'black')

def entered34(event):
    at34.configure(bg = 'black', fg = 'white')
def left34(event):
    at34.configure(bg = '#1aff40', fg = 'black')

def entered35(event):
    at35.configure(bg = 'black', fg = 'white')
def left35(event):
    at35.configure(bg = '#1aff40', fg = 'black')

def entered36(event):
    at36.configure(bg = 'black', fg = 'white')
def left36(event):
    at36.configure(bg = '#af7ffb', fg = 'black')

def entered37(event):
    at37.configure(bg = 'black', fg = 'white')
def left37(event):
    at37.configure(bg = '#49c9ff', fg = 'black')

def entered38(event):
    at38.configure(bg = 'black', fg = 'white')
def left38(event):
    at38.configure(bg = '#adaeb0', fg = 'black')

def entered39(event):
    at39.configure(bg = 'black', fg = 'white')
def left39(event):
    at39.configure(bg = 'yellow', fg = 'black')

def entered40(event):
    at40.configure(bg = 'black', fg = 'white')
def left40(event):
    at40.configure(bg = 'yellow', fg = 'black')

def entered41(event):
    at41.configure(bg = 'black', fg = 'white')
def left41(event):
    at41.configure(bg = 'yellow', fg = 'black')

def entered42(event):
    at42.configure(bg = 'black', fg = 'white')
def left42(event):
    at42.configure(bg = 'yellow', fg = 'black')

def entered43(event):
    at43.configure(bg = 'black', fg = 'white')
def left43(event):
    at43.configure(bg = 'yellow', fg = 'black')

def entered44(event):
    at44.configure(bg = 'black', fg = 'white')
def left44(event):
    at44.configure(bg = 'yellow', fg = 'black')

def entered45(event):
    at45.configure(bg = 'black', fg = 'white')
def left45(event):
    at45.configure(bg = 'yellow', fg = 'black')

def entered46(event):
    at46.configure(bg = 'black', fg = 'white')
def left46(event):
    at46.configure(bg = 'yellow', fg = 'black')

def entered47(event):
    at47.configure(bg = 'black', fg = 'white')
def left47(event):
    at47.configure(bg = 'yellow', fg = 'black')

def entered48(event):
    at48.configure(bg = 'black', fg = 'white')
def left48(event):
    at48.configure(bg = 'yellow', fg = 'black')

def entered49(event):
    at49.configure(bg = 'black', fg = 'white')
def left49(event):
    at49.configure(bg = '#ff5500', fg = 'black')

def entered50(event):
    at50.configure(bg = 'black', fg = 'white')
def left50(event):
    at50.configure(bg = '#ff5500', fg = 'black')

def entered51(event):
    at51.configure(bg = 'black', fg = 'white')
def left51(event):
    at51.configure(bg = '#ff55ff', fg = 'black')

def entered52(event):
    at52.configure(bg = 'black', fg = 'white')
def left52(event):
    at52.configure(bg = '#ff55ff', fg = 'black')

def entered53(event):
    at53.configure(bg = 'black', fg = 'white')
def left53(event):
    at53.configure(bg = '#1aff40', fg = 'black')
    
def entered54(event):
    at54.configure(bg = 'black', fg = 'white')
def left54(event):
    at54.configure(bg = '#af7ffb', fg = 'black')

def entered55(event):
    at55.configure(bg = 'black', fg = 'white')
def left55(event):
    at55.configure(bg = '#49c9ff', fg = 'black')

def entered56(event):
    at56.configure(bg = 'black', fg = 'white')
def left56(event):
    at56.configure(bg = '#adaeb0', fg = 'black')

def entered57(event):
    at57.configure(bg = 'black', fg = 'white')
def left57(event):
    at57.configure(bg = '#bcc514', fg = 'black')

def entered58(event):
    at58.configure(bg = 'black', fg = 'white')
def left58(event):
    at58.configure(bg = '#bcc514', fg = 'black')

def entered59(event):
    at59.configure(bg = 'black', fg = 'white')
def left59(event):
    at59.configure(bg = '#bcc514', fg = 'black')

def entered60(event):
    at60.configure(bg = 'black', fg = 'white')
def left60(event):
    at60.configure(bg = '#bcc514', fg = 'black')

def entered61(event):
    at61.configure(bg = 'black', fg = 'white')
def left61(event):
    at61.configure(bg = '#bcc514', fg = 'black')

def entered62(event):
    at62.configure(bg = 'black', fg = 'white')
def left62(event):
    at62.configure(bg = '#bcc514', fg = 'black')

def entered63(event):
    at63.configure(bg = 'black', fg = 'white')
def left63(event):
    at63.configure(bg = '#bcc514', fg = 'black')

def entered64(event):
    at64.configure(bg = 'black', fg = 'white')
def left64(event):
    at64.configure(bg = '#bcc514', fg = 'black')
    
def entered65(event):
    at65.configure(bg = 'black', fg = 'white')
def left65(event):
    at65.configure(bg = '#bcc514', fg = 'black')

def entered66(event):
    at66.configure(bg = 'black', fg = 'white')
def left66(event):
    at66.configure(bg = '#bcc514', fg = 'black')

def entered67(event):
    at67.configure(bg = 'black', fg = 'white')
def left67(event):
    at67.configure(bg = '#bcc514', fg = 'black')

def entered68(event):
    at68.configure(bg = 'black', fg = 'white')
def left68(event):
    at68.configure(bg = '#bcc514', fg = 'black')

def entered69(event):
    at69.configure(bg = 'black', fg = 'white')
def left69(event):
    at69.configure(bg = '#bcc514', fg = 'black')

def entered70(event):
    at70.configure(bg = 'black', fg = 'white')
def left70(event):
    at70.configure(bg = '#bcc514', fg = 'black')

def entered71(event):
    at71.configure(bg = 'black', fg = 'white')
def left71(event):
    at71.configure(bg = '#bcc514', fg = 'black')

def entered72(event):
    at72.configure(bg = 'black', fg = 'white')
def left72(event):
    at72.configure(bg = 'yellow', fg = 'black')

def entered73(event):
    at73.configure(bg = 'black', fg = 'white')
def left73(event):
    at73.configure(bg = 'yellow', fg = 'black')

def entered74(event):
    at74.configure(bg = 'black', fg = 'white')
def left74(event):
    at74.configure(bg = 'yellow', fg = 'black')

def entered75(event):
    at75.configure(bg = 'black', fg = 'white')
def left75(event):
    at75.configure(bg = 'yellow', fg = 'black')

def entered76(event):
    at76.configure(bg = 'black', fg = 'white')
def left76(event):
    at76.configure(bg = 'yellow', fg = 'black')

def entered77(event):
    at77.configure(bg = 'black', fg = 'white')
def left77(event):
    at77.configure(bg = 'yellow', fg = 'black')

def entered78(event):
    at78.configure(bg = 'black', fg = 'white')
def left78(event):
    at78.configure(bg = 'yellow', fg = 'black')

def entered79(event):
    at79.configure(bg = 'black', fg = 'white')
def left79(event):
    at79.configure(bg = 'yellow', fg = 'black')

def entered80(event):
    at80.configure(bg = 'black', fg = 'white')
def left80(event):
    at80.configure(bg = 'yellow', fg = 'black')

def entered81(event):
    at81.configure(bg = 'black', fg = 'white')
def left81(event):
    at81.configure(bg = '#ff5500', fg = 'black')

def entered82(event):
    at82.configure(bg = 'black', fg = 'white')
def left82(event):
    at82.configure(bg = '#ff5500', fg = 'black')

def entered83(event):
    at83.configure(bg = 'black', fg = 'white')
def left83(event):
    at83.configure(bg = '#ff5500', fg = 'black')

def entered84(event):
    at84.configure(bg = 'black', fg = 'white')
def left84(event):
    at84.configure(bg = '#ff55ff', fg = 'black')

def entered85(event):
    at85.configure(bg = 'black', fg = 'white')
def left85(event):
    at85.configure(bg = '#ff55ff', fg = 'black')

def entered86(event):
    at86.configure(bg = 'black', fg = 'white')
def left86(event):
    at86.configure(bg = '#af7ffb', fg = 'black')

def entered87(event):
    at87.configure(bg = 'black', fg = 'white')
def left87(event):
    at87.configure(bg = '#49c9ff', fg = 'black')

def entered88(event):
    at88.configure(bg = 'black', fg = 'white')
def left88(event):
    at88.configure(bg = '#adaeb0', fg = 'black')

def entered89(event):
    at89.configure(bg = 'black', fg = 'white')
def left89(event):
    at89.configure(bg = '#ff910b', fg = 'black')

def entered90(event):
    at90.configure(bg = 'black', fg = 'white')
def left90(event):
    at90.configure(bg = '#ff910b', fg = 'black')

def entered91(event):
    at91.configure(bg = 'black', fg = 'white')
def left91(event):
    at91.configure(bg = '#ff910b', fg = 'black')

def entered92(event):
    at92.configure(bg = 'black', fg = 'white')
def left92(event):
    at92.configure(bg = '#ff910b', fg = 'black')

def entered93(event):
    at93.configure(bg = 'black', fg = 'white')
def left93(event):
    at93.configure(bg = '#ff910b', fg = 'black')

def entered94(event):
    at94.configure(bg = 'black', fg = 'white')
def left94(event):
    at94.configure(bg = '#ff910b', fg = 'black')

def entered95(event):
    at95.configure(bg = 'black', fg = 'white')
def left95(event):
    at95.configure(bg = '#ff910b', fg = 'black')

def entered96(event):
    at96.configure(bg = 'black', fg = 'white')
def left96(event):
    at96.configure(bg = '#ff910b', fg = 'black')

def entered97(event):
    at97.configure(bg = 'black', fg = 'white')
def left97(event):
    at97.configure(bg = '#ff910b', fg = 'black')

def entered98(event):
    at98.configure(bg = 'black', fg = 'white')
def left98(event):
    at98.configure(bg = '#ff910b', fg = 'black')

def entered99(event):
    at99.configure(bg = 'black', fg = 'white')
def left99(event):
    at99.configure(bg = '#ff910b', fg = 'black')
    
def entered100(event):
    at100.configure(bg = 'black', fg = 'white')
def left100(event):
    at100.configure(bg = '#ff910b', fg = 'black')

def entered101(event):
    at101.configure(bg = 'black', fg = 'white')
def left101(event):
    at101.configure(bg = '#ff910b', fg = 'black')

def entered102(event):
    at102.configure(bg = 'black', fg = 'white')
def left102(event):
    at102.configure(bg = '#ff910b', fg = 'black')

def entered103(event):
    at103.configure(bg = 'black', fg = 'white')
def left103(event):
    at103.configure(bg = '#ff910b', fg = 'black')

def entered104(event):
    at104.configure(bg = 'black', fg = 'white')
def left104(event):
    at104.configure(bg = 'yellow', fg = 'black')

def entered105(event):
    at105.configure(bg = 'black', fg = 'white')
def left105(event):
    at105.configure(bg = 'yellow', fg = 'black')

def entered106(event):
    at106.configure(bg = 'black', fg = 'white')
def left106(event):
    at106.configure(bg = 'yellow', fg = 'black')

def entered107(event):
    at107.configure(bg = 'black', fg = 'white')
def left107(event):
    at107.configure(bg = 'yellow', fg = 'black')

def entered108(event):
    at108.configure(bg = 'black', fg = 'white')
def left108(event):
    at108.configure(bg = 'yellow', fg = 'black')

def entered109(event):
    at109.configure(bg = 'black', fg = 'white')
def left109(event):
    at109.configure(bg = 'yellow', fg = 'black')

def entered110(event):
    at110.configure(bg = 'black', fg = 'white')
def left110(event):
    at110.configure(bg = 'yellow', fg = 'black')

def entered111(event):
    at111.configure(bg = 'black', fg = 'white')
def left111(event):
    at111.configure(bg = 'yellow', fg = 'black')

def entered112(event):
    at112.configure(bg = 'black', fg = 'white')
def left112(event):
    at112.configure(bg = 'yellow', fg = 'black')

def entered113(event):
    at113.configure(bg = 'black', fg = 'white')
def left113(event):
    at113.configure(bg = '#ff5500', fg = 'black')

def entered114(event):
    at114.configure(bg = 'black', fg = 'white')
def left114(event):
    at114.configure(bg = '#ff5500', fg = 'black')

def entered115(event):
    at115.configure(bg = 'black', fg = 'white')
def left115(event):
    at115.configure(bg = '#ff5500', fg = 'black')

def entered116(event):
    at116.configure(bg = 'black', fg = 'white')
def left116(event):
    at116.configure(bg = '#ff5500', fg = 'black')

def entered117(event):
    at117.configure(bg = 'black', fg = 'white')
def left117(event):
    at117.configure(bg = '#ff5500', fg = 'black')

def entered118(event):
    at118.configure(bg = 'black', fg = 'white')
def left118(event):
    at118.configure(bg = '#af7ffb', fg = 'black')

# Start of the elements
#Period 1 - 3
at1 = Button(win, text = "H ", font = ('georgia', 15, 'bold'), width = 3, bg = '#f13800', command = lambda:Button_Click(1))
at1.place(x = 50, y = 50)
at1.bind('<Enter>', entered1)
at1.bind('<Leave>', left1)


at2 = Button(win, text = "He", font = ('georgia', 15, 'bold'),width = 3, bg = '#af7ffb', command = lambda:Button_Click(2))
at2.place(x = 985, y = 50)
at2.bind('<Enter>', entered2)
at2.bind('<Leave>', left2)

at3 = Button(win, text = "Li", font = ('georgia', 15, 'bold'),width = 3, bg = '#49c9ff',  command = lambda:Button_Click(3))
at3.place(x = 50, y = 95)
at3.bind('<Enter>', entered3)
at3.bind('<Leave>', left3)

at4 = Button(win, text = "Be", font = ('georgia', 15, 'bold'),width = 3, bg = '#adaeb0',  command = lambda:Button_Click(4))
at4.place(x = 105, y = 95)
at4.bind('<Enter>', entered4)
at4.bind('<Leave>', left4)

at5 = Button(win, text = "B", font = ('georgia', 15, 'bold'),width = 3, bg = '#1aff40',  command = lambda:Button_Click(5))
at5.place(x = 710, y = 95)
at5.bind('<Enter>', entered5)
at5.bind('<Leave>', left5)

at6 = Button(win, text = "C", font = ('georgia', 15, 'bold'),width = 3, bg = '#1aff40',  command = lambda:Button_Click(6))
at6.place(x = 765, y = 95)
at6.bind('<Enter>', entered6)
at6.bind('<Leave>', left6)

at7 = Button(win, text = "N", font = ('georgia', 15, 'bold'),width = 3, bg = '#1aff40',command = lambda:Button_Click(7))
at7.place(x = 820, y = 95)
at7.bind('<Enter>', entered7)
at7.bind('<Leave>', left7)

at8 = Button(win, text = "O", font = ('georgia', 15, 'bold'),width = 3, bg = '#1aff40',command = lambda:Button_Click(8))
at8.place(x = 875, y = 95)
at8.bind('<Enter>', entered8)
at8.bind('<Leave>', left8)

at9 = Button(win, text = "F", font = ('georgia', 15, 'bold'),width = 3, bg = '#1aff40',command = lambda:Button_Click(9))
at9.place(x = 930, y = 95)
at9.bind('<Enter>', entered9)
at9.bind('<Leave>', left9)

at10 = Button(win, text = "Ne", font = ('georgia', 15, 'bold'),width = 3, bg = '#af7ffb',command = lambda:Button_Click(10))
at10.place(x = 985, y = 95)
at10.bind('<Enter>', entered10)
at10.bind('<Leave>', left10)

at11 = Button(win, text = "Na", font = ('georgia', 15, 'bold'),width = 3, bg = '#49c9ff',command = lambda:Button_Click(11))
at11.place(x = 50, y = 140)
at11.bind('<Enter>', entered11)
at11.bind('<Leave>', left11)

at12 = Button(win, text = "Mg", font = ('georgia', 15, 'bold'),width = 3, bg = '#adaeb0',command = lambda:Button_Click(12))
at12.place(x = 105, y = 140)
at12.bind('<Enter>', entered12)
at12.bind('<Leave>', left12)


at13 = Button(win, text = "Al", font = ('georgia', 15, 'bold'),width = 3, bg = '#ff5500',command = lambda:Button_Click(13))
at13.place(x = 710, y = 140)
at13.bind('<Enter>', entered13)
at13.bind('<Leave>', left13)

at14 = Button(win, text = "Si", font = ('georgia', 15, 'bold'),width = 3, bg = '#ff55ff',command = lambda:Button_Click(14))
at14.place(x = 765, y = 140)
at14.bind('<Enter>', entered14)
at14.bind('<Leave>', left14)

at15 = Button(win, text = "P", font = ('georgia', 15, 'bold'),width = 3, bg = '#1aff40',command = lambda:Button_Click(15))
at15.place(x = 820, y = 140)
at15.bind('<Enter>', entered15)
at15.bind('<Leave>', left15)

at16 = Button(win, text = "S", font = ('georgia', 15, 'bold'),width = 3, bg = '#1aff40',command = lambda:Button_Click(16))
at16.place(x = 875, y = 140)
at16.bind('<Enter>', entered16)
at16.bind('<Leave>', left16)

at17 = Button(win, text = "Cl", font = ('georgia', 15, 'bold'),width = 3, bg = '#1aff40',command = lambda:Button_Click(17))
at17.place(x = 930, y = 140)
at17.bind('<Enter>', entered17)
at17.bind('<Leave>', left17)

at18 = Button(win, text = "Ar", font = ('georgia', 15, 'bold'),width = 3, bg = '#af7ffb',command = lambda:Button_Click(18))
at18.place(x = 985, y = 140)
at18.bind('<Enter>', entered18)
at18.bind('<Leave>', left18)

at19 = Button(win, text = "K ", font = ('georgia', 15, 'bold'),width = 3, bg = '#49c9ff',command = lambda:Button_Click(19))
at19.place(x = 50, y = 185)
at19.bind('<Enter>', entered19)
at19.bind('<Leave>', left19)

at20 = Button(win, text = "Ca", font = ('georgia', 15, 'bold'),width = 3, bg = '#adaeb0',command = lambda:Button_Click(20))
at20.place(x = 105, y = 185)
at20.bind('<Enter>', entered20)
at20.bind('<Leave>', left20)

at21 = Button(win, text = "Sc", font = ('georgia', 15, 'bold'),width = 3, bg = 'yellow',command = lambda:Button_Click(21))
at21.place(x = 160, y = 185)
at21.bind('<Enter>', entered21)
at21.bind('<Leave>', left21)

at22 = Button(win, text = "Ti", font = ('georgia', 15, 'bold'),width = 3, bg = 'yellow',command = lambda:Button_Click(22))
at22.place(x = 215, y = 185)
at22.bind('<Enter>', entered22)
at22.bind('<Leave>', left22)

at23 = Button(win, text = "V", font = ('georgia', 15, 'bold'),width = 3, bg = 'yellow',command = lambda:Button_Click(23))
at23.place(x = 270, y = 185)
at23.bind('<Enter>', entered23)
at23.bind('<Leave>', left23)

at24 = Button(win, text = "Cr", font = ('georgia', 15, 'bold'),width = 3, bg = 'yellow',command = lambda:Button_Click(24))
at24.place(x = 325, y = 185)
at24.bind('<Enter>', entered24)
at24.bind('<Leave>', left24)

at25 = Button(win, text = "Mn", font = ('georgia', 15, 'bold'),width = 3, bg = 'yellow',command = lambda:Button_Click(25))
at25.place(x = 380, y = 185)
at25.bind('<Enter>', entered25)
at25.bind('<Leave>', left25)

at26 = Button(win, text = "Fe", font = ('georgia', 15, 'bold'),width = 3, bg = 'yellow',command = lambda:Button_Click(26))
at26.place(x = 435, y = 185)
at26.bind('<Enter>', entered26)
at26.bind('<Leave>', left26)

at27 = Button(win, text = "Co", font = ('georgia', 15, 'bold'),width = 3, bg = 'yellow',command = lambda:Button_Click(27))
at27.place(x = 490, y = 185)
at27.bind('<Enter>', entered27)
at27.bind('<Leave>', left27)

at28 = Button(win, text = "Ni", font = ('georgia', 15, 'bold'),width = 3, bg = 'yellow',command = lambda:Button_Click(28))
at28.place(x = 545, y = 185)
at28.bind('<Enter>', entered28)
at28.bind('<Leave>', left28)

at29 = Button(win, text = "Cu", font = ('georgia', 15, 'bold'),width = 3, bg = 'yellow',command = lambda:Button_Click(29))
at29.place(x = 600, y = 185)
at29.bind('<Enter>', entered29)
at29.bind('<Leave>', left29)

at30 = Button(win, text = "Zn", font = ('georgia', 15, 'bold'),width = 3, bg = 'yellow',command = lambda:Button_Click(30))
at30.place(x = 655, y = 185)
at30.bind('<Enter>', entered30)
at30.bind('<Leave>', left30)

at31 = Button(win, text = "Ga", font = ('georgia', 15, 'bold'),width = 3, bg = '#ff5500',command = lambda:Button_Click(31))
at31.place(x = 710, y = 185)
at31.bind('<Enter>', entered31)
at31.bind('<Leave>', left31)

at32 = Button(win, text = "Ge", font = ('georgia', 15, 'bold'),width = 3, bg = '#ff55ff',command = lambda:Button_Click(32))
at32.place(x = 765, y = 185)
at32.bind('<Enter>', entered32)
at32.bind('<Leave>', left32)

at33 = Button(win, text = "As", font = ('georgia', 15, 'bold'),width = 3, bg = '#ff55ff',command = lambda:Button_Click(33))
at33.place(x = 820, y = 185)
at33.bind('<Enter>', entered33)
at33.bind('<Leave>', left33)

at34 = Button(win, text = "Se", font = ('georgia', 15, 'bold'),width = 3, bg = '#1aff40',command = lambda:Button_Click(34))
at34.place(x = 875, y = 185)
at34.bind('<Enter>', entered34)
at34.bind('<Leave>', left34)

at35 = Button(win, text = "Br", font = ('georgia', 15, 'bold'),width = 3, bg = '#1aff40',command = lambda:Button_Click(35))
at35.place(x = 930, y = 185)
at35.bind('<Enter>', entered35)
at35.bind('<Leave>', left35)

at36 = Button(win, text = "Kr", font = ('georgia', 15, 'bold'),width = 3, bg = '#af7ffb',command = lambda:Button_Click(36))
at36.place(x = 985, y = 185)
at36.bind('<Enter>', entered36)
at36.bind('<Leave>', left36)

at37 = Button(win, text = "Rb ", font = ('georgia', 15, 'bold'),width = 3, bg = '#49c9ff',command = lambda:Button_Click(37))
at37.place(x = 50, y = 230)
at37.bind('<Enter>', entered37)
at37.bind('<Leave>', left37)

at38 = Button(win, text = "Sr", font = ('georgia', 15, 'bold'),width = 3, bg = '#adaeb0',command = lambda:Button_Click(38))
at38.place(x = 105, y = 230)
at38.bind('<Enter>', entered38)
at38.bind('<Leave>', left38)

at39 = Button(win, text = "Y", font = ('georgia', 15, 'bold'),width = 3, bg = 'yellow',command = lambda:Button_Click(39))
at39.place(x = 160, y = 230)
at39.bind('<Enter>', entered39)
at39.bind('<Leave>', left39)

at40 = Button(win, text = "Zr", font = ('georgia', 15, 'bold'),width = 3, bg = 'yellow',command = lambda:Button_Click(40))
at40.place(x = 215, y = 230)
at40.bind('<Enter>', entered40)
at40.bind('<Leave>', left40)

at41 = Button(win, text = "Nb", font = ('georgia', 15, 'bold'),width = 3, bg = 'yellow',command = lambda:Button_Click(41))
at41.place(x = 270, y = 230)
at41.bind('<Enter>', entered41)
at41.bind('<Leave>', left41)

at42 = Button(win, text = "Mo", font = ('georgia', 15, 'bold'),width = 3, bg = 'yellow',command = lambda:Button_Click(42))
at42.place(x = 325, y = 230)
at42.bind('<Enter>', entered42)
at42.bind('<Leave>', left42)

at43 = Button(win, text = "Tc", font = ('georgia', 15, 'bold'),width = 3, bg = 'yellow',command = lambda:Button_Click(43))
at43.place(x = 380, y = 230)
at43.bind('<Enter>', entered43)
at43.bind('<Leave>', left43)

at44 = Button(win, text = "Ru", font = ('georgia', 15, 'bold'),width = 3, bg = 'yellow',command = lambda:Button_Click(44))
at44.place(x = 435, y = 230)
at44.bind('<Enter>', entered44)
at44.bind('<Leave>', left44)

at45 = Button(win, text = "Rh", font = ('georgia', 15, 'bold'),width = 3, bg = 'yellow',command = lambda:Button_Click(45))
at45.place(x = 490, y = 230)
at45.bind('<Enter>', entered45)
at45.bind('<Leave>', left45)

at46 = Button(win, text = "Pd", font = ('georgia', 15, 'bold'),width = 3, bg = 'yellow',command = lambda:Button_Click(46))
at46.place(x = 545, y = 230)
at46.bind('<Enter>', entered46)
at46.bind('<Leave>', left46)

at47 = Button(win, text = "Ag", font = ('georgia', 15, 'bold'),width = 3, bg = 'yellow',command = lambda:Button_Click(47))
at47.place(x = 600, y = 230)
at47.bind('<Enter>', entered47)
at47.bind('<Leave>', left47)

at48 = Button(win, text = "Cd", font = ('georgia', 15, 'bold'),width = 3, bg = 'yellow',command = lambda:Button_Click(48))
at48.place(x = 655, y = 230)
at48.bind('<Enter>', entered48)
at48.bind('<Leave>', left48)

at49 = Button(win, text = "In", font = ('georgia', 15, 'bold'),width = 3, bg = '#ff5500',command = lambda:Button_Click(49))
at49.place(x = 710, y = 230)
at49.bind('<Enter>', entered49)
at49.bind('<Leave>', left49)

at50 = Button(win, text = "Sn", font = ('georgia', 15, 'bold'),width = 3, bg = '#ff5500',command = lambda:Button_Click(50))
at50.place(x = 765, y = 230)
at50.bind('<Enter>', entered50)
at50.bind('<Leave>', left50)

at51 = Button(win, text = "Sb", font = ('georgia', 15, 'bold'),width = 3, bg = '#ff55ff',command = lambda:Button_Click(51))
at51.place(x = 820, y = 230)
at51.bind('<Enter>', entered51)
at51.bind('<Leave>', left51)

at52 = Button(win, text = "Te", font = ('georgia', 15, 'bold'),width = 3, bg = '#ff55ff',command = lambda:Button_Click(52))
at52.place(x = 875, y = 230)
at52.bind('<Enter>', entered52)
at52.bind('<Leave>', left52)

at53 = Button(win, text = "I", font = ('georgia', 15, 'bold'),width = 3, bg = '#1aff40',command = lambda:Button_Click(53))
at53.place(x = 930, y = 230)
at53.bind('<Enter>', entered53)
at53.bind('<Leave>', left53)

at54 = Button(win, text = "Xe", font = ('georgia', 15, 'bold'),width = 3, bg = '#af7ffb',command = lambda:Button_Click(54))
at54.place(x = 985, y = 230)
at54.bind('<Enter>', entered54)
at54.bind('<Leave>', left54)

at55 = Button(win, text = "Cs", font = ('georgia', 15, 'bold'),width = 3, bg = '#49c9ff',command = lambda:Button_Click(55))
at55.place(x = 50, y = 275)
at55.bind('<Enter>', entered55)
at55.bind('<Leave>', left55)

at56 = Button(win, text = "Ba", font = ('georgia', 15, 'bold'),width = 3, bg = '#adaeb0',command = lambda:Button_Click(56))
at56.place(x = 105, y = 275)
at56.bind('<Enter>', entered56)
at56.bind('<Leave>', left56)

at57 = Button(win, text = "La", font = ('georgia', 15, 'bold'),width = 3, bg = '#bcc514',command = lambda:Button_Click(57))
at57.place(x = 160, y = 275)
at57.bind('<Enter>', entered57)
at57.bind('<Leave>', left57)

# Start of Lanthanides
at58 = Button(win, text = "Ce", font = ('georgia', 15, 'bold'),width = 3, bg = '#bcc514',command = lambda:Button_Click(58))
at58.place(x = 160, y = 420)
at58.bind('<Enter>', entered58)
at58.bind('<Leave>', left58)

at59 = Button(win, text = "Pr", font = ('georgia', 15, 'bold'),width = 3, bg = '#bcc514',command = lambda:Button_Click(59))
at59.place(x = 215, y = 420)
at59.bind('<Enter>', entered59)
at59.bind('<Leave>', left59)

at60 = Button(win, text = "Nd", font = ('georgia', 15, 'bold'),width = 3, bg = '#bcc514',command = lambda:Button_Click(60))
at60.place(x = 270, y = 420)
at60.bind('<Enter>', entered60)
at60.bind('<Leave>', left60)

at61 = Button(win, text = "Pm", font = ('georgia', 15, 'bold'),width = 3, bg = '#bcc514',command = lambda:Button_Click(61))
at61.place(x = 325, y = 420)
at61.bind('<Enter>', entered61)
at61.bind('<Leave>', left61)

at62 = Button(win, text = "Sm", font = ('georgia', 15, 'bold'),width = 3, bg = '#bcc514',command = lambda:Button_Click(62))
at62.place(x = 380, y = 420)
at62.bind('<Enter>', entered62)
at62.bind('<Leave>', left62)

at63 = Button(win, text = "Eu", font = ('georgia', 15, 'bold'),width = 3, bg = '#bcc514',command = lambda:Button_Click(63))
at63.place(x = 435, y = 420)
at63.bind('<Enter>', entered63)
at63.bind('<Leave>', left63)

at64 = Button(win, text = "Gd", font = ('georgia', 15, 'bold'),width = 3, bg = '#bcc514',command = lambda:Button_Click(64))
at64.place(x = 490, y = 420)
at64.bind('<Enter>', entered64)
at64.bind('<Leave>', left64)

at65 = Button(win, text = "Tb", font = ('georgia', 15, 'bold'),width = 3, bg = '#bcc514',command = lambda:Button_Click(65))
at65.place(x = 545, y = 420)
at65.bind('<Enter>', entered65)
at65.bind('<Leave>', left65)

at66 = Button(win, text = "Dy", font = ('georgia', 15, 'bold'),width = 3, bg = '#bcc514',command = lambda:Button_Click(66))
at66.place(x = 600, y = 420)
at66.bind('<Enter>', entered66)
at66.bind('<Leave>', left66)

at67 = Button(win, text = "Ho", font = ('georgia', 15, 'bold'),width = 3, bg = '#bcc514',command = lambda:Button_Click(67))
at67.place(x = 655, y = 420)
at67.bind('<Enter>', entered67)
at67.bind('<Leave>', left67)

at68 = Button(win, text = "Er", font = ('georgia', 15, 'bold'),width = 3, bg = '#bcc514',command = lambda:Button_Click(68))
at68.place(x = 710, y = 420)
at68.bind('<Enter>', entered68)
at68.bind('<Leave>', left68)

at69 = Button(win, text = "Tm", font = ('georgia', 15, 'bold'),width = 3, bg = '#bcc514',command = lambda:Button_Click(69))
at69.place(x = 765, y = 420)
at69.bind('<Enter>', entered69)
at69.bind('<Leave>', left69)

at70 = Button(win, text = "Yb", font = ('georgia', 15, 'bold'),width = 3, bg = '#bcc514',command = lambda:Button_Click(70))
at70.place(x = 820, y = 420)
at70.bind('<Enter>', entered70)
at70.bind('<Leave>', left70)

at71 = Button(win, text = "Lu", font = ('georgia', 15, 'bold'),width = 3, bg = '#bcc514',command = lambda:Button_Click(71))
at71.place(x = 875, y = 420)
at71.bind('<Enter>', entered71)
at71.bind('<Leave>', left71)

#End of Lanthanides

at72 = Button(win, text = "Hf", font = ('georgia', 15, 'bold'),width = 3, bg = 'yellow',command = lambda:Button_Click(72))
at72.place(x = 215, y = 275)
at72.bind('<Enter>', entered72)
at72.bind('<Leave>', left72)

at73 = Button(win, text = "Ta", font = ('georgia', 15, 'bold'),width = 3, bg = 'yellow',command = lambda:Button_Click(73))
at73.place(x = 270, y = 275)
at73.bind('<Enter>', entered73)
at73.bind('<Leave>', left73)

at74 = Button(win, text = "W", font = ('georgia', 15, 'bold'),width = 3, bg = 'yellow',command = lambda:Button_Click(74))
at74.place(x = 325, y = 275)
at74.bind('<Enter>', entered74)
at74.bind('<Leave>', left74)

at75 = Button(win, text = "Re", font = ('georgia', 15, 'bold'),width = 3, bg = 'yellow',command = lambda:Button_Click(75))
at75.place(x = 380, y = 275)
at75.bind('<Enter>', entered75)
at75.bind('<Leave>', left75)

at76 = Button(win, text = "Os", font = ('georgia', 15, 'bold'),width = 3, bg = 'yellow',command = lambda:Button_Click(76))
at76.place(x = 435, y = 275)
at76.bind('<Enter>', entered76)
at76.bind('<Leave>', left76)

at77 = Button(win, text = "Ir", font = ('georgia', 15, 'bold'),width = 3, bg = 'yellow',command = lambda:Button_Click(77))
at77.place(x = 490, y = 275)
at77.bind('<Enter>', entered77)
at77.bind('<Leave>', left77)

at78 = Button(win, text = "Pt", font = ('georgia', 15, 'bold'),width = 3, bg = 'yellow',command = lambda:Button_Click(78))
at78.place(x = 545, y = 275)
at78.bind('<Enter>', entered78)
at78.bind('<Leave>', left78)

at79 = Button(win, text = "Au", font = ('georgia', 15, 'bold'),width = 3, bg = 'yellow',command = lambda:Button_Click(79))
at79.place(x = 600, y = 275)
at79.bind('<Enter>', entered79)
at79.bind('<Leave>', left79)

at80 = Button(win, text = "Hg", font = ('georgia', 15, 'bold'),width = 3, bg = 'yellow',command = lambda:Button_Click(80))
at80.place(x = 655, y = 275)
at80.bind('<Enter>', entered80)
at80.bind('<Leave>', left80)

at81 = Button(win, text = "Tl", font = ('georgia', 15, 'bold'),width = 3, bg = '#ff5500',command = lambda:Button_Click(81))
at81.place(x = 710, y = 275)
at81.bind('<Enter>', entered81)
at81.bind('<Leave>', left81)

at82 = Button(win, text = "Pb", font = ('georgia', 15, 'bold'),width = 3, bg = '#ff5500',command = lambda:Button_Click(82))
at82.place(x = 765, y = 275)
at82.bind('<Enter>', entered82)
at82.bind('<Leave>', left82)

at83 = Button(win, text = "Bi", font = ('georgia', 15, 'bold'),width = 3, bg = '#ff5500',command = lambda:Button_Click(83))
at83.place(x = 820, y = 275)
at83.bind('<Enter>', entered83)
at83.bind('<Leave>', left83)

at84 = Button(win, text = "Po", font = ('georgia', 15, 'bold'),width = 3, bg = '#ff55ff',command = lambda:Button_Click(84))
at84.place(x = 875, y = 275)
at84.bind('<Enter>', entered84)
at84.bind('<Leave>', left84)

at85 = Button(win, text = "At", font = ('georgia', 15, 'bold'),width = 3, bg = '#ff55ff',command = lambda:Button_Click(85))
at85.place(x = 930, y = 275)
at85.bind('<Enter>', entered85)
at85.bind('<Leave>', left85)

at86 = Button(win, text = "Rn", font = ('georgia', 15, 'bold'),width = 3, bg = '#af7ffb',command = lambda:Button_Click(86))
at86.place(x = 985, y = 275)
at86.bind('<Enter>', entered86)
at86.bind('<Leave>', left86)

at87 = Button(win, text = "Fr", font = ('georgia', 15, 'bold'),width = 3, bg = '#49c9ff',command = lambda:Button_Click(87))
at87.place(x = 50, y = 320)
at87.bind('<Enter>', entered87)
at87.bind('<Leave>', left87)

at88 = Button(win, text = "Ra", font = ('georgia', 15, 'bold'),width = 3, bg = '#adaeb0',command = lambda:Button_Click(88))
at88.place(x = 105, y = 320)
at88.bind('<Enter>', entered88)
at88.bind('<Leave>', left88)

at89 = Button(win, text = "Ac", font = ('georgia', 15, 'bold'),width = 3, bg = '#ff910b',command = lambda:Button_Click(89))
at89.place(x = 160, y = 320)
at89.bind('<Enter>', entered89)
at89.bind('<Leave>', left89)

#Start of Actinindes
at90 = Button(win, text = "Th", font = ('georgia', 15, 'bold'),width = 3, bg = '#ff910b',command = lambda:Button_Click(90))
at90.place(x = 160, y = 465)
at90.bind('<Enter>', entered90)
at90.bind('<Leave>', left90)

at91 = Button(win, text = "Pa", font = ('georgia', 15, 'bold'),width = 3, bg = '#ff910b',command = lambda:Button_Click(91))
at91.place(x = 215, y = 465)
at91.bind('<Enter>', entered91)
at91.bind('<Leave>', left91)

at92 = Button(win, text = "U", font = ('georgia', 15, 'bold'),width = 3, bg = '#ff910b',command = lambda:Button_Click(92))
at92.place(x = 270, y = 465)
at92.bind('<Enter>', entered92)
at92.bind('<Leave>', left92)

at93 = Button(win, text = "Np", font = ('georgia', 15, 'bold'),width = 3, bg = '#ff910b',command = lambda:Button_Click(93))
at93.place(x = 325, y = 465)
at93.bind('<Enter>', entered93)
at93.bind('<Leave>', left93)

at94 = Button(win, text = "Pu", font = ('georgia', 15, 'bold'),width = 3, bg = '#ff910b',command = lambda:Button_Click(94))
at94.place(x = 380, y = 465)
at94.bind('<Enter>', entered94)
at94.bind('<Leave>', left94)

at95 = Button(win, text = "Am", font = ('georgia', 15, 'bold'),width = 3, bg = '#ff910b',command = lambda:Button_Click(95))
at95.place(x = 435, y = 465)
at95.bind('<Enter>', entered95)
at95.bind('<Leave>', left95)

at96 = Button(win, text = "Cm", font = ('georgia', 15, 'bold'),width = 3, bg = '#ff910b',command = lambda:Button_Click(96))
at96.place(x = 490, y = 465)
at96.bind('<Enter>', entered96)
at96.bind('<Leave>', left96)

at97 = Button(win, text = "Bk", font = ('georgia', 15, 'bold'),width = 3, bg = '#ff910b',command = lambda:Button_Click(97))
at97.place(x = 545, y = 465)
at97.bind('<Enter>', entered97)
at97.bind('<Leave>', left97)

at98 = Button(win, text = "Cf", font = ('georgia', 15, 'bold'),width = 3, bg = '#ff910b',command = lambda:Button_Click(98))
at98.place(x = 600, y = 465)
at98.bind('<Enter>', entered98)
at98.bind('<Leave>', left98)

at99 = Button(win, text = "Es", font = ('georgia', 15, 'bold'),width = 3, bg = '#ff910b',command = lambda:Button_Click(99))
at99.place(x = 655, y = 465)
at99.bind('<Enter>', entered99)
at99.bind('<Leave>', left99)

at100 = Button(win, text = "Fm", font = ('georgia', 15, 'bold'),width = 3, bg = '#ff910b',command = lambda:Button_Click(100))
at100.place(x = 710, y = 465)
at100.bind('<Enter>', entered100)
at100.bind('<Leave>', left100)

at101 = Button(win, text = "Md", font = ('georgia', 15, 'bold'),width = 3, bg = '#ff910b',command = lambda:Button_Click(101))
at101.place(x = 765, y = 465)
at101.bind('<Enter>', entered101)
at101.bind('<Leave>', left101)

at102 = Button(win, text = "No", font = ('georgia', 15, 'bold'),width = 3, bg = '#ff910b',command = lambda:Button_Click(102))
at102.place(x = 820, y = 465)
at102.bind('<Enter>', entered102)
at102.bind('<Leave>', left102)

at103 = Button(win, text = "Lr", font = ('georgia', 15, 'bold'),width = 3, bg = '#ff910b',command = lambda:Button_Click(103))
at103.place(x = 875, y = 465)
at103.bind('<Enter>', entered103)
at103.bind('<Leave>', left103)

#End of Actinindes

at104 = Button(win, text = "Rf", font = ('georgia', 15, 'bold'),width = 3, bg = 'yellow',command = lambda:Button_Click(104))
at104.place(x = 215, y = 320)
at104.bind('<Enter>', entered104)
at104.bind('<Leave>', left104)

at105 = Button(win, text = "Db", font = ('georgia', 15, 'bold'),width = 3, bg = 'yellow',command = lambda:Button_Click(105))
at105.place(x = 270, y = 320)
at105.bind('<Enter>', entered105)
at105.bind('<Leave>', left105)

at106 = Button(win, text = "Sg", font = ('georgia', 15, 'bold'),width = 3, bg = 'yellow',command = lambda:Button_Click(106))
at106.place(x = 325, y = 320)
at106.bind('<Enter>', entered106)
at106.bind('<Leave>', left106)

at107 = Button(win, text = "Bh", font = ('georgia', 15, 'bold'),width = 3, bg = 'yellow',command = lambda:Button_Click(107))
at107.place(x = 380, y = 320)
at107.bind('<Enter>', entered107)
at107.bind('<Leave>', left107)

at108 = Button(win, text = "Hs", font = ('georgia', 15, 'bold'),width = 3, bg = 'yellow',command = lambda:Button_Click(108))
at108.place(x = 435, y = 320)
at108.bind('<Enter>', entered108)
at108.bind('<Leave>', left108)

at109 = Button(win, text = "Mt", font = ('georgia', 15, 'bold'),width = 3, bg = 'yellow',command = lambda:Button_Click(109))
at109.place(x = 490, y = 320)
at109.bind('<Enter>', entered109)
at109.bind('<Leave>', left109)

at110 = Button(win, text = "Ds", font = ('georgia', 15, 'bold'),width = 3, bg = 'yellow',command = lambda:Button_Click(110))
at110.place(x = 545, y = 320)
at110.bind('<Enter>', entered110)
at110.bind('<Leave>', left110)

at111 = Button(win, text = "Rg", font = ('georgia', 15, 'bold'),width = 3, bg = 'yellow',command = lambda:Button_Click(111))
at111.place(x = 600, y = 320)
at111.bind('<Enter>', entered111)
at111.bind('<Leave>', left111)

at112 = Button(win, text = "Cn", font = ('georgia', 15, 'bold'),width = 3, bg = 'yellow',command = lambda:Button_Click(112))
at112.place(x = 655, y = 320)
at112.bind('<Enter>', entered112)
at112.bind('<Leave>', left112)

at113 = Button(win, text = "Nh", font = ('georgia', 15, 'bold'),width = 3, bg = '#ff5500',command = lambda:Button_Click(113))
at113.place(x = 710, y = 320)
at113.bind('<Enter>', entered113)
at113.bind('<Leave>', left113)

at114 = Button(win, text = "Fl", font = ('georgia', 15, 'bold'),width = 3, bg = '#ff5500',command = lambda:Button_Click(114))
at114.place(x = 765, y = 320)
at114.bind('<Enter>', entered114)
at114.bind('<Leave>', left114)

at115 = Button(win, text = "Mc", font = ('georgia', 15, 'bold'),width = 3, bg = '#ff5500',command = lambda:Button_Click(115))
at115.place(x = 820, y = 320)
at115.bind('<Enter>', entered115)
at115.bind('<Leave>', left115)

at116 = Button(win, text = "Lv", font = ('georgia', 15, 'bold'),width = 3, bg = '#ff5500',command = lambda:Button_Click(116))
at116.place(x = 875, y = 320)
at116.bind('<Enter>', entered116)
at116.bind('<Leave>', left116)

at117 = Button(win, text = "Ts", font = ('georgia', 15, 'bold'),width = 3, bg = '#ff5500',command = lambda:Button_Click(117))
at117.place(x = 930, y = 320)
at117.bind('<Enter>', entered117)
at117.bind('<Leave>', left117)

at118 = Button(win, text = "Og", font = ('georgia', 15, 'bold'),width = 3, bg = '#af7ffb',command = lambda:Button_Click(118))
at118.place(x = 985, y = 320)
at118.bind('<Enter>', entered118)
at118.bind('<Leave>', left118)
# End of Elements

p_1 = Label(win, text = 'P - 1', bg = '#f7e7ff', font = ('baskeville old face',13, 'bold'))
p_1.place(x = 5, y = 58)

p_2 = Label(win, text = 'P - 2', bg = '#f7e7ff', font = ('baskeville old face',13, 'bold'))
p_2.place(x = 5, y = 102)

p_3 = Label(win, text = 'P - 3', bg = '#f7e7ff', font = ('baskeville old face',13, 'bold'))
p_3.place(x = 5, y = 148)

p_4 = Label(win, text = 'P - 4', bg = '#f7e7ff', font = ('baskeville old face',13, 'bold'))
p_4.place(x = 5, y = 191)

p_5 = Label(win, text = 'P - 5', bg = '#f7e7ff', font = ('baskeville old face',13, 'bold'))
p_5.place(x = 5, y = 238)

p_6 = Label(win, text = 'P - 6', bg = '#f7e7ff', font = ('baskeville old face',13, 'bold'))
p_6.place(x = 5, y = 285)

p_7 = Label(win, text = 'P - 7', bg = '#f7e7ff', font = ('baskeville old face',13, 'bold'))
p_7.place(x = 5, y = 327)

lantha = Label(win, text = 'Lanthanoids', bg = '#f7e7ff', font = ('baskeville old face',13, 'bold'))
lantha.place(x = 50, y = 428)

actan = Label(win, text = 'Actinoids', bg = '#f7e7ff', font = ('baskeville old face',13, 'bold'))
actan.place(x = 75, y = 473)

g1 = Label (win,text = '1', bg = '#f7e7ff', font = ('baskeville old face',13, 'bold') ) 
g1.place(x = 63, y = 25)

g2 = Label (win,text = '2', bg = '#f7e7ff', font = ('baskeville old face',13, 'bold') ) 
g2.place(x = 120, y = 68)

g3 = Label (win,text = '3', bg = '#f7e7ff', font = ('baskeville old face',13, 'bold') ) 
g3.place(x = 178, y = 160)

g4 = Label (win,text = '4', bg = '#f7e7ff', font = ('baskeville old face',13, 'bold') ) 
g4.place(x = 230, y = 160)

g5 = Label (win,text = '5', bg = '#f7e7ff', font = ('baskeville old face',13, 'bold') ) 
g5.place(x = 284, y = 160)

g6 = Label (win,text = '6', bg = '#f7e7ff', font = ('baskeville old face',13, 'bold') ) 
g6.place(x = 338, y = 160)

g7 = Label (win,text = '7', bg = '#f7e7ff', font = ('baskeville old face',13, 'bold') ) 
g7.place(x = 394, y = 160)

g8 = Label (win,text = '8', bg = '#f7e7ff', font = ('baskeville old face',13, 'bold') ) 
g8.place(x = 450, y = 160)

g9 = Label (win,text = '9', bg = '#f7e7ff', font = ('baskeville old face',13, 'bold') ) 
g9.place(x = 508, y = 160)

g10 = Label (win,text = '10', bg = '#f7e7ff', font = ('baskeville old face',13, 'bold') ) 
g10.place(x = 558, y = 160)

g11 = Label (win,text = '11', bg = '#f7e7ff', font = ('baskeville old face',13, 'bold') ) 
g11.place(x = 610, y = 160)

g12 = Label (win,text = '12', bg = '#f7e7ff', font = ('baskeville old face',13, 'bold') ) 
g12.place(x = 664, y = 160)

g13 = Label (win,text = '13', bg = '#f7e7ff', font = ('baskeville old face',13, 'bold') ) 
g13.place(x = 722, y = 68)

g14 = Label (win,text = '14', bg = '#f7e7ff', font = ('baskeville old face',13, 'bold') ) 
g14.place(x = 778, y = 68)

g15 = Label (win,text = '15', bg = '#f7e7ff', font = ('baskeville old face',13, 'bold') ) 
g15.place(x = 832, y = 68)

g16 = Label (win,text = '16', bg = '#f7e7ff', font = ('baskeville old face',13, 'bold') ) 
g16.place(x = 888, y = 68)

g17 = Label (win,text = '17', bg = '#f7e7ff', font = ('baskeville old face',13, 'bold') ) 
g17.place(x = 944, y = 68)

g18 = Label (win,text = '18', bg = '#f7e7ff', font = ('baskeville old face',13, 'bold') ) 
g18.place(x = 998, y = 25)




def AlkaliMetals(event):
    at1.configure(bg = 'black')
    at2.configure(bg = 'black')
    at3.configure(bg = '#49c9ff')
    at4.configure(bg = 'black')
    at5.configure(bg = 'black')
    at6.configure(bg = 'black')
    at7.configure(bg = 'black')
    at8.configure(bg = 'black')
    at9.configure(bg = 'black')
    at10.configure(bg = 'black')
    at11.configure(bg = '#49c9ff')
    at12.configure(bg = 'black')
    at13.configure(bg = 'black')
    at14.configure(bg = 'black')
    at15.configure(bg = 'black')
    at16.configure(bg = 'black')
    at17.configure(bg = 'black')
    at18.configure(bg = 'black')
    at19.configure(bg = '#49c9ff')
    at20.configure(bg = 'black')
    at21.configure(bg = 'black')
    at22.configure(bg = 'black')
    at23.configure(bg = 'black')
    at24.configure(bg = 'black')
    at25.configure(bg = 'black')
    at26.configure(bg = 'black')
    at27.configure(bg = 'black')
    at28.configure(bg = 'black')
    at29.configure(bg = 'black')
    at30.configure(bg = 'black')
    at31.configure(bg = 'black')
    at32.configure(bg = 'black')
    at33.configure(bg = 'black')
    at34.configure(bg = 'black')
    at35.configure(bg = 'black')
    at36.configure(bg = 'black')
    at37.configure(bg = '#49c9ff')
    at38.configure(bg = 'black')
    at39.configure(bg = 'black')
    at40.configure(bg = 'black')
    at41.configure(bg = 'black')
    at42.configure(bg = 'black')
    at43.configure(bg = 'black')
    at44.configure(bg = 'black')
    at45.configure(bg = 'black')
    at46.configure(bg = 'black')
    at47.configure(bg = 'black')
    at48.configure(bg = 'black')
    at49.configure(bg = 'black')
    at50.configure(bg = 'black')
    at51.configure(bg = 'black')
    at52.configure(bg = 'black')
    at53.configure(bg = 'black')
    at54.configure(bg = 'black')
    at55.configure(bg = '#49c9ff')
    at56.configure(bg = 'black')
    at57.configure(bg = 'black')
    at58.configure(bg = 'black')
    at59.configure(bg = 'black')
    at60.configure(bg = 'black')
    at61.configure(bg = 'black')
    at62.configure(bg = 'black')
    at63.configure(bg = 'black')
    at64.configure(bg = 'black')
    at65.configure(bg = 'black')
    at66.configure(bg = 'black')
    at67.configure(bg = 'black')
    at68.configure(bg = 'black')
    at69.configure(bg = 'black')
    at70.configure(bg = 'black')
    at71.configure(bg = 'black')
    at72.configure(bg = 'black')
    at73.configure(bg = 'black')
    at74.configure(bg = 'black')
    at75.configure(bg = 'black')
    at76.configure(bg = 'black')
    at77.configure(bg = 'black')
    at78.configure(bg = 'black')
    at79.configure(bg = 'black')
    at80.configure(bg = 'black')
    at81.configure(bg = 'black')
    at82.configure(bg = 'black')
    at83.configure(bg = 'black')
    at84.configure(bg = 'black')
    at85.configure(bg = 'black')
    at86.configure(bg = 'black')
    at87.configure(bg = '#49c9ff')
    at88.configure(bg = 'black')
    at89.configure(bg = 'black')
    at90.configure(bg = 'black')
    at91.configure(bg = 'black')
    at92.configure(bg = 'black')
    at93.configure(bg = 'black')
    at94.configure(bg = 'black')
    at95.configure(bg = 'black')
    at96.configure(bg = 'black')
    at97.configure(bg = 'black')
    at98.configure(bg = 'black')
    at99.configure(bg = 'black')
    at100.configure(bg = 'black')
    at101.configure(bg = 'black')
    at102.configure(bg = 'black')
    at103.configure(bg = 'black')
    at104.configure(bg = 'black')
    at105.configure(bg = 'black')
    at106.configure(bg = 'black')
    at107.configure(bg = 'black')
    at108.configure(bg = 'black')
    at109.configure(bg = 'black')
    at110.configure(bg = 'black')
    at111.configure(bg = 'black')
    at112.configure(bg = 'black')
    at113.configure(bg = 'black')
    at114.configure(bg = 'black')
    at115.configure(bg = 'black')
    at116.configure(bg = 'black')
    at117.configure(bg = 'black')
    at118.configure(bg = 'black')
    

def AlkaliMetalsleft(event):
    at1.configure(bg = '#f13800')
    at2.configure(bg = '#af7ffb')
    at3.configure(bg = '#49c9ff')
    at4.configure(bg = '#adaeb0')
    at5.configure(bg = '#1aff40')
    at6.configure(bg = '#1aff40')
    at7.configure(bg = '#1aff40')
    at8.configure(bg = '#1aff40')
    at9.configure(bg = '#1aff40')
    at10.configure(bg = '#af7ffb')
    at11.configure(bg = '#49c9ff')
    at12.configure(bg = '#adaeb0')
    at13.configure(bg = '#ff5500')
    at14.configure(bg = '#ff55ff')
    at15.configure(bg = '#1aff40')
    at16.configure(bg = '#1aff40')
    at17.configure(bg = '#1aff40')
    at18.configure(bg = '#af7ffb')
    at19.configure(bg = '#49c9ff')
    at20.configure(bg = '#adaeb0')
    at21.configure(bg = 'yellow')
    at22.configure(bg = 'yellow')
    at23.configure(bg = 'yellow')
    at24.configure(bg = 'yellow')
    at25.configure(bg = 'yellow')
    at26.configure(bg = 'yellow')
    at27.configure(bg = 'yellow')
    at28.configure(bg = 'yellow')
    at29.configure(bg = 'yellow')
    at30.configure(bg = 'yellow')
    at31.configure(bg = '#ff5500')
    at32.configure(bg = '#ff55ff')
    at33.configure(bg = '#ff55ff')
    at34.configure(bg = '#1aff40')
    at35.configure(bg = '#1aff40')
    at36.configure(bg = '#af7ffb')
    at37.configure(bg = '#49c9ff')
    at38.configure(bg = '#adaeb0')
    at39.configure(bg = 'yellow')
    at40.configure(bg = 'yellow')
    at41.configure(bg = 'yellow')
    at42.configure(bg = 'yellow')
    at43.configure(bg = 'yellow')
    at44.configure(bg = 'yellow')
    at45.configure(bg = 'yellow')
    at46.configure(bg = 'yellow')
    at47.configure(bg = 'yellow')
    at48.configure(bg = 'yellow')
    at49.configure(bg = '#ff5500')
    at50.configure(bg = '#ff5500')
    at51.configure(bg = '#ff55ff')
    at52.configure(bg = '#ff55ff')
    at53.configure(bg = '#1aff40')
    at54.configure(bg = '#af7ffb')
    at55.configure(bg = '#49c9ff')
    at56.configure(bg = '#adaeb0')
    at57.configure(bg = '#bcc514')
    at58.configure(bg = '#bcc514')
    at59.configure(bg = '#bcc514')
    at60.configure(bg = '#bcc514')
    at61.configure(bg = '#bcc514')
    at62.configure(bg = '#bcc514')
    at63.configure(bg = '#bcc514')
    at64.configure(bg = '#bcc514')
    at65.configure(bg = '#bcc514')
    at66.configure(bg = '#bcc514')
    at67.configure(bg = '#bcc514')
    at68.configure(bg = '#bcc514')
    at69.configure(bg = '#bcc514')
    at70.configure(bg = '#bcc514')
    at71.configure(bg = '#bcc514')
    at72.configure(bg = 'yellow')
    at73.configure(bg = 'yellow')
    at74.configure(bg = 'yellow')
    at75.configure(bg = 'yellow')
    at76.configure(bg = 'yellow')
    at77.configure(bg = 'yellow')
    at78.configure(bg = 'yellow')
    at79.configure(bg = 'yellow')
    at80.configure(bg = 'yellow')
    at81.configure(bg = '#ff5500')
    at82.configure(bg = '#ff5500')
    at83.configure(bg = '#ff5500')
    at84.configure(bg = '#ff55ff')
    at85.configure(bg = '#ff55ff')
    at86.configure(bg = '#af7ffb')
    at87.configure(bg = '#49c9ff')
    at88.configure(bg = '#adaeb0')
    at89.configure(bg = '#ff910b')
    at90.configure(bg = '#ff910b')
    at91.configure(bg = '#ff910b')
    at92.configure(bg = '#ff910b')
    at93.configure(bg = '#ff910b')
    at94.configure(bg = '#ff910b')
    at95.configure(bg = '#ff910b')
    at96.configure(bg = '#ff910b')
    at97.configure(bg = '#ff910b')
    at98.configure(bg = '#ff910b')
    at99.configure(bg = '#ff910b')
    at100.configure(bg = '#ff910b')
    at101.configure(bg = '#ff910b')
    at102.configure(bg = '#ff910b')
    at103.configure(bg = '#ff910b')
    at104.configure(bg = 'yellow')
    at105.configure(bg = 'yellow')
    at106.configure(bg = 'yellow')
    at107.configure(bg = 'yellow')
    at108.configure(bg = 'yellow')
    at109.configure(bg = 'yellow')
    at110.configure(bg = 'yellow')
    at111.configure(bg = 'yellow')
    at112.configure(bg = 'yellow')
    at113.configure(bg = '#ff5500')
    at114.configure(bg = '#ff5500')
    at115.configure(bg = '#ff5500')
    at116.configure(bg = '#ff5500')
    at117.configure(bg = '#ff5500')
    at118.configure(bg = '#af7ffb')

def alkalineentered(event):
    at1.configure(bg = 'black')
    at2.configure(bg = 'black')
    at3.configure(bg = 'black')
    at4.configure(bg = '#adaeb0')
    at5.configure(bg = 'black')
    at6.configure(bg = 'black')
    at7.configure(bg = 'black')
    at8.configure(bg = 'black')
    at9.configure(bg = 'black')
    at10.configure(bg = 'black')
    at11.configure(bg = 'black')
    at12.configure(bg = '#adaeb0')
    at13.configure(bg = 'black')
    at14.configure(bg = 'black')
    at15.configure(bg = 'black')
    at16.configure(bg = 'black')
    at17.configure(bg = 'black')
    at18.configure(bg = 'black')
    at19.configure(bg = 'black')
    at20.configure(bg = '#adaeb0')
    at21.configure(bg = 'black')
    at22.configure(bg = 'black')
    at23.configure(bg = 'black')
    at24.configure(bg = 'black')
    at25.configure(bg = 'black')
    at26.configure(bg = 'black')
    at27.configure(bg = 'black')
    at28.configure(bg = 'black')
    at29.configure(bg = 'black')
    at30.configure(bg = 'black')
    at31.configure(bg = 'black')
    at32.configure(bg = 'black')
    at33.configure(bg = 'black')
    at34.configure(bg = 'black')
    at35.configure(bg = 'black')
    at36.configure(bg = 'black')
    at37.configure(bg = 'black')
    at38.configure(bg ='#adaeb0')
    at39.configure(bg = 'black')
    at40.configure(bg = 'black')
    at41.configure(bg = 'black')
    at42.configure(bg = 'black')
    at43.configure(bg = 'black')
    at44.configure(bg = 'black')
    at45.configure(bg = 'black')
    at46.configure(bg = 'black')
    at47.configure(bg = 'black')
    at48.configure(bg = 'black')
    at49.configure(bg = 'black')
    at50.configure(bg = 'black')
    at51.configure(bg = 'black')
    at52.configure(bg = 'black')
    at53.configure(bg = 'black')
    at54.configure(bg = 'black')
    at55.configure(bg = 'black')
    at56.configure(bg = '#adaeb0')
    at57.configure(bg = 'black')
    at58.configure(bg = 'black')
    at59.configure(bg = 'black')
    at60.configure(bg = 'black')
    at61.configure(bg = 'black')
    at62.configure(bg = 'black')
    at63.configure(bg = 'black')
    at64.configure(bg = 'black')
    at65.configure(bg = 'black')
    at66.configure(bg = 'black')
    at67.configure(bg = 'black')
    at68.configure(bg = 'black')
    at69.configure(bg = 'black')
    at70.configure(bg = 'black')
    at71.configure(bg = 'black')
    at72.configure(bg = 'black')
    at73.configure(bg = 'black')
    at74.configure(bg = 'black')
    at75.configure(bg = 'black')
    at76.configure(bg = 'black')
    at77.configure(bg = 'black')
    at78.configure(bg = 'black')
    at79.configure(bg = 'black')
    at80.configure(bg = 'black')
    at81.configure(bg = 'black')
    at82.configure(bg = 'black')
    at83.configure(bg = 'black')
    at84.configure(bg = 'black')
    at85.configure(bg = 'black')
    at86.configure(bg = 'black')
    at87.configure(bg = 'black')
    at88.configure(bg = '#adaeb0')
    at89.configure(bg = 'black')
    at90.configure(bg = 'black')
    at91.configure(bg = 'black')
    at92.configure(bg = 'black')
    at93.configure(bg = 'black')
    at94.configure(bg = 'black')
    at95.configure(bg = 'black')
    at96.configure(bg = 'black')
    at97.configure(bg = 'black')
    at98.configure(bg = 'black')
    at99.configure(bg = 'black')
    at100.configure(bg = 'black')
    at101.configure(bg = 'black')
    at102.configure(bg = 'black')
    at103.configure(bg = 'black')
    at104.configure(bg = 'black')
    at105.configure(bg = 'black')
    at106.configure(bg = 'black')
    at107.configure(bg = 'black')
    at108.configure(bg = 'black')
    at109.configure(bg = 'black')
    at110.configure(bg = 'black')
    at111.configure(bg = 'black')
    at112.configure(bg = 'black')
    at113.configure(bg = 'black')
    at114.configure(bg = 'black')
    at115.configure(bg = 'black')
    at116.configure(bg = 'black')
    at117.configure(bg = 'black')
    at118.configure(bg = 'black')

def alkalineleft(event):
    at1.configure(bg = '#f13800')
    at2.configure(bg = '#af7ffb')
    at3.configure(bg = '#49c9ff')
    at4.configure(bg = '#adaeb0')
    at5.configure(bg = '#1aff40')
    at6.configure(bg = '#1aff40')
    at7.configure(bg = '#1aff40')
    at8.configure(bg = '#1aff40')
    at9.configure(bg = '#1aff40')
    at10.configure(bg = '#af7ffb')
    at11.configure(bg = '#49c9ff')
    at12.configure(bg = '#adaeb0')
    at13.configure(bg = '#ff5500')
    at14.configure(bg = '#ff55ff')
    at15.configure(bg = '#1aff40')
    at16.configure(bg = '#1aff40')
    at17.configure(bg = '#1aff40')
    at18.configure(bg = '#af7ffb')
    at19.configure(bg = '#49c9ff')
    at20.configure(bg = '#adaeb0')
    at21.configure(bg = 'yellow')
    at22.configure(bg = 'yellow')
    at23.configure(bg = 'yellow')
    at24.configure(bg = 'yellow')
    at25.configure(bg = 'yellow')
    at26.configure(bg = 'yellow')
    at27.configure(bg = 'yellow')
    at28.configure(bg = 'yellow')
    at29.configure(bg = 'yellow')
    at30.configure(bg = 'yellow')
    at31.configure(bg = '#ff5500')
    at32.configure(bg = '#ff55ff')
    at33.configure(bg = '#ff55ff')
    at34.configure(bg = '#1aff40')
    at35.configure(bg = '#1aff40')
    at36.configure(bg = '#af7ffb')
    at37.configure(bg = '#49c9ff')
    at38.configure(bg = '#adaeb0')
    at39.configure(bg = 'yellow')
    at40.configure(bg = 'yellow')
    at41.configure(bg = 'yellow')
    at42.configure(bg = 'yellow')
    at43.configure(bg = 'yellow')
    at44.configure(bg = 'yellow')
    at45.configure(bg = 'yellow')
    at46.configure(bg = 'yellow')
    at47.configure(bg = 'yellow')
    at48.configure(bg = 'yellow')
    at49.configure(bg = '#ff5500')
    at50.configure(bg = '#ff5500')
    at51.configure(bg = '#ff55ff')
    at52.configure(bg = '#ff55ff')
    at53.configure(bg = '#1aff40')
    at54.configure(bg = '#af7ffb')
    at55.configure(bg = '#49c9ff')
    at56.configure(bg = '#adaeb0')
    at57.configure(bg = '#bcc514')
    at58.configure(bg = '#bcc514')
    at59.configure(bg = '#bcc514')
    at60.configure(bg = '#bcc514')
    at61.configure(bg = '#bcc514')
    at62.configure(bg = '#bcc514')
    at63.configure(bg = '#bcc514')
    at64.configure(bg = '#bcc514')
    at65.configure(bg = '#bcc514')
    at66.configure(bg = '#bcc514')
    at67.configure(bg = '#bcc514')
    at68.configure(bg = '#bcc514')
    at69.configure(bg = '#bcc514')
    at70.configure(bg = '#bcc514')
    at71.configure(bg = '#bcc514')
    at72.configure(bg = 'yellow')
    at73.configure(bg = 'yellow')
    at74.configure(bg = 'yellow')
    at75.configure(bg = 'yellow')
    at76.configure(bg = 'yellow')
    at77.configure(bg = 'yellow')
    at78.configure(bg = 'yellow')
    at79.configure(bg = 'yellow')
    at80.configure(bg = 'yellow')
    at81.configure(bg = '#ff5500')
    at82.configure(bg = '#ff5500')
    at83.configure(bg = '#ff5500')
    at84.configure(bg = '#ff55ff')
    at85.configure(bg = '#ff55ff')
    at86.configure(bg = '#af7ffb')
    at87.configure(bg = '#49c9ff')
    at88.configure(bg = '#adaeb0')
    at89.configure(bg = '#ff910b')
    at90.configure(bg = '#ff910b')
    at91.configure(bg = '#ff910b')
    at92.configure(bg = '#ff910b')
    at93.configure(bg = '#ff910b')
    at94.configure(bg = '#ff910b')
    at95.configure(bg = '#ff910b')
    at96.configure(bg = '#ff910b')
    at97.configure(bg = '#ff910b')
    at98.configure(bg = '#ff910b')
    at99.configure(bg = '#ff910b')
    at100.configure(bg = '#ff910b')
    at101.configure(bg = '#ff910b')
    at102.configure(bg = '#ff910b')
    at103.configure(bg = '#ff910b')
    at104.configure(bg = 'yellow')
    at105.configure(bg = 'yellow')
    at106.configure(bg = 'yellow')
    at107.configure(bg = 'yellow')
    at108.configure(bg = 'yellow')
    at109.configure(bg = 'yellow')
    at110.configure(bg = 'yellow')
    at111.configure(bg = 'yellow')
    at112.configure(bg = 'yellow')
    at113.configure(bg = '#ff5500')
    at114.configure(bg = '#ff5500')
    at115.configure(bg = '#ff5500')
    at116.configure(bg = '#ff5500')
    at117.configure(bg = '#ff5500')
    at118.configure(bg = '#af7ffb')

def transitionentered(event):
    at1.configure(bg = 'black')
    at2.configure(bg = 'black')
    at3.configure(bg = 'black')
    at4.configure(bg = 'black')
    at5.configure(bg = 'black')
    at6.configure(bg = 'black')
    at7.configure(bg = 'black')
    at8.configure(bg = 'black')
    at9.configure(bg = 'black')
    at10.configure(bg = 'black')
    at11.configure(bg = 'black')
    at12.configure(bg = 'black')
    at13.configure(bg = 'black')
    at14.configure(bg = 'black')
    at15.configure(bg = 'black')
    at16.configure(bg = 'black')
    at17.configure(bg = 'black')
    at18.configure(bg = 'black')
    at19.configure(bg = 'black')
    at20.configure(bg = 'black')
    at21.configure(bg = 'yellow')
    at22.configure(bg = 'yellow')
    at23.configure(bg = 'yellow')
    at24.configure(bg = 'yellow')
    at25.configure(bg = 'yellow')
    at26.configure(bg = 'yellow')
    at27.configure(bg = 'yellow')
    at28.configure(bg = 'yellow')
    at29.configure(bg = 'yellow')
    at30.configure(bg = 'yellow')
    at31.configure(bg = 'black')
    at32.configure(bg = 'black')
    at33.configure(bg = 'black')
    at34.configure(bg = 'black')
    at35.configure(bg = 'black')
    at36.configure(bg = 'black')
    at37.configure(bg = 'black')
    at38.configure(bg = 'black')
    at39.configure(bg = 'yellow')
    at40.configure(bg = 'yellow')
    at41.configure(bg = 'yellow')
    at42.configure(bg = 'yellow')
    at43.configure(bg = 'yellow')
    at44.configure(bg = 'yellow')
    at45.configure(bg = 'yellow')
    at46.configure(bg = 'yellow')
    at47.configure(bg = 'yellow')
    at48.configure(bg = 'yellow')
    at49.configure(bg = 'black')
    at50.configure(bg = 'black')
    at51.configure(bg = 'black')
    at52.configure(bg = 'black')
    at53.configure(bg = 'black')
    at54.configure(bg = 'black')
    at55.configure(bg = 'black')
    at56.configure(bg = 'black')
    at57.configure(bg = 'black')
    at58.configure(bg = 'black')
    at59.configure(bg = 'black')
    at60.configure(bg = 'black')
    at61.configure(bg = 'black')
    at62.configure(bg = 'black')
    at63.configure(bg = 'black')
    at64.configure(bg = 'black')
    at65.configure(bg = 'black')
    at66.configure(bg = 'black')
    at67.configure(bg = 'black')
    at68.configure(bg = 'black')
    at69.configure(bg = 'black')
    at70.configure(bg = 'black')
    at71.configure(bg = 'black')
    at72.configure(bg = 'yellow')
    at73.configure(bg = 'yellow')
    at74.configure(bg = 'yellow')
    at75.configure(bg = 'yellow')
    at76.configure(bg = 'yellow')
    at77.configure(bg = 'yellow')
    at78.configure(bg = 'yellow')
    at79.configure(bg = 'yellow')
    at80.configure(bg = 'yellow')
    at81.configure(bg = 'black')
    at82.configure(bg = 'black')
    at83.configure(bg = 'black')
    at84.configure(bg = 'black')
    at85.configure(bg = 'black')
    at86.configure(bg = 'black')
    at87.configure(bg = 'black')
    at88.configure(bg = 'black')
    at89.configure(bg = 'black')
    at90.configure(bg = 'black')
    at91.configure(bg = 'black')
    at92.configure(bg = 'black')
    at93.configure(bg = 'black')
    at94.configure(bg = 'black')
    at95.configure(bg = 'black')
    at96.configure(bg = 'black')
    at97.configure(bg = 'black')
    at98.configure(bg = 'black')
    at99.configure(bg = 'black')
    at100.configure(bg = 'black')
    at101.configure(bg = 'black')
    at102.configure(bg = 'black')
    at103.configure(bg = 'black')
    at104.configure(bg = 'yellow')
    at105.configure(bg = 'yellow')
    at106.configure(bg = 'yellow')
    at107.configure(bg = 'yellow')
    at108.configure(bg = 'yellow')
    at109.configure(bg = 'yellow')
    at110.configure(bg = 'yellow')
    at111.configure(bg = 'yellow')
    at112.configure(bg = 'yellow')
    at113.configure(bg = 'black')
    at114.configure(bg = 'black')
    at115.configure(bg = 'black')
    at116.configure(bg = 'black')
    at117.configure(bg = 'black')
    at118.configure(bg = 'black')

def transitionleft(event):
    at1.configure(bg = '#f13800')
    at2.configure(bg = '#af7ffb')
    at3.configure(bg = '#49c9ff')
    at4.configure(bg = '#adaeb0')
    at5.configure(bg = '#1aff40')
    at6.configure(bg = '#1aff40')
    at7.configure(bg = '#1aff40')
    at8.configure(bg = '#1aff40')
    at9.configure(bg = '#1aff40')
    at10.configure(bg = '#af7ffb')
    at11.configure(bg = '#49c9ff')
    at12.configure(bg = '#adaeb0')
    at13.configure(bg = '#ff5500')
    at14.configure(bg = '#ff55ff')
    at15.configure(bg = '#1aff40')
    at16.configure(bg = '#1aff40')
    at17.configure(bg = '#1aff40')
    at18.configure(bg = '#af7ffb')
    at19.configure(bg = '#49c9ff')
    at20.configure(bg = '#adaeb0')
    at21.configure(bg = 'yellow')
    at22.configure(bg = 'yellow')
    at23.configure(bg = 'yellow')
    at24.configure(bg = 'yellow')
    at25.configure(bg = 'yellow')
    at26.configure(bg = 'yellow')
    at27.configure(bg = 'yellow')
    at28.configure(bg = 'yellow')
    at29.configure(bg = 'yellow')
    at30.configure(bg = 'yellow')
    at31.configure(bg = '#ff5500')
    at32.configure(bg = '#ff55ff')
    at33.configure(bg = '#ff55ff')
    at34.configure(bg = '#1aff40')
    at35.configure(bg = '#1aff40')
    at36.configure(bg = '#af7ffb')
    at37.configure(bg = '#49c9ff')
    at38.configure(bg = '#adaeb0')
    at39.configure(bg = 'yellow')
    at40.configure(bg = 'yellow')
    at41.configure(bg = 'yellow')
    at42.configure(bg = 'yellow')
    at43.configure(bg = 'yellow')
    at44.configure(bg = 'yellow')
    at45.configure(bg = 'yellow')
    at46.configure(bg = 'yellow')
    at47.configure(bg = 'yellow')
    at48.configure(bg = 'yellow')
    at49.configure(bg = '#ff5500')
    at50.configure(bg = '#ff5500')
    at51.configure(bg = '#ff55ff')
    at52.configure(bg = '#ff55ff')
    at53.configure(bg = '#1aff40')
    at54.configure(bg = '#af7ffb')
    at55.configure(bg = '#49c9ff')
    at56.configure(bg = '#adaeb0')
    at57.configure(bg = '#bcc514')
    at58.configure(bg = '#bcc514')
    at59.configure(bg = '#bcc514')
    at60.configure(bg = '#bcc514')
    at61.configure(bg = '#bcc514')
    at62.configure(bg = '#bcc514')
    at63.configure(bg = '#bcc514')
    at64.configure(bg = '#bcc514')
    at65.configure(bg = '#bcc514')
    at66.configure(bg = '#bcc514')
    at67.configure(bg = '#bcc514')
    at68.configure(bg = '#bcc514')
    at69.configure(bg = '#bcc514')
    at70.configure(bg = '#bcc514')
    at71.configure(bg = '#bcc514')
    at72.configure(bg = 'yellow')
    at73.configure(bg = 'yellow')
    at74.configure(bg = 'yellow')
    at75.configure(bg = 'yellow')
    at76.configure(bg = 'yellow')
    at77.configure(bg = 'yellow')
    at78.configure(bg = 'yellow')
    at79.configure(bg = 'yellow')
    at80.configure(bg = 'yellow')
    at81.configure(bg = '#ff5500')
    at82.configure(bg = '#ff5500')
    at83.configure(bg = '#ff5500')
    at84.configure(bg = '#ff55ff')
    at85.configure(bg = '#ff55ff')
    at86.configure(bg = '#af7ffb')
    at87.configure(bg = '#49c9ff')
    at88.configure(bg = '#adaeb0')
    at89.configure(bg = '#ff910b')
    at90.configure(bg = '#ff910b')
    at91.configure(bg = '#ff910b')
    at92.configure(bg = '#ff910b')
    at93.configure(bg = '#ff910b')
    at94.configure(bg = '#ff910b')
    at95.configure(bg = '#ff910b')
    at96.configure(bg = '#ff910b')
    at97.configure(bg = '#ff910b')
    at98.configure(bg = '#ff910b')
    at99.configure(bg = '#ff910b')
    at100.configure(bg = '#ff910b')
    at101.configure(bg = '#ff910b')
    at102.configure(bg = '#ff910b')
    at103.configure(bg = '#ff910b')
    at104.configure(bg = 'yellow')
    at105.configure(bg = 'yellow')
    at106.configure(bg = 'yellow')
    at107.configure(bg = 'yellow')
    at108.configure(bg = 'yellow')
    at109.configure(bg = 'yellow')
    at110.configure(bg = 'yellow')
    at111.configure(bg = 'yellow')
    at112.configure(bg = 'yellow')
    at113.configure(bg = '#ff5500')
    at114.configure(bg = '#ff5500')
    at115.configure(bg = '#ff5500')
    at116.configure(bg = '#ff5500')
    at117.configure(bg = '#ff5500')
    at118.configure(bg = '#af7ffb')
    
def Nonmetalsentered(event):
    at1.configure(bg = 'black')
    at2.configure(bg = 'black')
    at3.configure(bg = 'black')
    at4.configure(bg = 'black')
    at5.configure(bg = '#1aff40')
    at6.configure(bg = '#1aff40')
    at7.configure(bg = '#1aff40')
    at8.configure(bg = '#1aff40')
    at9.configure(bg = '#1aff40')
    at10.configure(bg = 'black')
    at11.configure(bg = 'black')
    at12.configure(bg = 'black')
    at13.configure(bg = 'black')
    at14.configure(bg = 'black')
    at15.configure(bg = '#1aff40')
    at16.configure(bg = '#1aff40')
    at17.configure(bg = '#1aff40')
    at18.configure(bg = 'black')
    at19.configure(bg = 'black')
    at20.configure(bg = 'black')
    at21.configure(bg = 'black')
    at22.configure(bg = 'black')
    at23.configure(bg = 'black')
    at24.configure(bg = 'black')
    at25.configure(bg = 'black')
    at26.configure(bg = 'black')
    at27.configure(bg = 'black')
    at28.configure(bg = 'black')
    at29.configure(bg = 'black')
    at30.configure(bg = 'black')
    at31.configure(bg = 'black')
    at32.configure(bg = 'black')
    at33.configure(bg = 'black')
    at34.configure(bg = '#1aff40')
    at35.configure(bg = '#1aff40')
    at36.configure(bg = 'black')
    at37.configure(bg = 'black')
    at38.configure(bg = 'black')
    at39.configure(bg = 'black')
    at40.configure(bg = 'black')
    at41.configure(bg = 'black')
    at42.configure(bg = 'black')
    at43.configure(bg = 'black')
    at44.configure(bg = 'black')
    at45.configure(bg = 'black')
    at46.configure(bg = 'black')
    at47.configure(bg = 'black')
    at48.configure(bg = 'black')
    at49.configure(bg = 'black')
    at50.configure(bg = 'black')
    at51.configure(bg = 'black')
    at52.configure(bg = 'black')
    at53.configure(bg = '#1aff40')
    at54.configure(bg = 'black')
    at55.configure(bg = 'black')
    at56.configure(bg = 'black')
    at57.configure(bg = 'black')
    at58.configure(bg = 'black')
    at59.configure(bg = 'black')
    at60.configure(bg = 'black')
    at61.configure(bg = 'black')
    at62.configure(bg = 'black')
    at63.configure(bg = 'black')
    at64.configure(bg = 'black')
    at65.configure(bg = 'black')
    at66.configure(bg = 'black')
    at67.configure(bg = 'black')
    at68.configure(bg = 'black')
    at69.configure(bg = 'black')
    at70.configure(bg = 'black')
    at71.configure(bg = 'black')
    at72.configure(bg = 'black')
    at73.configure(bg = 'black')
    at74.configure(bg = 'black')
    at75.configure(bg = 'black')
    at76.configure(bg = 'black')
    at77.configure(bg = 'black')
    at78.configure(bg = 'black')
    at79.configure(bg = 'black')
    at80.configure(bg = 'black')
    at81.configure(bg = 'black')
    at82.configure(bg = 'black')
    at83.configure(bg = 'black')
    at84.configure(bg = 'black')
    at85.configure(bg = 'black')
    at86.configure(bg = 'black')
    at87.configure(bg = 'black')
    at88.configure(bg = 'black')
    at89.configure(bg = 'black')
    at90.configure(bg = 'black')
    at91.configure(bg = 'black')
    at92.configure(bg = 'black')
    at93.configure(bg = 'black')
    at94.configure(bg = 'black')
    at95.configure(bg = 'black')
    at96.configure(bg = 'black')
    at97.configure(bg = 'black')
    at98.configure(bg = 'black')
    at99.configure(bg = 'black')
    at100.configure(bg = 'black')
    at101.configure(bg = 'black')
    at102.configure(bg = 'black')
    at103.configure(bg = 'black')
    at104.configure(bg = 'black')
    at105.configure(bg = 'black')
    at106.configure(bg = 'black')
    at107.configure(bg = 'black')
    at108.configure(bg = 'black')
    at109.configure(bg = 'black')
    at110.configure(bg = 'black')
    at111.configure(bg = 'black')
    at112.configure(bg = 'black')
    at113.configure(bg = 'black')
    at114.configure(bg = 'black')
    at115.configure(bg = 'black')
    at116.configure(bg = 'black')
    at117.configure(bg = 'black')
    at118.configure(bg = 'black')



def Nonmetalsleft(event):
    at1.configure(bg = '#f13800')
    at2.configure(bg = '#af7ffb')
    at3.configure(bg = '#49c9ff')
    at4.configure(bg = '#adaeb0')
    at5.configure(bg = '#1aff40')
    at6.configure(bg = '#1aff40')
    at7.configure(bg = '#1aff40')
    at8.configure(bg = '#1aff40')
    at9.configure(bg = '#1aff40')
    at10.configure(bg = '#af7ffb')
    at11.configure(bg = '#49c9ff')
    at12.configure(bg = '#adaeb0')
    at13.configure(bg = '#ff5500')
    at14.configure(bg = '#ff55ff')
    at15.configure(bg = '#1aff40')
    at16.configure(bg = '#1aff40')
    at17.configure(bg = '#1aff40')
    at18.configure(bg = '#af7ffb')
    at19.configure(bg = '#49c9ff')
    at20.configure(bg = '#adaeb0')
    at21.configure(bg = 'yellow')
    at22.configure(bg = 'yellow')
    at23.configure(bg = 'yellow')
    at24.configure(bg = 'yellow')
    at25.configure(bg = 'yellow')
    at26.configure(bg = 'yellow')
    at27.configure(bg = 'yellow')
    at28.configure(bg = 'yellow')
    at29.configure(bg = 'yellow')
    at30.configure(bg = 'yellow')
    at31.configure(bg = '#ff5500')
    at32.configure(bg = '#ff55ff')
    at33.configure(bg = '#ff55ff')
    at34.configure(bg = '#1aff40')
    at35.configure(bg = '#1aff40')
    at36.configure(bg = '#af7ffb')
    at37.configure(bg = '#49c9ff')
    at38.configure(bg = '#adaeb0')
    at39.configure(bg = 'yellow')
    at40.configure(bg = 'yellow')
    at41.configure(bg = 'yellow')
    at42.configure(bg = 'yellow')
    at43.configure(bg = 'yellow')
    at44.configure(bg = 'yellow')
    at45.configure(bg = 'yellow')
    at46.configure(bg = 'yellow')
    at47.configure(bg = 'yellow')
    at48.configure(bg = 'yellow')
    at49.configure(bg = '#ff5500')
    at50.configure(bg = '#ff5500')
    at51.configure(bg = '#ff55ff')
    at52.configure(bg = '#ff55ff')
    at53.configure(bg = '#1aff40')
    at54.configure(bg = '#af7ffb')
    at55.configure(bg = '#49c9ff')
    at56.configure(bg = '#adaeb0')
    at57.configure(bg = '#bcc514')
    at58.configure(bg = '#bcc514')
    at59.configure(bg = '#bcc514')
    at60.configure(bg = '#bcc514')
    at61.configure(bg = '#bcc514')
    at62.configure(bg = '#bcc514')
    at63.configure(bg = '#bcc514')
    at64.configure(bg = '#bcc514')
    at65.configure(bg = '#bcc514')
    at66.configure(bg = '#bcc514')
    at67.configure(bg = '#bcc514')
    at68.configure(bg = '#bcc514')
    at69.configure(bg = '#bcc514')
    at70.configure(bg = '#bcc514')
    at71.configure(bg = '#bcc514')
    at72.configure(bg = 'yellow')
    at73.configure(bg = 'yellow')
    at74.configure(bg = 'yellow')
    at75.configure(bg = 'yellow')
    at76.configure(bg = 'yellow')
    at77.configure(bg = 'yellow')
    at78.configure(bg = 'yellow')
    at79.configure(bg = 'yellow')
    at80.configure(bg = 'yellow')
    at81.configure(bg = '#ff5500')
    at82.configure(bg = '#ff5500')
    at83.configure(bg = '#ff5500')
    at84.configure(bg = '#ff55ff')
    at85.configure(bg = '#ff55ff')
    at86.configure(bg = '#af7ffb')
    at87.configure(bg = '#49c9ff')
    at88.configure(bg = '#adaeb0')
    at89.configure(bg = '#ff910b')
    at90.configure(bg = '#ff910b')
    at91.configure(bg = '#ff910b')
    at92.configure(bg = '#ff910b')
    at93.configure(bg = '#ff910b')
    at94.configure(bg = '#ff910b')
    at95.configure(bg = '#ff910b')
    at96.configure(bg = '#ff910b')
    at97.configure(bg = '#ff910b')
    at98.configure(bg = '#ff910b')
    at99.configure(bg = '#ff910b')
    at100.configure(bg = '#ff910b')
    at101.configure(bg = '#ff910b')
    at102.configure(bg = '#ff910b')
    at103.configure(bg = '#ff910b')
    at104.configure(bg = 'yellow')
    at105.configure(bg = 'yellow')
    at106.configure(bg = 'yellow')
    at107.configure(bg = 'yellow')
    at108.configure(bg = 'yellow')
    at109.configure(bg = 'yellow')
    at110.configure(bg = 'yellow')
    at111.configure(bg = 'yellow')
    at112.configure(bg = 'yellow')
    at113.configure(bg = '#ff5500')
    at114.configure(bg = '#ff5500')
    at115.configure(bg = '#ff5500')
    at116.configure(bg = '#ff5500')
    at117.configure(bg = '#ff5500')
    at118.configure(bg = '#af7ffb')

def metalloidsentered(event):
    at1.configure(bg = 'black')
    at2.configure(bg = 'black')
    at3.configure(bg = 'black')
    at4.configure(bg = 'black')
    at5.configure(bg = 'black')
    at6.configure(bg = 'black')
    at7.configure(bg = 'black')
    at8.configure(bg = 'black')
    at9.configure(bg = 'black')
    at10.configure(bg = 'black')
    at11.configure(bg = 'black')
    at12.configure(bg = 'black')
    at13.configure(bg = 'black')
    at14.configure(bg = '#ff55ff')
    at15.configure(bg = 'black')
    at16.configure(bg = 'black')
    at17.configure(bg = 'black')
    at18.configure(bg = 'black')
    at19.configure(bg = 'black')
    at20.configure(bg = 'black')
    at21.configure(bg = 'black')
    at22.configure(bg = 'black')
    at23.configure(bg = 'black')
    at24.configure(bg = 'black')
    at25.configure(bg = 'black')
    at26.configure(bg = 'black')
    at27.configure(bg = 'black')
    at28.configure(bg = 'black')
    at29.configure(bg = 'black')
    at30.configure(bg = 'black')
    at31.configure(bg = 'black')
    at32.configure(bg = '#ff55ff')
    at33.configure(bg = '#ff55ff')
    at34.configure(bg = 'black')
    at35.configure(bg = 'black')
    at36.configure(bg = 'black')
    at37.configure(bg = 'black')
    at38.configure(bg = 'black')
    at39.configure(bg = 'black')
    at40.configure(bg = 'black')
    at41.configure(bg = 'black')
    at42.configure(bg = 'black')
    at43.configure(bg = 'black')
    at44.configure(bg = 'black')
    at45.configure(bg = 'black')
    at46.configure(bg = 'black')
    at47.configure(bg = 'black')
    at48.configure(bg = 'black')
    at49.configure(bg = 'black')
    at50.configure(bg = 'black')
    at51.configure(bg = '#ff55ff')
    at52.configure(bg = '#ff55ff')
    at53.configure(bg = 'black')
    at54.configure(bg = 'black')
    at55.configure(bg = 'black')
    at56.configure(bg = 'black')
    at57.configure(bg = 'black')
    at58.configure(bg = 'black')
    at59.configure(bg = 'black')
    at60.configure(bg = 'black')
    at61.configure(bg = 'black')
    at62.configure(bg = 'black')
    at63.configure(bg = 'black')
    at64.configure(bg = 'black')
    at65.configure(bg = 'black')
    at66.configure(bg = 'black')
    at67.configure(bg = 'black')
    at68.configure(bg = 'black')
    at69.configure(bg = 'black')
    at70.configure(bg = 'black')
    at71.configure(bg = 'black')
    at72.configure(bg = 'black')
    at73.configure(bg = 'black')
    at74.configure(bg = 'black')
    at75.configure(bg = 'black')
    at76.configure(bg = 'black')
    at77.configure(bg = 'black')
    at78.configure(bg = 'black')
    at79.configure(bg = 'black')
    at80.configure(bg = 'black')
    at81.configure(bg = 'black')
    at82.configure(bg = 'black')
    at83.configure(bg = 'black')
    at84.configure(bg = '#ff55ff')
    at85.configure(bg = '#ff55ff')
    at86.configure(bg = 'black')
    at87.configure(bg = 'black')
    at88.configure(bg = 'black')
    at89.configure(bg = 'black')
    at90.configure(bg = 'black')
    at91.configure(bg = 'black')
    at92.configure(bg = 'black')
    at93.configure(bg = 'black')
    at94.configure(bg = 'black')
    at95.configure(bg = 'black')
    at96.configure(bg = 'black')
    at97.configure(bg = 'black')
    at98.configure(bg = 'black')
    at99.configure(bg = 'black')
    at100.configure(bg = 'black')
    at101.configure(bg = 'black')
    at102.configure(bg = 'black')
    at103.configure(bg = 'black')
    at104.configure(bg = 'black')
    at105.configure(bg = 'black')
    at106.configure(bg = 'black')
    at107.configure(bg = 'black')
    at108.configure(bg = 'black')
    at109.configure(bg = 'black')
    at110.configure(bg = 'black')
    at111.configure(bg = 'black')
    at112.configure(bg = 'black')
    at113.configure(bg = 'black')
    at114.configure(bg = 'black')
    at115.configure(bg = 'black')
    at116.configure(bg = 'black')
    at117.configure(bg = 'black')
    at118.configure(bg = 'black')

def metalloidsleft(event):
    at1.configure(bg = '#f13800')
    at2.configure(bg = '#af7ffb')
    at3.configure(bg = '#49c9ff')
    at4.configure(bg = '#adaeb0')
    at5.configure(bg = '#1aff40')
    at6.configure(bg = '#1aff40')
    at7.configure(bg = '#1aff40')
    at8.configure(bg = '#1aff40')
    at9.configure(bg = '#1aff40')
    at10.configure(bg = '#af7ffb')
    at11.configure(bg = '#49c9ff')
    at12.configure(bg = '#adaeb0')
    at13.configure(bg = '#ff5500')
    at14.configure(bg = '#ff55ff')
    at15.configure(bg = '#1aff40')
    at16.configure(bg = '#1aff40')
    at17.configure(bg = '#1aff40')
    at18.configure(bg = '#af7ffb')
    at19.configure(bg = '#49c9ff')
    at20.configure(bg = '#adaeb0')
    at21.configure(bg = 'yellow')
    at22.configure(bg = 'yellow')
    at23.configure(bg = 'yellow')
    at24.configure(bg = 'yellow')
    at25.configure(bg = 'yellow')
    at26.configure(bg = 'yellow')
    at27.configure(bg = 'yellow')
    at28.configure(bg = 'yellow')
    at29.configure(bg = 'yellow')
    at30.configure(bg = 'yellow')
    at31.configure(bg = '#ff5500')
    at32.configure(bg = '#ff55ff')
    at33.configure(bg = '#ff55ff')
    at34.configure(bg = '#1aff40')
    at35.configure(bg = '#1aff40')
    at36.configure(bg = '#af7ffb')
    at37.configure(bg = '#49c9ff')
    at38.configure(bg = '#adaeb0')
    at39.configure(bg = 'yellow')
    at40.configure(bg = 'yellow')
    at41.configure(bg = 'yellow')
    at42.configure(bg = 'yellow')
    at43.configure(bg = 'yellow')
    at44.configure(bg = 'yellow')
    at45.configure(bg = 'yellow')
    at46.configure(bg = 'yellow')
    at47.configure(bg = 'yellow')
    at48.configure(bg = 'yellow')
    at49.configure(bg = '#ff5500')
    at50.configure(bg = '#ff5500')
    at51.configure(bg = '#ff55ff')
    at52.configure(bg = '#ff55ff')
    at53.configure(bg = '#1aff40')
    at54.configure(bg = '#af7ffb')
    at55.configure(bg = '#49c9ff')
    at56.configure(bg = '#adaeb0')
    at57.configure(bg = '#bcc514')
    at58.configure(bg = '#bcc514')
    at59.configure(bg = '#bcc514')
    at60.configure(bg = '#bcc514')
    at61.configure(bg = '#bcc514')
    at62.configure(bg = '#bcc514')
    at63.configure(bg = '#bcc514')
    at64.configure(bg = '#bcc514')
    at65.configure(bg = '#bcc514')
    at66.configure(bg = '#bcc514')
    at67.configure(bg = '#bcc514')
    at68.configure(bg = '#bcc514')
    at69.configure(bg = '#bcc514')
    at70.configure(bg = '#bcc514')
    at71.configure(bg = '#bcc514')
    at72.configure(bg = 'yellow')
    at73.configure(bg = 'yellow')
    at74.configure(bg = 'yellow')
    at75.configure(bg = 'yellow')
    at76.configure(bg = 'yellow')
    at77.configure(bg = 'yellow')
    at78.configure(bg = 'yellow')
    at79.configure(bg = 'yellow')
    at80.configure(bg = 'yellow')
    at81.configure(bg = '#ff5500')
    at82.configure(bg = '#ff5500')
    at83.configure(bg = '#ff5500')
    at84.configure(bg = '#ff55ff')
    at85.configure(bg = '#ff55ff')
    at86.configure(bg = '#af7ffb')
    at87.configure(bg = '#49c9ff')
    at88.configure(bg = '#adaeb0')
    at89.configure(bg = '#ff910b')
    at90.configure(bg = '#ff910b')
    at91.configure(bg = '#ff910b')
    at92.configure(bg = '#ff910b')
    at93.configure(bg = '#ff910b')
    at94.configure(bg = '#ff910b')
    at95.configure(bg = '#ff910b')
    at96.configure(bg = '#ff910b')
    at97.configure(bg = '#ff910b')
    at98.configure(bg = '#ff910b')
    at99.configure(bg = '#ff910b')
    at100.configure(bg = '#ff910b')
    at101.configure(bg = '#ff910b')
    at102.configure(bg = '#ff910b')
    at103.configure(bg = '#ff910b')
    at104.configure(bg = 'yellow')
    at105.configure(bg = 'yellow')
    at106.configure(bg = 'yellow')
    at107.configure(bg = 'yellow')
    at108.configure(bg = 'yellow')
    at109.configure(bg = 'yellow')
    at110.configure(bg = 'yellow')
    at111.configure(bg = 'yellow')
    at112.configure(bg = 'yellow')
    at113.configure(bg = '#ff5500')
    at114.configure(bg = '#ff5500')
    at115.configure(bg = '#ff5500')
    at116.configure(bg = '#ff5500')
    at117.configure(bg = '#ff5500')
    at118.configure(bg = '#af7ffb')

def postentered(event):
    at1.configure(bg = 'black')
    at2.configure(bg = 'black')
    at3.configure(bg = 'black')
    at4.configure(bg = 'black')
    at5.configure(bg = 'black')
    at6.configure(bg = 'black')
    at7.configure(bg = 'black')
    at8.configure(bg = 'black')
    at9.configure(bg = 'black')
    at10.configure(bg = 'black')
    at11.configure(bg = 'black')
    at12.configure(bg = 'black')
    at13.configure(bg = '#ff5500')
    at14.configure(bg = 'black')
    at15.configure(bg = 'black')
    at16.configure(bg = 'black')
    at17.configure(bg = 'black')
    at18.configure(bg = 'black')
    at19.configure(bg = 'black')
    at20.configure(bg = 'black')
    at21.configure(bg = 'black')
    at22.configure(bg = 'black')
    at23.configure(bg = 'black')
    at24.configure(bg = 'black')
    at25.configure(bg = 'black')
    at26.configure(bg = 'black')
    at27.configure(bg = 'black')
    at28.configure(bg = 'black')
    at29.configure(bg = 'black')
    at30.configure(bg = 'black')
    at31.configure(bg = '#ff5500')
    at32.configure(bg = 'black')
    at33.configure(bg = 'black')
    at34.configure(bg = 'black')
    at35.configure(bg = 'black')
    at36.configure(bg = 'black')
    at37.configure(bg = 'black')
    at38.configure(bg = 'black')
    at39.configure(bg = 'black')
    at40.configure(bg = 'black')
    at41.configure(bg = 'black')
    at42.configure(bg = 'black')
    at43.configure(bg = 'black')
    at44.configure(bg = 'black')
    at45.configure(bg = 'black')
    at46.configure(bg = 'black')
    at47.configure(bg = 'black')
    at48.configure(bg = 'black')
    at49.configure(bg = '#ff5500')
    at50.configure(bg = '#ff5500')
    at51.configure(bg = 'black')
    at52.configure(bg = 'black')
    at53.configure(bg = 'black')
    at54.configure(bg = 'black')
    at55.configure(bg = 'black')
    at56.configure(bg = 'black')
    at57.configure(bg = 'black')
    at58.configure(bg = 'black')
    at59.configure(bg = 'black')
    at60.configure(bg = 'black')
    at61.configure(bg = 'black')
    at62.configure(bg = 'black')
    at63.configure(bg = 'black')
    at64.configure(bg = 'black')
    at65.configure(bg = 'black')
    at66.configure(bg = 'black')
    at67.configure(bg = 'black')
    at68.configure(bg = 'black')
    at69.configure(bg = 'black')
    at70.configure(bg = 'black')
    at71.configure(bg = 'black')
    at72.configure(bg = 'black')
    at73.configure(bg = 'black')
    at74.configure(bg = 'black')
    at75.configure(bg = 'black')
    at76.configure(bg = 'black')
    at77.configure(bg = 'black')
    at78.configure(bg = 'black')
    at79.configure(bg = 'black')
    at80.configure(bg = 'black')
    at81.configure(bg = '#ff5500')
    at82.configure(bg = '#ff5500')
    at83.configure(bg = '#ff5500')
    at84.configure(bg = 'black')
    at85.configure(bg = 'black')
    at86.configure(bg = 'black')
    at87.configure(bg = 'black')
    at88.configure(bg = 'black')
    at89.configure(bg = 'black')
    at90.configure(bg = 'black')
    at91.configure(bg = 'black')
    at92.configure(bg = 'black')
    at93.configure(bg = 'black')
    at94.configure(bg = 'black')
    at95.configure(bg = 'black')
    at96.configure(bg = 'black')
    at97.configure(bg = 'black')
    at98.configure(bg = 'black')
    at99.configure(bg = 'black')
    at100.configure(bg = 'black')
    at101.configure(bg = 'black')
    at102.configure(bg = 'black')
    at103.configure(bg = 'black')
    at104.configure(bg = 'black')
    at105.configure(bg = 'black')
    at106.configure(bg = 'black')
    at107.configure(bg = 'black')
    at108.configure(bg = 'black')
    at109.configure(bg = 'black')
    at110.configure(bg = 'black')
    at111.configure(bg = 'black')
    at112.configure(bg = 'black')
    at113.configure(bg = '#ff5500')
    at114.configure(bg = '#ff5500')
    at115.configure(bg = '#ff5500')
    at116.configure(bg = '#ff5500')
    at117.configure(bg = '#ff5500')
    at118.configure(bg = 'black')

def postleft(event):
    at1.configure(bg = '#f13800')
    at2.configure(bg = '#af7ffb')
    at3.configure(bg = '#49c9ff')
    at4.configure(bg = '#adaeb0')
    at5.configure(bg = '#1aff40')
    at6.configure(bg = '#1aff40')
    at7.configure(bg = '#1aff40')
    at8.configure(bg = '#1aff40')
    at9.configure(bg = '#1aff40')
    at10.configure(bg = '#af7ffb')
    at11.configure(bg = '#49c9ff')
    at12.configure(bg = '#adaeb0')
    at13.configure(bg = '#ff5500')
    at14.configure(bg = '#ff55ff')
    at15.configure(bg = '#1aff40')
    at16.configure(bg = '#1aff40')
    at17.configure(bg = '#1aff40')
    at18.configure(bg = '#af7ffb')
    at19.configure(bg = '#49c9ff')
    at20.configure(bg = '#adaeb0')
    at21.configure(bg = 'yellow')
    at22.configure(bg = 'yellow')
    at23.configure(bg = 'yellow')
    at24.configure(bg = 'yellow')
    at25.configure(bg = 'yellow')
    at26.configure(bg = 'yellow')
    at27.configure(bg = 'yellow')
    at28.configure(bg = 'yellow')
    at29.configure(bg = 'yellow')
    at30.configure(bg = 'yellow')
    at31.configure(bg = '#ff5500')
    at32.configure(bg = '#ff55ff')
    at33.configure(bg = '#ff55ff')
    at34.configure(bg = '#1aff40')
    at35.configure(bg = '#1aff40')
    at36.configure(bg = '#af7ffb')
    at37.configure(bg = '#49c9ff')
    at38.configure(bg = '#adaeb0')
    at39.configure(bg = 'yellow')
    at40.configure(bg = 'yellow')
    at41.configure(bg = 'yellow')
    at42.configure(bg = 'yellow')
    at43.configure(bg = 'yellow')
    at44.configure(bg = 'yellow')
    at45.configure(bg = 'yellow')
    at46.configure(bg = 'yellow')
    at47.configure(bg = 'yellow')
    at48.configure(bg = 'yellow')
    at49.configure(bg = '#ff5500')
    at50.configure(bg = '#ff5500')
    at51.configure(bg = '#ff55ff')
    at52.configure(bg = '#ff55ff')
    at53.configure(bg = '#1aff40')
    at54.configure(bg = '#af7ffb')
    at55.configure(bg = '#49c9ff')
    at56.configure(bg = '#adaeb0')
    at57.configure(bg = '#bcc514')
    at58.configure(bg = '#bcc514')
    at59.configure(bg = '#bcc514')
    at60.configure(bg = '#bcc514')
    at61.configure(bg = '#bcc514')
    at62.configure(bg = '#bcc514')
    at63.configure(bg = '#bcc514')
    at64.configure(bg = '#bcc514')
    at65.configure(bg = '#bcc514')
    at66.configure(bg = '#bcc514')
    at67.configure(bg = '#bcc514')
    at68.configure(bg = '#bcc514')
    at69.configure(bg = '#bcc514')
    at70.configure(bg = '#bcc514')
    at71.configure(bg = '#bcc514')
    at72.configure(bg = 'yellow')
    at73.configure(bg = 'yellow')
    at74.configure(bg = 'yellow')
    at75.configure(bg = 'yellow')
    at76.configure(bg = 'yellow')
    at77.configure(bg = 'yellow')
    at78.configure(bg = 'yellow')
    at79.configure(bg = 'yellow')
    at80.configure(bg = 'yellow')
    at81.configure(bg = '#ff5500')
    at82.configure(bg = '#ff5500')
    at83.configure(bg = '#ff5500')
    at84.configure(bg = '#ff55ff')
    at85.configure(bg = '#ff55ff')
    at86.configure(bg = '#af7ffb')
    at87.configure(bg = '#49c9ff')
    at88.configure(bg = '#adaeb0')
    at89.configure(bg = '#ff910b')
    at90.configure(bg = '#ff910b')
    at91.configure(bg = '#ff910b')
    at92.configure(bg = '#ff910b')
    at93.configure(bg = '#ff910b')
    at94.configure(bg = '#ff910b')
    at95.configure(bg = '#ff910b')
    at96.configure(bg = '#ff910b')
    at97.configure(bg = '#ff910b')
    at98.configure(bg = '#ff910b')
    at99.configure(bg = '#ff910b')
    at100.configure(bg = '#ff910b')
    at101.configure(bg = '#ff910b')
    at102.configure(bg = '#ff910b')
    at103.configure(bg = '#ff910b')
    at104.configure(bg = 'yellow')
    at105.configure(bg = 'yellow')
    at106.configure(bg = 'yellow')
    at107.configure(bg = 'yellow')
    at108.configure(bg = 'yellow')
    at109.configure(bg = 'yellow')
    at110.configure(bg = 'yellow')
    at111.configure(bg = 'yellow')
    at112.configure(bg = 'yellow')
    at113.configure(bg = '#ff5500')
    at114.configure(bg = '#ff5500')
    at115.configure(bg = '#ff5500')
    at116.configure(bg = '#ff5500')
    at117.configure(bg = '#ff5500')
    at118.configure(bg = '#af7ffb')

def lanentered(event):
    at1.configure(bg = 'black')
    at2.configure(bg = 'black')
    at3.configure(bg = 'black')
    at4.configure(bg = 'black')
    at5.configure(bg = 'black')
    at6.configure(bg = 'black')
    at7.configure(bg = 'black')
    at8.configure(bg = 'black')
    at9.configure(bg = 'black')
    at10.configure(bg = 'black')
    at11.configure(bg = 'black')
    at12.configure(bg = 'black')
    at13.configure(bg = 'black')
    at14.configure(bg = 'black')
    at15.configure(bg = 'black')
    at16.configure(bg = 'black')
    at17.configure(bg = 'black')
    at18.configure(bg = 'black')
    at19.configure(bg = 'black')
    at20.configure(bg = 'black')
    at21.configure(bg = 'black')
    at22.configure(bg = 'black')
    at23.configure(bg = 'black')
    at24.configure(bg = 'black')
    at25.configure(bg = 'black')
    at26.configure(bg = 'black')
    at27.configure(bg = 'black')
    at28.configure(bg = 'black')
    at29.configure(bg = 'black')
    at30.configure(bg = 'black')
    at31.configure(bg = 'black')
    at32.configure(bg = 'black')
    at33.configure(bg = 'black')
    at34.configure(bg = 'black')
    at35.configure(bg = 'black')
    at36.configure(bg = 'black')
    at37.configure(bg = 'black')
    at38.configure(bg = 'black')
    at39.configure(bg = 'black')
    at40.configure(bg = 'black')
    at41.configure(bg = 'black')
    at42.configure(bg = 'black')
    at43.configure(bg = 'black')
    at44.configure(bg = 'black')
    at45.configure(bg = 'black')
    at46.configure(bg = 'black')
    at47.configure(bg = 'black')
    at48.configure(bg = 'black')
    at49.configure(bg = 'black')
    at50.configure(bg = 'black')
    at51.configure(bg = 'black')
    at52.configure(bg = 'black')
    at53.configure(bg = 'black')
    at54.configure(bg = 'black')
    at55.configure(bg = 'black')
    at56.configure(bg = 'black')
    at57.configure(bg = '#bcc514')
    at58.configure(bg = '#bcc514')
    at59.configure(bg = '#bcc514')
    at60.configure(bg = '#bcc514')
    at61.configure(bg = '#bcc514')
    at62.configure(bg = '#bcc514')
    at63.configure(bg = '#bcc514')
    at64.configure(bg = '#bcc514')
    at65.configure(bg = '#bcc514')
    at66.configure(bg = '#bcc514')
    at67.configure(bg = '#bcc514')
    at68.configure(bg = '#bcc514')
    at69.configure(bg = '#bcc514')
    at70.configure(bg = '#bcc514')
    at71.configure(bg = '#bcc514')
    at72.configure(bg = 'black')
    at73.configure(bg = 'black')
    at74.configure(bg = 'black')
    at75.configure(bg = 'black')
    at76.configure(bg = 'black')
    at77.configure(bg = 'black')
    at78.configure(bg = 'black')
    at79.configure(bg = 'black')
    at80.configure(bg = 'black')
    at81.configure(bg = 'black')
    at82.configure(bg = 'black')
    at83.configure(bg = 'black')
    at84.configure(bg = 'black')
    at85.configure(bg = 'black')
    at86.configure(bg = 'black')
    at87.configure(bg = 'black')
    at88.configure(bg = 'black')
    at89.configure(bg = 'black')
    at90.configure(bg = 'black')
    at91.configure(bg = 'black')
    at92.configure(bg = 'black')
    at93.configure(bg = 'black')
    at94.configure(bg = 'black')
    at95.configure(bg = 'black')
    at96.configure(bg = 'black')
    at97.configure(bg = 'black')
    at98.configure(bg = 'black')
    at99.configure(bg = 'black')
    at100.configure(bg = 'black')
    at101.configure(bg = 'black')
    at102.configure(bg = 'black')
    at103.configure(bg = 'black')
    at104.configure(bg = 'black')
    at105.configure(bg = 'black')
    at106.configure(bg = 'black')
    at107.configure(bg = 'black')
    at108.configure(bg = 'black')
    at109.configure(bg = 'black')
    at110.configure(bg = 'black')
    at111.configure(bg = 'black')
    at112.configure(bg = 'black')
    at113.configure(bg = 'black')
    at114.configure(bg = 'black')
    at115.configure(bg = 'black')
    at116.configure(bg = 'black')
    at117.configure(bg = 'black')
    at118.configure(bg = 'black')

def lanleft(event):
    at1.configure(bg = '#f13800')
    at2.configure(bg = '#af7ffb')
    at3.configure(bg = '#49c9ff')
    at4.configure(bg = '#adaeb0')
    at5.configure(bg = '#1aff40')
    at6.configure(bg = '#1aff40')
    at7.configure(bg = '#1aff40')
    at8.configure(bg = '#1aff40')
    at9.configure(bg = '#1aff40')
    at10.configure(bg = '#af7ffb')
    at11.configure(bg = '#49c9ff')
    at12.configure(bg = '#adaeb0')
    at13.configure(bg = '#ff5500')
    at14.configure(bg = '#ff55ff')
    at15.configure(bg = '#1aff40')
    at16.configure(bg = '#1aff40')
    at17.configure(bg = '#1aff40')
    at18.configure(bg = '#af7ffb')
    at19.configure(bg = '#49c9ff')
    at20.configure(bg = '#adaeb0')
    at21.configure(bg = 'yellow')
    at22.configure(bg = 'yellow')
    at23.configure(bg = 'yellow')
    at24.configure(bg = 'yellow')
    at25.configure(bg = 'yellow')
    at26.configure(bg = 'yellow')
    at27.configure(bg = 'yellow')
    at28.configure(bg = 'yellow')
    at29.configure(bg = 'yellow')
    at30.configure(bg = 'yellow')
    at31.configure(bg = '#ff5500')
    at32.configure(bg = '#ff55ff')
    at33.configure(bg = '#ff55ff')
    at34.configure(bg = '#1aff40')
    at35.configure(bg = '#1aff40')
    at36.configure(bg = '#af7ffb')
    at37.configure(bg = '#49c9ff')
    at38.configure(bg = '#adaeb0')
    at39.configure(bg = 'yellow')
    at40.configure(bg = 'yellow')
    at41.configure(bg = 'yellow')
    at42.configure(bg = 'yellow')
    at43.configure(bg = 'yellow')
    at44.configure(bg = 'yellow')
    at45.configure(bg = 'yellow')
    at46.configure(bg = 'yellow')
    at47.configure(bg = 'yellow')
    at48.configure(bg = 'yellow')
    at49.configure(bg = '#ff5500')
    at50.configure(bg = '#ff5500')
    at51.configure(bg = '#ff55ff')
    at52.configure(bg = '#ff55ff')
    at53.configure(bg = '#1aff40')
    at54.configure(bg = '#af7ffb')
    at55.configure(bg = '#49c9ff')
    at56.configure(bg = '#adaeb0')
    at57.configure(bg = '#bcc514')
    at58.configure(bg = '#bcc514')
    at59.configure(bg = '#bcc514')
    at60.configure(bg = '#bcc514')
    at61.configure(bg = '#bcc514')
    at62.configure(bg = '#bcc514')
    at63.configure(bg = '#bcc514')
    at64.configure(bg = '#bcc514')
    at65.configure(bg = '#bcc514')
    at66.configure(bg = '#bcc514')
    at67.configure(bg = '#bcc514')
    at68.configure(bg = '#bcc514')
    at69.configure(bg = '#bcc514')
    at70.configure(bg = '#bcc514')
    at71.configure(bg = '#bcc514')
    at72.configure(bg = 'yellow')
    at73.configure(bg = 'yellow')
    at74.configure(bg = 'yellow')
    at75.configure(bg = 'yellow')
    at76.configure(bg = 'yellow')
    at77.configure(bg = 'yellow')
    at78.configure(bg = 'yellow')
    at79.configure(bg = 'yellow')
    at80.configure(bg = 'yellow')
    at81.configure(bg = '#ff5500')
    at82.configure(bg = '#ff5500')
    at83.configure(bg = '#ff5500')
    at84.configure(bg = '#ff55ff')
    at85.configure(bg = '#ff55ff')
    at86.configure(bg = '#af7ffb')
    at87.configure(bg = '#49c9ff')
    at88.configure(bg = '#adaeb0')
    at89.configure(bg = '#ff910b')
    at90.configure(bg = '#ff910b')
    at91.configure(bg = '#ff910b')
    at92.configure(bg = '#ff910b')
    at93.configure(bg = '#ff910b')
    at94.configure(bg = '#ff910b')
    at95.configure(bg = '#ff910b')
    at96.configure(bg = '#ff910b')
    at97.configure(bg = '#ff910b')
    at98.configure(bg = '#ff910b')
    at99.configure(bg = '#ff910b')
    at100.configure(bg = '#ff910b')
    at101.configure(bg = '#ff910b')
    at102.configure(bg = '#ff910b')
    at103.configure(bg = '#ff910b')
    at104.configure(bg = 'yellow')
    at105.configure(bg = 'yellow')
    at106.configure(bg = 'yellow')
    at107.configure(bg = 'yellow')
    at108.configure(bg = 'yellow')
    at109.configure(bg = 'yellow')
    at110.configure(bg = 'yellow')
    at111.configure(bg = 'yellow')
    at112.configure(bg = 'yellow')
    at113.configure(bg = '#ff5500')
    at114.configure(bg = '#ff5500')
    at115.configure(bg = '#ff5500')
    at116.configure(bg = '#ff5500')
    at117.configure(bg = '#ff5500')
    at118.configure(bg = '#af7ffb')

def actentered(event):
    at1.configure(bg = 'black')
    at2.configure(bg = 'black')
    at3.configure(bg = 'black')
    at4.configure(bg = 'black')
    at5.configure(bg = 'black')
    at6.configure(bg = 'black')
    at7.configure(bg = 'black')
    at8.configure(bg = 'black')
    at9.configure(bg = 'black')
    at10.configure(bg = 'black')
    at11.configure(bg = 'black')
    at12.configure(bg = 'black')
    at13.configure(bg = 'black')
    at14.configure(bg = 'black')
    at15.configure(bg = 'black')
    at16.configure(bg = 'black')
    at17.configure(bg = 'black')
    at18.configure(bg = 'black')
    at19.configure(bg = 'black')
    at20.configure(bg = 'black')
    at21.configure(bg = 'black')
    at22.configure(bg = 'black')
    at23.configure(bg = 'black')
    at24.configure(bg = 'black')
    at25.configure(bg = 'black')
    at26.configure(bg = 'black')
    at27.configure(bg = 'black')
    at28.configure(bg = 'black')
    at29.configure(bg = 'black')
    at30.configure(bg = 'black')
    at31.configure(bg = 'black')
    at32.configure(bg = 'black')
    at33.configure(bg = 'black')
    at34.configure(bg = 'black')
    at35.configure(bg = 'black')
    at36.configure(bg = 'black')
    at37.configure(bg = 'black')
    at38.configure(bg = 'black')
    at39.configure(bg = 'black')
    at40.configure(bg = 'black')
    at41.configure(bg = 'black')
    at42.configure(bg = 'black')
    at43.configure(bg = 'black')
    at44.configure(bg = 'black')
    at45.configure(bg = 'black')
    at46.configure(bg = 'black')
    at47.configure(bg = 'black')
    at48.configure(bg = 'black')
    at49.configure(bg = 'black')
    at50.configure(bg = 'black')
    at51.configure(bg = 'black')
    at52.configure(bg = 'black')
    at53.configure(bg = 'black')
    at54.configure(bg = 'black')
    at55.configure(bg = 'black')
    at56.configure(bg = 'black')
    at57.configure(bg = 'black')
    at58.configure(bg = 'black')
    at59.configure(bg = 'black')
    at60.configure(bg = 'black')
    at61.configure(bg = 'black')
    at62.configure(bg = 'black')
    at63.configure(bg = 'black')
    at64.configure(bg = 'black')
    at65.configure(bg = 'black')
    at66.configure(bg = 'black')
    at67.configure(bg = 'black')
    at68.configure(bg = 'black')
    at69.configure(bg = 'black')
    at70.configure(bg = 'black')
    at71.configure(bg = 'black')
    at72.configure(bg = 'black')
    at73.configure(bg = 'black')
    at74.configure(bg = 'black')
    at75.configure(bg = 'black')
    at76.configure(bg = 'black')
    at77.configure(bg = 'black')
    at78.configure(bg = 'black')
    at79.configure(bg = 'black')
    at80.configure(bg = 'black')
    at81.configure(bg = 'black')
    at82.configure(bg = 'black')
    at83.configure(bg = 'black')
    at84.configure(bg = 'black')
    at85.configure(bg = 'black')
    at86.configure(bg = 'black')
    at87.configure(bg = 'black')
    at88.configure(bg = 'black')
    at89.configure(bg = '#ff910b')
    at90.configure(bg = '#ff910b')
    at91.configure(bg = '#ff910b')
    at92.configure(bg = '#ff910b')
    at93.configure(bg = '#ff910b')
    at94.configure(bg = '#ff910b')
    at95.configure(bg = '#ff910b')
    at96.configure(bg = '#ff910b')
    at97.configure(bg = '#ff910b')
    at98.configure(bg = '#ff910b')
    at99.configure(bg = '#ff910b')
    at100.configure(bg = '#ff910b')
    at101.configure(bg = '#ff910b')
    at102.configure(bg = '#ff910b')
    at103.configure(bg = '#ff910b')
    at104.configure(bg = 'black')
    at105.configure(bg = 'black')
    at106.configure(bg = 'black')
    at107.configure(bg = 'black')
    at108.configure(bg = 'black')
    at109.configure(bg = 'black')
    at110.configure(bg = 'black')
    at111.configure(bg = 'black')
    at112.configure(bg = 'black')
    at113.configure(bg = 'black')
    at114.configure(bg = 'black')
    at115.configure(bg = 'black')
    at116.configure(bg = 'black')
    at117.configure(bg = 'black')
    at118.configure(bg = 'black')

def actleft(event):
    at1.configure(bg = '#f13800')
    at2.configure(bg = '#af7ffb')
    at3.configure(bg = '#49c9ff')
    at4.configure(bg = '#adaeb0')
    at5.configure(bg = '#1aff40')
    at6.configure(bg = '#1aff40')
    at7.configure(bg = '#1aff40')
    at8.configure(bg = '#1aff40')
    at9.configure(bg = '#1aff40')
    at10.configure(bg = '#af7ffb')
    at11.configure(bg = '#49c9ff')
    at12.configure(bg = '#adaeb0')
    at13.configure(bg = '#ff5500')
    at14.configure(bg = '#ff55ff')
    at15.configure(bg = '#1aff40')
    at16.configure(bg = '#1aff40')
    at17.configure(bg = '#1aff40')
    at18.configure(bg = '#af7ffb')
    at19.configure(bg = '#49c9ff')
    at20.configure(bg = '#adaeb0')
    at21.configure(bg = 'yellow')
    at22.configure(bg = 'yellow')
    at23.configure(bg = 'yellow')
    at24.configure(bg = 'yellow')
    at25.configure(bg = 'yellow')
    at26.configure(bg = 'yellow')
    at27.configure(bg = 'yellow')
    at28.configure(bg = 'yellow')
    at29.configure(bg = 'yellow')
    at30.configure(bg = 'yellow')
    at31.configure(bg = '#ff5500')
    at32.configure(bg = '#ff55ff')
    at33.configure(bg = '#ff55ff')
    at34.configure(bg = '#1aff40')
    at35.configure(bg = '#1aff40')
    at36.configure(bg = '#af7ffb')
    at37.configure(bg = '#49c9ff')
    at38.configure(bg = '#adaeb0')
    at39.configure(bg = 'yellow')
    at40.configure(bg = 'yellow')
    at41.configure(bg = 'yellow')
    at42.configure(bg = 'yellow')
    at43.configure(bg = 'yellow')
    at44.configure(bg = 'yellow')
    at45.configure(bg = 'yellow')
    at46.configure(bg = 'yellow')
    at47.configure(bg = 'yellow')
    at48.configure(bg = 'yellow')
    at49.configure(bg = '#ff5500')
    at50.configure(bg = '#ff5500')
    at51.configure(bg = '#ff55ff')
    at52.configure(bg = '#ff55ff')
    at53.configure(bg = '#1aff40')
    at54.configure(bg = '#af7ffb')
    at55.configure(bg = '#49c9ff')
    at56.configure(bg = '#adaeb0')
    at57.configure(bg = '#bcc514')
    at58.configure(bg = '#bcc514')
    at59.configure(bg = '#bcc514')
    at60.configure(bg = '#bcc514')
    at61.configure(bg = '#bcc514')
    at62.configure(bg = '#bcc514')
    at63.configure(bg = '#bcc514')
    at64.configure(bg = '#bcc514')
    at65.configure(bg = '#bcc514')
    at66.configure(bg = '#bcc514')
    at67.configure(bg = '#bcc514')
    at68.configure(bg = '#bcc514')
    at69.configure(bg = '#bcc514')
    at70.configure(bg = '#bcc514')
    at71.configure(bg = '#bcc514')
    at72.configure(bg = 'yellow')
    at73.configure(bg = 'yellow')
    at74.configure(bg = 'yellow')
    at75.configure(bg = 'yellow')
    at76.configure(bg = 'yellow')
    at77.configure(bg = 'yellow')
    at78.configure(bg = 'yellow')
    at79.configure(bg = 'yellow')
    at80.configure(bg = 'yellow')
    at81.configure(bg = '#ff5500')
    at82.configure(bg = '#ff5500')
    at83.configure(bg = '#ff5500')
    at84.configure(bg = '#ff55ff')
    at85.configure(bg = '#ff55ff')
    at86.configure(bg = '#af7ffb')
    at87.configure(bg = '#49c9ff')
    at88.configure(bg = '#adaeb0')
    at89.configure(bg = '#ff910b')
    at90.configure(bg = '#ff910b')
    at91.configure(bg = '#ff910b')
    at92.configure(bg = '#ff910b')
    at93.configure(bg = '#ff910b')
    at94.configure(bg = '#ff910b')
    at95.configure(bg = '#ff910b')
    at96.configure(bg = '#ff910b')
    at97.configure(bg = '#ff910b')
    at98.configure(bg = '#ff910b')
    at99.configure(bg = '#ff910b')
    at100.configure(bg = '#ff910b')
    at101.configure(bg = '#ff910b')
    at102.configure(bg = '#ff910b')
    at103.configure(bg = '#ff910b')
    at104.configure(bg = 'yellow')
    at105.configure(bg = 'yellow')
    at106.configure(bg = 'yellow')
    at107.configure(bg = 'yellow')
    at108.configure(bg = 'yellow')
    at109.configure(bg = 'yellow')
    at110.configure(bg = 'yellow')
    at111.configure(bg = 'yellow')
    at112.configure(bg = 'yellow')
    at113.configure(bg = '#ff5500')
    at114.configure(bg = '#ff5500')
    at115.configure(bg = '#ff5500')
    at116.configure(bg = '#ff5500')
    at117.configure(bg = '#ff5500')
    at118.configure(bg = '#af7ffb')


leg = Label(win, text = "LEGEND",width = 90 ,bg = "black", fg = "white", font = ("georgia", 14, "bold"))
leg.place(x = 0 , y = 540)

leg1 = Button(win, text = "Alkali Metals", font = ('georgia', 10, 'bold'), bg = '#49c9ff', command = AlkaliMetals)
leg1.place(x = 42, y = 580)
leg1.bind('<Enter>', AlkaliMetals)
leg1.bind('<Leave>', AlkaliMetalsleft )

leg2 = Button(win, text = "Alkaline Earth Metals", font = ('georgia', 10, 'bold'), bg = '#adaeb0')
leg2.place(x = 150, y = 580)
leg2.bind('<Enter>', alkalineentered)
leg2.bind('<Leave>', alkalineleft)

leg3 = Button(win, text = "Transition Metals", font = ('georgia', 10, 'bold'), bg = 'yellow')
leg3.place(x = 322, y = 580)
leg3.bind('<Enter>',transitionentered)
leg3.bind('<Leave>',transitionleft)

leg4 = Button(win, text = "Non Metals", font = ('georgia', 10, 'bold'), bg = '#1aff40')
leg4.place(x = 467, y = 580)
leg4.bind('<Enter>', Nonmetalsentered)
leg4.bind('<Leave>', Nonmetalsleft )

leg5 = Button(win, text = "Metalloids", font = ('georgia', 10, 'bold'), bg = '#ff55ff')
leg5.place(x = 564, y = 580)
leg5.bind('<Enter>',metalloidsentered)
leg5.bind('<Leave>',metalloidsleft)

leg6 = Button(win, text = "Post Transition Metals", font = ('georgia', 10, 'bold'), bg = '#ff5500')
leg6.place(x = 655, y = 580)
leg6.bind('<Enter>',postentered)
leg6.bind('<Leave>',postleft)

leg7 = Button(win, text = "Lanthanoides", font = ('georgia', 10, 'bold'), bg = '#bcc514')
leg7.place(x = 834, y = 580)
leg7.bind('<Enter>',lanentered)
leg7.bind('<Leave>',lanleft)

leg8 = Button(win, text = "Actinoides", font = ('georgia', 10, 'bold'), bg = '#ff910b')
leg8.place(x = 949, y = 580)
leg8.bind('<Enter>',actentered)
leg8.bind('<Leave>',actleft)

x = msg.askyesnocancel('Complete Activity', 'Do you want to Know how many elements are possible with your name!')

if x == True:
    # Dictionary for Symbols and Elements
    d = {"h" : "hydrogen" , "he" : "helium" , "li" : "lithium" ,
         "be" : "beryllium" , "b" : "boron" , "c" : "carbon" ,
         "n" : "nitrogen" , "o" : "oxygen" , "f" : "fluorine" ,
         "ne" : "neon" , "na" : "sodium" , "mg" : "magnesium" ,
         "al" : "aluminium" , "si" : "silicon" , "p" : "phosphorous" ,
         "s" : "sulphur" , "cl" : "chlorine" , "ar" : "argon" ,
         "k" : "potassium" , "ca" : "calcium" , "sc" : "scandium" ,
         "ti" : "titanium" , "v" : "vanadium" , "cr" : "chromium" ,
         "mn" : "manganese" , "fe" : "iron" , "co" : "cobalt" ,
         "ni" : "nickel" , "cu" : "copper" , "zn" : "zinc" ,
         "ga" : "gallium" , "ge" : "germanium" , "as" : "arsenic" ,
         "se" : "seleniuim" , "br" : "bromine" , "kr" : "krypton" ,
         "rb" : "rubudium" , "sr" : "strontium" , "y" : "yttrium" ,
         "zr" : "zirconium" ,"nb" : "niobium" , "mb" : "molybdenum" ,
         "tc" : "tectinium" ,"ru" : "ruthenium" , "rh" : "rhodium" ,
         "pd" : "palladium" ,"ag" : "silver" , "cd" : "cadmium" ,
         "in" : "indium" , "sn" : "tin" , "sb" : "antimony" ,
         "te" : "tellurium" , "i" : "iodine" , "xe" : "xenon" ,
         "cs" : "ceasium" , "ba" : "barium" , "la" : "lanthanum" ,
         "ce" : "cerium" , "pr" : "prasodymium" , "nd" : "neodymium" ,
         "pm" : "pramathium" , "sm" : "samarium" , "eu" : "europium" ,
         "gd" : "gadolinum" , "tb" : "terbium" , "dy" : "dysprosium" ,
         "ho" : "holmium" , "er" : "erbium" , "tm" : "thullium" ,
         "yb" : "ytterbium" , "lu" : "lutetium" , "hf" : "halfnium" ,
         "ta" : "tantalum" , "w" : "tungsten" , "re" : "rehenium" ,
         "os" : "osmium" , "ir" : "iridium" , "pt" : "platinum" ,
         "au" : "gold" , "hg" : "mercury" , "tl" : "thallium" ,
         "pb" : "lead" , "bi" : "bismuth" , "po" : "polonium" ,
         "at" : "astatine" , "rn" : "radon" , "fr" : "francium" ,
         "ra" : "radium" , "ac" : "actinum" , "th" : "thorium" ,
         "pa" : "proctactinum" , "u" : "uranium" , "np" : "neptunium" ,
         "pu" : "plutonium" , "am" : "americium" , "cm" : "curium" ,
         "bk" : "berkelium" , "cf" : "californium" , "es" : "einsteinium" ,
         "fm" : "fermium" , "md" : "mendelevium" , "no" : " nobelium" ,
         "lr" : "iridium" , "rf" : "rutherfordium" , "db" : "dubnium" ,
         "sg" : "seaborgium" , "bh" : "bohrium" , "hs" : "hassium" ,
         "mt" : "meitneium" , "ds" : "dysprossium" , "rg" : "roetgenium" ,
         "cn" : "coppernecium" , "nh" : "nihoium" , "fl" : "flervovium" ,
         "mc" : "meterbinium" , "lv" : "livermorium" , "ts" : "tenessene" ,
         "og" : "oganessene"}


    board =  Toplevel()
    board.configure(bg = '#f7e7ff')
    board.resizable = (False, False)
    board.title('Finding Elements')
    board.geometry('1000x620')
    board.iconbitmap('periodic-table.ico')

    def sub():
        global l2,l3,t1,t2,l4
        
        l2 =  Label(board, text = 'Elements Having One Letter In Symbol', font = ("arial", 15, "bold"), width = 33, bg = 'light green' )
        l2.place(x = 25, y = 190)

        l3 =  Label(board, text = 'Elements Having Two Letters In Symbol', font = ("arial", 15, "bold"), width = 33, bg = 'light green')
        l3.place(x = 500, y = 190)

        t1 = scrolledtext.ScrolledText(board, width = 33, height = 13, font = ('courIo_radiusr new',15))
        t1.place(x = 25, y = 230)

        t2 = scrolledtext.ScrolledText(board, width = 33, height = 13,font = ('courIo_radiusr new',15))
        t2.place(x = 500, y = 230)
        # Empty lists for iteration
        a = z = x = []
        # IdentifIo_radiusrs for counting
        b = c = 0
        
        inp=sv.get()
        inpt = inp.lower()
        
        for j in inpt:
            a=a+[j]
        perm = permutations(a,2)

        # Crating list of two letter permutations
        for i in list(perm):
            if i[0]+i[1] not in z:
                z=z+[i[0]+i[1]]
                
        # Creating list of one Letter permutations    
        for k in inpt:
            if k[0] not in x:
                x=x+[k[0]] 
            
        
        #Iteration for Checking matching Symbols for one Letter
        ins=''
        for l in range(len(x)):
            if x[l] in d:
                va=x[l].capitalize()
                lm='-'
                ka=d[x[l]].capitalize()
                ins=ins+va+lm+ka
                ins = ins + '''\t\t\t\t '''
                b=b+1

        # Iteration for Checking matching Symbols for two letters
        lmn=''
        for p in range(len(z)):
            if z[p] in d:
                par=z[p].capitalize()
                lu='-'
                kdf=d[z[p]].capitalize()
                lmn=lmn+par+lu+kdf
                lmn = lmn + '''\t\t\t\t '''
                c+=1



        b1 = str(b)
        c1 = str(c)
        to= b + c
        tot = str(to)
        t1.insert( INSERT, 'Number of Elements found are ')
        t1.insert( INSERT, b1 + '\n')
        t1.insert( INSERT,'\n')    
        t1.insert( INSERT, ins + '\n')
        t1.configure(state = 'disabled')
        t2.insert( INSERT, 'Number of Elements found are ')
        t2.insert( INSERT, c1 + '\n')
        t2.insert( INSERT,'\n') 
        t2.insert( INSERT, lmn + '\n')
        t2.configure(state = 'disabled')
        
        l4 =  Label(board, text = 'The total number of elements matched are ' + tot, font = ("times new roman", 20, "bold"), width = 40, bg = 'orange' )
        l4.place(x = 180, y = 550)
        
    def cls():
        
        global l2,l3,t1,t2,l4
        
        sv.set('')
        l2.place_forget()
        l3.place_forget()
        t1.place_forget()
        t2.place_forget()
        l4.place_forget()
      
       
        
    l1 =  Label(board, text = 'Find the Elements in your Name', width = 30, font = ("georgia", 25, "bold"), bg = "maroon", fg = "white")
    l1.pack()

    l1 =  Label(board, text = 'Find the Elements in your Name', font = ("arial", 15, "bold"), bg = 'sky blue' )
    l1.place(x = 25, y = 100)

    sv =  StringVar()

    e1 =  Entry(board,textvariable = sv , width = 30, font = ("Arial",15, "bold") )
    e1.place(x = 335, y = 100)
    e1.focus()

    b1 =  Button(board, text = 'Clear', command = cls, font = ('arial',10, 'bold'))
    b1.place(x = 300, y = 140)

    b2 =  Button(board, text = 'Submit', command = sub, font = ('arial',10, 'bold'))
    b2.place(x = 380, y = 140)

    board.mainloop()
    
win.mainloop()
