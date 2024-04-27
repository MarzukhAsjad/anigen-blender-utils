# Configuration for main.py
# Unsure if relative paths will work. Try to give absolute filepaths. 
BLEND_PATH = r'Xbot.blend'
IMPORT_PATH = r'..\Motions' # Make sure the .fbx motions are there in this directory
RENDER_PATH = r'..\output' # Make sure this directory exists
MOTIONS = [idle', 'walk', 'run'] # Update the array with the list of filenames for example ["Walk.fbx", "Run.fbx", "Drinking_water.fbx"] DO NOT USE SPACES IN FILENAMES
TOTAL_FRAMES = 200
