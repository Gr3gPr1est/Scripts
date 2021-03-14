# -*- coding: cp1250 -*-
import ctypes, sys
from ctypes import *
import io
from itertools import product
from sys import argv
import time

def test_function(ioctl):
    counter = 0
    while (counter != 10):
        print ioctl[counter]
        counter = counter + 1

ioctl_0 = [0,1,2,3,4,5,6,7,8,9]

test_function(ioctl_0)
