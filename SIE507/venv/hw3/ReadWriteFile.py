import numpy as np

class ReadWriteFile:
    def __init__(self):
        pass

    '''Function to read the text file'''
    def fileRead(self, filename):
        alphabet = ['A', 'B', 'C', 'D', 'E', 'F']  # Headers for columns when displaying seat arrangement

        seatColoumns=[]
        seatRows=[]

        file = open(filename,'r')                                                   # Open seats.txt in read only mode
        seatsReadList = file.readlines()                                            # Read the file
        seatsList = []                                                              # Define a blank list that will hold the seat arrangement

        for line in seatsReadList:                                                  # Iterate through the variable seatReadList
            rowSeat = []                                                            # Define a temporary list that will hold each character of the loop variable line
            for char in line:                                                       # Iterate through each character in the loop variable line
                if char == '\n':                                                    # If the new line character is detected, skip the execution of rest of the loop
                    continue
                rowSeat.append(char)                                                # Add character of the line to the temporary list
            seatsList.append(rowSeat)                                               # Add temporary list to the seat list

        for i in range(len(seatsList[0])):                                          # Loop to add respective column headers to the list
            seatColoumns.append(alphabet[i])

        for i in range(len(seatsList)):                                             # Loop to add respective row numbers to the list
            seatRows.append(str(i+1))

        seat_array = np.array(seatsList)
        file.close()
        return seat_array


    '''Function to write an array to a text file'''
    def fileWrite(self, array):
        file = open('seats.txt', 'w')  # Open/create a text file in write only mode
        for line in array:  # Iterate through each row in array
            for char in line:  # Iterate through each character in the loop variable line
                file.write(char)  # Write the character to the text file
            file.write('\n')  # Go to the next line in the text file after writing a line
        file.close()