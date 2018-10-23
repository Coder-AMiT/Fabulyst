import requests
import sys

provider_url = 'http://svc.metrotransit.org/nextrip/providers?format=json'
routes_url = 'http://svc.metrotransit.org/NexTrip/Routes?format=json'
stop_id_url = 'http://svc.metrotransit.org/NexTrip/Stops/{ROUTE}/{DIRECTION}?format=json'
get_timepoint_url = 'http://svc.metrotransit.org/NexTrip/{ROUTE}/{DIRECTION}/{STOP}?format=json'
directions = {'south': 1, 'east': 2, 'west': 3, 'north': 4}


class MetroTransit(object):
    def __init__(self):
        self.routes = self.get_routes()
        
    def get_time_point(self, route, stop, direction):
        route_id = self.get_route_id(route)
        direction_id = self.get_direction_id(direction)
        if not (route_id and direction_id):
            return None
        stop_id = self.get_stop_id(stop, route_id, direction_id)
        if not stop_id:
            return None
        r = requests.get(get_timepoint_url.format(ROUTE=route_id, DIRECTION=direction_id, STOP=stop_id))
        data = r.json()
        if not data:
            return None
        return data[0]['DepartureText']

    def get_route_id(self, route_name):
        for route_disc, values in self.routes.items():
            if route_name.lower() in route_disc:
                return values[1]
        return None

    @staticmethod
    def get_direction_id(direction):
        return directions.get(direction.lower())

    @staticmethod
    def get_stop_id(stop, route_id, direction_id):
        r = requests.get(stop_id_url.format(ROUTE=route_id, DIRECTION=direction_id))
        for data in r.json():
            if stop.lower() in data['Text'].lower():
                return data['Value']
        return None

    @staticmethod
    def get_providers():
        r = requests.get(provider_url)
        providers = {data['Text']: data['Value'] for data in r.json()}
        return providers

    @staticmethod
    def get_routes():
        r = requests.get(routes_url)
        routes = {data['Description'].lower(): [data['ProviderID'], data['Route']] for data in r.json()}
        return routes


if __name__ == '__main__':
    args = sys.argv
    if len(args) != 4:
        raise Exception('Please pass exactly three params ')
    route = args[1]
    stop = args[2]
    direction = args[3]
    Metro_object = MetroTransit()
    next_trip_time = Metro_object.get_time_point(route=route, stop=stop, direction=direction)
    print(next_trip_time)
