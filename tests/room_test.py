import unittest

from classes.room import Room
from classes.song import Song
from classes.guest import Guest

class TestRoom(unittest.TestCase):
    def setUp(self):
        
        self.room = Room("The Boom Boom Room", 10, 20)

        self.guest_1 = Guest("Mark", 100, "The Bitter End")
        self.guest_2 = Guest("Ellen", 100, "Late Night Talking")

        self.song_1 = Song("The Bitter End", "Placebo")
        self.song_2 = Song("Inner City Life", "Goldie")
        self.song_3 = Song("Late Night Talking", "Harry Styles")

    def test_room_has_name(self):
        self.assertEqual("The Boom Boom Room", self.room.room_name)

    def test_room_has_capacity(self):
        self.assertEqual(10, self.room.capacity)

    def test_room_has_entry_fee(self):
        self.assertEqual(20, self.room.entry_fee)

    def test_check_in_guest(self):
        self.room.check_in_guest(self.guest_2)
        self.assertEqual([self.guest_2], self.room.guests)

    
    # def test_check_out_guest(self):
    #     pass
    
    
    
    def test_add_song_to_room(self):
        self.room.add_song_to_room(self.song_2)
        self.assertEqual([self.song_2], self.room.songs)
