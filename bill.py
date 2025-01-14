ProductIdList=[]
ProductNameList=[]
QuantityList=[]
UnitPriceList=[]
SubTotalList=[]

def Input():
    while True:
        ProductId = int(input("Enter a product ID: "))
        if ProductId in ProductIdList:
            print("Product ID already exists. Please enter a different ID.")
            continue
        else:
            ProductIdList.append(ProductId)
            ProductName = input("Enter a product name: ")
            ProductNameList.append(ProductName)
            Quantity = int(input("Enter the quantity: "))
            QuantityList.append(Quantity)
            UnitPrice = int(input("Enter the unit price (₹): "))
            UnitPriceList.append(UnitPrice)
            AddMore = input("Do you want to add more items? [Y/N]: ")
            print("-----------------------------------")
        if AddMore in ["N", "n"]:
            break

Input()

#printing the list of items once the user enter's "N" or "n" as the answer

print("----------------PRODUCT LIST-----------------")
for i in range(len(ProductIdList)):
    print(f"Product ID: {ProductIdList[i]}, Product Name: {ProductNameList[i]}, Quantity: {QuantityList[i]}, Unit Price: ₹{UnitPriceList[i]}/-")
    print("-----------------------------------------")


# printing fresh Lists only if the list gets updated

def RemovingProductShowing():
  print("---------------UPDATED PRODUCT LIST---------------")
  for i in range(len(ProductIdList)):
      print(f"Product ID: {ProductIdList[i]}, Product Name: {ProductNameList[i]}, Quantity: {QuantityList[i]}, Unit Price: ₹{UnitPriceList[i]}/-")
      print("----------------------------------------------")


# removing product if any

RemoveProduct = input("Do you want to remove a product? [Y/N]: ")
if RemoveProduct == "Y" or RemoveProduct == "y":
    RemoveProductId = int(input("Enter Product ID to remove: "))
    if RemoveProductId in ProductIdList:
        indexOfelement = ProductIdList.index(RemoveProductId)
        del ProductIdList[indexOfelement]
        del ProductNameList[indexOfelement]
        del QuantityList[indexOfelement]
        del UnitPriceList[indexOfelement]
        print("Product removed successfully")
        print("-----------------------------------")
        RemovingProductShowing()
    else:
        print("Product ID not found")
else:
    print("No product removed")


#Total Calculation After and Before GST

for i in range(len(QuantityList)):
    Subtotal = (QuantityList[i] * UnitPriceList[i])
    SubTotalList.append(Subtotal)



#Calculation of final total

FinalTotal = sum(SubTotalList)
print(f"Final Total before discount: ₹{FinalTotal}/-")  # => FINAL TOTAL BEFORE DISCOUNT



#GST CALCULATION

GST = input("Do you want to add GST? [Y/N]: ")
if GST == "y" or GST == "Y":
    GSTRate = int(input("Enter GST Rate: "))
    GSTAmount = (FinalTotal * GSTRate / 100)
    totalwithGst = FinalTotal + GSTAmount
elif GST == "N" or GST == "n":
    GSTRate = 0
    GSTAmount = 0
    totalwithGst = FinalTotal
else:
    print("Invalid Input")



#discount function

def DiscountSection():
    global Number ,Discountpercent , DiscountAm, DiscountType,DiscountAmount,totalwithGst,FinalTotalafterdiscount
    # Creating Dictionary for a key-Pair value for user to choose any one
    Discount = {
        "1": "Percentage Discount on Total Bill (e.g., 5%, 10%, 15%)",
        "2": "Fixed Amount Discount on Total Bill (e.g., $10, $20)",
        "3": "Discount on Specific Product (e.g., 10% off on Product A)"
    }

    # Printing the Dictionary without the {}
    for key, value in Discount.items():
        print(f"{key}: {value}")

    Number = input("Enter Choice: ")

    # letting the user choose the key value from Discount Dictionary
    if Number == "1":
        DiscountType = float(input("Enter Discount Rate (%): "))
        Discountpercent = ((DiscountType / 100) * totalwithGst)
        FinalTotalafterdiscount = (totalwithGst - Discountpercent)


    elif Number == "2":
        DiscountAmount = int(input("Enter Discount Amount (₹): "))
        Discountpercent = (totalwithGst - DiscountAmount)


    elif Number == "3":
        Product = int(input("Enter Product ID you want your discount in? : "))
        if Product in ProductIdList:
            indexOfelementProduct = ProductIdList.index(Product)
            EnterDiscount = int(input(f"Enter Discount Rate on Product {ProductNameList[indexOfelementProduct]}(%) : "))
            Discountpercent =  round((EnterDiscount / 100) * SubTotalList[indexOfelementProduct])
            ProductTotalafterdiscount = (SubTotalList[indexOfelementProduct] - Discountpercent)
            newTotal = ((totalwithGst - SubTotalList[indexOfelementProduct]) + ProductTotalafterdiscount)
            totalwithGst = newTotal
        else:
         print("No product Found")
    else:
        print("Invalid Input")




# users choice for discount => calling the discount function

AddDiscount = input("Do you want to add a discount? [Y/N]: ")
if AddDiscount == "Y" or AddDiscount == "y":
    DiscountSection()
elif AddDiscount == "N" or AddDiscount == "n":
    FinalTotalafterdiscount = totalwithGst
else:
    print("Invalid Input")


#output:

print("-----------------------------------")
print("E-commerce Billing System Invoice")
print("-----------------------------------")
for i in range(len(ProductIdList)):
  print(f"Product ID: {ProductIdList[i]}")
  print(f"Product Name: {ProductNameList[i]}")
  print(f"Quantity: {QuantityList[i]}")
  print(f"Unit Price: ₹{UnitPriceList[i]}/-")
  print(f"Subtotal: ₹{SubTotalList[i]}/-")
  print("-----------------------------------")

print(f"Total before discount: ₹{FinalTotal}/-")

print(f"GST @ {GSTRate}%: ₹{GSTAmount}")
if Number == "2":
        print(f"Discount:  @ ₹{DiscountAmount}/-")
elif Number == "1":
        print(f"Discount @ {DiscountType}%: ₹{Discountpercent}/-")
elif Number == "3":
        print(f"Discount on Product: ₹{Discountpercent}/-")
else:
    print("No discount applied.")
print("-----------------------------------")\


if Number=="2":
    print(f"Final Total:  ₹ {((FinalTotal+GSTAmount)-DiscountAmount)}")
else:
    print(f"Final Total: ₹{((FinalTotal+GSTAmount)-Discountpercent)}/-")

print("----------------------------------")
print("Thank you for shopping with us!")
print("-----------------------------------")

