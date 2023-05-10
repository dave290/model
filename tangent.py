# tangent.py
# Input assumed tangential velocity of inner points
# Input galactic longitudes suitable for tangent point method (typically 30-70 deg)
# Input solar radius. Also velocity of LSR and apex
# Calculate tangent point radius and velocity shift at each galactic longitude

import math
degtorad=3.14159/180.0

gallon=[30,35,40,45,50,55,60,65,70] #in degrees
r_s=   7.6                   #in kiloparsecs
v_lsr= 220                   #in km/s
v_tp=  230                   #in km/s
apex_gallon=55.0*degtorad
apex_gallat=20.0*degtorad
apex_vel=13.0                #in km/s

apex_vel_projection=apex_vel*math.cos(apex_gallat)
N=len(gallon)
print("Gallon (deg), Radius (kpc), Velocity (km/s), Velocity shift (km/s)")
for i in range (N):
    r_tp=r_s*math.sin(degtorad*gallon[i])
    lsr_radial_vel=v_lsr*math.sin(degtorad*gallon[i])
    apex_radial_vel=apex_vel_projection*math.cos(degtorad*float(gallon[i])-apex_gallon)
    delta_v=v_tp-(lsr_radial_vel+apex_radial_vel)
    print(gallon[i],r_tp,v_tp,int(delta_v))
exit()

