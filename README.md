# AniGEN-blender-utils

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Description

This tool helps blend motions in Blender and render the animation with the given filenames using a local file directory of motion data. The paths for importing of motions, the base blender file with the character and the render path should all be modified in the config.py accordingly.

## Installation

1. Make sure you have Blender 3.1.2 version installed (can be higher)
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

   For Mac (Not tested):
   Setup environment variable for MAC uisng the following url: https://phoenixnap.com/kb/set-environment-variable-mac#:~:text=Permanent%20environment%20variables%20are%20added%20to%20the%20.bash_profile%20file%3A

   ```shell
   export [variable_name]=[variable_value]
   ```

6. After the setup, check if the environment variable works by typing the following in your shell:
   ```shell
   blender --version
   ```

## Running the program

1. Now redirect to the project directory if you have not done so
   ```
   cd anigen-blender-utils
   ```
2. Configure the paths for the hardcoded data and paths in main.py (line 15, line 27, line 49) and FindAndImport.py (line 92) and save the codes (`TODO: Make these dynamic`)
3. Run the program by typing the following command in the shell:
   ```shell
   blender Xbot.blend --background --python C:\Users\User\Desktop\FYP\blender-utils\main.py
   ```

## Contributing

If you would like to work on this repository as an AniGEN dev:

1. Clone the repository
2. Create a new branch.
3. Make your changes and commit them.
4. Push your changes to your remote branch
5. Submit a pull request.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
