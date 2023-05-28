class Room:
    def __init__ (self, room_name, capacity, entry_fee):
        self.room_name = room_name
        self.capacity = capacity
        self.entry_fee = entry_fee
        self.guests = []
        self.songs = []

    
    def check_in_guest(self, guest):
        if guest.guest_money >= self.entry_fee and len(self.guests) <= self.capacity:
            guest.guest_money -= self.entry_fee
            self.guests.append(guest)
            
    def check_out_guest(self, guest):
        if guest in self.guests:
            self.guests.remove(guest)
    
    def add_song_to_room(self, song):
        self.songs.append(song)

    