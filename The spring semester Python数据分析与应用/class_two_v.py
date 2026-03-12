import matplotlib.pyplot as plt
import numpy as np
t1 = np.arange(0.,5.,0.2)
t2 = np.arange(0.5,4.,0.3)
plt.plot(t1,t1,"r--", t2,t2**2,'b-p',t1,t1**3,"g-^")
plt.axis([0,6.0,0,120])
plt.show()