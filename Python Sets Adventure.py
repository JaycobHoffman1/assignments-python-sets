# Task 1: Flight Route Comparison

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

# Destinations that both airlines fly to
shared_destinations = ", ".join([destination for destination in our_routes.intersection(competitor_routes)])

print(f"Destinations that both airlines fly to: {shared_destinations}")

# Destinations unique to your airline
unique_destinations = ", ".join([destination for destination in our_routes.difference(competitor_routes)])

print(f"Destinations unique to our airlines: {unique_destinations}")

# Whether there are any destinations that neither airline shares
def check_shared_destinations(*destinations):
    return all([destination not in our_routes and destination not in competitor_routes for destination in destinations])

no_shared_destinations = check_shared_destinations("PDX", "LAS", "SFO") # Enter destinations here

print("Neither our routes nor our competitor's routes fly to these destinations."\
if no_shared_destinations else "Our routes and/or our competitor's routes fly to one or more of these destinations.")