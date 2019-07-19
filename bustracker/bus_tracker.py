from .base import Base

class BusTracker(Base):
    def __init__(self, agency):
        super(BusTracker, self).__init__(agency)        

    def get_prediction(self, stops):
        if (isinstance(stops, list) and len(stops) > 0):
            return self._request(stops)
        else:
            raise TypeError('stops should be a list of routeTag and stopTag')

