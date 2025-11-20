numsuma = 0 #1+2+3+4+5+6+7+8+9+10 = 55
numprod = 1 #1*2*3*4*5*6*7*8*9*10 = 3628800

for i in range (1, 11):
    numsuma = numsuma + i 
    numprod = numprod * i

print(f"La suma es {numsuma}")
print(f"El producto es {numprod}")