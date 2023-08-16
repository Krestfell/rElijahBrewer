extends Node

const MAX_RANGE = 150

# The scene for the sword ability (should be set in the editor)
@export var sword_ability: PackedScene

# Called when the node enters the scene tree for the first time.
func _ready():
	# Connect the timeout signal of the Timer to the on_timer_timeout function
	$Timer.timeout.connect(on_timer_timeout)

# Function to handle the timer timeout event
func on_timer_timeout():
	# Get the player node from the group "player"
	var player = get_tree().get_first_node_in_group("player") as Node2D
	
	# If the player node doesn't exist, return
	if player == null:
		return
	
	# Get a list of nodes in the "enemy" group
	var enemies = get_tree().get_nodes_in_group("enemy")
	
	# Filter the enemies list to keep only those within the maximum range
	enemies = enemies.filter(func(enemy: Node2D):
		return enemy.global_position.distance_squared_to(player.global_position) < pow(MAX_RANGE, 2)
	)
	
	# If there are no enemies within range, return
	if enemies.size() == 0:
		return
	
	# Sort the enemies list based on their distance to the player
	enemies.sort_custom(func(a: Node2D, b: Node2D):
		var a_distance = a.global_position.distance_squared_to(player.global_position)
		var b_distance = b.global_position.distance_squared_to(player.global_position)
		return a_distance < b_distance
	)
	
	# Instantiate the sword ability scene
	var sword_instance = sword_ability.instantiate() as Node2D
	
	# Add the sword instance as a child of the player's parent
	player.get_parent().add_child(sword_instance)
	
	# Set the sword instance's position near the selected enemy
	sword_instance.global_position = enemies[0].global_position
	sword_instance.global_position += Vector2.RIGHT.rotated(randf_range(0, TAU)) * 4
	
	# Calculate the direction to the enemy
	var enemy_direction = enemies[0].global_position - sword_instance.global_position
	
	# Set the sword instance's rotation to face the enemy
	sword_instance.rotation = enemy_direction.angle()
