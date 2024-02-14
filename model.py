#import pandas as pd
import pylab
from mesa import Agent, Model
from mesa.space import MultiGrid
from mesa.time import StagedActivation
from mesa.time import RandomActivation
from random import random
#import tqdm as tqdm
from pylab import *
import random as rd
from mesa.datacollection import DataCollector

#j'utilise mesa pour la creation et la gestion d'environnement et d'agent
#pour en savoir plus sur mesa:https://mesa.readthedocs.io/en/latest/


class individus(Agent): #classe agent predefinis dans mesa
    t_incub=0#temps d'incubation 
    t_infect=0#temps d'infection
#dans la classe agent, on créer les fonctions propres aux agents
    def __init__(self,model,_id_,function,health):#création d'un agent
#function= role sociale de l'agent (vieux, etudiant,travailleur), health=etat de santée
#model est l'environnement (la ville) dans lequel les agents se trouvent
#id est le numero d'identifiant propre à l'agent (obligatoire)
        super().__init__(_id_,model)#l'agent hérite des propriétés du model dans lequel il se trouve
        self.bus_number=-1#les agents prendront le bus, il est important de savoir lequel
        self.function=function
        self.health=health
        self._id_=_id_#aquisition des parametres par l'agent
        self.position=0#j'utilise un systeme de position, chaque numeor est associé à un lieu
        if self.function!="mineur":
            self.foyer=(self._id_-self.model.mineurs)//2
        else:#foyer correspond au numero de la famille dans lequel se trouve l'agent et reflète son  logement
            self.foyer=(self._id_//2)

    def etat(self):#evolution de l'état de santé d'un agent, self renvoie à l'agent
        if self.health=="infecte":
            if self.t_incub<3:
                self.t_incub+=1/48 #1 pas toutes les demi heures
            else:
                self.health="infectieux"
                self.model.infectieux+=1
                self.model.infecte-=1
        elif self.health=="infectieux":
            if self.t_infect<8:
                self.t_infect+=1/48 
            else:
                self.health="gueris"
                self.model.gueris+=1
                self.model.infectieux-=1
                
    def contamination(self,grille):#fonction de contamination, grille correspond aux lieu où la contamination à lieu
        if self.health=="infectieux":
            cellmates=[(grille.get_cell_list_contents(i)) for i in (grille.get_neighborhood(self.pos,moore=True,include_center=True))]
            for j in cellmates:
                for a in j:
                    if a.health=="sains":
                        if random()>=0.6:
                            a.health="infecte"
                            self.model.infecte+=1
                            self.model.sains-=1
                            self.model.contaminé_tot+=1
                            
    def bus_move(self):#mouvement d'un agent dans un bus
        possible_steps=self.model.bus[self.bus_number][0].get_neighborhood(self.pos,moore=True,include_center=True)
        new_position=self.random.choice(possible_steps)
        self.model.bus[self.bus_number][0].move_agent(self,new_position)
    def bus_contamination(self):#conatmination des agents dans un bus
        x=self.model.contaminé_tot#nombre totale de contaminés
        self.contamination(self.model.bus[self.bus_number][0])#execution de la fonction de contagion dans le bus
        self.model.bus_contagion+=self.model.contaminé_tot-x#nombre de contaminé dans le bus
    def bus(self):#fonctionnement d'un agent dans un bus selon la nouvelle position du bus et le role sociale de l'agent, celui-ci vas descendre ou non du bus
        destination=self.model.bus_pos[self.bus_number//2]
        if destination==1 and self.function=="mineur":    
            self.model.classes[(self._id_)//40][1].add(self)
            x = rd.randrange(7)
            y = rd.randrange(10)
            self.model.bus[self.bus_number][1].remove(self)
            self.model.bus[self.bus_number][0].remove_agent(self)
            self.model.classes[(self._id_)//40][0].place_agent(self,(x,y))
            self.model.classes[(self._id_)//40][0].move_to_empty(self)
            self.position=1
        elif destination==2 and self.function=="prolo":
            self.model.usine[1].add(self)
            x = rd.randrange(126)#126
            y = rd.randrange(161)#161
            self.model.bus[self.bus_number][1].remove(self)
            self.model.bus[self.bus_number][0].remove_agent(self)
            self.model.usine[0].place_agent(self,(x,y))
          #  self.model.usine_space.move_to_empty(self)
            self.position=2
#        elif [self.model.destination=="hospitale"] and [self.function=="soignant"]:
 #           self.model.hospitale.add(self)  remove_agent
        elif destination==0:

            self.model.bus[self.bus_number][1].remove(self)
            self.model.bus[self.bus_number][0].remove_agent(self)  
            self.model.menages[self.foyer][1].add(self)
            x = rd.randrange(5)
            y = rd.randrange(10)
            self.model.menages[self.foyer][0].place_agent(self,(x,y))
            self.position=0
            
        
    def famille_move(self):
        possible_steps=self.model.menages[self.foyer][0].get_neighborhood(self.pos,moore=True,include_center=True)
        new_position=self.random.choice(possible_steps)
        self.model.menages[self.foyer][0].move_agent(self,new_position)
    def famille_contamination(self):
        x=self.model.contaminé_tot
        self.contamination(self.model.menages[self.foyer][0])
        self.model.famille_contagion+=self.model.contaminé_tot-x
    def school(self):
        x=self.model.contaminé_tot
        self.contamination(self.model.classes[(self._id_)//40][0])
        self.model.ecole_contagion+=self.model.contaminé_tot-x
    def usine_move(self):
        possible_steps=self.model.usine[0].get_neighborhood(self.pos,moore=True,include_center=True)
        new_position=self.random.choice(possible_steps)
        self.model.usine[0].move_agent(self,new_position)
    def usine_contamination(self):
        q=self.model.contaminé_tot
        self.contamination(self.model.usine[0])
        self.model.usine_contagion+=(self.model.contaminé_tot-q)
    def arret_bus(self):
             for i in range(3):
                if self.model.bus_pos[i]==self.position:
                    u=i
             if self.model.bus[2*u][1].get_agent_count()<60:
                 m=2*u
             else:
                 m=2*u+1
             self.bus_number=m
             self.model.arret_bus[self.position].remove(self)
             self.model.bus[m][1].add(self)
             x =rd.randrange(4)#rd.randint(0,3)
             y =rd.randrange(14)
             self.model.bus[m][0].place_agent(self,(x,y))
#avant d'aller dans un bus les agents vont dans un arrêt de bus (plus facile à gérer)       


#notre ville est composée de foyers, d'une ecole et d'une usine (je voulais mettre un hosto et un supermarché mais pas eu le temps)





class ville(Model):
    def __init__(self,population,nb_malades):#creation du model
        self.running=True#jsp à quoi ca sert, mais c necessaire
        self.schedule=RandomActivation(self)#on fonctionne avec des schedules, dans lesquels on rentre des fonctions dans un certain ordre et qui seront executé dans cet ordre
        self.pas=0#nombre d'execution du modele
        self.bus_contagion=0#statistiques
        self.ecole_contagion=0
        self.famille_contagion=0
        self.usine_contagion=0
        
        self.sains=population-nb_malades
        self.infectieux=nb_malades
        self.infecte=0
        self.gueris=0
        self.morts=0
        self.contaminé_tot=nb_malades
        self.liste_matin=[]
        self.liste_aprem=[]
        self.popu=population
        malades=[rd.randrange(population+1) for i in range(nb_malades)]
        self.agents=[]
        self.mineurs=2*int(population*0.09)
        self.adultes=[i for i in range(self.mineurs,population)]
        self.famille=[(i,i+1,i+self.mineurs,i+self.mineurs+1) for i in range(0,self.mineurs,2)]+[(i,i+1) for i in range(2*self.mineurs,population,2)]
        self.nb_familles=len(self.famille)
        self.nb_classes=((self.mineurs)//40)+1
        self.date=0
        self.heure=0
        self.sains=population
        arrets=["arret_bus"]
        self.arret_bus=[ StagedActivation(self,arrets) for i in range(3)]
        self.destinations=["quartier_res","ecole","usine"]
        self.bus_pos=[0,1,2]#les destinations des bus
        school_stages=["etat","school"]#schedules associés aux differents lieux
        usine_stage=["etat","usine_move","usine_contamination"]
        bus_stages=["etat","bus_move","bus_contamination","bus"]
        famille_stage=["etat","famille_move","famille_contamination"]
        
        #self.ecole=StagedActivation(self,school_stages,True)
        #self.usine=StagedActivation(self,usine_stage,True)
#        self.hospitale=StagedActivation(self,hospitale_stages,True)
        
        #self.classe=MultiGrid(7,10,False)   usine_space
        '''self.bus_agent=RandomActivation(self)
        popu
        list_bus=[bus(self,i,i//2) for i in range(6)]
        for i in list_bus:
            self.bus_agent.add(i)'''
        
        #création des sous-modeles propres à chaque lieux
        self.bus=[(MultiGrid(4,14,False),StagedActivation(self,bus_stages,True)) for i in range(9)]#on fait 9 bus pour 3 destinations donc les pas se feront dans 3 bus simultanément à chaque pas
        self.menages=[(MultiGrid(6,11,False),StagedActivation(self,famille_stage,True)) for i in range(self.nb_familles)]
        self.classes=[(MultiGrid(8,11,False),StagedActivation(self,school_stages,True)) for i in range((self.mineurs//40)+3)]
#        self.hospitale_space=MultiGrid(125,160,False)
        self.usine=(MultiGrid(126,161,False),StagedActivation(self,usine_stage,True))#(126,161)
        for i in range(self.mineurs):
            if i in malades:
                santé="infectieux"
            else:
                santé="sains"
            q=individus(self,i,"mineur",santé)#création des agents dans le modèle
            self.menages[q.foyer][1].add(q)#dabord placés dans les foyer
            x = self.random.randrange(5)
            y = self.random.randrange(10)
            self.menages[q.foyer][0].place_agent(q,(x,y))
            self.agents.append(q)
            self.schedule.add(q)
#            self.classes[(i//40)+1][1].add(q)
#            for i in range(mineurs,mineurs+soignants):
 #           q=individus(self,i,"soignants")
  #          self.QR.add(q)
        for i in range(self.mineurs,population):
            if i in malades:
                santé= "infectieux"
            else:
                santé="sains"
            q=individus(self,i,"prolo",santé)
            self.menages[q.foyer][1].add(q)
            x = self.random.randrange(5)
            y = self.random.randrange(10)
            self.menages[q.foyer][0].place_agent(q,(x,y))
            self.agents.append(q)
            self.schedule.add(q)
        self.dc=DataCollector(#collection des donnés (marche pas trop)
            model_reporters={"sains":lambda m:m.sains,"infectieux":lambda m:m.infectieux,
            "infecte":lambda m:m.infecte,"gueris":lambda m:m.gueris,"morts":lambda m:m.morts,
            "date": lambda m:m.date, "heure": lambda m:m.heure, "contaminés tot": lambda m:m.contaminé_tot,
            "bus contamination": lambda m:m.bus_contagion, "ecole contamination": lambda m:m.ecole_contagion,
            "usine contamination": lambda m:m.usine_contagion,"famille contamination": lambda m:m.famille_contagion},
            agent_reporters={"health":"health"})
            
    def step(self):#execution du modele
        self.dc.collect(self)#colection des donnés
        self.pas+=1
        if self.heure==0:
            self.date+=1
            self.liste_matin=[i for i in range(self.popu)]#ceux qui prennent le bus le matin
            self.liste_aprem=(self.liste_matin).copy()#ceux qui le prennent l'aprem
            rd.shuffle(self.liste_matin)
            rd.shuffle(self.liste_aprem)
        self.heure=(self.heure+1/2)%24
        if 7<=self.heure<=10:#execution des differentes fonction selon l'heure de la journée
            if len(self.liste_matin)>=120:
                a=120#places dans deux bus
            else:
                a=len(self.liste_matin)
            for i in range(a):
                x=self.liste_matin.pop()
                agent=self.agents[x]#agent d'id x
                if agent.function=="mineur":
                    maison=x//2
                else:
                    maison=(x-self.mineurs)//2#numero du foyer
                self.menages[maison][0].remove_agent(agent)
                self.menages[maison][1].remove(agent)#il quitte un lieu donc on l'nenleves de la liste d'agents dans un lieu
                self.arret_bus[0].add(agent)
                
            for i in range(self.nb_familles):
                self.menages[i][1].step()
                
           # for i in range(3):
            #    if self.dest_bus[i]==0:
             #       w=i#numero des bus
           # self.arret_bus[0].step()
            for i in range(3):
               self.arret_bus[i].step()
         #   for i in range(3):
          #      self.dest_bus[i]=(self.dest_bus[i]+1)%3    
           # for i in range(6):                    
            #    self.bus[i][1].step()
            for i in range(self.nb_classes):
                self.classes[i][1].step()
            self.usine[1].step()

        if 8<=self.heure<=18:
            for i in range(self.nb_familles):
                self.menages[i][1].step()
            for i in range(self.nb_classes):
                self.classes[i][1].step()
            self.usine[1].step()
            for i in range(3):
               self.arret_bus[i].step()
            
        if 18<=self.heure:
            if len(self.liste_aprem)>=120:
                t=120
            else:
                t=len(self.liste_aprem)
            for i in range(t):
                x=self.liste_aprem.pop()
                agent=self.agents[x]#agent d'id x
                if agent.function=="mineur":
                    self.classes[x//40][0].remove_agent(agent)
                    self.classes[x//40][1].remove(agent)
                    self.arret_bus[1].add(agent)
                else:
                    self.usine[0].remove_agent(agent)
                    self.usine[1].remove(agent)
                    self.arret_bus[2].add(agent)

            self.arret_bus[1].step()
            self.arret_bus[2].step()
           # for i in range(3):
            #    self.dest_bus[i]=(self.dest_bus[i]+1)%3                        
            #self.bus.step()
            for i in range(self.nb_classes):
                self.classes[i][1].step()
            self.usine[1].step()
            for i in range(self.nb_familles):
                self.menages[i][1].step()  
        [x,y,z]=self.bus_pos
        self.bus_pos=[y,z,x]
        
        #for i in range(3):
         #  self.arret_bus[i].step()
        for i in range(9):                    
                self.bus[i][1].step()    
                
m=ville(800,5)#création de la ville              

import matplotlib.pyplot as plt
x=[]
y=[]
y2=[]
y3=[]
y4=[]
y5=[]
for i in range(1200):#nombre de pas
    m.step()#execution d'un pas du modele
    x.append(i)
    y.append(m.sains)
    y2.append(m.infecte)
    y3.append(m.infectieux)
    y4.append(m.gueris)
    y5.append(m.morts)
pylab.figure(figsize=(10,10))
plt.plot(x,y, label="sains")
plt.plot(x,y2, label="infecte")
plt.plot(x,y3, label="infectieux")
plt.plot(x,y4, label="gueris")
plt.plot(x,y5, label="morts")
plt.legend()
plt.savefig('figsize_test0.png')
plt.show()
print("contaminés tot: "+ str(m.contaminé_tot) +
      " bus contamination: "+ str(m.bus_contagion) +
      " ecole contamination :"+ str(m.ecole_contagion) +
      " usine contamination :"+ str(m.usine_contagion) +
      " famille contamination :"+ str(m.famille_contagion))
