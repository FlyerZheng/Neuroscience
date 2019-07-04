import random as rnd
import numpy as np
import matplotlib.pyplot as plt

def get_spike_train(rate,big_t,tau_ref):

    if 1<=rate*tau_ref:
        print("firing rate not possible given refractory period f/p")
        return []


    exp_rate=rate/(1-tau_ref*rate)

    spike_train=[]

    t=rnd.expovariate(exp_rate)

    while t< big_t:
        spike_train.append(t)
        t+=tau_ref+rnd.expovariate(exp_rate)

    return spike_train


def load_data(filename,T):

    data_array = [T(line.strip()) for line in open(filename, 'r')]

    return data_array

Hz=1.0
sec=1.0
ms=0.001

rate=35.0 *Hz
tau_ref=5*ms
big_t=1000*sec

# spike_train=get_spike_train(rate,big_t,tau_ref)

# print(len(spike_train)/big_t)
# print("",spike_train)

def get_fano_factor(spiketrain,big_t,time_interval):
	n = int(big_t/time_interval)
	spike_count=[0]*n
	for i in range(len(spiketrain)):
		j = int(spiketrain[i]/time_interval)
		spike_count[j] += 1
	# print(spike_count)
	# print(len(spike_count))
	# print(np.var(spike_count)/np.mean(spike_count))
	return np.var(spike_count)/np.mean(spike_count)


def get_cov_inter_spike(spiketrain):
	inter_spike_interval = [None]*(len(spiketrain)-1)
	for i in range(len(inter_spike_interval)):
		inter_spike_interval[i] = spiketrain[i+1] - spiketrain[i]
	# print(inter_spike_interval)
	# print(np.std(inter_spike_interval)/np.mean(inter_spike_interval))
	return np.std(inter_spike_interval)/np.mean(inter_spike_interval)


print("Question 1:")

print("With no refractory period,the spike train is:")
spike_train = get_spike_train(rate,big_t,0)
# print(spike_train)
print("the fano factor over wondows of width 10ms :",get_fano_factor(spike_train,1000,0.01))
print("the fano factor over wondows of width 50ms :",get_fano_factor(spike_train,1000,0.05))
print("the fano factor over wondows of width 100ms :",get_fano_factor(spike_train,1000,0.1))
print("the coefficient of variation of the inter-spike interval :",get_cov_inter_spike(spike_train))
print("")

print("With 5ms refractory period,the spike train is:")
spike_train = get_spike_train(rate,big_t,tau_ref)
# print(spike_train)
print("the fano factor over wondows of width 10ms :",get_fano_factor(spike_train,1000,0.01))
print("the fano factor over wondows of width 50ms :",get_fano_factor(spike_train,1000,0.05))
print("the fano factor over wondows of width 100ms :",get_fano_factor(spike_train,1000,0.1))
print("the coefficient of variation of the inter-spike interval :",get_cov_inter_spike(spike_train))
print("")


print("Question 2:")

spikes=load_data("rho.dat",int)
spikes_decoding = []
for i in range(len(spikes)):
	if (spikes[i] == 1):
		spikes_decoding.append(i*0.002)

# print(spikes_decoding)
print("the fano factor over wondows of width 10ms :",get_fano_factor(spikes_decoding,1200,0.01))
print("the fano factor over wondows of width 50ms :",get_fano_factor(spikes_decoding,1200,0.05))
print("the fano factor over wondows of width 100ms :",get_fano_factor(spikes_decoding,1200,0.1))
print("the coefficient of variation of the inter-spike interval :",get_cov_inter_spike(spikes_decoding))
print("")


print("Question 3:")

stimulus=load_data("stim.dat",float)	#len = 60000,50 one group, 1200 intervals in total
sta = [0]*50
for i in range(50):
	for j in range(len(spikes)):
		if (spikes[j] == 1 and j > 50):
			sta[i] += stimulus[j-(50-i)]
	sta[i] = sta[i]/sum(spikes)

x=[]
for i in range(50):
	x.append(-100+2*i)

# plt.plot(x, sta)
# plt.xlabel('time before the spike') 
# plt.ylabel('average stimulus')
# plt.title("spike triggered average over a 100 ms window") 
# plt.show()
# plt.savefig("sta.jpg")
print("")


print("Question COMSM2127:")

def plot_sta_pairs_notadjacent(t_interval):
	posi_delta = int(t_interval/2)
	sta = [0]*50
	for i in range(50):
		for j in range(len(spikes)):
			if (spikes[j] == 1 and spikes[j+posi_delta] == 1 and j > 50):
				sta[i] += stimulus[j-(50-i)]
		sta[i] = sta[i]/sum(spikes)

	plt.plot(x, sta)
	plt.xlabel('time before the spike') 
	plt.ylabel('average stimulus')
	plt.title("stimulus triggered by pairs of spikes(not adjacent),\ntime interval : "+str(t_interval)+"ms")
	plt.show()


def plot_sta_pairs_adjacent(t_interval):
	posi_delta = int(t_interval/2)
	sta = [0]*50
	for i in range(50):
		for j in range(len(spikes)):
			if (spikes[j] == 1 and spikes[j+posi_delta] == 1 and sum(spikes[j+1:j+posi_delta-1]) == 0 and j > 50):
				sta[i] += stimulus[j-(50-i)]
				# flag = True
				# for k in range(posi_delta):
				# 	if( spikes[j+k] == 1):
				# 		flag = False
						
				# if (flag == True):
				# 	sta[i] += stimulus[j-(50-i)]	
		sta[i] = sta[i]/sum(spikes)
	plt.plot(x, sta)
	plt.xlabel('time before the spike') 
	plt.ylabel('average stimulus')
	plt.title("stimulus triggered by pairs of spikes(adjacent),\ntime interval : "+str(t_interval)+"ms")
	plt.show()

# plot_sta_pairs_notadjacent(2)
# plot_sta_pairs_notadjacent(10)
# plot_sta_pairs_notadjacent(20)
# plot_sta_pairs_notadjacent(50)

plot_sta_pairs_adjacent(2)
plot_sta_pairs_adjacent(10)
plot_sta_pairs_adjacent(20)
plot_sta_pairs_adjacent(50)






