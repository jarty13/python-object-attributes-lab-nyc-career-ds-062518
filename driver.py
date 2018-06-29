class Driver:

    @property
    def first(self):
        return self._first

    @first.setter
    def first (self,first):
        self._first = first

    @first.deleter
    def first(self):
        del self._first

#last name decorator

    @property
    def last(self):
        return self._last

    @last.setter
    def last (self,last):
        self._last= last

    @last.deleter
    def last(self):
        del self._last

# miles_driven decorator
    @property
    def miles_driven(self):
        return self._miles_driven

    @miles_driven.setter
    def miles_driven (self,miles_driven):
        self._miles_driven = miles_driven

    @miles_driven.deleter
    def miles_driven(self):
        del self._miles_driven
    #
# rating decorator
    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self,rating):
        self._rating = rating

    @rating.deleter
    def rating(self):
        del self._rating


    #
    # def rating (self,rating):
    #     return self._rating = rating
    #
    def greet_passenger(self, first, last):
        return "Hello! I'll be your driver today. My name is {} {}".format(self.first, self.last)
