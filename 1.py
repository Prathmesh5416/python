#A Basic Aircraft

# Exercise 1, part 1
print("# Exercise 1, part 1")
aircrafts = {"x": 54, "y": 36}

print(aircrafts["x"])
print(aircrafts["y"])


# Exercise 1, part 2
print("\n# Exercise 1, part 2")
Aircrafts = ["aircraft_1", "aircraft_2", "aircraft_3", "aircraft_4", "aircraft_5"]
coordinates = [17,15, 76,63, 51,83, 73,30, 23,94]

var = 0
for aircraft in Aircrafts:
    print(aircraft, "coordinates are: ", coordinates[var], coordinates[var+1])
    var+= 2

