t1 = (4, 3, 2, 2, -1, 18)
t2 = (2, 4, 8, 8, 3, 2)

res = ()

for i in range (0, len(t1)):
    mult = t1[i] * t2[i]
    res = res + (mult,)

print(f"THE MULTIPLY IS : {res}")