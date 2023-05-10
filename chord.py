# chord.py
# modified 1/25/2023
# Input galactic longitude and radius (in light years) for galactic arm points
# Input galactic radius of sun and velocity of LSR.
# Input velocity of target arm
# Output relative velocity and doppler shift along calculated galactic longitude
# Only input data for one arm at a time. Adjust arm velocity to best match observed shifts

import math
radtodeg=180.0/3.14159
degtorad=3.14159/180.0

r_s=8.0*3260                          #kpc to ly
v_lsr=220                             #km/s
apex_gallon=55.0	              #deg
apex_gallat=20.0                      #deg
apex_gallon_rad=apex_gallon*degtorad  #rad
apex_gallat_rad=apex_gallat*degtorad  #rad
apex_vel=13                           #13 km/s, 

name="10 kpc, 32600 ly"
gal_lon=[50,60,70,80,84,100,115,130,150,165,190,210,220,235,240]
gal_rad=[32600,32600,32600,32600,32600,32600,32600,32600,32600,32600,32600,32600,32600,32600,32600]
vel_object=200

#Main Block*****************************************************************************
apex_vel_projection=apex_vel*math.cos(apex_gallat_rad)
radius=[0];gallon=[0];vel_relative=[0];note=[0]
N=len(gal_lon)
for i in range(N):
    alpha=degtorad*gal_lon[i]
    r=gal_rad[i]
    if gal_lon[i]>0 and gal_lon[i]<=(apex_gallon+90.0):
        arg=(r_s/r)*math.sin(alpha)
        b=math.asin(arg)
        oa=b-1.5708
        apex_radial_vel=apex_vel_projection*math.cos(degtorad*float(gal_lon[i])-apex_gallon_rad)
        delta_v=vel_object*math.cos(oa)-v_lsr*math.cos(1.5708-alpha)-apex_radial_vel
        if r<r_s:
            note.append("inner, gallon<145, apex velocity decreases magnitude of observed POS (receding) velocity shift")
        else:
            note.append("outer, gallon<145, apex velocity increases magnitude of observed NEG (approaching) velocity shift")
        #endif
    #endif

    if gal_lon[i]>(apex_gallon+90.0) and gal_lon[i]<=180:
        arg=(r_s/r)*math.sin(alpha)
        b=math.asin(arg)
        oa=1.5708-b
        apex_radial_vel=apex_vel_projection*math.cos(3.14159-degtorad*float(gal_lon[i])+apex_gallon_rad)
        delta_v=vel_object*math.cos(oa)-v_lsr*math.cos(1.5708-alpha)+apex_radial_vel
        note.append("outer, 145<gallon<180 apex velocity decreases magnitude of observed NEG (approaching) velocity shift")
    #endif

    if gal_lon[i]>180 and gal_lon[i]<270:
        arg=-(r_s/r)*math.sin(alpha)
        b=math.asin(arg)
        oa=1.5708-b
        apex_radial_vel=apex_vel_projection*math.cos(3.14159+apex_gallon_rad-degtorad*float(gal_lon[i]))
        delta_v=v_lsr*math.cos(4.712-alpha)-vel_object*math.cos(oa)+apex_radial_vel
        note.append("outer, gallon>180, apex velocity increases magnitude of observed POS (receding) velocity shift")
    #endif

    radius.append(r)
    gallon.append(radtodeg*alpha)
    vel_relative.append(delta_v)
#endfor
radius.pop(0),gallon.pop(0),vel_relative.pop(0),note.pop(0)

#Output to terminal
print("Arm Name, Velocity (km/s)")
print(name,vel_object)
print("Apex Velocity (km/s), LSR Velocity (km/s),Solar Radius (ly)")
print(apex_vel,v_lsr,int(r_s))
print(" ")
print("gal_long (deg), radius (ly), rel_vel (km/s)")
for i in range(N):
    #print(i+1,int(1.0001*gallon[i]),int(radius[i]),int(vel_relative[i]),note[i])
    print(i+1,int(1.0001*gallon[i]),int(radius[i]),int(vel_relative[i]))
#endfor

exit()
