#!/usr/bin/env python3
try:
    import pykst as kst
except ImportError:
    import sys
    import os
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    import pykst as kst

client=kst.Client("TestX2")

v1 = client.new_generated_vector(-10, 10, 1000)
e1 = client.new_equation(v1, "sin(x)")
c1 = client.new_curve(e1.x(), e1.y())
p1 = client.new_plot()
p1.add(c1)

client.new_tab()
e1 = client.new_equation(v1, "cos(x)")
c1 = client.new_curve(e1.x(), e1.y())
p1 = client.new_plot()
p1.add(c1)


client.export_graphics_file("tmp.png", all_tabs = True, autosave_period = 5)
