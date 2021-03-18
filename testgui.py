from tkinter import *
from tkinter import filedialog, scrolledtext, Menu, Spinbox
from worldmap import *
from json import *
class app():
    worldfile = ''
    world = 0
    root = Tk()
    menu = Menu(root)
    filemenu = Menu(menu)
    save = Menu(filemenu)
    txt = scrolledtext.ScrolledText(root, width=60, height=40)
    def __init__(self):
        self.root.geometry("1920x1080")
        self.root.config(menu = self.menu) 
        self.txt.grid(column=0, row=0 ,rowspan = 6)
        self.sbut = Button(self.root, command = self.saveworld, text = 'сохранить изменения')
        self.sbut.grid(column = 0, row = 7, sticky = NSEW)
        self.filemenu.add_command(label ="открыть", command = self.openfile)
        self.save.add_command(label = "json", command = self.createJSON)
        self.save.add_command(label = "фото", command = self.saveImage)
        self.save.add_command(label = "мир TeaSurvival", command = self.createArray)
        self.filemenu.add_cascade(label = "сохранить как" , menu = self.save)
        self.menu.add_cascade(label = 'файл', menu = self.filemenu)
        self.root.mainloop()
    def openfile(self):
        self.worldfile = filedialog.askopenfilename(filetypes = [('TeaSurvival world files','*.js*'),('JSON files','*.json'),('txt files','*.txt'),('all files','*')])
        try:
            self.world = list(GetWorld(filename = self.worldfile))
        except:
            self.txt.insert(INSERT,'open file error')
        else:
            self.txt.insert(INSERT, str(self.world))
    def saveworld(self):
        self.world = json.loads(self.txt.get(1.0, END))
    def saveImage(self):
        tile = Label(self.root, text = 'размер пикселя: ')
        self.sb = Spinbox(self.root, width = 5, from_ = 1,to = 40)
        isbut = Button(self.root, text = 'сохранить как изображение', command =self.createImage)
        tile.grid(column = 1, row = 0)
        self.sb.grid(column = 2, row = 0)
        isbut.grid(column = 1, row = 0 , columnspan = 2, sticky = SE)
    def createImage(self):
        createPhoto(int(self.sb.get()),tiles= tiles, array=self.world)
    def createArray(self):
        arFile = open(str(filedialog.asksaveasfilename(filetype=[('TeaSurvival world','*.jsts')])),'w')
        arFile.write(str(self.world))
    def createJSON(self):
        arFile = open(str(filedialog.asksaveasfilename(filetype=[('JSON file','*.json')])),'w')
        arfile.write(json.dump(self.world))

if __name__ == "__main__":
    a = app()