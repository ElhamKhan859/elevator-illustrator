import time

def visualize_elevators(floors, current_position, destination_position):
    while current_position != destination_position:     
        building_structure = "--- " * floors  
        building_structure = building_structure.split(" ")
        building_structure[current_position] = "ELV"
        building_structure = " ".join(building_structure)
        print(building_structure)
        time.sleep(1)
        if current_position < destination_position:
            current_position+=1
        else:
            current_position-=1
    building_structure = "--- " * floors 
    building_structure = building_structure.split(" ")
    building_structure[current_position] = "ELV"
    building_structure = " ".join(building_structure)
    print(building_structure)

floors = 10

current_position_elevator_1 = 0
current_position_elevator_2 = 0

user_floor = int(input("Enter your desired floor: "))

while True:
    distance_elevator_1_with_user = abs(user_floor - current_position_elevator_1)
    distance_elevator_2_with_user = abs(user_floor - current_position_elevator_2)

    if distance_elevator_1_with_user > distance_elevator_2_with_user:
        visualize_elevators(floors, current_position_elevator_1, user_floor)
    else:
        current_position_elevator_1 = user_floor
        visualize_elevators(floors, current_position_elevator_2, user_floor)

    user_floor = int(input("Enter your desired floor: "))
    if user_floor == -1:
        break


        



    