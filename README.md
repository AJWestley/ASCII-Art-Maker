# ASCII Art Maker

This is just a little script that let's you turn any image you have into ASCII art.

## ASCII.py

### Overview:
ASCII.py houses the ASCII_Artwork object class, which creates an ASCII artwork from an image.
ASCII.py can be run as a command-line version of the program.

### The ASCII_Artwork Class

- Constructor:
  - Creates an empty ASCII_Art object.
  - Arguments: None

- import_adjust:
  - Imports an image, greyscales it and resizes it.
  - Arguments:
    - path: The filepath of the image to be adjusted.
    - ideal_width: The amount of characters wide to make the resulting art. Defaults to 100
    - height_scale_factor: Scaling to make up for how characters are usually taller than they are wide. Defaults to 0.6

- translate:
  - Turns the object's image into ASCII art.
  - Arguments:
    - inv: Inverts the colours of the art. Defaults to False

- to_string:
  - Returns a single-line string of the ASCII artwork.
  - Arguments: None
 
- print_ascii:
  - Prints the ASCII artwork to the terminal.
  - Arguments: None
 
- pixel_to_ascii:
  - Takes a greyscale pixel and returns a corresponding ASCII character.
  - Arguments:
    - pixel_val: The value of the pixel to be converted.
    - inv: Inverts the colour of the ASCII character returned. Defaults to False

## GUI.py

A GUI version of the application, created using the tkinter framework.
Displays the resulting art in a tkinter label. 

## Features to be added

- Error checking
- gif support
- Auto animations and art
