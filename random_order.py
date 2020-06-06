from calculation import calculate_time
import argparse
import random

def random_order(passengers):
    random.shuffle(passengers)
    return passengers

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--verbose", help="increase verbosity of output", 
                         action="store_true")
    parser.add_argument("rows", help="number of rows in the plane")
    parser.add_argument("width", help="number of seats per row in the plane")
    args = parser.parse_args()

    passengers = [(i, j) for i in range(int(args.width)) for j in range(int(args.rows))]
    passengers = random_order(passengers)

    print(calculate_time(passengers, args.verbose))
