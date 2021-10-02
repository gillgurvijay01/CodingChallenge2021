# Question # GCC 2021 Coding
# Submitted by GillGurvijay01


def securitiesBuying(z, security_value):
    for i in range(0, len(security_value)):
        security_value[i] = int(security_value[i])
    no_of_stocks=0
    value=0
   #participants code here
    security_value.sort()
    security_value=list(security_value)
    security_value=security_value[::-1]
    while((z-value)>=min(security_value)):
        for i in security_value:
                if i>z:
                   continue
                elif i==0:
                    break
                else:
                    no_of_stocks=no_of_stocks+1
                    value+=i     
   
    return no_of_stocks

z= int(input())
security_value = []
security_value = input().split(" ")
no_of_stocks_purchased=securitiesBuying(z,security_value)
print(no_of_stocks_purchased)


