import pylab
from mesa import Agent, Model
from mesa.space import MultiGrid
from mesa.time import StagedActivation
from random import random
from mesa.datacollection import DataCollector

        
class individus(Agent): #définition des agents
    def __init__(self,_id_,model,healtH):
        super().__init__(_id_,model)
        self.t_incub=0#temps d'incubation et de guérison initialisés à 0
        self.t_infect=0
        self.health=healtH
        self.death=10
    def move(self): #fonction de mouvement dans l'espace
        possible_steps=self.model.grid.get_neighborhood(self.pos,moore=True,include_center=True)
        new_position=self.random.choice(possible_steps)
        self.model.grid.move_agent(self,new_position)
    def etat(self):#fonction régissant l'état de santé de l'individus
        if self.health=="infecte":
            if self.t_incub<5:
                self.t_incub+=1/48 #1 pas toutes les demi-heures
            else:
                self.health="infectieux"
                self.model.infectieux+=1
                self.model.infecte-=1
                if random()<0.007:
                    self.death=8*random()
        elif self.health=="infectieux":
            if self.death<=self.t_infect:
                self.health="morts"
                self.model.grid.remove_agent(self)
                self.model.schedul.remove(self)
                self.model.infectieux-=1
                self.model.morts+=1
            elif self.t_infect<8:
                self.t_infect+=1/24 
            else:
                    self.health="gueris"
                    self.model.gueris+=1
                    self.model.infectieux-=1
    def contamination(self):#fonction permettant à un agent d'en contaminer un autre
        if self.health=="infectieux":
            cellmates=[(self.model.grid.get_cell_list_contents(i)) 
            for i in (self.model.grid.get_neighborhood
                      (self.pos,moore=True,include_center=True))]
            for j in cellmates:
                for a in j:
                    if a.health=="sains":
                        if random()<=3/384:
                            a.health="infecte"
                            self.model.infecte+=1
                            self.model.sains-=1

        
            
        
class environnement(Model): #definition de l'environnement
    def __init__(self,N,m,width,height):
        self.infectieux=m        
        self.sains=N
        self.infecte=0
        self.agent=[]       #paramètres de l'environnement
        self.gueris=0
        self.heure=0
        self.morts=0
        self.date=0
        self.grid = MultiGrid(width, height, False)#espace de l'environnement
        stages=["move","contamination","etat"]
        self.schedul= StagedActivation(self,stages,True)#stockage des agents   
        for i in range((self.sains)): #création des agents sains
            a=individus(i,self,"sains")            
            self.schedul.add(a)
            q=self.random.randrange(self.grid.width)
            p=self.random.randrange(self.grid.height)
            self.grid.place_agent(a, (q,p)) #placer les agents dans l'espace
            self.agent.append(a) #stocker les agents dans le model

        for i in range((self.sains),(self.sains)+(self.infectieux)):
            a=individus(i,self,"infectieux")
            self.schedul.add(a)
            q=self.random.randrange(self.grid.width)
            p=self.random.randrange(self.grid.height)
            self.grid.place_agent(a, (q,p)) 
            self.agent.append(a)
            
        self.dc=DataCollector(  #collecte de donnés pour la representation
            model_reporters={"sains":lambda m:m.sains,"infectieux":lambda m:m.infectieux,
                             "infecte":lambda m:m.infecte,"gueris":lambda m:m.gueris,"morts":lambda m:m.morts},
            agent_reporters={"health":"health"})
        
    def step(self): #ce que fera le modèle à chaque pas
        if self.heure==0:
            self.date+=1
        self.heure=(self.heure+1/2)%24
        self.dc.collect(self)
        self.schedul.step()
           

              
m=environnement(1200,1,30,40)                   
'''
import matplotlib.pyplot as plt
x=[]
y=[]
y2=[]
y3=[]
y4=[]
y5=[]
for i in range(1500):
    m.step()
    x.append(i)
    y.append(m.sains)
    y2.append(m.infecte)
    y3.append(m.infectieux)
    y4.append(m.gueris)
    y5.append(m.morts)
pylab.figure(figsize=(5,5))
plt.plot(x,y, label="sains")
plt.plot(x,y2, label="infecte")
plt.plot(x,y3, label="infectieux")
plt.plot(x,y4, label="gueris")
plt.plot(x,y5, label="morts")
plt.legend()
plt.show()'''