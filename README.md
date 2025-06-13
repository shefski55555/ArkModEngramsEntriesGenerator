A simple python script to auto generate some usefule information files about your ark mod. Designed for use with ASA have no idea how it might work with ASE mods but if the fire structure is similiar don't see why it'd be an issue.

Generates 2 files, one includes all items and engrams for your mod, seperated by folder. The other creates ini configuration lines which will remove/hide all the engrams added by your mod. I like giving this option so it's easy to hide a feature of my mods if a user doesn't like it.

To use just put the Create Engram Entries Files.py and Extras Text.txt into your mod's content folder. (eg:ARKDevkit\Projects\ShooterGame\Mods\{MOD Name}\Content).

Ensure python3 is installed, you can easily install it in Windows by opening the terminal and typing winget install --id Python.Python.3.13

Important note, when you have generated your files either remove the "Create Engram Entries Files.py" file or rename it to a .txt otherwise Curseforege will reject the mod.


Example outputs:
https://pastebin.com/CXjvMSVZ
https://pastebin.com/1GFQHzCJ