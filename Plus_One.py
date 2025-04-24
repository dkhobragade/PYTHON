digits = [1,2,3]


count =0
a=[]

for i in range(len(digits)):
    count  += digits[i]*10**(len(digits)-1-i)
count +=1

while count!=0:
    val = a.append(count%10)
    count//=10
print(a[::-1])

