from search import UndirectedGraph, GraphProblem, best_first_graph_search, astar_search
from items import items
from map import map_greedy, map_astar

# Get input from user
print("================================================================================================================================")
print("                                               ████▓▒░▓▒░⡷⠂PickNShip⠐⢾░▒▓░▒▓████                                               ")
print("================================================================================================================================")
print("Welcome to the freightage service!")
print("Please enter the following information:")
truck_capacity = int(input("Enter truck capacity (in kg): "))
start_location = input("Enter start location: ")
end_location = input("Enter end location: ")
est_time = input("Enter estimated time (e.g. '01-12-23'): ")
print("generate....")

# Find the shortest route using greedy algorithm
problem_greedy = GraphProblem(start_location, end_location, map_greedy)
route_greedy = [node.state for node in best_first_graph_search(problem_greedy, lambda node: node.path_cost).path()]

# Find the shortest route using A* algorithm
problem_astar = GraphProblem(start_location, end_location, map_astar)
route_astar = [node.state for node in astar_search(problem_astar).path()]

# Sort items based on location and estimated time
sorted_items = sorted(items, key=lambda x: (x['location'] == end_location, x['est_time'], x['weight']))

# Select items that can fit in the truck using greedy algorithm
total_weight = 0
selected_items = []
for item in sorted_items:
    if item['location'] in route_greedy and item['est_time'] == est_time:
        if total_weight + item['weight'] <= truck_capacity:
            selected_items.append(item)
            total_weight += item['weight']

# Print results
print("Results:")
print(f"Truck capacity: {truck_capacity} kg")
print(f"Estimated time: {est_time}")
print(f"Route astar: {route_astar}")
print(f"Route greedy: {route_greedy}")
print(f"Selected items ({len(selected_items)} items, {total_weight} kg):")
for item in selected_items:
    print(f"- {item['name']} ({item['location']}) : {item['weight']} kg")
print(f"Total weight: {total_weight} kg")
print("Thank you for using our service!")
print("================================================================================================================================")

