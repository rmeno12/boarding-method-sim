from calculation import calculate_time
import argparse

def back_to_front(passengers):
    return list(reversed(sorted(passengers, key = lambda x: x[1])))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--verbose", help="increase verbosity of output", 
                         action="store_true")
    args = parser.parse_args()

    passengers = [(i, j) for i in range(2) for j in range(50)]
    passengers = back_to_front(passengers)

    print(calculate_time(passengers, args.verbose))
