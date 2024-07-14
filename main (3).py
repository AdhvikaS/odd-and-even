#Adhvika

def gem(number):
    even = []
    odd = []
    for n in number:
        if n%2==0:
            even.append(n**2)
        elif n%2!=0:
            odd.append(n)
return even+odd
number=[34,7,5,72,82]
print(gem(number))
