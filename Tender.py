ans="y"
Tender=[]
while ans=="y":
    print("1.Tender Id")
    print("2. Title")
    print("3.Tender start Date")
    print("4.Tender End Date")
    print("5.Discription")
    print("6.exit")
    print("enter tender between 1 to 6:")
    choice=int(input("Enter the number between 1 to 6:"))

    if (choice==1):
        tenter_id=input("Enter Tender_Id :")
        Tender.append({"Tender Id": tenter_id})
    elif(choice==2):
        tender_name=input("Enter Title:")
        Tender.append({"Title":tender_name})
    elif(choice==3):
        tender_id=input("Enter Tender start date:")
        Tender.append({"Tender start Date":tender_id})
    elif(choice==4):
         tender_id=input("Enter Tender End date:")
         Tender.append({"Tender End Date":tender_id})
    elif(choice==5):
         tender_id=input("Enter discription:")
         Tender.append({"Tender Discription":tender_id})
    elif(choice==6):
        break
    else:
        print("Invalid option. Please enter between 1 to 7.")
    ans = input("Do you want to continue (y/n)? ")

print("Tenders:", Tender)


