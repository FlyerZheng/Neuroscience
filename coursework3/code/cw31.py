import matplotlib.pyplot as plt
import math

def dV(V):
   return (El-V+Rm*Ie)/tau

def lif(t0,t1,dt,V0,Vt,Vr):
    ts = [t0]
    Vs = [V0]
    while ts[-1] <= t1:
        if Vs[-1] < Vt:
            V = Vs[-1] + dV(Vs[-1])*dt
            ts.append(ts[-1] + dt)
            Vs.append(V)
        else:
            Vs[-1] = Vr
    return ts, Vs


#question1
t0 = 0
t1 = 1000
V0 = -70
tau = 10
El = -70
Vr = -70
Vt = -40
Rm = 10*math.pow(10, 9)
Ie = 3.1*math.pow(10, -9)
dt = 1

ts,Vs = lif(t0,t1,dt,V0,Vt,Vr)

# plt.ylim([-70,0]);
plt.plot(ts, Vs, label="31mV")
plt.xlabel("t (ms)")
plt.ylabel("V (mv)")
plt.title("an integrate and fire model")
plt.legend(loc=0)
plt.savefig('Q1')
plt.show()









