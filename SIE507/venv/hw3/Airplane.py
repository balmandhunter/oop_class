from ReadWriteFile import ReadWriteFile

class Airplane:
    def __init__(self, rows=None, seats=None, filename=None):
        # initialize the seating chart from a file
        if filename and seats is None and rows is None:
            seatlist = ReadWriteFile()
            self.seat_chart = seatlist.fileRead(filename)
        # initialize the seating chart from user entered rows and seats
        elif seats is not None and rows is not None and filename is None:
            self.rows = rows
            self.seats = seats
            self.seat_chart =

        # throw error
        elif (seats is not None or rows is not None) and filename is not None:
            print("Invalid Plane - enter either a filename or rows/seats, but not both")         # Display an error message for invalid entry
        else:
            print("Invalid Plane - please enter rows seats seats or a filename")                 # Display an error message for invalid entry

    def getSeatChart(self):
        pass

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

    def __printSeatChart(seld, rows, seats):
        pass

    def __makeSeatChartFromFile(self):
        pass

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
