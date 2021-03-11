import numpy as np

class Airplane:
    def __init__(self, rows=None, seats=None, filename=None):
        # initialize the seating chart from a file
        if filename and seats is None and rows is None:
            self.filename = filename
            self.seat_chart = self.__makeSeatChartFromFile()
        # initialize the seating chart from user entered rows and seats
        elif seats is not None and rows is not None and filename is None:
            self.rows = rows
            self.seats = seats
            self.seat_chart = np.full((rows, seats), '.')
        # throw error if user enters row/seat and a filename
        elif (seats is not None or rows is not None) and filename is not None:
            print("Invalid Plane - enter either a filename or rows/seats, but not both")         # Display an error message for invalid entry
        # throw error if users doesn't enter a row/seat combo or a filename
        else:
            print("Invalid Plane - please enter rows seats seats or a filename")                 # Display an error message for invalid entry

    def getSeatChart(self):
        return self.seat_chart

    def printSeatChart(self):
        print(self.getSeatChart())

    def bookSeat(self, seat):
        pass

    def cancelSeat(self, seat):
        pass

    def isSeatAvailable(self, seat):
        pass

    def getAvailableSeat(self, seat):
        pass

    def __makeSeatChart(self, rows, seats):
        pass


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

class Seat:
    def __init__(self, row, number):
        self.row = row
        self.number = number
        self.occupied = False
        pass

    def OccupySeat(self):
        self.occupied = True
        pass

    def EmptySeat(self):
        self.occupied = False
        pass

    def print(self):
        if self.occupied == True:
            print("Seat: ", self.row, self.number, "Occupied")
        else:
            print("Seat: ", self.row, self.number, "Empty")
