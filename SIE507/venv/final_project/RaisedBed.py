import numpy as np
from SquareFoot import Square


class RaisedBed:
    def __init__(self, rows=None, seats=None, filename=None):
        # initialize the seating chart from a file
        if filename and seats is None and rows is None:
            self.filename = filename
            self.seat_chart = self.__makeSeatChartFromFile()
            self.rows = self.seat_chart.shape[0]
            self.seats = self.seat_chart.shape[1]
        # initialize the seating chart from user entered rows and seats
        elif seats is not None and rows is not None and filename is None:
            self.rows = rows
            self.seats = seats
            self.seat_chart = np.full((rows, seats), '.')
        # throw error if user enters row/seat and a filename
        elif (seats is not None or rows is not None) and filename is not None:
            # Display an error message for invalid entry
            print("Invalid Plane - enter either a filename or rows/seats, but not both")
        # throw error if users doesn't enter a row/seat combo or a filename
        else:
            # Display an error message for invalid entry
            print("Invalid Plane - please enter rows seats seats or a filename")

        # initialize a dictionary of seat objects
        self.__initializeSeats()

        if filename is not None:
            self.bookSeatsFromChartFile()

    '''Function to get the seating chart'''
    def get_planting_chart(self):
        return self.seat_chart

    '''Function to print a user-friendly seating chart'''
    def printSeatChart(self):
        alphabet = ['A', 'B', 'C', 'D', 'E', 'F']  # Headers for columns when displaying seat arrangement

        fileColoumn = len(self.seat_chart[0])  # Variable to store number of columns in the list
        print('{0:<3}'.format(' '), end='')

        count = 0  # Counter
        for i in range(fileColoumn):  # For loop to display column headers depending on the number of columns
            if count == fileColoumn / 2:  # Display an space in middle of the column
                print(' ', end='')
            print(alphabet[i], end='')  # Display the respective letter from the list alphabet
            count += 1
        print()

        rowNum = 1
        for line in self.seat_chart:  # For loop to display the row number and the respective seat arrangement
            print('{0:<3}'.format(rowNum), end='')
            count = 0
            for char in line:
                if count == fileColoumn / 2:  # Display an space in the middle of the column
                    print(' ', end='')
                print(char, end='')
                count += 1
            rowNum += 1
            print()

    '''Function to book a seat'''
    def bookSeat(self, Seat):
        Seat.OccupySeat()
        self.__updateSeatChart(Seat)

    '''Function to check seats to see if they are available'''
    def isSeatAvailable(self, Seat):
        if Seat.occupied:
            return False
        else:
            return True

    '''Function to update the seating chart when a seat is booked'''
    def __updateSeatChart(self, Seat):
        self.seat_chart[Seat.row][Seat.number] = 'X'

    '''Function to make a seat chart array from a text file'''
    def __makeSeatChartFromFile(self):
        alphabet = ['A', 'B', 'C', 'D', 'E', 'F']  # Headers for columns when displaying seat arrangement

        seatColoumns = []
        seatRows = []

        file = open(self.filename, 'r')  # Open seats.txt in read only mode
        seatsReadList = file.readlines()  # Read the file
        seatsList = []  # Define a blank list that will hold the seat arrangement

        for line in seatsReadList:  # Iterate through the variable seatReadList
            rowSeat = []  # Define a temporary list that will hold each character of the loop variable line
            for char in line:  # Iterate through each character in the loop variable line
                if char == '\n':  # If the new line character is detected, skip the execution of rest of the loop
                    continue
                rowSeat.append(char)  # Add character of the line to the temporary list
            seatsList.append(rowSeat)  # Add temporary list to the seat list

        for i in range(len(seatsList[0])):  # Loop to add respective column headers to the list
            seatColoumns.append(alphabet[i])

        for i in range(len(seatsList)):  # Loop to add respective row numbers to the list
            seatRows.append(str(i + 1))

        seat_array = np.array(seatsList)
        file.close()
        return seat_array

    '''Function to create a list of empty seat objects, based on the plane's seating chart'''
    def __initializeSeats(self):
        # create an empty list for seat objects
        self.seat_obj_list = [[0] * self.seats for i in range(self.rows)]

        # loop through the rows and seats, and create a seat object for every seat, and save all of the seat names
        # in an array
        for row in range(0, self.rows):
            for number in range(0, self.seats):
                # seat_name = 'r' + str(row) + 'n' + str(number)
                self.seat_obj_list[row][number] = Seat(row, number)
                # exec(seat_name + "= Seat(row, number)")

    '''Function to occupy the seat objects for seats that are shown as booked in the seat chart'''
    def bookSeatsFromChartFile(self):
        for row in range(0, self.rows):
            for num in range(0, self.seats):
                if self.seat_chart[row, num] == 'X':
                    self.seat_obj_list[row][num].OccupySeat()

    '''Function to write an the seat chart to a text file'''
    def writeSeatChartToFile(self):
        file = open('seats.txt', 'w')       # Open/create a text file in write only mode
        for line in self.seat_chart:        # Iterate through each row in array
            for char in line:               # Iterate through each character in the loop variable line
                file.write(char)            # Write the character to the text file
            file.write('\n')                # Go to the next line in the text file after writing a line
        file.close()
