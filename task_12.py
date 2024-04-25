from task_11 import Dessert
class JellyBean(Dessert):
    def __init__(self, name=None, calories=None, flavor=None):
        super(JellyBean, self).__init__(name, calories)
        self._flavor = flavor
 
    @property
    def flavor(self):
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        self._flavor = flavor

    def is_delicious(self):
        return self._flavor != "black licorice"

