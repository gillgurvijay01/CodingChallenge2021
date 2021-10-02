
it=input()
it=it.split(" ")
for i in range (0,len(it)):
    it[i] = int(it[i])
s1=it[0]
s2=it[1]
sum=it[2]
l1=input()
l1=l1.split(" ")
for i in range (0,len(l1)):
    l1[i] = int(l1[i])
l2=input()
l2=l2.split(" ")
for i in range (0,len(l2)):
    l2[i] = int(l2[i])
l3=l1+l2
l3.sort()
l3=list(l3)
l3=l3[::-1]
s=0
counter=0
while(sum-s<min(l3)):
    for i in l3:
        if i<(sum-s):
            s+=i
            counter+=1
print(counter)
             