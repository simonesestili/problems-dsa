class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        departs, arrivs = defaultdict(list), defaultdict(list)
        first, last = 9e9, -9e9
        for trip in trips:
            count, depart, arriv = trip
            departs[depart].append(count)
            arrivs[arriv].append(count)
            first, last = min(first, depart), max(last, arriv) 
        peopleInCar = 0

        for i in range(first, last + 1):
            if i in arrivs:
                for people in arrivs[i]:
                    peopleInCar -= people
            if i in departs:
                for people in departs[i]:
                    peopleInCar += people
            if peopleInCar > capacity:
                return False
        return True    
