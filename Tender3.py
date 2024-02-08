import mysql.connector
mybb=mysql.connector.connect(host="localhost",
                             user="root",
                             password="S@16112001",
                             database="tender_management_system")
print(mybb)
ans='y'
Tender3=[]
while ans=='y':
    print("1.BidID")
    print("2.TenderID")
    print("3.SupplierID")
    print("4.Amount")
    print("5.SubmissionDate")
    print("6.Exit")
    print("Enter number between 1 to 6")
    choice=int(input("Enter number between 1 to 6:"))
    if(choice==1):
        Tender3_Id=input("Enter BidID:")
        Tender3.append({"BidID":Tender3_Id})
    elif(choice==2):
        Tender3_Id=input("Enter TenderID:")
        Tender3.append({"TenderID":Tender3_Id})
    elif(choice==3):
        Tender3_Id=input("Enter SupplierID")
        Tender3.append({"SupplierId":Tender3_Id})
    elif(choice==4):
        Tender3_Id=input("Enter Amount:")
        Tender3.append({"Amount":Tender3_Id})
    elif(choice==5):
        Tender3_Id=input("Enter SubmissionDate:")
        Tender3.append({"SubmissionDate":Tender3_Id})
    elif(choice==6):
        break
    else:
        print("Error 404.Please enter the valid number")
    ans=input("Do you want to continue(y/n)?")
    print("Tenders",Tender3)

