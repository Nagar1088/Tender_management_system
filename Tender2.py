ans='y'
Tender2=[]
while ans=='y':
    print("1.ItemID")
    print("2.TenderID")
    print("3.Name")
    print("4.Description")
    print("5.Quantity")
    print("6.Exit")
    print("Enter number between 1 to 6")
    choice=int(input("Enter number between 1 to 6:"))
    if(choice==1):
        tender2_id=input("Enter ItemID:")
        Tender2.append({"ItemID":tender2_id})
    elif(choice==2):
        tender2_id=input("Enter TenderID:")
        Tender2.append({"TenderID":tender2_id})
    elif(choice==3):
        tender2_id=input("Enter Name:")
        Tender2.append({"Name":tender2_id})
    elif(choice==4):
        tender2_id=input("Enter Description:")
        Tender2.append({"Description":tender2_id})
    elif(choice==5):
        tender2_id=input("Enter Quantity:")
        Tender2.append({"Quantity":tender2_id})
    elif(choice==6):
        break
    else:
        print("Error 404.Please enter valid number")
    
    ans=input("Do you want to continue(y/n)?")
    print("Tenders",Tender2)





