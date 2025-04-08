
import import_spec
import numpy as np
import matplotlib.pyplot as plt
import scipy

_1c2 = import_spec.import_file('Det1LightsOnGain20Amp1Volts1000Coincide2 6225-7225.Chn')
_1c2s = import_spec.import_file('Det1Scint2LightsOnGain20Amp1Volts1000Coincide2 24225-27225.Chn')
data = - np.array(_1c2s) + 3.336*np.array(_1c2)
plt.figure()
plt.plot(np.linspace(0,len(data),len(data)),data)
plt.xlabel('channel')
plt.ylabel('counts')
plt.show()