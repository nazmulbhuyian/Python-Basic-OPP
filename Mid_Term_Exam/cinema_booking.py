
class Star_Cinema:
    hall_list = []

    def entry_hall(self, hall):
        if isinstance(hall, Hall):
            self.hall_list.append(hall)
        else:
            print("Invalid object. Please provide an instance of the Hall class.")

class Hall:
    def __init__(self, rows, cols ):
        self.__seats = {}
        self.__show_list = []
        self.__cols = cols
        self.__rows = rows
        self.__show_seats = {}

        for row in range(1, rows + 1):
            seat_row = []
            for col in range(1, cols + 1):
                seat_row.append(0)
            self.__seats[row] = seat_row


    def entry_show(self, id, movie_name, time ):
        show_info = (id, movie_name, time )
        self.__show_list.append(show_info)

        show_seats = {}
        for row in range(1, self.__rows + 1):
            seat_row = []
            for col in range(1, self.__cols + 1):
                seat_row.append(0)
            show_seats[row] = seat_row
    
        self.__show_seats[id] = show_seats


    def book_seats(self, show_id, seat_list):
        if show_id not in self.__show_seats:
            print("Invalid show ID.")
            return

        for row, col in seat_list:
            if ( row not in self.__seats or col not in range(1, self.__cols + 1) or self.__seats[row][col - 1] != 0 ):
                print(f"Invalid seat: Row {row}, Column {col}")
                return

        for row, col in seat_list:
            self.__seats[row][col - 1] = 1
            self.__show_seats[show_id][row][col - 1] = 1

        print("Seats booked successfully!")

    def view_show_list(self):
        return self.__show_list

    def view_available_seats(self, show_id):
        if show_id not in self.__show_seats:
            print("Invalid show ID.")
            return None

        available_seats = []
        seats = self.__show_seats[show_id]
        for row, seat_row in seats.items():
            for col, status in enumerate(seat_row):
                if status == 0:
                    available_seats.append((row, col + 1))
        return available_seats

hall1 = Hall(rows=5, cols=6)

cinema = Star_Cinema()
cinema.entry_hall(hall1)
hall1.entry_show("111", "Jawhan", "12:00 PM" )
hall1.entry_show("112", "Pathan", "3:00 PM" )


while True:
    print('1. View All Show Today')
    print('2. View Available Seats')
    print('3. Book Ticket')
    print('4. Exit')
    num = input()
    if num == "1":
        print(f"Show List: {hall1.view_show_list()}")

    elif num == "2":
        id = input('Enter Your ID: ')
        print(f"Available Seats for Show S1: {hall1.view_available_seats(id)}")

    elif num == "3":
        show_id = input("Enter Show ID: ")
        row = int(input("Enter Row Number: "))
        col = int(input("Enter Column Number: "))
        seat_to_book = [(row, col)]
        available_seats = hall1.view_available_seats(show_id)

        if not available_seats:
            print("No such show or all seats are booked.")
        elif (row, col) not in available_seats:
            print(f"Seat {row}, {col} is not available.")
        else:
            hall1.book_seats(show_id, seat_to_book)
            print("Ticket booked successfully!")

    elif num == "4":
        break

    else:
        print("Invalid input. Please choose a valid option.")