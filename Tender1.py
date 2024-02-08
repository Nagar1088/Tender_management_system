ans="y"
Tender1=[]
while ans=="y":
    print("1.Supplier_Id")
    print("2.Name")
    print("3.Contact_info")
    print("4.Exit")
    print("enter tender between 1 to 4:")
    choice=int(input("Enter number between1 to 4:"))
    if(choice==1):
       tender1_id=input("Enter Supplier_Id:")
       Tender1.append({"Supplier_Id":tender1_id})
    elif (choice==2):
        tender1_id=input("Enter Name:")
        Tender1.append({"Name":tender1_id})
    elif(choice==3):
        tender1_id=input("Enter Contact_info:")
        Tender1.append({"Contact_info":tender1_id})
    elif(choice==4):
        break
    else:
        print("Invalid Option.Please Enter between 1 to 4")
    
    ans=input("Do you want to continue(y/n)?")
    print("Tenders",Tender1)
    