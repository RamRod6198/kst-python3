#!/usr/bin/env python3
try:
    import pykst as kst
except ImportError:
    import sys
    import os
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    import pykst as kst

client=kst.Client("TestVectors")
client.quit()

