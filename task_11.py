class Dessert:
    def __init__(self, name=None, calories=None):
        self._name = name
        self._calories = calories

    @property
    def calories(self):
        return self._calories

    @calories.setter
    def calories(self, calories):
        self._calories = calories

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def is_healthy(self):
        if type(self._calories) in (int, float) and self._calories < 200:
            return True
        else:
            return False

    def is_delicious(self):
        return True

