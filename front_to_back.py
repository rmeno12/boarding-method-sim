from calculation import calculate_time
import argparse

def front_to_back(passengers):
    return sorted(passengers, key = lambda x: x[1])

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--verbose", help="increase verbosity of output", 
                         action="store_true")
    parser.add_argument("rows", help="number of rows in the plane")
    parser.add_argument("width", help="number of seats per row in the plane")
    args = parser.parse_args()

    passengers = [(i, j) for i in range(int(args.width)) for j in range(int(args.rows))]
    passengers = front_to_back(passengers)

    print(calculate_time(passengers, args.verbose))
