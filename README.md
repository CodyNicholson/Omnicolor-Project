# Omnicolor Project

#### Project Introduction:

Our goal is to build a tool that will take input color names from and compute both an RGB value for that described color and provide a simplified color name. For example, “Decorous Amber” should return: {"rgb": [255, 191, 0], "simplified": "Orange"}

#### Business Case / Benefits Of Project:

This project will assist users in choosing a color for their car by giving them a wide variety of options and a demo of the color they are considering on the car that they want

#### Objectives & Scope:

To build our tool we will use a combination of machine learning, data mining, and frontend tools. There are hundreds of different names for colors. Our machine learning tools (likely to be a neural network) will be able to approximate just the right shade of a color based on the name. In order to create this neural network we will need to identify features of our data that we can use to determine the correct RGB value. This is where data mining skills will be used. Lastly, we will use frontend skills to display an image of the color our algorithm computes next to the “color name” text box in real-time, as well as the simplified color name for that color. See the pictures below for more details.

***

## Use Cases

#### No text, no cursor in textbox:

![alt tag](readme_imgs/empty.jpg)

#### No text, cursor in textbox:

![alt tag](readme_imgs/cursorInBox.jpg)

#### Text in textbox, doesn’t recognize color name:

![alt tag](readme_imgs/unknownColor.jpg)

#### Text in textbox, does recognize color name:

![alt tag](readme_imgs/knownColor.jpg)
