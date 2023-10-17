
class Star_Cinema:
    hall_list = []

    @classmethod
    def entry_hall(cls, hall):
        if isinstance(hall, Hall):
            cls.hall_list.append(hall)
        else:
            print("Invalid object. Please provide an instance of the Hall class.")


class Hall:
    def __init__(self, rows, cols, hall_no):
        self.__seats = {}  # Private dictionary to store seats information
        self.__show_list = []  # Private list of tuples for show information
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        self.__show_seats = {}

        # Initialize seats with all seats as available (0)
        for row in range(1, rows + 1):
            seat_row = []
            for col in range(1, cols + 1):
                seat_row.append(0)
            self.__seats[row] = seat_row

    def __str__(self):
        return f"Hall No: {self.__hall_no}, Rows: {self.__rows}, Columns: {self.__cols}"

    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self.__show_list.append(show_info)
        self.__show_seats[id] = self.__seats.copy()

    def book_seats(self, show_id, seat_list):
        if show_id not in self.__show_seats:
            print("Invalid show ID.")
            return

        for row, col in seat_list:
            if (
                row not in self.__seats
                or col not in range(1, self.__cols + 1)
                or self.__seats[row][col - 1] != 0
            ):
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



if __name__ == "__main__":
    # Create a Hall object and initialize it with rows, cols, and hall_no
    hall1 = Hall(rows=5, cols=6, hall_no=1)

    # Create a Star_Cinema object and add the Hall object to its hall_list using inheritance
    cinema = Star_Cinema()
    cinema.entry_hall(hall1)

    # Entry shows in the Hall
    hall1.entry_show("S1", "Movie A", "12:00 PM")
    hall1.entry_show("S2", "Movie B", "3:00 PM")

    # Book seats in a show
    hall1.book_seats("S1", [(1, 2), (2, 3)])

    # View available seats in a show
    available_seats = hall1.view_available_seats("S1")
    print(f"Available Seats for Show S1: {available_seats}")

    # View show list
    show_list = hall1.view_show_list()
    print(f"Show List: {show_list}")
