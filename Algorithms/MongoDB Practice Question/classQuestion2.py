# Practice Problem: Hotel Room Reservation Management System

# A hotel chain needs a system to manage room reservations. You have been tasked with developing some features for this backend system to streamline the reservation process.

# Background Information:

# Hotels have different types of rooms, such as Single, Double, and Suite.
# Each room has a unique number within each hotel.
# Guests can book rooms of a specific type in a hotel.
# Each reservation is associated with a unique identifier, the guest's name, and the room number.
# Please build the room reservation system with the following methods:

# addRoom(room: Room) that adds a new room to the system.
# getAvailableRooms(room_type: str) -> List[Room] that accepts the type of room (string) and returns a list of available rooms of that type, sorted by room number.
# bookRoom(room_number: int, guest_name: str) -> str that reserves the room if it is available, or prints a message indicating that the room is not available.
# cancelBooking(reservation_id: int) -> str that cancels an existing reservation if the correct reservation ID is provided.

from datetime import datetime
from collections import defaultdict
import heapq
class Room:
    def __init__(self, id, hotel, type):
        self.id = id
        self.hotel = hotel
        self.type = type
        self.availability = True
    
    def __gt__(self, other):
        return self.id > other.id

class Reservation:
    def __init__(self, id, room, guestName):
        self.id = id
        self.room = room
        self.guestName = guestName
        self.isDone = False
        self.date = datetime.now().strftime("%Y-%m-%d")

class HotelManagement:
    def __init__(self):
        self.hashMapReservations = {}
        self.hashMapHeap = defaultdict(list)
        self.reservations = []
        self.count = 0
    
    def addRoom(self, hotel, room):
        heapq.heappush(self.hashMapHeap[hotel], (room))
        print("Room added successfully")
        
    def getAvailability(self, room_type, hotel):
        copyHeap = self.hashMapHeap[hotel][:]
        availability = []
        while copyHeap:
            room = heapq.heappop(copyHeap)
            if room.availability and room.type == room_type:
                availability.append(room.id)
        return availability

    def bookRoom(self, id, hotel, guestName):
        roomFound = False
        for room in self.hashMapHeap[hotel]:
            if id == room.id and room.availability:
                room.availability = False
                id = "reservation" + str(self.count)
                reservation = Reservation(id, room, guestName)
                self.reservations.append((reservation))
                self.hashMapReservations[id] = reservation
                print("Reservation Successfull with id: ", id)
                roomFound = True
                break
        
        if not roomFound:
            print("Room not Found")
    
    def cancelBooking(self, id):
        if id in self.hashMapReservations:
            currentRoom = self.hashMapReservations[id]
            currentRoom.isDone = True
            currentRoom.room.availability = True
            print("Booking was Canceled Successfully")
        else:
            print("Reservation id not found")
    
    def viewReservations(self):
        for reservation in self.reservations:
            status = "Active" if reservation.isDone == False else "Completed"
            print("Reservation with ID: ", reservation.id, ", guestName: ", reservation.guestName, ", and room: ", reservation.room.id, " is currently: ", status)

if __name__ == '__main__':
    room1 = Room(101, 'Hotel A', 'Single')
    room2 = Room(102, 'Hotel A', 'Double')
    room3 = Room(103, 'Hotel A', 'Suite')
    room4 = Room(104, 'Hotel A', 'Single')
    room5 = Room(103, 'Hotel A', 'Single')
    room6 = Room(201, 'Hotel B', 'Double')

    hotelSystem = HotelManagement()

    hotelSystem.addRoom('Hotel A', room1)
    hotelSystem.addRoom('Hotel A', room2)
    hotelSystem.addRoom('Hotel A', room3)
    hotelSystem.addRoom('Hotel A', room4)
    hotelSystem.addRoom('Hotel B', room6)
    hotelSystem.addRoom('Hotel A', room5)

    print("Available Single Rooms in Hotel A:", hotelSystem.getAvailability('Single', 'Hotel A'))


    hotelSystem.bookRoom(101, 'Hotel A', 'John Doe')


    hotelSystem.bookRoom(101, 'Hotel A', 'Jane Smith')


    print("Available Single Rooms in Hotel A after booking:", hotelSystem.getAvailability('Single', 'Hotel A'))
    hotelSystem.viewReservations()

    hotelSystem.cancelBooking('reservation0')
    
    hotelSystem.viewReservations()
    print("Available Single Rooms in Hotel A after canceling:", hotelSystem.getAvailability('Single', 'Hotel A'))
