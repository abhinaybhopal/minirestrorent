menu={"chai":10,
      "kadak_chai":20,
      "cofee":15,
      "pizza":50,
      "barger":70,
      "sigret":12,
      "fizza":10,
      "drink":50,
      }
totle_amount=0
flag=0
print("wellcome to sonu restrount")
order=str(input("do you want to order (yes/no)"))
if "yes"==order.strip():
    print("chai:10 \nkadak chai:20 \ncofee:15 \npizza:50 \nbarger:70 \nsigret:12 \nfizza:10 \ndrink:50")
    while "yes"==str(input("conform (yes/no):")):
        flag=1
        order=list(map(str,input("what do you order:").split()))
        for i in order:
            totle_amount +=menu[i]
        print("Thanku sir/madem again what do you want order",end="")
    
    
else:
    print("Thank you sir/madem")
if flag==1:
    print("thank you sir/madem your totle bill is ",totle_amount)
