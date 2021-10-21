import math
import numpy as np
import matplotlib.pyplot as plt
(fig, ax) = plt.subplots(figsize = (20,20))

stativ_høyde = 2 #stativet er 1,5 over bakken
stav_lengde = 200 #hvor lang staven med måleren er, denne er viktig ettersom "giringen" er en mulitplikasjon av denne
a_gir = 1.25*stav_lengde   #hvor mye lenger "girestaven" er
c_gir = 2*stav_lengde   #hvor mye lenger "girestaven" er

#for å få mer nøyaktige målinger gires vinklingen opp:
def c_amp(c):   #c er den ekte vinkelen over 90*
    c = math.radians(c)
    b = math.sqrt((stav_lengde**2)+(c_gir**2)-2*stav_lengde*c_gir*math.cos(c))
    v = math.asin((math.sin(c)*c_gir)/b)
    return math.degrees(v)

def a_amp(a):   #vinkel på kikkert inn. vinkel på skiven ut
    a = math.radians(a)
    b = math.sqrt((stav_lengde**2)+(a_gir**2)-2*stav_lengde*a_gir*math.cos(a))
    v = math.asin((math.sin(a)*a_gir)/b)
    return math.degrees(v)


def a_fraskive(av): #vinkel fra skive inn. Vinkel på kikkert ut
    av = math.radians(av)
    r = (math.cos(av))**2
    s = math.acos((-stav_lengde*(r-1)+(1/2)*math.sqrt((2*stav_lengde*(r-1))**2-4*(stav_lengde**2*(1-r)-a_gir**2*r)))/a_gir)
    s = math.degrees(s)
    return s

def c_fraskive(cv): #vinkel fra skive inn. Vinkel på kikkert ut
    cv = math.radians(cv)
    r = (math.cos(cv))**2
    s = math.acos((-stav_lengde*(r-1)+(1/2)*math.sqrt((2*stav_lengde*(r-1))**2-4*(stav_lengde**2*(1-r)-c_gir**2*r)))/c_gir)
    s = math.degrees(s)
    return s


def a_sektor(a):    #grader fra rett frem, og ned
    a = math.radians(90-a)
    return (1/math.cos(a))*math.sin(a)  #sec(x) = 1/cos(x)

def c_sektor(c):    #grader over 90* (som er rett frem)
    c = math.radians(c)
    return stativ_høyde*math.sin(c)*(1/math.cos(c))

def høyde(a,c):
    return a_sektor(a)*c_sektor(c)+stativ_høyde


a_max = 16 #måler ikke mer enn 14 grader ned fra rett frem
c_max = 61 #måler ikke mer enn 60 grader opp fra rett frem
a_val = []
a_ang = []
a_v = 0
a_v_last = 1


while a_amp(a_v) <= a_amp(a_max):
    if round(a_sektor(a_v)*10,1).is_integer() and a_amp(a_v) > a_v_last+1:
        a_ang.append(a_amp(a_v))
        a_val.append(round(a_sektor(a_v),1))
        a_v_last = a_amp(a_v)
        
    a_v += 0.001

c_val = []
c_ang = []
c_v = 0.001
c_v_last = 0.002

while c_amp(c_v) <= c_amp(c_max):
    if round((c_sektor(c_v))*1000,1).is_integer() and c_amp(c_v) > c_v_last+1:
        c_ang.append(c_amp(c_v))
        c_val.append(round(c_sektor(c_v),3))
        c_v_last = c_amp(c_v)
        
    c_v += 0.01





alphas = []

for i in range(0, len(c_ang)):
    alpha=(2*np.pi/360)
    alphas.append(c_ang[i]*alpha+np.deg2rad(90))


coordX = np.cos(alphas)
coordY = np.sin(alphas)
points = np.c_[coordX, coordY, alphas]
r = 1.04 #verdiplassering unna sentrum
ax.scatter(points[:,0], points[:,1])

for i in range(0,len(points)):
    a = points[i,2] 
    x,y = (r*np.cos(a), r*np.sin(a))
    if points[i,0] < 0: 
        a = a - np.pi
    ax.text(x,y, f"{c_val[len(points)-i-1]}", rotation = np.rad2deg(a), ha="center", va="center")   #{round(c_fraskive(c_ang[len(points)-i-1]),2)}: 


ax.axis("off")
plt.gca().set_aspect('equal')

plt.show()

(fig, ax) = plt.subplots(figsize = (20,20))
alphas = []

for i in range(0, len(a_ang)):
    alpha=(2*np.pi/360)
    alphas.append(a_ang[i]*alpha+np.deg2rad(180))


coordX = np.cos(alphas)
coordY = np.sin(alphas)
points = np.c_[coordX, coordY, alphas]
r = 1.04 #verdiplassering unna sentrum
ax.scatter(points[:,0], points[:,1])

for i in range(0,len(points)):
    a = points[i,2] 
    x,y = (r*np.cos(a), r*np.sin(a))
    if points[i,0] < 0: 
        a = a - np.pi
    ax.text(x,y, f"{a_val[i]}", rotation = np.rad2deg(a), ha="center", va="center") #{round(a_fraskive(a_ang[i]),2)}: 

ax.axis("off")
plt.gca().set_aspect('equal')

plt.show()
