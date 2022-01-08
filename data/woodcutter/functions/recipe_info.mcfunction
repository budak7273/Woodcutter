# Clear scoreboard cause
scoreboard players set @s wc_stonecutter_interact 0

# Info on Woodcutter recipes
tellraw @s ["",{"text":"\u2139","color":"blue"},{"text":" Click ","color":"gray"},{"text":"here","underlined":true,"color":"white","clickEvent":{"action":"open_url","value":"http://bit.ly/WoodcutterDatapack"}},{"text":" to see recipes added by Woodcutter","color":"gray"}]