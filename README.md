# Woodcutter

Datapack for Minecraft that allows crafting of wood products at the Stonecutter in a similar fashion to stone products. It has a saw blade on top of it, after all.

All recipes are generated from template files via `generate_json.py`, so you're free to edit them and regenerate as you see fit.

The Stonecutter does not support recipes consuming more than of the input item ([marked as not a bug](https://bugs.mojang.com/browse/MC-151141)), so some recipes such as doors are cheaper than they should be.

![Example photo with oak planks](https://i.imgur.com/FkdLxLH.png)

A number of convenience recipes are provided in addition to the expected "planks to stairs."

None of these resources allow for creating more wood out of nothing, but sometimes they give you a better crafting return than if you had used the crafting table, just like the vanilla stonecutter does to stone variants.

## Features

- Shapeless crafting recipe: 2 Slabs of the same variant -> 1 Plank of that variant
  - It works in any item placement, but if the slab already has a "stacked vertically" shaped crafting recipe (ex. Bamboo slabs), that takes precedence, so don't stack them vertically in the case.
- Stonecutter recipes for all wood variants described in detail below (including correctly priced Bamboo)
- Stonecutter recipes for recycling some items described in detail below

**Most common recipes**:

Be sure to read below these screenshots for the full list of all supported recipes.

![Logs](https://i.imgur.com/M7qohQB.png)
![Wood](https://i.imgur.com/YcExopl.png)
![Planks](https://i.imgur.com/k0fvJ9j.png)
![Stripped](https://i.imgur.com/ucxj7Z7.png)

<!-- For these screenshots, include all the white on the top, 2 pixels out inclusive from the right, same for bottom, stop just before white on the left -->

### Woodworking

(sometimes gives you a better resource cost)

- Log -> Composter
- Planks -> Button
- Planks -> Door
- Planks -> Fence
- Planks -> Fence Gate (yes this could be Log, but I figured this made more sense given a fence is one plank too)
- Planks -> Pressure Plate
- Planks -> Sign
- Planks -> Hanging Sign
- Planks -> Stairs
- Planks -> Trapdoor
- Planks -> Ladder
- Sign -> Hanging Sign
- Hanging Sign -> Sign
- Converting Bamboo components to and from the Mosaic variant

### Stripping/Shaving

(generally performing the axe interact action, but in the stonecutter)

- Log -> Stripped Log
- Log -> Stripped Wood
- Wood -> Stripped Wood
- Wood -> Stripped Log
- Stripped Wood -> Stripped Log

### Shredding

(bypass crafting steps, same resource output)

- Log -> 4 Planks
- Log -> 8 Sticks
- Log -> 8 Slabs
- Planks -> 2 Sticks
- Planks -> 2 Slabs
- Slab -> 1 Stick

### Rebarking

(allow 1 -> 1 cycling back to woods from stripped variants)

- Log -> Wood (normally 4 -> 3 in the crafting grid, this makes it 1 -> 1)
- Stripped Log -> Log (to go back to the start of the options)

### Reclaiming

(get some resources back by taking something apart)

- Saplings (including azalea and fungus saplings) -> 2 Sticks
- Bamboo Block -> 9 bamboo
- Bow, Fishing Rod, Carrot on a Stick -> 3 Sticks
- Warped Fungus on a Stick -> 5 Sticks (3 rod + 2 fungus)
- Painting, Item Frame, Glow Item Frame -> 8 Sticks
- Armor Stand -> 5 Sticks
- Crossbow -> 4 Sticks
- Boat -> 5 Planks of the respective wood
- Chest Boat -> 13 Planks of the respective wood
- Mangrove Roots -> 4 Sticks
- Muddy Mangrove Roots -> 4 Sticks
- Muddy Mangrove Roots -> 1 Mud
- Stairs -> 1 Stick
- Ladder -> 1 Stick
- Jukebox -> 1 Diamond
- Note Block -> 1 Redstone
- Bookshelf -> 3 Books
- Beehive -> 3 Honeycomb

## Commands (operators only)

- `/function woodcutter:reinstall`
  - Convenience command. Reinstalls the pack from scratch and reloads all datapacks.
    Has the potential to fix bugs you encounter with the datapack.
- `/function woodcutter:uninstall`
  - Run before uninstalling the pack - cleans up all scoreboard values and such.
- `/function woodcutter:recipe_info`
  - Display the informational message players see when they visit a Stonecutter, has a link to this page.
- `/scoreboard players set wc_checker_interval wc_options <value>`
  - Set the update interval to a number of ticks. Default is 30. You shouldn't have to change this.
