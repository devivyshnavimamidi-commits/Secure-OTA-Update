name=input("enter your name:")

list='''
  1.Rice=5kg bag
  2.suger=15kg
  3.flour=5kg
  4.meat=1kg
  5.cooking oil=2liters
  6.salt=2kg
  7.paste=1kg
  8.noodle=10 packets
  9.oates=18 b0xes
  10.chips=20 packets
'''
items={
         "rice":5,
         "suger":15,
         "flour":5,
         "meat":1,
         "cooking oil":2,
         "salt":2,
         "paste":1,
         "noodle":10,
         "oates":18,
         "chips":20
}
ilist=[]
qlist=[]
plist=[]
price=0
finalprice=0
totalprice=0
pricelist=[]
while True:
 choice1=input("enter 4 if you want to buy or 5 to exit :")
 if "4"==choice1:
    print(list)
    
 elif "5"==choice1:
    print("thank you! come again")
 else:
    print("invalide choice try again")
 while True:
      choice2=input("enter 4 if you want to buy or 5 to exit :")
      if "5"==choice2:
       print("thank you! come again")
      elif "4"==choice2:
          item=input("choose your item :").lower()
          while True:
              item_quantity=input("enter your quantity:")
              if item_quantity.isdigit():
                  quantity=int(item_quantity)
                  break
              else:
                  print("invalide quantity try again")
      if item in items:
         price=quantity*items[item]
         pricelist.append((item,quantity,items[item],price))
         totalprice+=price
         ilist.append(item)
         plist.append(price)
         qlist.append(quantity)
      else:
         print("selected items is out of stock, choose another item")
         
      if totalprice>0:
         tax_amount=(totalprice*10)/100
         finalprice=totalprice+tax_amount
         print(25* "=", "pythonlife super market", 25*"=")
         print(" "*29,"hyderabad")
         print("name :",name,30*" ")
         print(50*" _")
         print("S.No",10*" ","items",10*" ","quantity",10*" ","price")
         for i in range(len(pricelist)):
            print(i+1,14*" ",ilist[i],13*" ",qlist[i],14*" ",plist[i])
         print(40*" _")
         print(50*" ","total amount :","rs",totalprice)
         print("Tax Amount :",52*" ","RS",tax_amount)
         print(40*"_")
         print(50*" ","final amount :","RS",finalprice)
         print(40*"_")
         print(21*" ","Thank you and visit again",21*"")
         print(40*"_")
         
         
