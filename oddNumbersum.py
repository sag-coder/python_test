sum = 0

for i in range(101):
    j = i%2
    if  j:
        print ( " " +str(i), end='')
        sum=sum+i
print("\nsome of first 100 odd number "+str(sum))

print(" ")
sum=0
for i in range(101):
    j = i%2
    if not j:
        print ( " " +str(i), end='')
        sum=sum+i
print("\nsome of first 100 even number "+str(sum))