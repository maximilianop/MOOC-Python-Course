# tee ratkaisu tänne
# Write your solution here
import math

def get_station_data(filename: str) -> dict:
    stations = {}
    with open(filename) as file:
        for line in file:
            line = line.strip().split(';')
            if line[0] == 'Longitude':
                continue
            stations[line[3]] = (float(line[0]), float(line[1]))
    return stations

def distance(stations: dict, station1: str, station2: str) -> float:
    x_km = (stations[station1][0] - stations[station2][0]) * 55.26
    y_km = (stations[station1][1] - stations[station2][1]) * 111.2
    return math.sqrt(x_km**2 + y_km**2)

def greatest_distance(stations: dict) -> tuple:
    maximum = ('station1', 'station2', 0)
    station_names = []
    for station in stations:
        station_names.append(station)
    i = 0
    while i in range(0, len(station_names)-1):
        station = station_names[i]
        j = i + 1
        while j < len(station_names):
            dist = distance(stations, station, station_names[j])
            if dist > maximum[2]:
                maximum = (station, station_names[j], dist)
            j += 1
        i += 1
    return maximum
        

if __name__ == "__main__": 
    stations = get_station_data('stations1.csv')
    print(distance(stations, 'Designmuseo', 'Hietalahdentori'))
    dist = greatest_distance(stations)
    print(dist)
