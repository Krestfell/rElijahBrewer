extends CharacterBody2D

const MAX_SPEED = 210


# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	# Get the movement vector from user input
	var movement_vector = get_movement_vector()
	
	# Normalize the movement vector to get the direction
	var direction = movement_vector.normalized()
	
	# Calculate the velocity using the direction and maximum speed
	velocity = direction * MAX_SPEED
	
	# Move and slide the character
	move_and_slide()


func get_movement_vector():
	# Get the horizontal and vertical movement from user input
	var x_movement = Input.get_action_strength("move_right") - Input.get_action_strength("move_left")
	var y_movement = Input.get_action_strength("move_down") - Input.get_action_strength("move_up")
	
	# Create a vector with the horizontal and vertical movement
	return Vector2(x_movement, y_movement)
