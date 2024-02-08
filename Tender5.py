ans='y'
Tender5=[]
while ans=='y':
    print("1.UserID")
    print("2.Username")
    print("3.Password")
    print("4.Email")
    print("5.UserType")
    print("6.Exit")
    print("Enter number between 1 to 6")
    choice=int(input("Enter number between 1 to 6:"))
    if(choice==1):
        Tender5_Id=input("Enter UserID:")
        Tender5.append({"UserID":Tender5_Id})
    elif(choice==2):
        Tender5_Id=input("Enter Username:")
        Tender5.append({"Username":Tender5_Id})
    elif(choice==3):
        Tender5_Id=input("Enter Password:")
        Tender5.append({"Password":Tender5_Id})
    elif(choice==4):
        Tender5_Id=input("Enter Email:")
        Tender5.append({"Email":Tender5_Id})
    elif(choice==5):
        Tender5_Id=input("Enter UserType:")
        Tender5.append({"UserType":Tender5_Id})
    elif(choice==6):
        break
    else:
        print("Error 404.Please enter the valid number")
    ans=input("Do you want to continue(y/n)?")
    print("Tenders",Tender5)
