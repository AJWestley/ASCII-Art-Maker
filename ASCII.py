import os
import cv2
import numpy as np

def import_adjust(path: str, ideal_width: int = 100):
    
    # import image, then greyscale and resize
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    scale_factor = ideal_width / img.shape[1]
    scaled_dimensions = (int(img.shape[1] * scale_factor), int(img.shape[0] * scale_factor * 0.6)) # extra height scale for rectangular cells
    
    return cv2.resize(img, scaled_dimensions, interpolation=cv2.INTER_AREA)

def pixel_to_ascii(pixel_val: int) -> str:
    ascii_vals = ['%', '#', '+', '*', '=', '-', ':', '.', ' ']
    
    # formula to get an ascii index from a pixel value
    # 0->25 = index 0 then index goes up every 30
    pixel_val += 4
    i = pixel_val // 30
    
    return ascii_vals[i]

def translate(image):
    ascii_image = []
    for row in image:
        ascii_row = [pixel_to_ascii(pixel) for pixel in row]
        ascii_image.append(ascii_row)
    return ascii_image

def print_ascii(ascii_image):
    print()
    for row in ascii_image:
        for pixel in row:
            print(pixel, end='')
        print()

if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')
    image = import_adjust('spaceguy.jpg', 150)
    ascii_image = translate(image)
    print_ascii(ascii_image)