# AniGEN-blender-utils

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Description

This tool helps blend motions in Blender and render the animation with the given filenames using a local file directory of motion data. The paths for importing of motions, the base blender file with the character and the render path should all be modified. It is important to note that I have tried this with Mixamo Animations only. Essentially the character bones for any motion data will have to match for the the character within the .blend file and the other motions. This uses Non Linear Animation (NLA) from Blender to blend the motions. Also this has only been tested on a Windows and MacOS machine. So unsure if other OS platforms will work the same.

## Motions

To test AniGEN-blender-utils, some motions files have been given in a zip folder. These motions are downlaoded from [MIXAMO](https://www.mixamo.com/). The link for the zip is as follows:

[`Motions-zip`](https://drive.google.com/file/d/1WRxv5IbdIXOPL2ixJ9xUF0IAUkblPilD/view?usp=drive_link)

Use these motions for test purposes by using the names of the files as the motions in the `config.py`.

## Current Features
1. Importing FBX files (for the motions) automatically
2. Blending of in-place motions automatically (Does not support blending of not in-place motions)
3. Rendering the motions automatically using Blender's NLA.
4. Exporting the final FBX (currently it's buggy and will have to be fixed in a newer version)

## Future Features
1. Fix Exporting the FBX.
2. Support for blending non in-place motions so that displacement is properly adjusted
3. Camera adjustment when doing non in-place motions
4. Simple environment generations
5. More support

## Installation

1. Make sure you have Blender 3.1.2 version installed (some inconsistency with version 4)
2. Clone this repository to your local machine.
   ```shell
   git clone https://github.com/MarzukhAsjad/anigen-blender-utils.git
   ```
3. Navigate to the project directory.
   ```shell
   cd anigen-blender-utils
   ```
4. Setup blender's path to your environment variables

   For Windows:
   To do this, redirect to where Blender has been installed. The path on my machine is

   ```
   C:\Program Files\Blender Foundation\Blender 3.1
   ```

   Set the environment variable as "blender" and the environment value as the path.
   So it should be similar. This is the usual setup for windows.

   For macOS:
   Setup environment variable for macOS uisng the following url: https://docs.blender.org/manual/en/latest/advanced/command_line/launch/macos.html

6. After the setup, check if the environment variable works by typing the following in your shell:
   ```shell
   blender --version
   ```

## Running the program

1. Now redirect to the project directory if you have not done so
   ```
   cd anigen-blender-utils
   ```
2. Configure the paths for the import paths, the render output path and other variables in the config.py
3. Run the program by typing the following command in the shell:
   ```shell
   blender Xbot.blend --background --python main.py
   ```

## Contributing

If you would like to work on this repository:

1. Clone the repository
2. Create a new branch.
3. Make your changes and commit them.
4. Push your changes to your remote branch
5. Submit a pull request.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
