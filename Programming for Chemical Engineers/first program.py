
import math as m

x=int(input('Enter hot fluid inlet temperature '))
x1=int(input('Enter hot fluid outlet temperature '))
y=int(input('Enter cold fluid inlet temperature '))
y1=int(input('Enter cold fluid outlet temperature '))
LMTD=((x-y)-(x1-y1))/m.log((x-y)/(x1-y1))
print('log mean temperature difference for co-current system is '+str(LMTD)) 