<!-- omit in toc -->
# Remote Moon Block Caster
<!-- omit in toc -->
#### Video Demo:  <URL HERE>
<!-- omit in toc -->
#### Description:
This program is a remote moon blocks caster designed for individuals of Chinese descent seeking guidance and support from the Gods. In traditional practice, users ask questions and cast two moon blocks, which have yin and yang sides. A favorable response from the Gods is represented by one yin and one yang, while receiving two of the same side indicates a negative response from Gods. This application simulates this ritual, providing a convenient solution for those living abroad or unable to visit temples. . Developed as my CS50P final project in October 2024, it features original pixel art designs created by Taylor Liao, using Pixaki. It offers a meaningful way to connect with cultural practices and spiritual guidance from a distance.

<!-- omit in toc -->
## TODO List
- [ ] Implement feature to throw moon blocks when the space key is pressed.
- [ ] Allow clicking on arrows to switch Gods.
- [ ] Add sound effects for throwing moon blocks and receiving responses.
- [ ] Add sound effects for switching God
- [ ] Implementing the laughing blocks response from God
- [ ] Use PyInstaller to package the application as a .exe file

<!-- omit in toc -->
## Table of Contents
- [Usage](#usage)
- [Features](#features)
- [Code Structure](#code-structure)
- [Acknowledgments](#acknowledgments)
- [Future Work](#future-work)

## Usage
Interacting with the Application:
-  Ask your question, then throw the moon blocks by pressing the space key or clicking the arrows to switch between Gods.
- The response will be displayed based on the sides of the moon blocks.

Key Bindings:
- Left: Switch to the God on the left
- Right: Switch to the God on the right

Example Usage:
- Start the program, ask a question like "Should I take this job?", and then throw the moon blocks to receive guidance from the Gods.

## Features
- Simulates the moon blocks casting experience.
- Provides various choices of Gods.
- Displays responses based on the sides of the moon blocks.
- Provides a user-friendly interface.

## Code Structure
The project is organized into several key components to facilitate the moon blocks casting simulation. Below is a brief overview of the main files and their responsibilities:

- **project.py**: The main entry point of the application. This file initializes Pygame, sets up the game loop, and handles user interactions.

- **assets/**: This directory contains all the graphical assets used in the project, including:
  - **cup/**: Contains pixel art images for the moon blocks.
  - **gods/**: Contains pixel art images for the Gods.
  - **buttons/**: Contains pixel art images for the buttons.
  - **arrow.png**: The pixel art image for the arrow.


The project includes several key classes and functions, each responsible for specific aspects of the moon blocks casting simulation:

- ``PgObject``: The base class for all drawable objects in the application. It defines common properties and methods for rendering and updating objects on the screen.

- ``Image``: A class responsible for image animation.

- ``Text``: This class takes pygame rendered text as input, enabling the display of messages and instructions on the screen with customizable fonts and sizes.

- ``Button``: A class that implements button functionality and interactions, facilitating user input and providing visual feedback.

- ``main``: The entry point of the program. This function initializes Pygame, sets up the display, and runs the main game loop, handling events, updating the game state, and rendering graphics.

- ``getPath``: A utility function that retrieves the file path for assets used in the application.

- ``loadImgObject``: This function takes file paths as input and loads them as Pygame objects into the application. It handles any necessary transformations required for properly displaying images on the screen.

- ``redrawWindow``: A function that updates the display, redrawing all elements on the screen to reflect the current state of the application.


## Acknowledgments
- Special thanks to the CS50 Harvard team for providing this incredible course, which is both free and exceptional.
- I would like to acknowledge the Pygame community for their excellent resources and documentation, which were invaluable in implementing the features of this program.
- This project is inspired by traditional practices of moon block casting in Chinese culture, and I hope it brings this cultural heritage to those living abroad or unable to visit temples.
- I appreciate the feedback from friends and family during the testing phase, which helped improve the user experience.
- Special thanks to [Coding With Russ](https://www.youtube.com/watch?v=G8MYGDf_9ho&t=889s) and [Tech With Tim](https://www.youtube.com/watch?v=i6xMBig-pP4&list=PLzMcBGfZo4-lp3jAExUCewBfMx3UZFkh5) for their informative videos on Pygame tutorials, which significantly influenced my approach to this project. This project would have died without them.


## Future Work
- Rewrite the program as an Android app or webpage.
- Add animation when switching Gods.
- Helper icon for users unfamiliar with the ritual.
- Uniform the color palette used for all UI elements for a more balanced appearance.
- Potentially expand the selection of Gods.
