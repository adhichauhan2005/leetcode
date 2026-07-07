 cars = []

        for i in range(len(position)):
            time = float(target - position[i]) / speed[i]
            cars.append((position[i], time))

        cars.sort(reverse=True)

        fleets = 0
        slowest_time = 0

        for pos, time in cars:
            if time > slowest_time:
                fleets += 1
                slowest_time = time

        return fleets
