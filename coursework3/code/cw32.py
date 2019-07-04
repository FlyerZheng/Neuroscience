import matplotlib.pyplot as plt
import random
import numpy as np
t0 = 0
t1 = 1000
tau_m = 20
tau_s = 10
El = -70
V_rest = -80
Vt = -54
RI = 18
g_max = 0.15
dt = 1
P = 0.5



def sim_synaps():
    time = np.arange(t0, t1, dt)
    V1 = np.zeros(len(time))
    V2 = np.zeros(len(time))
    S1 = np.zeros(len(time))
    S2 = np.zeros(len(time))
    V1[0] = random.randint(-80, -54)
    V2[0] = random.randint(-80, -54)
    # print(V1,V2,S1,S2)
    for i in range(1, len(time)):
        S1[i] = S1[i-1]-S1[i-1]*dt/tau_s
        S2[i] = S2[i-1]-S2[i-1]*dt/tau_s
        V1[i] = V1[i-1]+(El-V1[i-1]+RI+g_max*S1[i-1]*(E_syn-V1[i-1]))*dt/tau_m
        V2[i] = V2[i-1]+(El-V2[i-1]+RI+g_max*S2[i-1]*(E_syn-V2[i-1]))*dt/tau_m

        if (V1[i]>Vt):
            V1[i] = V_rest
            S2[i] +=P

        if (V2[i]>Vt):
            V2[i] = V_rest
            S1[i] +=P

    return V1,V2,time



# def dV(neuron,V,t,isP):
#     return (V_rest - V + I(V,t,neuron,isP))*dt

# def I(V,t,neuron,isP):
#     return g_max*s(t,neuron,isP)*(E_syn - V)

# def s(t,neuron,isP):
#     if (neuron == 1):
#         if (isP == 1):
#             return S1[t-1]+S1[t-1]*dt/tau_s+0.5
#         else:
#             return S1[t-1]+S1[t-1]*dt/tau_s  
#     if (neuron == 2):
#         if (isP == 1):
#             return S2[t-1]+S2[t-1]*dt/tau_s+0.5
#         else:
#             return S2[t-1]+S2[t-1]*dt/tau_s  


# def synapses_model():
#     time = np.arange(t0, t1+dt, dt)
#     V1 = np.empty(len(time))
#     V2 = np.empty(len(time))
#     S1 = np.empty(len(time))
#     S2 = np.empty(len(time))

#     V1[0] = random.randint(-80, -54)
#     V2[0] = random.randint(-80, -54)
#     for i in range(1, len(time)):
#         # if (V2[i-1]>Vt):
#         #     V1[i] = V1[i-1] + dV(1,V1[i-1],i,1)*dt
#         # else:
#         V1[i] = V1[i-1] + dV(1,V1[i-1],i,0)*dt

#         if (V1[i]>Vt):
#             V1[i] = V_rest
#             spike1.append(time)
#             V2[i] = V2[i-1] + dV(2,V2[i-1],i,1)*dt
#             if (V2[i]>Vt):
#                 V2[i] = V_rest
#                 spike2.append(time)
#         else:
#             V2[i] = V2[i-1] + dV(2,V2[i-1],i,0)*dt
#             if (V2[i]>Vt):
#                 V2[i] = V_rest
#                 spike2.append(time)

#     return V1,V2,time


E_syn = -80

V1,V2,time = sim_synaps()
print(V1,V2,time)
print(len(V1),len(V2),len(time))
# plt.plot(time[0:110],V1[0:110],color='red',label='neuron1')
# plt.plot(time[0:110],V2[0:110],color='blue',label='neuron2')
plt.plot(time,V1,color='red',label='neuron1')
plt.plot(time,V2,color='blue',label='neuron2')
plt.xlabel("t (ms)")
plt.ylabel("V(mv)")
plt.title("Inhibitory with E_syn = -80mV")
plt.legend(loc=2)
plt.savefig('Q2_-80mA')
plt.show()

E_syn = 0

V1,V2,time = sim_synaps()
print(V1,V2,time)
print(len(V1),len(V2),len(time))
plt.plot(time,V1,color='red',label='neuron1')
plt.plot(time,V2,color='blue',label='neuron2')
plt.xlabel("t (ms)")
plt.ylabel("V(mv)")
plt.title("Excitatory with E_syn = 0mV")
plt.legend(loc=2)
plt.savefig('Q2_0mA')
plt.show()