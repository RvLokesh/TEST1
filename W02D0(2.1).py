# #iNPUT()
s="Vamshi"
print(list(s))

num = int(input("enter the no."))
if num > 0:
    if num%2==0:
        print("no. is postive & even", num**2)
    else:
        print("no. is positive & odd", num**3)
else:
    print("no. is negative or zero")

