from django.test import TestCase
from .models import Location

# Create your tests here.
class Location(TestCase):

    #set up method
    def setUp(self):
        self.nairobi= Location(location='nairobi')

    def test_instance(self):
        self.assertTrue(isinstance(self.nairobi,Location))

    def tearDown(self):
        Location.objects.all()

    def test_save_method(self):
        self.nairobi.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(location)>0)

