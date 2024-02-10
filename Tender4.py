import mysql.connector
mycb=mysql.connector.connect(host="localhost",
                             user="root",
                             password="S@16112001",
                             database="tender_management_system")
cursor=mycb.cursor()

while True:

    bid_id=int(input("Enter bid_id :"))
    Tender_Id=int(input("Enter Tender_Id :"))
    supplier_id=int(input("Enter supplier_id"))
    amount=int(input("Enter amount :"))
    submissionDate=input("Enter  submissionDate :")

    query="insert into bids_table(bid_id,Tender_Id,supplier_id,amount,submissionDate) values(%s,%s,%s,%s,%s)"
    cursor.execute(query,(bid_id,Tender_Id,supplier_id,amount,submissionDate))

    mycb.commit()
    
    choice = input("1 -> Enter more\n2 -> Exit\nEnter choice: ")
    if choice == '2':
        break