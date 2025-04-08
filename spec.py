import import_spec
import numpy as np
import matplotlib.pyplot as plt
import scipy

data = import_spec.import_file('Det1LightsOnGain20Amp1Volts1000Coincide2 6225-7225.Chn')
plt.figure()
plt.plot(np.linspace(0,len(data),len(data)),data)
plt.xlabel('channel')
plt.ylabel('counts')
plt.show()