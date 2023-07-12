class Customer:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, first_name):
        if isinstance(first_name, str) and 1 <= len(first_name) <= 25:
            self._first_name = first_name
        else:
            raise Exception
        
    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, last_name):
        if isinstance(last_name, str) and 1 <= len(last_name) <= 25:
            self._last_name = last_name
        else:
            raise Exception
        
    def reviews(self):
        from classes.review import Review
        return [review for review in Review.all if review.customer == self]
    
    def restaurants(self):
        from classes.review import Review
        return [review.restaurant for review in Review.all if review.customer == self]

    def num_reviews(self):
        from classes.review import Review
        return len([review for review in Review.all if review.customer == self])
