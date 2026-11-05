import unittest
from locations import get_locations
from locations import get_buslocations

class TestLocations(unittest.TestCase):
    
    def test_get_locations(self):
        locations = get_locations()
        self.assertIsInstance(locations, dict)

    def test_locations_have_location(self):
        locations = get_locations()
        for location in locations.values():
            self.assertIsInstance(location, dict)
            self.assertIn("lat", location)
            self.assertIn("lng", location)
class TestBusLocations(unittest.TestCase):
    def test_get_buslocations(self):
        buslocations = get_buslocations()
        self.assertIsInstance(buslocations, dict)

    def test_buslocations_have_location(self):
        buslocations = get_buslocations()
        for location in buslocations.values():
            self.assertIsInstance(location, dict)
            self.assertIn("lat", location)
            self.assertIn("lng", location)

    
