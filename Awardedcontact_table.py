import Database
mydb = Database.connect_to_database()
cursor=mydb.cursor()
while True:

    contract_id=int(input("Enter contract_id :"))
    tenderid=int(input("Enter tenderid :"))
    supplier_id=int(input("Enter  supplier_id :"))
    bid_id=int(input("Enter bid_id :"))
    awardedDate=input("Enter awardedDate :")

    Query="insert into awardedcontracts_table(contract_id,tenderid, supplier_id,bid_id,awardedDate) values(%s,%s,%s,%s,%s)"
    cursor.execute(Query,(contract_id,tenderid, supplier_id,bid_id,awardedDate))
    
    mydb.commit()

    choice = input("1 -> Enter more\n2 -> Exit\nEnter choice: ")
    if choice == '2':
        break

