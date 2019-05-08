import os

WORD_TO_REPLACE = "WOOD"
TEMPLATES_DIR_RELATIVE = "\\templates"
OUTPUT_DIR_RELATIVE = "\\data\\woodcutter\\recipes"
#ADVANCEMENT_DIR_RELATIVE = "\\data\\woodcutter\\advancements\\recipes\\misc"
woods = ['oak', 'spruce', 'birch', 'dark_oak', 'acacia', 'jungle']

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
                        print("\t" + variant)
                        newFileName = file.replace(WORD_TO_REPLACE, variant)
                        with open(outputDir + "\\" + newFileName, "w+") as newf:
                                for line in newLines:
                                        temp = line.replace(WORD_TO_REPLACE, variant)
                                        #print("Writing: " + temp)
                                        newf.write(temp)
                        #print("appending " + newFileName + " to " + variant + " recipe list")
                        #eachVariantRecipeNames[variant].append(newFileName)
                        
#for variant in woods:
#        print("Writing advancement for " + variant")
        
        
        
	
