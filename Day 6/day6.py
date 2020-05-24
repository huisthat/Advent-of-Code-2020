
with open("day6.txt") as file:
    data = file.read().splitlines()
    
# find the last element of the line
# have a list of the planet in a line, 
# have a dictionary of each planet, with the number of direct and indirect orbits it has

last_planet = []

for orbit in data:
    temp_last = orbit[4:]
    count = 0
    for i in data:
        if temp_last == i[:3]:
            break

        else:
            count += 1
        
    if count == 1656:
        last_planet.append(temp_last)

# print(last_planet)

def find_line(planet):
    line = [planet]
    count = 0
    while count != 1656:
        count = 0
        for orbit in data:
            if planet == orbit[4:]:
                line.insert(0, orbit[:3])
                break

            else:
                count += 1
        planet = orbit[:3]
    return line
        

for planet in last_planet: 
    if planet == 'YOU':
        initial_position = find_line(planet)
    
    elif planet == 'SAN':
        final_position = find_line(planet)

connecting_planet = final_position[0]
for i in initial_position:
    for j in final_position:
        if i == j:
            temp_connecting_planet = j
        
        if final_position.index(temp_connecting_planet) > final_position.index(connecting_planet):
            connecting_planet = temp_connecting_planet

min_orbit_trans = (initial_position.index('YOU') - initial_position.index(connecting_planet)) + (final_position.index('SAN') - final_position.index(connecting_planet)) - 2
print(min_orbit_trans)




# print(last_planet)

# for line in last_planet:
#     for planet in line:
#             count_planet[planet] = line.index(planet) 


# count_planet = {}
# print(count_planet)

# total_count = 0
# for k, v in count_planet.items():
#     total_count += v

# print(total_count)

