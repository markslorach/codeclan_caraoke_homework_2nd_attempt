import unittest

from classes.room import Room
from classes.song import Song
from classes.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        
        self.guest_1 = Guest("Mark", 100, "The Bitter End")
        self.guest_2 = Guest("Ellen", 100, "Late Night Talking")
        

    def test_guest_has_name(self):
        self.assertEqual("Mark", self.guest_1.guest_name)

