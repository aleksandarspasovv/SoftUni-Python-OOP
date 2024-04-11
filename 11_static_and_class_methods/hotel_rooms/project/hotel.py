from hotel_rooms.project.room import Room


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
    def free_room(self, room_number):
        try:
            room = next(filter(lambda r: r.name == room_number, self.rooms))

        except StopIteration:
            return 