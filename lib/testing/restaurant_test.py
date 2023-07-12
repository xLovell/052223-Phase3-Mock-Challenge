import pytest

from classes.restaurant import Restaurant
from classes.customer import Customer
from classes.review import Review

class TestRestaurant:
    '''Restaurant in restaurant.py'''

    def test_has_name(self):
        '''has the name passed into __init__'''
        restaurant = Restaurant("Mel's")

        assert restaurant.name == "Mel's"

    def test_validates_name(self):
        '''has name as unchangeable string'''
        with pytest.raises(Exception):
            Restaurant('')

        with pytest.raises(Exception):
            Restaurant(1)

        with pytest.raises(Exception):
            restaurant = Restaurant("Rudy's")
            restaurant.name = "Rudolph's"

    def test_has_many_reviews(self):
        '''restaurant has many reviews'''
        restaurant = Restaurant("Mels")
        customer = Customer('Steve', 'Wayne')
        review_1 = Review(customer, restaurant, 2)
        review_2 = Review(customer, restaurant, 5)

        assert len(restaurant.reviews()) == 2
        assert review_1 in restaurant.reviews()
        assert review_2 in restaurant.reviews()

    def test_has_many_customers(self):
        '''restaurant has many customers'''
        restaurant = Restaurant("Mels")
        customer = Customer('Steve', 'Wayne')
        customer_2 = Customer('Dima', 'Bay')
        Review(customer, restaurant, 2)
        Review(customer_2, restaurant, 5)

        assert len(restaurant.customers()) == 2
        assert customer in restaurant.customers()
        assert customer_2 in restaurant.customers()

    def test_average(self):
        '''average_star_rating() gets average of restaurant's review ratings'''
        restaurant = Restaurant("Mels")
        customer = Customer('Steve', 'Wayne')
        customer_2 = Customer('Dima', 'Bay')
        Review(customer, restaurant, 2)
        Review(customer_2, restaurant, 5)

        assert(restaurant.average_star_rating() == 3.5)
