from enum import Enum
import os



TEMPLATES_DEFAULT_SUBFOLDER = "woodworking"
subfolder_filename_keywords = [
    "shaving", "stripping", "shredding", "rebarking", "reclaiming"
]

TEMPLATES_DIR_RELATIVE = "\\templates"
OUTPUT_DIR_RELATIVE = "\\data\\woodcutter\\recipes"
#ADVANCEMENT_DIR_RELATIVE = "\\data\\woodcutter\\advancements\\recipes\\misc"


WORD_TO_REPLACE_PRIMARY = "WOOD"
WORD_TO_REPLACE_LOG = "WOOD_log"
WORD_TO_REPLACE_STRIPPED_WOOD = "WOOD_wood"
WORD_TO_REPLACE_SAPLING = "WOOD_sapling"
WORD_TO_REPLACE_BOAT = "WOOD_boat"

class WoodType():

    def __init__(self, name: str, template_overrides: list[tuple[str, str]] = [], skip_templates: list[str] = []):
        self.name = name
        self.template_overrides = template_overrides
        self.skip_templates = skip_templates

woods = [
    'oak',
    'spruce',
    'birch',
    'dark_oak',
    'acacia',
    'jungle',
    ('warped', 'warped_stem', 'warped_hyphae', 'warped_fungus'),
    ('crimson', 'crimson_stem', 'crimson_hyphae', 'crimson_fungus'),
    'cherry',
    ('bamboo', 'bamboo_block', 'bamboo_block', 'bamboo', 'bamboo_raft'),
    # TODO special control to skip certain recipes
    # TODO special control to replace custom strings (bamboo chestraft)?
    ('mangrove', 'mangrove_log', 'mangrove_wood', 'mangrove_propagule'),
]
# format for each wood item is ('<plank/generic>', <optional_log_and_stripped_override>, <optional_stripped_wood_override>, <optional_sapling_override>, <optional_boat_override>)
# if specifying any optional fields, you must specify them all, so that order is maintained

new_woods = [
    WoodType('oak'),
    WoodType('spruce'),
    WoodType('birch'),
    WoodType('dark_oak'),
    WoodType('acacia'),
    WoodType('jungle'),
    WoodType('warped',
             template_overrides=[
                 (WORD_TO_REPLACE_LOG, 'warped_stem'),
                 (WORD_TO_REPLACE_STRIPPED_WOOD, 'warped_hyphae'),
                 (WORD_TO_REPLACE_SAPLING, 'warped_fungus')
             ]),
    WoodType('crimson',
             template_overrides=[
                 (WORD_TO_REPLACE_LOG, 'crimson_stem'),
                 (WORD_TO_REPLACE_STRIPPED_WOOD, 'crimson_hyphae'),
                 (WORD_TO_REPLACE_SAPLING, 'crimson_fungus')
             ]),
    WoodType('cherry'),
    WoodType('bamboo',
            # TODO need to handle the stripey planks too
             template_overrides=[
                 (WORD_TO_REPLACE_LOG, 'bamboo_block'),
                 (WORD_TO_REPLACE_STRIPPED_WOOD, 'stripped_bamboo_block'),
                 (WORD_TO_REPLACE_SAPLING, 'bamboo'),
                 ('WOOD_boat', 'bamboo_raft'),
                 ('WOOD_chest_boat', 'bamboo_chest_raft')
             ],
             skip_templates=['stripped', 'sapling_to_stick_reclaiming', 'log_to_stick_shredding', 'log_to_planks_shredding', 'log_to_slab_shredding'],
    ),
    WoodType('mangrove',
             template_overrides=[
                 (WORD_TO_REPLACE_SAPLING, 'mangrove_propagule'),
             ]),
]

def conditional_make_dir(path):
    if not os.path.exists(path):
        print(f"Creating directory {path}")
        os.makedirs(path)

currentDir = os.path.dirname(os.path.abspath(__file__))
templatesDir = f'{currentDir}{TEMPLATES_DIR_RELATIVE}'
outputDir = f'{currentDir}{OUTPUT_DIR_RELATIVE}'
#advanceDir = currentDir + ADVANCEMENT_DIR_RELATIVE

print(f"Reading templates from {templatesDir}\nOutputting to {outputDir}")

conditional_make_dir(templatesDir)
templateFiles = os.listdir(templatesDir)
if len(templateFiles) == 0:
    raise FileNotFoundError('No template files found in templates directory')
print("Found the following template candidates: ")
print(templateFiles)

conditional_make_dir(outputDir)

#if(not(os.path.exists(advanceDir))):
#    print("Advancement directory did not exist; creating")
#    os.makedirs(advanceDir)

#eachVariantRecipeNames = []
#for variant in woods:
#    eachVariantRecipeNames["" + variant] = []

for templateFileName in templateFiles:
    if not ".json" in templateFileName:
        print(f'Skipping non-json file: {templateFileName}')
        continue
    print(f'Processing recipe template: {templateFileName}')

    templateFileLines = []
    with open(f'{templatesDir}\\{templateFileName}', "r") as file:
        for line in file:
            templateFileLines.append(line)

    for variant in woods:
        has_overrides = type(variant) is tuple

        primary_name = variant[0] if has_overrides else variant
        log_and_stripped_override_name = variant[1] if has_overrides else None
        stripped_wood_override_name = variant[2] if has_overrides else None
        sapling_override_name = variant[3] if has_overrides else None
        boat_override_name = variant[4] if has_overrides and len(variant) >= 5 else None

        print(f"\t{primary_name} (has overrides?: {has_overrides})")
        newFileName = templateFileName.replace(WORD_TO_REPLACE_PRIMARY, primary_name)
        # if "boat" in newFileName and has_overrides:
            # break # override woods don't have boat variants, so don't generate boat related recipes for them
        
        # Decide where to organize the output file
        subfolderName = primary_name
        for keyword in subfolder_filename_keywords:
            if keyword in templateFileName:
                subfolderName += f'\\{keyword}'
                break
        if subfolderName is primary_name:
            subfolderName += f'\\{TEMPLATES_DEFAULT_SUBFOLDER}'

        outputFolder = f'{outputDir}\\{subfolderName}'
        conditional_make_dir(outputFolder)
        with open(f'{outputFolder}\\{newFileName}', "w+") as newfile:
            for line in templateFileLines:
                resultLine = line
                if has_overrides:
                    # first, replace the more specific lines, then the general ones
                    resultLine = resultLine.replace(WORD_TO_REPLACE_LOG, log_and_stripped_override_name)
                    resultLine = resultLine.replace(WORD_TO_REPLACE_STRIPPED_WOOD, stripped_wood_override_name)
                    resultLine = resultLine.replace(WORD_TO_REPLACE_SAPLING, sapling_override_name)
                    if boat_override_name:
                        resultLine = resultLine.replace(WORD_TO_REPLACE_BOAT, boat_override_name)
                # regardless of overrides, replace WOOD with the wood variant
                resultLine = resultLine.replace(WORD_TO_REPLACE_PRIMARY, primary_name)
                #print("Writing: " + resultLine)
                newfile.write(resultLine)
            #print("appending " + newFileName + " to " + variant + " recipe list")
            #eachVariantRecipeNames[variant].append(newFileName)

#for variant in woods:
#    print("Writing advancement for " + variant")

print("Generation complete, copy the contents of this folder to a datapack (ex `<save folder>/datapacks/woodcutter` and use `/datapack enable \"file/woodcutter\"` to enable")
print("Remember to delete the output directory if you're changed template file names and are re-running the script!")
