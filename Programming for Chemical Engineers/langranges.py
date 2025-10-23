
x = [-2,1,3,7]
y = [5,7,11,34]
xi = 0
n = len(x)
s = 0.0
for i in range(n):
    pr = 1
    for j in range(n):
        if i != j:
            pr *= (xi - x[j]) / (x[i] - x[j])
    s += y[i]*pr
print(s)

