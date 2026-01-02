#!/usr/bin/env python3

# Demonstrate curves, data vectors, equations, spectra, and histograms

import sys
import os

# Ensure we can find pykst regardless of working directory
script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(script_dir)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

import pykst as kst

# Use absolute path for data file since KST has its own working directory
datafile = os.path.join(script_dir, "demodata.dat")

client = kst.Client("DataObjects")

# create a 2x2 grid of plots
P1 = client.new_plot(font_size=12)
P1.set_stroke_width(1)
P2 = client.new_plot(font_size=12)
P2.set_stroke_width(1)
P3 = client.new_plot(font_size=12)
P3.set_stroke_width(1)
P4 = client.new_plot(font_size=12)
P4.set_stroke_width(1)
P5 = client.new_plot(font_size=12)
P5.set_stroke_width(1)
client.cleanup_layout(2)

# plot a curve made from data vectors
dv1 = client.new_data_vector(datafile, field="Column 1", start=0, num_frames=2000)
dv2 = client.new_data_vector(datafile, field="Column 2", start=0, num_frames=2000)
dv3 = client.new_data_vector(datafile, field="Column 3", start=0, num_frames=2000)

c1 = client.new_curve(dv1, dv2)
c1.set_color("red")
c1.set_line_width(2)
P1.add(c1)

# plot x^2 from -1 to 1
gv1 = client.new_generated_vector(-1.0, 1.0, 100)
eq1 = client.new_equation(gv1, "x^2")
c2 = client.new_curve(eq1.x(), eq1.y())
c2.set_color("green")
c2.set_line_width(2)
P2.add(c2)

# plot the spectrum of vector dv2
sp1 = client.new_spectrum(dv2,
                          sample_rate=60.0,
                          interleaved_average=True,
                          fft_length=9,
                          output_type=3)
c3 = client.new_curve(sp1.x(), sp1.y())
c3.set_color("blue")
c3.set_line_width(2)
P3.add(c3)

# plot a histogram of dv2
h1 = client.new_histogram(dv2)
c4 = client.new_curve(h1.x(), h1.y())
c4.set_color("black")
c4.set_line_width(1)
c4.set_bar_fill_color("dark green")
c4.set_has_bars()
c4.set_has_lines(False)
P4.add(c4)

# plot the cross spectrum of dv2 vs dv3
sc1 = client.new_generated_scalar(10)
sc2 = client.new_generated_scalar(60)
xs1 = client.new_cross_spectrum(dv2, dv3, sc1, sc2)
c5 = client.new_curve(xs1.x(), xs1.y())
c5.set_color("green")
c5.set_line_width(1)
P3.add(c5)

# demo cumulative sum
x1 = client.new_generated_scalar(1.0)
sum1 = client.new_sum_filter(gv1, x1)
c6 = client.new_curve(gv1, sum1.output_sum())
c6.set_color("green")
c6.set_line_width(1)
P5.add(c6)
