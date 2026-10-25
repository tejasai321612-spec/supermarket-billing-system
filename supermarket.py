print("WELCOME TO SAI SUPER MARKET")
print("select your product by using the below numbers")
Rice=160
Milk=80
Bread=40
Eggs=70
Shampoo=50
Soap=50
Toothpaste=80
CookingOil=200
Biscuits=20
Tissuepaper=45
InstantNoodles=70
Choclates=40
print("1.Rice              160 rupees")
print("2.Milk              80  rupees")
print("3.Bread             40  rupees")
print("4.Eggs              70  rupees")
print("5.Shampoo           50 rupees")
print("6.Soap              50  rupees")
print("7.Toothpaste        80  rupees")
print("8.CookingOli        200 rupees")
print("9.Biscuits          20  rupees")
print("10.Tissuepaper      45  rupees")
print("11.InstantNoodles   70  rupees")
print("12.Choclates        40 rupees")
rice_total=0
milk_total=0
bread_total=0
eggs_total=0
shampoo_total=0
soap_total=0
toothpaste_total=0
cookingoil_total=0
biscuits_total=0
tissuepaper_total=0
instantnoodles_total=0
choclates_total=0
yesorno="Y"
while yesorno=="Y":
 customerproducts=int(input("enter ur products by using numbers like(1,2,3,....): "))
 if customerproducts==1:
    quantity=int(input("Enter how many KG's of Rice (like 1,2,etc):"))
    rice_total+=quantity*Rice
 elif customerproducts==2:
      quantity=int(input("Enter how many Litres of Milk (like 1,2,etc):"))
      milk_total+=quantity*Milk
 elif customerproducts==3:
      quantity=int(input("Enter how much Quantity you Want (like 1,2,etc):"))
      bread_total+=quantity*Bread
 elif customerproducts==4:
      quantity=int(input("Enter how much quantity You Want (like 1,2,etc):"))
      eggs_total+=quantity*Eggs
 elif customerproducts==5:
      quantity=int(input("Enter how much quantity You Want (like 1,2,etc):"))
      shampoo_total+=quantity*Shampoo
 elif customerproducts==6:
      quantity=int(input("Enter how much quantity You Want (like 1,2,etc):"))
      soap_total+=quantity*Soap
 elif customerproducts==7:
      quantity=int(input("Enter how much quantity You Want (like 1,2,etc):"))
      toothpaste_total+=quantity*Toothpaste
 elif customerproducts==8:
      quantity=int(input("Enter how much quantity You Want (like 1,2,etc):"))
      cookingoil_total+=quantity*CookingOil
 elif customerproducts==9:
      quantity=int(input("Enter how much quantity You Want (like 1,2,etc):"))
      biscuits_total+=quantity*Biscuits
 elif customerproducts==10:
      quantity=int(input("Enter how much quantity You Want (like 1,2,etc):"))
      tissuepaper_total+=quantity*Tissuepaper
 elif customerproducts==11:
      quantity=int(input("Enter how much quantity You Want (like 1,2,etc):"))
      instantnoodles_total+=quantity*InstantNoodles
 elif customerproducts==12:
      quantity=int(input("Enter how much quantity You Want (like 1,2,etc):"))
      choclates_total+=quantity*Choclates
 else:
     print("entered invalid number sir, please try again")
 yesorno=input("Do you want to continue Press Y or not press N:").upper()

total_bill=rice_total+milk_total+bread_total+eggs_total+shampoo_total+soap_total+toothpaste_total+cookingoil_total+biscuits_total+instantnoodles_total+choclates_total+tissuepaper_total
print("Here is Your bill Sir : ",total_bill,"rupees")


   
