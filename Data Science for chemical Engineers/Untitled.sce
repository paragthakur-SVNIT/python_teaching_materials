

x=input('Enter hot fluid inlet temperature ')
x1=input('Enter hot fluid outlet temperature ')
y=input('Enter cold fluid inlet temperature ')
y1=input('Enter cold fluid outlet temperature ')
LMTD=((x-y)-(x1-y1))/log((x-y)/(x1-y1))
disp('log mean temp difference',LMTD) 
