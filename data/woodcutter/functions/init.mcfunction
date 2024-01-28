# Print load message
tellraw @a ["",{"text":"\u2714","color":"dark_green"},{"text":" Woodcutter datapack loaded.\nVisit a Stonecutter and get sawing!"},{"text":"\nMore info "},{"text":"here","underlined":true,"clickEvent":{"action":"open_url","value":"http://bit.ly/WoodcutterDatapack"}}]

# Set up scoreboard values for tracking interact with Stonecutters
scoreboard objectives add wc_stonecutter_interact minecraft.custom:minecraft.interact_with_stonecutter

# Set up scoreboard values for timed functions and internal settings
scoreboard objectives add wc_internals dummy "Woodcutter Internal"

# Set up per-player scoreboard for tracking if they want to see the chat message when opening a stonecutter
scoreboard objectives add wc_disable_reminder_message trigger "Woodcutter Disable Recipes Message"

# Set up options scoreboard
scoreboard objectives add wc_options dummy "Woodcutter Datapack"
scoreboard objectives modify wc_options displayname {"text":"Woodcutter Datapack","bold":true,"color":"yellow"}

# Bee easter egg
scoreboard objectives add wc_easteregg_bee minecraft.crafted:minecraft.honeycomb "Woodcutter Bee Easter Egg"

# init effect checking player interval to every 30 ticks (1.5 second)
scoreboard players set wc_checker_interval wc_options 30
