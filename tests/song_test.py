import unittest

from classes.room import Room
from classes.song import Song
from classes.guest import Guest

class TestSong(unittest.TestCase):
    def setUp(self):
       
       self.song_1 = Song("The Bitter End", "Placebo")
       self.song_2 = Song("Inner City Life", "Goldie")
       self.song_3 = Song("Late Night Talking", "Harry Styles")

    
    def test_song_has_title(self):
        self.assertEqual("The Bitter End", self.song_1.title)

    def test_song_has_artist(self):
        self.assertEqual("Goldie", self.song_2.artist)