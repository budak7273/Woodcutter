import os


DEFAULT_SUBFOLDER = "woodworking"
SUBFOLDER_FILENAME_KEYWORDS = [
    "shaving", "stripping", "shredding", "rebarking", "reclaiming", "crafting"
]

TEMPLATES_DIR_RELATIVE = "/templates"
OUTPUT_DIR_RELATIVE = "/data/woodcutter/recipes"
DEBUG_PRINT_DIRECTORY_CREATION = False

WORD_TO_REPLACE_MATERIAL = "WOOD"
WORD_TO_REPLACE_LOG = "WOOD_log"
WORD_TO_REPLACE_STRIPPED_WOOD = "WOOD_wood"
WORD_TO_REPLACE_SAPLING = "WOOD_sapling"
WORD_TO_REPLACE_BOAT = "WOOD_boat"

class WoodVariant():
    def __init__(self, material: str, template_overrides: list[tuple[str, str]] = [], template_name_skip_patterns: list[str] = []):
        self.material = material
        self.template_overrides = template_overrides
        self.template_name_skip_patterns = template_name_skip_patterns

WOOD_VARIANTS = [
    WoodVariant('oak'),
    WoodVariant('spruce'),
    WoodVariant('birch'),
    WoodVariant('dark_oak'),
    WoodVariant('acacia'),
    WoodVariant('jungle'),
    WoodVariant('warped',
             template_overrides=[
                 (WORD_TO_REPLACE_LOG, 'warped_stem'),
                 (WORD_TO_REPLACE_STRIPPED_WOOD, 'warped_hyphae'),
                 (WORD_TO_REPLACE_SAPLING, 'warped_fungus')
             ],
             template_name_skip_patterns=['boat']),
    WoodVariant('crimson',
             template_overrides=[
                 (WORD_TO_REPLACE_LOG, 'crimson_stem'),
                 (WORD_TO_REPLACE_STRIPPED_WOOD, 'crimson_hyphae'),
                 (WORD_TO_REPLACE_SAPLING, 'crimson_fungus')
             ],
             template_name_skip_patterns=['boat']),
    WoodVariant('cherry'),
    WoodVariant('bamboo',
             template_overrides=[
                 (WORD_TO_REPLACE_LOG, 'bamboo_block'),
                 (WORD_TO_REPLACE_STRIPPED_WOOD, 'stripped_bamboo_block'),
                 (WORD_TO_REPLACE_SAPLING, 'bamboo'),
                 ('WOOD_boat', 'bamboo_raft'),
                 ('WOOD_chest_boat', 'bamboo_chest_raft')
             ],
            # Bamboo lacks a Wood (bark) variant and has a different log->plans ratio
             template_name_skip_patterns=['stripped_wood', 'wood_to', 'to_wood', 'sapling_to_stick_reclaiming', 'log_to_wood', 'log_to_stick', 'log_to_planks', 'log_to_slab'],
    ),
    WoodVariant('mangrove',
             template_overrides=[
                 (WORD_TO_REPLACE_SAPLING, 'mangrove_propagule'),
             ]),
    WoodVariant('potato',
             template_overrides=[
                 (WORD_TO_REPLACE_LOG, 'potato_stem'),
                 (WORD_TO_REPLACE_SAPLING, 'potato_sprouts')
             ],
             template_name_skip_patterns=['boat', 'stripped', 'shaving', 'rebarking']),
]

def conditional_make_dir(path):
    if not os.path.exists(path):
        if DEBUG_PRINT_DIRECTORY_CREATION:
            print(f"Creating directory {path}")
        os.makedirs(path)

currentDirectory = os.path.dirname(os.path.abspath(__file__))
templateDirectory = f'{currentDirectory}{TEMPLATES_DIR_RELATIVE}'
outputDirectory = f'{currentDirectory}{OUTPUT_DIR_RELATIVE}'

print(f"Reading templates from {templateDirectory}\nOutputting to {outputDirectory}")

conditional_make_dir(templateDirectory)
templateFiles = os.listdir(templateDirectory)
if len(templateFiles) == 0:
    raise FileNotFoundError('No template files found in templates directory')
print("Found the following template candidates: ")
print(templateFiles)

conditional_make_dir(outputDirectory)

for templateFileName in templateFiles:
    if not ".json" in templateFileName:
        print(f'Skipping non-json file: {templateFileName}')
        continue
    print(f'Processing recipe template: {templateFileName}')

    material_agnostic_template = False

    templateFileLines: list[str] = []
    with open(f'{templateDirectory}/{templateFileName}', "r") as file:
        for line in file:
            templateFileLines.append(line)

    for variant in WOOD_VARIANTS:
        print(f"\t{variant.material} (# overrides: {len(variant.template_overrides)}) (# skip patterns: {len(variant.template_name_skip_patterns)})")

        skip_this_variant = False
        for pattern in variant.template_name_skip_patterns:
            if pattern in templateFileName:
                print(f'\t\t{variant.material} SKIPPED because template name contains matches skip pattern: "{pattern}"')
                skip_this_variant = True
                break
        if skip_this_variant:
            continue

        outputFileName = templateFileName.replace(WORD_TO_REPLACE_MATERIAL, variant.material)

        subfolderName: str
        if outputFileName is templateFileName:
            print('\tMaterial-agnostic template detected, only processing this template once')
            material_agnostic_template = True
            subfolderName = 'custom'
        else:
            subfolderName = variant.material

        foundSubfolderInTemplateName = False
        for keyword in SUBFOLDER_FILENAME_KEYWORDS:
            if keyword in templateFileName:
                subfolderName += f'/{keyword}'
                foundSubfolderInTemplateName = True
                break
        if not foundSubfolderInTemplateName:
            subfolderName += f'/{DEFAULT_SUBFOLDER}'

        outFolder = f'{outputDirectory}/{subfolderName}'
        conditional_make_dir(outFolder)
        with open(f'{outFolder}/{outputFileName}', "w+") as newfile:
            for line in templateFileLines:
                resultLine = line

                if not material_agnostic_template:
                    for override in variant.template_overrides:
                        resultLine = resultLine.replace(override[0], override[1])

                    # apply the standard replacement
                    resultLine = resultLine.replace(WORD_TO_REPLACE_MATERIAL, variant.material)

                #print("Writing: " + resultLine)
                newfile.write(resultLine)

        if material_agnostic_template:
            break

print("Generation complete, copy the contents of this folder to a datapack (ex `<save folder>/datapacks/woodcutter` and use `/datapack enable \"file/woodcutter\"` to enable")
print("Remember to delete the output directory if you're changed template file names and are re-running the script!")
