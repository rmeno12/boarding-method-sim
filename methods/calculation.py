def calculate_time(passengers, verbose=False):
    if verbose: print()
    if verbose: print("Seating", passengers)
    if len(passengers) <= 1:
        if verbose: print("Seating one or fewer passengers so no wait")
        return 0
    row = passengers[0][1]
    total_time = 0
    last_seated = passengers[0]
    if verbose: print("Currently with", passengers[0], "at row", row)
    for index, passenger in enumerate(passengers[1:]):
        if verbose: print(passenger, "can go to row", row - index - 1)
        if passenger[1] <= row - index - 1 and passenger[1] != row:
            if verbose: print("Person and row match!")
            last_seated = passenger
            total_time += len(passengers[1:index+1])
            if verbose: print("Splitting into", passengers[1:index+1], 
                              "and", passengers[index+1:])
            if verbose: print("People have waited", total_time, 
                              "units in the first section")
            total_time += (calculate_time(passengers[1:index+1], verbose) 
                           + calculate_time(passengers[index+1:], verbose))
            break
    else:
        if verbose: print("No one lined up, moving everyone forward")
        total_time += len(passengers[1:])
        if verbose: print("People have waited", total_time, "units this section")
        total_time += calculate_time(passengers[1:], verbose)
    return total_time
