import pytest

from classes.restaurant import Restaurant
from classes.customer import Customer
from classes.review import Review

class TestCustomer:
    '''Customer in customer.py'''

    def test_has_name(self):
        '''has the first name and last name passed into __init__'''
        customer = Customer('Steve', 'Wayne')
        assert customer.first_name == "Steve"
        assert customer.last_name == "Wayne"

    def test_validates_name(self):
        '''has first and last names as strings between 1 and 25 characters, inclusive'''
        with pytest.raises(Exception):
            Customer('', 'Lastname')

        with pytest.raises(Exception):
            Customer('Firstname', '')

        with pytest.raises(Exception):
            Customer('F' * 26, 'Lastname')

        with pytest.raises(Exception):
            Customer('Firstname', 'L' * 26)

        with pytest.raises(Exception):
            Customer(1, 'Lastname')

        with pytest.raises(Exception):
            Customer('Firstname', 2)

    def test_has_many_reviews(self):
        '''customer has many reviews'''
        restaurant = Restaurant("Mels")
        customer = Customer('Steve', 'Wayne')
        review_1 = Review(customer, restaurant, 2)
        review_2 = Review(customer, restaurant, 5)

        assert len(customer.reviews()) == 2
        assert review_1 in customer.reviews()
        assert review_2 in customer.reviews()

    def test_has_many_restaurants(self):
        '''customer has many restaurants.'''
        restaurant = Restaurant("Mels")
        restaurant_2 = Restaurant("Chipotle")

        customer = Customer('Steve', 'Wayne')
        Review(customer, restaurant, 2)
        Review(customer, restaurant_2, 5)

        assert restaurant in customer.restaurants()
        assert restaurant_2 in customer.restaurants()

    def test_get_number_of_reviews(self):
        '''test get_number_of_reviews()'''
        restaurant = Restaurant("Mels")
        customer = Customer('Steve', 'Wayne')
        Review(customer, restaurant, 2)
        Review(customer, restaurant, 5)

        assert customer.num_reviews() == 2
