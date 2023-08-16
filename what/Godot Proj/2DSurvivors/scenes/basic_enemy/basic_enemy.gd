extends CharacterBody2D

# Maximum speed of the enemy
const MAX_SPEED = 85

# Called when the node enters the scene tree for the first time.
func _ready():
	# Connect the area_entered signal of the Area2D to the on_area_entered method
	$Area2D.area_entered.connect(on_area_entered)

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	# Get the direction vector towards the player
	var direction = get_direction_to_player()
	
	# Calculate the velocity using the direction and maximum speed
	velocity = direction * MAX_SPEED
	
	# Move and slide the enemy
	move_and_slide()

# Calculate the direction vector towards the player
func get_direction_to_player():
	# Get the player node from the group "player"
	var player_node = get_tree().get_first_node_in_group("player") as Node2D
	
	# Check if the player node exists
	if player_node != null:
		# Calculate the direction vector towards the player and normalize it
		return (player_node.global_position - global_position).normalized()
	
	# If the player node doesn't exist or is not found, return a zero vector
	return Vector2.ZERO

# Called when the enemy enters an area
func on_area_entered(other_area: Area2D):
	# Destroy the enemy when it enters an area (collision with another object)
	queue_free()
