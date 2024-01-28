# reset the interval counter back to zero
scoreboard players set wc_timer_player wc_internals 0

# enable the trigger objective so people can opt out of the recipe reminder message
scoreboard players enable @a wc_disable_reminder_message

# run the checker for having opened a woodcutter
execute as @a[scores={wc_stonecutter_interact=1.., wc_disable_reminder_message=0}] run function woodcutter:recipe_info

# run the checker for beehive easter egg
execute as @a[scores={wc_easteregg_bee=1..}] run function woodcutter:easteregg_bee
