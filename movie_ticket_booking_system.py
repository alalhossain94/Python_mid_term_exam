class Star_Cinema:
    hall_list=[]
    
    def entry_hall(self,hall):
        self.hall_list.append(hall)

class Hall(Star_Cinema):
    def __init__(self,rows,cols,hall_no) -> None:
        self._seats={}
        self._show_list=[]
        self._rows=rows
        self._cols=cols
        self._hall_no=hall_no

    def entry_show(self,id,movie_name,time):
        show_information=(id,movie_name,time)
        self._show_list.append(show_information)

        seats=[]
        for i in range(self._rows):
            row=[0]* self._cols
            seats.append(row)
            self._seats[id]=seats

    def book_seats(self,id,user_choice):
        if id in self._seats:
            for seat in user_choice:
                row,col=seat
                if self._seats[id][row][col]==0:
                    self._seats[id][row][col]=1
                    print("Congratulations! Booking Confirmed, Enjoy the Movie.")
                else:
                    print("Error!: Already Booked, Please try another one.")
        else:
            print("Error: ID Or Seat Number Invalid ! Kindly Check Again.")


    def view_show_list(self):
        for show in self._show_list:
            print(f"ID: {show[0]} Movie Name: {show[1]} Time: {show[2]}")

    def view_available_seats(self,id):
        if id in self._seats:
            for r in range(self._rows):
                for c in range(self._cols):
                    if self._seats[id][r][c]==0:
                        print(f'Seats: ({r}, {c})')
        else:
            print("Error: No Running show!")

hall_1 =Hall(7,7,1)
cinema=Star_Cinema()
cinema.entry_hall(hall_1)
hall_1.entry_show(101,"Rise of the Planet of the Apes", "08:00 PM")
hall_1.entry_show(201,"Shawshank Redemption", "10:00 PM")
hall_1.entry_show(301,"The Amazing Spider-man", "12:00 PM")

                        
print("1. VIEW ALL SHOW TODAY")
print("2. VIEW AVAILABLE SEATS")
print("3. BOOK TICKET")
print("4. EXIT")

choice=int(input("Enter Option: " ))
while True:
    if (choice==1):
        hall_1.view_show_list()
        print("********************")
    elif (choice==2):
        show_id=int(input("Enter Show ID: "))
        hall_1.view_available_seats(show_id)
        print("********************")
    elif (choice==3):
        show_id=int(input("Enter Show ID: "))
        row=int(input("Enter Row No: "))
        col=int(input("Enter Column No: "))
        hall_1.book_seats(show_id, [(row,col)])
        print("********************")

    print("1. VIEW ALL SHOW TODAY")
    print("2. VIEW AVAILABLE SEATS")
    print("3. BOOK TICKET")
    print("4. EXIT")
    print("********************")
    choice=int(input("Enter Option: " ))
    print("********************")
