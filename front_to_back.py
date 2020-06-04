from .. import calulation

def front_to_back(passengers):
    return sorted(passengers, key = lambda x: x[1])

passengers = [(i, j) for i in range(1) for j in range(10)]
passengers = front_to_back(passengers)

print(calculate_time(passengers, True))
