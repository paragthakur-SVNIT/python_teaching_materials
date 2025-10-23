#algorithm for if else loop
Temp = int(input('Enter Temperature value '))
if Temp > 60:
    print('Temperature should be decreased')
elif Temp <= 60 and Temp >40:
    print('Maintain Temperature')
elif Temp <= 40 and Temp >0:
    print('Increase Temperature')
else:
    print('Enter valid temperature')