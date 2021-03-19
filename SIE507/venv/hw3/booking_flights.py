from Airplane import Airplane
from Bookings import BookingMgr

# Initialize a plane, using rows and seats or a seats.txt file
myprivateplane = Airplane(filename='seats.txt')
myBookingMgr = BookingMgr(myprivateplane, booking_file_name='flight_bookings.csv')
myBookingMgr.UserMenu()
