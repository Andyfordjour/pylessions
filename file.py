##total= int(hrs)*float(rate)
#print('pay:',total)

hrs = input("Enter hrs:")
rate = input('Enter rate')
#prt=float(hrs)*float(rate)
hr =float(hrs)
rt = float(rate)
if hr>40:
    prt=hr*rt
    ovt =(hr-40)*(rt*0.50)
    total = prt + ovt
else:
    total =hr*rt
print("your pay",total)
