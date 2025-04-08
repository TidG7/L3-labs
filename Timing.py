import import_spec
import numpy as np
import matplotlib.pyplot as plt
import scipy

data = import_spec.import_file('Det2TimingGood 10325-13325.Chn')
x = np.linspace(0,9.8,len(data))
def func(x,a,b,c):
    return a*np.exp(-b*(x)) + c
range_min = 1900
sub_x = x[range_min:]
sub_data = data[range_min:]
guess = [190,1/2.2,5]
params, pcov = scipy.optimize.curve_fit(func, sub_x, sub_data, guess, maxfev=10000)
plt.figure()
plt.plot(x,data)
plt.plot(x,[func(i,*params) for i in x], color='r')
# plt.plot(x[2000:],[200*np.exp(-1/2.2*(i))+5 for i in x[2000:]], color='g')
plt.vlines(x[range_min],ymin=0,ymax=250,linestyles='dashed',colors='y')
plt.xlabel('$time/\mu s$')
plt.ylabel('counts')
print(data)
print(len(data))
print(params)
tau = 1/params[1]
print(tau)
plt.show()

t = (2.2-tau)*(10**(-6))
max_L = 15000
min_L = 10000
mass = 0.1134289259 * scipy.constants.m_p
c = scipy.constants.c
L_prime = 1/np.sqrt(1/(min_L**2)+1/(t*c)**2)
gam = 1/np.sqrt(1-(L_prime/(t*c))**2)
print(L_prime)
print(gam)
print(mass)
E = gam*mass*c**2 /(1.6*10**(-19))/(1*10**9)
print(E)
