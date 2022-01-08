# reset the interval counter back to zero
scoreboard players set wc_timer_player wc_internals 0

# run the checker for having opened a woodcutter
execute as @a[scores={wc_stonecutter_interact=1..}] if score @s wc_stonecutter_interact matches 1.. run function woodcutter:recipe_info