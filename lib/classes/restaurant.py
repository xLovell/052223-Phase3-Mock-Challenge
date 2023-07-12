class Restaurant:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) and not hasattr(self, "name"):
            self._name = name
        else:
            raise Exception
        
    def reviews(self):
        from classes.review import Review
        return [review for review in Review.all if review.restaurant == self]
    
    def customers(self):
        from classes.review import Review
        return [review.customer for review in Review.all if review.restaurant == self]

    def average_star_rating(self):
        from classes.review import Review
        r = [review.rating for review in Review.all if review.restaurant == self]
        return sum(r) / len(r)