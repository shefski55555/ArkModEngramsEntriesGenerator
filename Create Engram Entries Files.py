import os

dir = os.path.dirname(__file__)
engramTitle = ''
primalTitle = ''
lastEngramFolder = ''
lastPrimalFolder = ''
engrams = []
unformattedEngrams = []
primalItems = []

def fileFound(filepath):
    global engramTitle, primalTitle, lastEngramFolder, lastPrimalFolder

    if not filepath.endswith(".uasset"):
        return

    filename = os.path.splitext(os.path.basename(filepath))[0]

    if "EngramEntry" not in filename and "PrimalItem" not in filename:
        return

    folder = os.path.basename(os.path.dirname(filepath))  # Always get the folder name safely

    if "EngramEntry" in filename:
        if folder != lastEngramFolder:
            engramTitle = f"\n//{folder}\n"
        else:
            engramTitle = ''
        engrams.append(engramTitle + filename + "_C\n")
        unformattedEngrams.append(filename + "_C\n")
        lastEngramFolder = folder

    elif "PrimalItem" in filename:
        if folder != lastPrimalFolder:
            primalTitle = f"\n//{folder}\n"
        else:
            primalTitle = ''
        primalItems.append(primalTitle + filename + "_C\n")
        lastPrimalFolder = folder

# Use os.walk for simpler recursive file traversal
for root, dirs, files in os.walk(dir):
    for file in files:
        fileFound(os.path.join(root, file))

# Write output files
with open(os.path.join(dir, "Output - Engrams + Items.txt"), "w") as nameFile:
    nameFile.write("[Engram Entries]\n")
    nameFile.writelines(engrams)
    print("Wrote All Engram Entries")

    nameFile.write("\n[Primal Items]\n")
    nameFile.writelines(primalItems)
    print("Wrote All Primal Items")

    extras_path = os.path.join(dir, "Extras Text.txt")
    if os.path.exists(extras_path):
        with open(extras_path, "r") as extrasFile:
            nameFile.write("\n")
            nameFile.write(extrasFile.read())
            print("Added Extra Text")

# Write hidden engrams config
with open(os.path.join(dir, "Output - Hide All Engrams.txt"), "w") as hiddenEngramsFile:
    for engramEntry in unformattedEngrams:
        hiddenEngramsFile.write(
            f'OverrideNamedEngramEntries=(EngramClassName="{engramEntry.strip()}",EngramHidden=True,EngramPointsCost=0,EngramLevelRequirement=1,RemoveEngramPreReq=False)\n'
        )
    print("Wrote Hidden file, number of engrams: " + str(len(unformattedEngrams)))

print("done")
input()
