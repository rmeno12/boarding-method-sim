from calculation import calculate_time
import argparse
import random

def window_middle_aisle(passengers, width):
    if width == 1 or width == 2:
        random.shuffle(passengers)
        return passengers
    
    windows = [person for person in passengers if person[0] == 0 or person[0] == width - 1]
    middles = []
    aisles = []

    if width % 2 == 0:
        aisles = [person for person in passengers if (person[0] == width / 2 - 1 or person[0] == width / 2) and person not in windows]
        middles = [person for person in passengers if person not in aisles and person not in windows]
    else:
        aisles = [person for person in passengers if (person[0] == width // 2 or person[0] == width // 2 + 1) and person not in windows]
        middles = [person for person in passengers if person not in aisles and person not in windows]
    
    random.shuffle(windows)
    random.shuffle(middles)
    random.shuffle(aisles)

    return windows + middles + aisles


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--verbose", help="increase verbosity of output", 
                         action="store_true")
    parser.add_argument("rows", help="number of rows in the plane")
    parser.add_argument("width", help="number of seats per row in the plane")
    args = parser.parse_args()

    passengers = [(i, j) for i in range(int(args.width)) for j in range(int(args.rows))]
    passengers = window_middle_aisle(passengers, int(args.width))

    print(calculate_time(passengers, args.verbose))
