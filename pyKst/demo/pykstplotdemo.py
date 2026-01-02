#!/usr/bin/env python3
try:
    import pykstplot as plt
except ImportError:
    import sys
    import os
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    import pykstplot as plt
#import matplotlib.pyplot as plt
import numpy as np

x = np.linspace( -10, 10, 100)
y = np.sin(x)
z = np.cos(x)

plt.subplot(221)
plt.plot(x,y*y, linewidth=2, color = "green", linestyle="-.", label="greenline")
plt.subplot(122)
plt.plot(x,y,"k.")
plt.subplot(223)
plt.plot(x,z,"m*", markersize=6, color="blue")
plt.subplot(221, axisbg="lightblue")
plt.plot(x,z)
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Title")

plt.figure()
plt.plot([1,3,7,15])

plt.show()

#plt.savefig("pltdemo.eps")
