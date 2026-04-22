
csv_content = """Cities,Boston,Buffalo,Chicago,Cleveland,Dallas,Denver,Detroit,El Paso,Houston
Boston,0,457,983,639,1815,1991,702,2358,1886
Buffalo,457,0,536,192,1387,1561,252,1928,1532
Chicago,983,536,0,344,931,1050,279,1439,1092
Cleveland,639,192,344,0,1205,1369,175,1746,1358
Dallas,1815,1387,931,1205,0,801,1167,625,242
Denver,1991,1561,1050,1369,801,0,1310,652,1032
Detroit,702,252,279,175,1167,1301,0,1696,1312
El Paso,2358,1928,1439,1746,625,652,1696,0,756
Houston,1886,1532,1092,1358,242,1032,1312,756,0"""

filename = "09.Project Distances.csv"
with open(filename, "w") as file:
    file.write(csv_content)

distance_matrix = []
with open(filename, "r") as file:
    for line in file:
        # Strip newline and split by comma
        row = line.strip().split(',')
        distance_matrix.append(row)

print(distance_matrix)
print()

from_city = input("Enter From City: ")
to_city = input("Enter To City: ")

cities_in_col = [row[0] for row in distance_matrix]
cities_in_row = distance_matrix[0]

from_index = -1
to_index = -1

if from_city in cities_in_col:
    from_index = cities_in_col.index(from_city)
else:
    print("Invalid From City")

if to_city in cities_in_row:
    to_index = cities_in_row.index(to_city)
else:
    print("Invalid To City")

if from_index != -1 and to_index != -1:
    distance = distance_matrix[from_index][to_index]
    print(f"{from_city} to {to_city} - {distance} miles")
