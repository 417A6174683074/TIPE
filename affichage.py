from environnement import environnement

from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import ChartModule  


chart1 = ChartModule([{"Label":"sains","Color":"blue"},
                     {"Label": "infectés","Color": "grey"},
                     {"Label":"infectieux","Color":"red"},
                     {"Label":"guéris","Color":"green"},
                     {"Label":"morts","Color":"black"}],
                    data_collector_name='dc')

chart2 = ChartModule([{"Label": "contaminations totales","Color": "grey"},
                     {"Label":"bus contaminations","Color":"blue"},
                     {"Label":"école contaminations","Color":"red"},
                     {"Label":"usine contaminations","Color":"green"},
                     {"Label":"famille contaminations","Color":"black"}],
                    data_collector_name='dc')

'''
def agent_viz(agent):
    viz = {"Shape": "circle",
                 "Filled": "true",
                 "r": 0.7}
    if agent.health=="infectieux":
        viz["Color"] = "red"
        viz["Layer"] = 2
        viz["r"]=0.3
    elif agent.health=="gueris":
        viz["Color"] = "green"
        viz["Layer"] = 3
        viz["r"]=0.2
    elif agent.health=="infecte":
        viz["Color"]="grey"
        viz["Layer"]=1
        viz["r"]=0.5
    else:
        viz["Color"]="blue"
        viz["Layer"]=0
    return viz'''
server = ModularServer(environnement,[chart1,chart2],"epidemie",{"population":1200,"nb_malades":5})
server.port = 8528 # The default
server.launch()


'''               
m=ville(1200,5)                   
from pylab import *
import matplotlib.pyplot as plt
x=[]
y=[]
y2=[]
y3=[]
y4=[]
y5=[]
for i in range(1200):
    m.step()
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
legend()
plt.savefig('figsize_test0.png')
plt.show()
print("contaminés tot: "+ str(m.contaminé_tot) +
      " bus contamination: "+ str(m.bus_contagion) +
      " ecole contamination :"+ str(m.ecole_contagion) +
      " usine contamination :"+ str(m.usine_contagion) +
      " famille contamination :"+ str(m.famille_contagion))'''
