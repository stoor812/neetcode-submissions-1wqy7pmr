class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position,speed))
        cars.sort(key=lambda x:x[0], reverse=True)

        stackedFleets = []

        for i in range(len(cars)):
            t = (target - cars[i][0]) / cars[i][1]
            print(t)

            if len(stackedFleets) == 0:
                stackedFleets.append(t)
            elif t > stackedFleets[-1]:
                stackedFleets.append(t)

        return len(stackedFleets)