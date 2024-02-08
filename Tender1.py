import mysql.connector
myab=mysql.connector.connect(host="localhost",
                             user="root",
                             password="S@16112001",
                             database="tender_management_system")
print(myab)
ans='y'
Tender2=[]
while ans=='y':
    print("1.supplierId")
    print("2.name")
    print("3.contactInfo")
    print("4.Exit")
    print("Enter number between 1 to 4")
    choice=int(input("Enter number between 1 to 4:"))
    if(choice==1):
        tender2_id=input("Enter supplierId:")
        Tender2.append({"supplierId":tender2_id})
    elif(choice==2):
        tender2_id=input("Enter name:")
        Tender2.append({"name":tender2_id})
    elif(choice==3):
        tender2_id=input("Enter contactInfo:")
        Tender2.append({"contactInfo":tender2_id})
    elif(choice==4):
        break
    else:
        print("Error 404.Please enter valid number")
    
    ans=input("Do you want to continue(y/n)?")
    print("Tenders",Tender2)