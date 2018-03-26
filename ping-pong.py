from tkinter import*
from math import*
from timeit import default_timer


#déplacement balle
class Bille:
    def __init__(self,x=0,y=0):
        self.x=40
        self.y=70
        self.objet=0
        self.id=0
        self.alpha=45
        self.avancerx=True
        self.avancery=True
        self.demarrer=True

    def setDemarrer(self,bool):
        self.demarrer=bool

    def placer(self,can):
        self.objet=can.create_oval(self.x-5,self.y-5,self.x+5,self.y+5,fill="orange")

    def deplacer(self,can,x,y):
        can.coords(self.objet,x-5,y-5,x+5,y+5)
        self.x=x
        self.y=y

    def setAngle(self,angle):
        self.alpha=angle

    def rebond(self,raquette1,raquette2):
        if self.x<=35:
            if self.y>=raquette1.getY() and self.y<=raquette1.getY()+50:
                return True
        if self.x>=465:
            if self.y>=raquette2.getY() and self.y<=raquette2.getY()+50:
                return True
        return False
            
    def deplacement(self,can):
        global point_joueur_1
        global point_joueur_2
    	
        if self.alpha==45:
            dx=1
            dy=1
            
        
        if self.x<=35:
            if self.rebond(raquette1,raquette2)==True:
                self.avancerx=True
                self.x+=dx
            else:
                self.demarrer=False
                point_joueur_1+=1
                relancer()
                
            
        if self.x>=465:
            if self.rebond(raquette1,raquette2)==True:
                self.avancerx=False
                self.x-=dx
            else:
                self.demarrer=False
                point_joueur_2+=1
                relancer()
        
        update_points()        
                
        if self.x<465 and self.avancerx==True:
            self.x+=dx
        if self.x>30 and self.avancerx==False:
            self.x-=dx

          
        if self.y<=10:
            self.avancery=True
            self.y+=dy
        if self.y>=290:
            self.avancery=False
            self.y-=dy
        if self.y<290 and self.avancery==True:
            self.y+=dy
        if self.y>10 and self.avancery==False:
            self.y-=dy
        can.coords(self.objet,self.x-5,self.y-5,self.x+5,self.y+5)

        if self.demarrer==True:
            self.id=can.after(12,dep)
    
        
    def stop(self,can):
        can.after_cancel(self.id)
        
def demarrer():
    boule.setDemarrer(True)
    boule.deplacement(can)
    updateTime()

def dep():
    boule.deplacement(can)

def relancer():
    global bouton
    boule.deplacer(can,35,70)
    bouton.config(text="Relancer")


#déplacement raquette
class Raquette:
    def __init__(self,x=0,y=0,numero=0):
        self.x=x
        self.y=y
        self.numero=numero
        self.objet1=0
        self.id=0

    def getY(self):
        return self.y
        
    def placer(self,can):
        self.objet1=can.create_rectangle(self.x,self.y,self.x+20,self.y+50,fill="red")
        

    def deplacement(self,can,event):
        if self.numero==1:
            if event.char=="z":
                if self.y>0:
                    self.y=self.y-5
                    can.coords(self.objet1,10,self.y,30,self.y+50)

            if event.char=="s":
                if self.y<250:
                    self.y=self.y+5
                    can.coords(self.objet1,10,self.y,30,self.y+50)

        if self.numero==2:
            if event.char=="p":
                if self.y>0:
                    self.y=self.y-5
                    can.coords(self.objet1,490,self.y,470,self.y+50)

            if event.char=="m":
                if self.y<250:
                    self.y=self.y+5
                    can.coords(self.objet1,470,self.y,490,self.y+50)



            

def deplacer(evt):
    raquette1.deplacement(can,evt)
    raquette2.deplacement(can,evt)

def update_points():
	global can
	global point_joueur_1
	global point_joueur_2
	global texte_joueur_1
	global texte_joueur_2
	can.itemconfigure(texte_joueur_1, text=str(point_joueur_2))
	can.itemconfigure(texte_joueur_2, text=str(point_joueur_1))

# interface tkinter
fen= Tk()

can = Canvas(fen, width=500, height=300, background='#CDEAE7')

point_joueur_1 = 0
point_joueur_2 = 0

rectangleD = can.create_rectangle(360,260,470,290,width=2,outline='#FFC300')
rectangleG= can.create_rectangle(100,260,210,290,width=2,outline='#900C3F')
rectangleH= can.create_rectangle(200,50,300,10,width=2,outline='#113589')
rectangleB= can.create_rectangle(450,250,50,70,fill='#0B610B',width=0)

lignecontourB = can.create_line(450,250,50,250,fill='white',width=10)
lignecontourH = can.create_line(450,70,50,70,fill='white',width=10)
lignecontourD = can.create_line(450,255,450,65,fill='white',width=10)
lignecontourG = can.create_line(50,255,50,65,fill='white',width=10)
lignecentreG = can.create_line(350,160,450,160,fill='white',width=10)
lignecentreD = can.create_line(50,160,150,160,fill='white',width=10)
lignecentreM = can.create_line(250,250,250,70,fill='white',width=10)

texte2 = can.create_text(320,275, text="joueur 2",fill='#FFC300',font="courrier 15")
texte1 = can.create_text(60,275,text="joueur 1",fill='#900C3F',font="courrier 15")
texte3 = can.create_text(160,28,text="temps:",fill='#113589',font="courrier 15")
texte_joueur_1 = can.create_text(120, 275, text="0", font="courrier 15")
texte_joueur_2 = can.create_text(380, 275, text="0", font="courrier 15")
"affichage du chrono"
text_clock = can.create_text(250, 30,font='courrier 20',fill='#113589')

"boutton quitter"
Button(fen, text = 'Quitter', command = fen.destroy).pack(side = BOTTOM)

#chrono
def updateTime():
    "on démarre le timer par déffaut"
    now = default_timer() - start
    dessineTime(now)
    fen.after(1000, updateTime)
    
def dessineTime(time):
    "on configure sont affichage par seconde minute et heure"
    minutes, seconds = divmod(time, 60)
    hours, minutes = divmod(minutes, 60)
    "on montre comment l'afficher"
    str_time = "%d:%02d:%02d" % (hours, minutes, seconds)
    "configuration de l'affichage"
    can.itemconfigure(text_clock, text = str_time)

"démarer le timer"
start = default_timer()

dessineTime(start)

can.pack()
boule=Bille(0,0)

boule.placer(can)
bouton=Button(text="Lancer",command=demarrer)
bouton.pack()

raquette1=Raquette(10,50,1)
raquette1.placer(can)

raquette2=Raquette(470,50,2)
raquette2.placer(can)


can.bind("<Key>",deplacer)
# updateTime()
can.focus_set()
fen.mainloop()

