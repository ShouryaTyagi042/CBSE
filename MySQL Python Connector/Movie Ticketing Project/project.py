import mysql.connector as sql
mydb = sql.connect(host="localhost", user="root",
                   passwd="lm10barcelona", database="movie")
mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE movie ")

# mycursor.execute("CREATE TABLE bookings(Movie varchar(20),Tickets varchar(5),Name varchar(30),ph varchar(17)) ")


movies = ["1. Godzilla vs Kong", "2. Mumbai Saga",
          "3. Roohi", "4. Tom and Jerry"]
res = ["BOOKINGS SUCCESSFUL", "", "BOOKINGS CANCELLED", ""]
while True:
    if mydb.is_connected:
        print("\nPVR THEATRE BOOKINGS")
        print("1. BOOK TICKETS")
        print("2. CHECK BOOKINGS")
        print("3. CANCEL BOOKINGS")
        print("4. EXIT")
        ch = int(input("Enter your choice , select the number : "))
    else:
        print("connection error")
        break
    if ch == 1:
        print("currently showing")
        for x in movies:
            print(x)

        mov = input("Enter your choice :")
        ticket = int(input("Enter no of tickets you want:"))
        name = input("Enter your NAME: ")
        num = input("Phone number: ")
        mycursor.execute("INSERT INTO bookings VALUES('{}','{}','{}','{}')".format(
            mov, ticket, name, num))
        # print("Booking Successful")
    elif ch == 2:
        inp = input("Enter your Phone number :")
        mycursor.execute("select * from bookings where ph='{}'".format(inp))
        for k in mycursor:
            print("Movie name:{}\t , tickets:{}\t , Name : {} \t ,Phone :{} \t ".format(
                movies[int(int(k[0]) - 1)], k[1], k[2], k[3]))

    elif ch == 3:
        inp = input("Enter your phone number  ")
        mycursor.execute("DELETE FROM bookings WHERE ph ='{}'".format(inp))
    try:
        mydb.commit()
        print(res[ch - 1])
    except:
        mycursor.rollback()
        print("Connection Error")
    if ch == 4:
        print("Thank you for choosing PVR Cinemas ")
        break
