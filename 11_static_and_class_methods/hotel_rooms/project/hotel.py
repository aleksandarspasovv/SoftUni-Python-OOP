from project.room import Room


class Hotel:

    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):

        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        try:
            room = next(filter(lambda x: x.number == room_number, self.rooms))

        except StopIteration:
            return

        result = room.take_room(people)

        if not result:
            self.guests += people

    def free_room(self, room_number):
        try:
            room = next(filter(lambda r: r.name == room_number, self.rooms))

        except StopIteration:
            return

        people = room.guests
        result = room.free_room()

        if not result:
            self.guests -= people

    def status(self):
        return f"Hotel {self.name} has {self.guests} total guests\n"\
               f"Free rooms: {', '.join(str(r.number) for r in self.rooms if not r.is_taken)}\n"\
               f"Taken rooms: {', '.join(str(r.number) for r in self.rooms if r.is_taken)}"



hotel = Hotel.from_stars(5)

first_room = Room(1, 3)
second_room = Room(2, 2)
third_room = Room(3, 1)

hotel.add_room(first_room)
hotel.add_room(second_room)
hotel.add_room(third_room)

hotel.take_room(1, 4)
hotel.take_room(1, 2)
hotel.take_room(3, 1)
hotel.take_room(3, 1)

print(hotel.status())
