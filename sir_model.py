import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
N = 2000. #nombre d'individus
t_remission=8 
I0, R0 = 1, 0 #nombres initiaux d'infectés et de soignés
S0 = N - I0 - R0 #nombre de personnes susceptible
beta, gamma = 1/8, 1/t_remission #rythmes de contact et de rémission
tmax = 1000 
Nt = 1000
t = np.linspace(0, tmax, Nt+1)
def derivative(X, t):
    S, I, R = X
    dotS = -beta * S * I /N
    dotI = beta * S * I/N  - gamma * I   #système d'equation des blocs
    dotR = gamma * I
    return np.array([dotS, dotI, dotR])
X0 = S0, I0, R0 #Initial conditions vector
res = integrate.odeint(derivative, X0, t) #résolution du système
S, I, R = res.T
plt.figure()
plt.grid()
plt.plot(t, S, 'orange', label='Susceptibles')
plt.plot(t, I, 'r', label='Infectés')
plt.plot(t, R, 'g', label='guéris')
plt.xlabel('jours')
plt.ylabel('population')
plt.ylim([0,N])
plt.legend()

plt.show()
