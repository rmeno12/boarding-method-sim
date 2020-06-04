def calculate_time(people):
	print()
	print("Seating", people)
	if len(people) <= 1:
		print("Seating one or fewer people so no wait")
		return 0
	row = people[0][1]
	total_time = 0
	last_seated = people[0]
	print("Currently with", people[0], "at row", row)
	for index, person in enumerate(people[1:]):
		print(person, "can go to row", row - index - 1)
		if person[1] <= row - index - 1 and person[1] != row:
			print("Person and row match!")
			last_seated = person
			total_time += len(people[1:index+1])
			print("Splitting into", people[1:index+1], "and", people[index+1:])
			print("People have waited", total_time, "units in the first section")
			total_time += calculate_time(people[1:index+1]) + calculate_time(people[index+1:])
			break
	else:
		print("No one lined up, moving everyone forward")
		total_time += len(people[1:])
		print("People have waited", total_time, "units this section")
		total_time += calculate_time(people[1:])
	return total_time
