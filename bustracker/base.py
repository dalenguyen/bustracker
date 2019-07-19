from requests import get

class Base(object):
    def __init__(self, agency):        
        self.agency = agency

    def _prepare_request(self, stops):
        """
        Basic NextBus Request URL
        """

        stopsParams = ''
        for stop in stops:            
            stopsParams += '&stops=' + str(stop['routeTag']) + '|' + str(stop['stopTag'])

        print(stopsParams)
        url = 'http://webservices.nextbus.com/service/publicJSONFeed?command=predictionsForMultiStops&a={agency}&{stops}'.format(
            agency = self.agency,
            stops = stopsParams
        )        

        return url

    def _request(self, stops):
        url = self._prepare_request(stops)
        data = get(url)

        return data.json()