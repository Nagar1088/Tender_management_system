ans='y'
Tender4=[]
while ans=='y':
    print("1.ContractID")
    print("2.TenderID")
    print("3.BidID")
    print("4.AwardDate")
    print("5.Exit")
    print("Enter number between 1 to 6")
    choice=int(input("Enter number between 1 to 6:"))
    if(choice==1):
        Tender4_Id=input("Enter ContractID:")
        Tender4.append({"ContractID":Tender4_Id})
    elif(choice==2):
        Tender4_Id=input("Enter TenderID:")
        Tender4.append({"TenderID":Tender4_Id})
    elif(choice==3):
        Tender4_Id=input("Enter BidID:")
        Tender4.append({"BidID":Tender4_Id})
    elif(choice==4):
        Tender4_Id=input("Enter AwardDate:")
        Tender4.append({"AwardDate":Tender4_Id})
    elif(choice==5):
        break
    else:
        print("Error 404.Please enter the valid number")
    ans=input("Do you want to continue(y/n)?")
    print("Tenders",Tender4)