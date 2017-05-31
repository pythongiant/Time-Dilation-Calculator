#!/usr/bin/env python3
import math
print("\t Welcome To the Time Dilation Calculator")
t=input("Elapsed Time at body(seconds): ")
v=input("Speed(km/s): ")
speed_of_light=299792.458
print(int(t)/math.sqrt(1-(int(v)**2/speed_of_light**2)))
