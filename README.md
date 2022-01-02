# Woodcutter

Datapack for Minecraft that allows crafting of wood products at the Stonecutter in a similar fashion to stone products. It has a saw blade on top of it, after all.

All recipes are generated from template files via `generate_json.py`, so you're free to edit them and regenerate as you see fit.

The Stonecutter does not support recipes consuming more than of the input item ([marked as not a bug](https://bugs.mojang.com/browse/MC-151141)), so some recipes such as doors are cheaper than they should be. 

![Example photo with oak planks](https://cdn.discordapp.com/attachments/574825191738179584/575518681463914496/unknown.png)

A number of convenience recipes are provided in addition to the expected "planks to stairs."

None of these resources allow for creating more wood out of nothing, but sometimes they give you a better crafting return than if you had used the crafting table, just like the vanilla stonecutter does to stone variants.

## Features

- Provides shapeless crafting recipe: 2 slabs of the same variant -> 1 plank of that variant

- Provides Stonecutter recipes for all wood variants that do the following:

### Shredding

(bypass crafting steps, same resource output)

- Log -> 4 planks
- Log -> 8 sticks
- Log -> 8 slabs
- Planks -> 2 sticks
- Planks -> 2 slabs

### Rebarking

(allow 1->1 cycling back to woods from stripped variants)

- Stripped Log -> Log (to go back to the start of the options)
- Log -> Wood (normally 4 -> 3 in the crafting grid, this makes it 1 -> 1)

### Stripping/Shaving

(generally performing the axe action, but in the stonecutter)

- Log -> Stripped Log
- Log -> Stripped Wood
- Wood -> Stripped Wood
- Wood -> Stripped Log
- Stripped Wood -> Stripped Log

### Woodworking

(crafting that sometimes gives you better resource cost)

- Log -> Composter
- Planks -> Button
- Planks -> Door
- Planks -> Fence
- Planks -> Fence Gate (yes this could be Log, but I figured this made more sense)
- Planks -> Pressure Plate
- Planks -> Sign
- Planks -> Stairs
- Planks -> Trapdoor
- Planks -> Ladder

### Reclaiming

(get resources back from a recipe, never allowing for potential wood type conversions, though)

- Saplings (including azalea and fungus saplings) -> 2 sticks
- Bow, Fishing Rod, Carrot on a Stick -> 3 sticks
- Warped Fungus on a Stick -> 5 sticks (3 rod + 2 fungus)
- Painting, Item Frame, Glow Item Frame -> 8 sticks
- Armor Stand -> 5 sticks
- Crossbow -> 4 sticks
- Boat -> 5 planks of the respective wood