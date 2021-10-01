# Bank and its Cashier
# GCC Coding Challenge 2021 - Link = https://github.com/CS-CodingChallenge/gcc-2021-gillgurvijay01/blob/main/Question1/
# My Github - GillGurvijay01
# Submitted by Gurvijay Singh Gill
def totalNotes(amount):
    diff=[]
    sum=[]
    unit1=0
    unit2=0
    if amount==1:
        return 1
    elif amount==2:
        return 2
    elif amount==0:
        return 0
    else :    
        for i in range (1,amount):
            unit1=i
            if ((amount-i)%2==0):
                unit2=(amount-i)//2
            else:
                unit1+=1
                unit2=(amount-i)//2
            d=unit1-unit2
            if d<0:
                d*=-1
            diff.append(d)
            sum.append(unit1+unit2)
            unit1=unit2=0
     
    return (sum[diff.index(min(diff))])
print(totalNotes(32))

