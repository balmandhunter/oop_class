from Airplane import Airplane
from Seat import Seat
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

    def assignSeat(self, seat):
        self.seat = seat
        self.seat.OccupySeat()

    def print(self):
        print(self.firstname, self.lastname)
        self.seat.print()


class BookingMgr:
    def __init__(self, plane, booking_file_name=None):
        self.plane = plane
        if booking_file_name:
            self.booking_file_name = booking_file_name
            # make a df from the imported file
            self.__makeBookingdfFromFile()
            # make sure there aren't any booked seats in the plane's seat chart
            # that don't have a booking in the booking file
            self.__checkSeatChartBookingFileParity()
            # for every entry in the booking file, make sure the seat is booked, and the
            # plane's seating chart is updated
            self.__bookSeatChartFromBookingFile()
        else:
            self.df_booking = None

    '''Book a seat on a plane, and update the booking and seat chart files'''
    def bookSeat(self, booking, seat):
        self.booking = booking
        # check to see if a seat is available
        if self.plane.isSeatAvailable(seat):
            # book the seat on the plane
            self.plane.bookSeat(seat)
            # assign the seat to the booking
            booking.assignSeat(seat)
            # update the booking df
            self.__update_booking_df(seat)
            # update the seat chart file
            self.plane.writeSeatChartToFile()
            # update the bookings file
            self.__update_booking_file()
            return True
        else:
            print("Seat is not available. Please select an available seat.")
            self.plane.printSeatChart()
            self.__userInputSeat()

    '''Give users the option to book another seat when they finish booking.'''
    def __bookAgain(self):
        book_again = input("\n Would you like to book another seat (yes or no):")
        if book_again == 'no':
            print("Thanks for booking with SIE508 Air. Enjoy your trip!")
            exit()
        elif book_again == 'yes':
            self.UserMenu()
        else:
            print("Invalid Input")
            input("\n Would you like to book another seat (yes or no):")

    '''Ask user to input a seat. Book it if it's available, or ask for another entry if not.'''
    def __userInputSeat(self):
        selection = input("Row and seat letter (row, seat):")
        selection = selection.split(", ")
        selected_row = int(selection[0]) - 1
        row_dict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
        selected_number = row_dict[str(selection[1])]

        # Create a new booking for the user's entered data
        newBooking = Booking(self.last_name, self.first_name)
        # Grab the seat the user requested from the plane's list of seat objects
        askSeat = self.plane.seat_obj_list[selected_row][selected_number]
        # book the seat, or return an error if it's occupied
        if self.bookSeat(newBooking, askSeat):
            print("Seat was successfully booked.")
            self.__bookAgain()
        else:
            print("Seat is not available. Please select an available seat.")
            self.__userInputSeat()

    '''Function to interact with user'''
    def UserMenu(self):
        self.first_name, self.last_name = input("\nPlease input your name (firstname, lastname):").split(", ")
        print("\nCurrently Available Seats:")
        self.plane.printSeatChart()
        print("\nWhich seat would you like to select?")
        self.__userInputSeat()

    '''Function to update the booking file when a booking is created'''
    def __update_booking_file(self):
        self.df_booking.to_csv("flight_bookings.csv", index=False, header=False)

    '''Function to add new bookings to the booking df'''
    def __update_booking_df(self, seat):
        # create a new df for the current booking (add 1 to the row and number to account for
        # zero indexing)
        return_row = seat.GetRow() + 1
        return_num = seat.GetNumber() + 1
        df_new_booking = pd.DataFrame.from_dict({'lastname': [self.booking.getLastName()],
                                                 'firstname': [self.booking.getFirstName()],
                                                 'row_': [return_row],
                                                 'number': [return_num]})
        # If the booking df already exists, append the new booking to it
        if self.df_booking is not None:
            self.df_booking = self.df_booking.append(df_new_booking)
        else:
            self.df_booking = df_new_booking

    '''Function to create a dataframe of booking information from a csv'''
    def __makeBookingdfFromFile(self):
        self.df_booking = pd.read_csv(self.booking_file_name,
                                      header=None,
                                      names=['lastname', 'firstname', 'row_', 'number'],
                                      index_col=None)

    '''Function to update the plane and seats with booking information from a csv file'''
    def __bookSeatChartFromBookingFile(self):
        # iterate through the dataframe
        for idx, row in self.df_booking.iterrows():
            chart_row = row.row_ - 1
            chart_num = row.number - 1
            # check to see if the seat is marked as occupied on the plane's seat chart
            if self.plane.seat_chart[chart_row, chart_num] != 'X':
                # grab the seat object for the seat
                seat = self.plane.seat_obj_list[chart_row][chart_num]
                # book the seat on the plane
                self.plane.bookSeat(seat)
                # book the seat objects
                self.plane.bookSeatsFromChartFile()
                # make a booking
                booking = Booking(row.lastname, row.firstname)
                # assign the seat to the booking
                booking.assignSeat(seat)
                # update the seat chart file
                self.plane.writeSeatChartToFile()

    '''Check to make sure that there aren't seats shown as booked in seats.txt
    that don't have a booking in flight_bookings.csv'''
    def __checkSeatChartBookingFileParity(self):
        # iterate through the plane's seat chart
        for row in range(0, self.plane.rows):
            for num in range(0, self.plane.seats):
                # find seats that show up as booked
                if self.plane.seat_chart[row, num] == 'X':
                    # check to see if the dataframe has someone booked in the seat (adjust for zero indexing)
                    if self.df_booking[(self.df_booking.row_ == row + 1) & (self.df_booking.number == num + 1)].empty:
                        raise Exception("A seat shown as occupied in the seats.txt file does not"
                                        "have an associated booking. Please check your input files.")
