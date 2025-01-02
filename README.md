# Traffic

This project was completed for the HarvardX CS50 Ai course in Python. It uses the Tensorflow/Keras library and a Convolutional Neural Network model to train itself to identify and categorize different traffic signs, however it can be used for any type of image. Some setup is required.

## Setup

The "gtsrb" folder should contain a folder for each category of image. One category is provided (0), and inside contains a ppm image file for an image of that category.

For each category of image:
- Create a folder with a new number (0, 1, 2, etc.)
- put every image that matches the category inside that image
- Edit traffic.py and change "num_categories" to match the amount of folders
- Example: I have 2 categories of iamges, "Bee" and "3." I would add all "Bee" images to folder 0, and "3" to folder 1. I would then change "num_categories" to 2.
