from tkinter import *
from tkinter import font
import random
from time import sleep

numCortisol = 10
numLuciferase = 100
cortisol = []

WIDTH = 1000
HEIGHT = 550

"""
A 2D vector class with the two elements represented as x and y
-Contains vector addition, subtraction, division, etc. functions
"""
class vector:
	# initialize the vector for a given x and y
	def __init__(self, x, y):
		self.x = float(x)
		self.y = float(y)

	# represent the vector - dont think this will be needed
	def __repr__(self):
		return 'x = ' + str(self.x) + ', y = ' + str(self.y)

	# add two vectors and return the resulting vector
	def __add__(self, other):
		return vector(self.x + other.x, self.y + other.y)

	# subtract two vectors and return the resulting vector
	def __sub__(self, other):
		return vector(self.x - other.x, self.y - other.y)

	# multiply two vectors and return the resulting vector
	def __mul__(self, other):
		return vector(self.x * other, self.y * other)

	# divide two vectors and return the resulting vector
	def __div__(self, other):
		return vector(self.x / other, self.y / other)

	# add another vector to this vector
	def __iadd__(self, other):
		self.x += other.x
		self.y += other.y
		return self

	# subtract another vector from this vector
	def __isub__(self, other):
		self.x -= other.x
		self.y -= other.y
		return self

	# divide this vector by another vector
	def __itruediv__(self, other):
		if isinstance(other, vector):
			self.x /= other.x if other.x else 1
			self.y /= other.y if other.y else 1
		else:
			self.x /= other
			self.y /= other
		return self

	# return the magnitude of this vector
	def mag(self):
		return ((self.x ** 2) + (self.y ** 2)) ** 0.5


class Cortisol:
    def __init__(self):
        self.position = self.randomPlacingCortisol()
        self.velocity = vector(0,0)

    def randomPlacingCortisol(self):
        x = random.randint(10,WIDTH-10) #Modify later when sub with img
        y = random.randint(10,HEIGHT-10)
        return vector(x,y)

    def move(self):
        frameVector = self.outOfFrameRule()
        randVector = self.randMove()
        self.velocity = frameVector + randVector
        #speed limit
        
        self.position += self.velocity

    def randMove(self):
        x = random.randint(-10,10)
        y = random.randint(-10,10)
        randVector = vector(x,y)
        return randVector

    def outOfFrameRule(self):
        frameVector = vector(0,0)

        if self.position.x >= WIDTH:
            frameVector += vector(-10,0)
        if self.position.x <= 0:
            frameVector += vector(10,0)
        if self.position.y >= HEIGHT:
            frameVector += vector(0,-10)
        if self.position.y <= 0:
            frameVector += vector(0,10)
        return frameVector

def initiateCortisol():
    for i in range(numCortisol):
        newMolecule = Cortisol()
        cortisol.append(newMolecule)
    return
        
def createWindow():
    
    simWindow = Tk()
    simWindow.geometry('%dx%d+%d+%d' % (WIDTH,HEIGHT+50,(simWindow.winfo_screenwidth() - WIDTH)/2,(simWindow.winfo_screenheight() - HEIGHT)/2))
    simWindow.bind_all('<Escape>',lambda event: event.widget.destroy())

    fontHeader = font.Font(family = "Times New Roman", size = "24", underline = 0, weight = "bold")
    fontBody = font.Font(family = "Times New Roman", size = "16")

    TitleFrame = Frame(simWindow, height = 50)
    TitleFrame.pack()

    windowLabel = Label(TitleFrame, text = "Cortisol Simulation", font = fontHeader)
    windowLabel.pack()

    canvas = Canvas(simWindow, width = WIDTH, height = HEIGHT, background = 'white')
    canvas.pack(side = BOTTOM)
    return simWindow, canvas

def drawCortisol(window,canvas):
   # cortisolImg = PhotoImage(file = '')
    for i in range(numCortisol):
        #newMolecule = canvas.create_image(molecule[0],molecule[1], image=cortisolImg) 
        newMolecule = canvas.create_rectangle(cortisol[i].position.x,cortisol[i].position.y,cortisol[i].position.x+10,cortisol[i].position.y+10, fill="black")
        cortisol[i].move()
        
    canvas.pack()
    window.update()
    sleep(0.1)
    canvas.delete(ALL)
    
    

def main():
    window, canvas = createWindow()
    initiateCortisol()
    for i in range(1000000):
        drawCortisol(window,canvas)
    
main()
