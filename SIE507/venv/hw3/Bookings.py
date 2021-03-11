from Airplane import Airplane, Seat
import pandas as pd

class Booking:
    def __init__(self, lastname, firstname):
        self.lastname = lastname
        self.firstname = firstname
        pass

    def getLastName(self):
        return self.lastname

    def getFirstName(self):
        return self.firstname

    def AssignSeat(self, seat):
        self.seat = seat
        self.seat.OccupySeat()

    def print(self):
        print(self.firstname, self.lastname)
        self.seat.print()

class BookingMgr:
    def __init__(self, Plane, booking_file_name=None):
        self.plane = Plane
        if booking_file_name:
            self.booking_file_name = booking_file_name
            df_booking = self.__makeBookingdfFromFile()

    def bookSeat(self, seat, booking):
        self.booking = booking
        # check to see if a seat is available
        if self.plane.isSeatAvailable(seat):
            # book the seat on the plane
            self.plane.bookSeat(seat)
            # assign the seat to the booking
            self.booking.AssignSeat(seat)
            return True
        else:
            print("Seat is not available.")
            return False

    def UserMenu(self):
        first_name, last_name = input("\nPlease input your name (firstname, lastname):").split()
        print("\nCurrently Available Seats:")
        self.plane.PrintSeatChart()
        print("\nWhich seat would you like to select?")
        selection = input("Row and seat (row,seat):")
        selection = selection.split(",")
        selected_row = int(selection[0])
        selected_seat = int(selection[1])
        row = [last_name, first_name, str(selected_row), str(selected_seat)]

        newBooking = Booking(last_name, first_name)
        askSeat = Seat(selected_row, selected_seat)
        if self.bookSeat(newBooking, askSeat):
            print("Seat was successfully booked.")
            return True
        else:
            print("Sorry. Seat not available.")
            return False

    def __update_booking_file(self):
        pass

    def __update

    def __makeBookingdfFromFile(self):
        df = pd.read_csv(self.booking_file_name, index_col=None)
        print(df.head())