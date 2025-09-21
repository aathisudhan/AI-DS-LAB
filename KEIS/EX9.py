import math
# STEP 2: Define current and target locations start_x, start_y = 0, 1	# As per output sample target_x, target_y = 0, 1493683 # End far "up" current_x, current_y = start_x, start_y

# STEP 3: Define obstacles (none for this output, easy to extend) obstacles = set() # Example: {(0,5), (1,10)}

# STEP 4: Euclidean distance
def euclidean_distance(x1, y1, x2, y2): return math.sqrt((x2-x1)*2 + (y2-y1)*2)

# STEP 5: Check for obstacles def is_obstacle(x, y):
return (x, y) in obstacles


# STEP 6: Move forward by one step (only "up" for this output) def move_forward(x, y, direction):
# Supports "up", "down", "left", "right" if direction == "up":
return x, y+1
elif direction == "down": return x, y-1
elif direction == "left": return x-1, y
 
elif direction == "right": return x+1, y
else:
return x, y


# STEP 7 & 8: Turn functions (not used for output, but provided) def turn_left(direction):
dirs = ["up", "left", "down", "right"] idx = dirs.index(direction)
return dirs[(idx+1)%4]


def turn_right(direction):
dirs = ["up", "right", "down", "left"] idx = dirs.index(direction)
return dirs[(idx+1)%4]


# STEP 9: Main program logic current_direction = "up"
step = 1
max_steps = target_y - start_y + 1
while (current_x, current_y) != (target_x, target_y): print(f"Current Location:({current_x}, {current_y})") print(f"Direction:{current_direction}") print(f"Steps:{step}\n")
# For this sample, always move 'up'
next_x, next_y = move_forward(current_x, current_y, current_direction) # If no obstacle, move
 
if not is_obstacle(next_x, next_y): current_x, current_y = next_x, next_y step += 1
else:
# If obstacle, break (not shown in output sample) print("Encountered obstacle. Stopping.")
break


# STEP 10: Print final state
print(f"Current Location:({current_x}, {current_y})") print(f"Direction:{current_direction}") print(f"Steps:{step}")

# STEP 11: End program (implicit)
