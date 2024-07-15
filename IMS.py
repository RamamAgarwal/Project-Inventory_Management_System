fd = open("Inventory.txt",'r')
products=fd.read().split('\n')
fd.close()
for i in products:
    print(i)
ui_prod_id=input("Enter the product id: ")
ui_prod_quan=input("Enter the product quantity: ")

updated_prod_lst= []

for product in products:
    prod_details=product.split(',')
    
    if prod_details[0]==ui_prod_id:
        print("----------------------------------")
        print("Product Name   :        ",prod_details[1])
        print("Price          :        ",prod_details[2])
        print("Quantity       :        ",ui_prod_quan)
        print("----------------------------------")
        print("Billing Amount :        ",int(prod_details[2])*int(ui_prod_quan))
        print("----------------------------------")
    
    prod_details[3]= int(prod_details[3]) - int(ui_prod_quan)
    updated_prod_lst.append(prod_details)
    
fm=open("Inventory.txt",'w')
for i in updated_prod_lst:
    prod = i[0] + "," + i[1] + "," + i[2] + "," + str(i[3]) + "\n"
    fm.write(prod)
fm.close()