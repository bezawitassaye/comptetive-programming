from collections import defaultdict

class UndergroundSystem:
    def __init__(self):
        # Dictionary to store the check-in information
        self.check_ins = {}
        # Dictionary to store the total travel time and count between stations
        self.travel_times = defaultdict(lambda: [0, 0])

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        # Store the check-in information for the customer
        self.check_ins[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        # Retrieve the check-in information for the customer
        start_station, start_time = self.check_ins[id]
        # Calculate the travel time
        travel_time = t - start_time
        # Update the total travel time and count for the station pair
        self.travel_times[(start_station, stationName)][0] += travel_time
        self.travel_times[(start_station, stationName)][1] += 1
        # Remove the check-in information
        del self.check_ins[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        # Retrieve the total travel time and count for the station pair
        total_time, count = self.travel_times[(startStation, endStation)]
        # Calculate the average travel time
        average_time = total_time / count
        return average_time