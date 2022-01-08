# Woodcutter

Datapack for Minecraft that allows crafting of wood products at the Stonecutter in a similar fashion to stone products. It has a saw blade on top of it, after all.

All recipes are generated from template files via `generate_json.py`, so you're free to edit them and regenerate as you see fit.

The Stonecutter does not support recipes consuming more than of the input item ([marked as not a bug](https://bugs.mojang.com/browse/MC-151141)), so some recipes such as doors are cheaper than they should be. 

![Example photo with oak planks](https://i.imgur.com/FkdLxLH.png)

A number of convenience recipes are provided in addition to the expected "planks to stairs."

None of these resources allow for creating more wood out of nothing, but sometimes they give you a better crafting return than if you had used the crafting table, just like the vanilla stonecutter does to stone variants.

## Features

- Provides shapeless crafting recipe: 2 slabs of the same variant -> 1 plank of that variant
- Provides Stonecutter recipes for all wood variants that do the following:

**Most common recipes**:

See below for the full list of all supported recipes

![Logs](https://i.imgur.com/M7qohQB.png)
![Wood](https://i.imgur.com/YcExopl.png)
![Planks](https://i.imgur.com/k0fvJ9j.png)
![Stripped](https://i.imgur.com/ucxj7Z7.png)

<!-- For these screenshots, include all the white on the top, 2 pixels out inclusive from the right, same for bottom, stop just before white on the left -->

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

### Stripping/Shaving

(generally performing the axe interact action, but in the stonecutter)

- Log -> Stripped Log
- Log -> Stripped Wood
- Wood -> Stripped Wood
- Wood -> Stripped Log
- Stripped Wood -> Stripped Log

### Shredding

(bypass crafting steps, same resource output)

- Log -> 4 planks
- Log -> 8 sticks
- Log -> 8 slabs
- Planks -> 2 sticks
- Planks -> 2 slabs
- Slab -> 1 stick

### Rebarking

(allow 1 -> 1 cycling back to woods from stripped variants)

- Stripped Log -> Log (to go back to the start of the options)
- Log -> Wood (normally 4 -> 3 in the crafting grid, this makes it 1 -> 1)

### Reclaiming

(get resources back from a recipe, never allowing for potential wood type conversions, though)

- Saplings (including azalea and fungus saplings) -> 2 sticks
- Bow, Fishing Rod, Carrot on a Stick -> 3 sticks
- Warped Fungus on a Stick -> 5 sticks (3 rod + 2 fungus)
- Painting, Item Frame, Glow Item Frame -> 8 sticks
- Armor Stand -> 5 sticks
- Crossbow -> 4 sticks
- Boat -> 5 planks of the respective wood

## Commands (operators only)

* `/function woodcutter:reinstall`
  * Convenience command. Reinstalls the pack from scratch and reloads all datapacks.
    Has the potential to fix bugs you encounter with the datapack.
* `/function woodcutter:uninstall`
  * Run before uninstalling the pack - cleans up all scoreboard values and such.
    Does not delete, nor affect the functionality of, existing potions.
* `/function woodcutter:advancement_trigger`
  * Display the informational message players see when they visit a Stonecutter, has a link to this page.
* `/scoreboard players set wc_checker_interval wc_options <value>`
  * Set the update interval to a number of ticks. Default is 30. You shouldn't have to change this.