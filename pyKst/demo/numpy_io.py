#!/usr/bin/env python3
try:
    import pykst as kst
except ImportError:
    import sys
    import os
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    import pykst as kst
import numpy as np
import time

client=kst.Client("VectorIO")

t0 = time.perf_counter()

# create a pair of numpy arrays
x = np.linspace( 0, 50, 500000)
y = np.sin(x)

t1 = time.perf_counter()

# copy the numpy arrays into kst and plot them
V1 = client.new_editable_vector(x)
V2 = client.new_editable_vector(y)
c1 = client.new_curve(V1, V2)
p1 = client.new_plot()
p1.add(c1)

t2 = time.perf_counter()

# copy numpy array back into python.
A = V2.get_numpy_array()

t3 = time.perf_counter()

# manipulate the array in python, and plot it in kst
A = A*A
V3 = client.new_editable_vector(A)
c2 = client.new_curve(V1, V3)
p1.add(c2)

# manipulate it again, and replace it in kst
A = A/2
V2.load(A)

print("creation of numpy arrays took", t1 - t0, "s")
print("copying onto kst and plotting took", t2-t1, "s")
print("copying from kst into python took:", t3-t2, "s")

