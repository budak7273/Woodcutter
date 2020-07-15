import os

WORD_TO_REPLACE = "WOOD"
WORD_TO_REPLACE_LOG = "WOOD_log"
WORD_TO_REPLACE_STRIPPED_WOOD = "WOOD_wood"
TEMPLATES_DIR_RELATIVE = "\\templates"
OUTPUT_DIR_RELATIVE = "\\data\\woodcutter\\recipes"
#ADVANCEMENT_DIR_RELATIVE = "\\data\\woodcutter\\advancements\\recipes\\misc"
woods = ['oak', 'spruce', 'birch', 'dark_oak', 'acacia', 'jungle', ('warped', 'warped_stem', 'warped_hyphae'), ('crimson', 'crimson_stem', 'crimson_hyphae')]
# format for each wood item is ('<plank/generic>', <optional_log_and_stripped_override>, <optional_stripped_wood_override>)
# if specifying a optional_stripped_wood_override you must also specify a optional_log_and_stripped_override

currentDir = os.path.dirname(os.path.abspath(__file__))
templatesDir = currentDir + TEMPLATES_DIR_RELATIVE
outputDir = currentDir + OUTPUT_DIR_RELATIVE
#advanceDir = currentDir + ADVANCEMENT_DIR_RELATIVE
print("Reading templates from " + templatesDir + "\nOutputting to " + outputDir)
templateFiles = os.listdir(templatesDir)
print("Found the following templates: ")
print(templateFiles)

if(not(os.path.exists(outputDir))):
        print("Output directory did not exist; creating")
        os.makedirs(outputDir)
#if(not(os.path.exists(advanceDir))):
#        print("Advancement directory did not exist; creating")
#        os.makedirs(advanceDir)

#eachVariantRecipeNames = []
#for variant in woods:
#        eachVariantRecipeNames["" + variant] = []
        
for file in templateFiles:
        if ".json" in file:
                print('Processing recipe template ' + file )
                newLines = []
                with open(templatesDir + "\\" + file, "r") as f:
                        #read_data = f.read()
                        for line in f:
                                newLines.append(line)
                                #print(line, end='')
                #print(newLines)
                for variant in woods:
                        has_overrides = type(variant) is tuple
                        
                        primary_name = variant[0] if has_overrides else variant
                        log_and_stripped_override_name = variant[1] if has_overrides else None
                        stripped_wood_override_name = variant[2] if has_overrides else None
                        
                        print("\t" + primary_name + " (has overrides: " + str(has_overrides) + ")")
                        newFileName = file.replace(WORD_TO_REPLACE, primary_name)
                        with open(outputDir + "\\" + newFileName, "w+") as newfile:
                                for line in newLines:
                                        resultLine = line
                                        if has_overrides: #first replace the more specific lines, then the general ones
                                            resultLine = resultLine.replace(WORD_TO_REPLACE_LOG, log_and_stripped_override_name)
                                            resultLine = resultLine.replace(WORD_TO_REPLACE_STRIPPED_WOOD, stripped_wood_override_name)
                                        #regardless of overrides, replace WOOD with the wood variant
                                        resultLine = resultLine.replace(WORD_TO_REPLACE, primary_name)
                                        #print("Writing: " + resultLine)
                                        newfile.write(resultLine)
                        #print("appending " + newFileName + " to " + variant + " recipe list")
                        #eachVariantRecipeNames[variant].append(newFileName)
                        
#for variant in woods:
#        print("Writing advancement for " + variant")
        
        
        
	
