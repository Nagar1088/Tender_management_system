import mysql.connector
myab=mysql.connector.connect(host="localhost",
                             user="root",
                             password="S@16112001",
                             database="tender_management_system")
cursor=myab.cursor()
table_creation_query="""create table suppliers_table(supplierId int primary key int not null auto_increment,
                        name varchar(30) not null,
                        contactInfo int not null unique)"""
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
    
    
    print("Tenders",Tender2)

insert_query="""insert into  suppliers_table(supplierId,name,contactInfo)
                values
                (%s,%s,%s)"""
cursor.execute(insert_query)
myab.commit()
ans=input("Do you want to continue(y/n)?")
cursor.close()
myab.close()
