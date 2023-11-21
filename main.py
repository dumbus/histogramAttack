import os
from PIL import Image
import cv2
import matplotlib.pyplot as plt

def main():    
    images_folders = get_sorted_images()

    for folder in images_folders:
        for image_name in folder:
            image = Image.open(image_name)
            cv2_image = cv2.imread(image_name, 0)

            width = image.size[0]
            height = image.size[1]

            brightness_matrix = get_brightness_matrix(image, width, height)
            print_brightness_matrix(brightness_matrix, width, height, image_name)
            print_histogram(cv2_image, image_name)

def get_brightness_matrix(image, width, height):
    pixels = image.load() # values of pixels of image
    
    matrix = []
    for x in range(width):
        row = []
        for y in range(height):
            pix_brightness = pixels[x, y]
            row.append(pix_brightness)
        matrix.append(row)

    return matrix

def print_brightness_matrix(brightness_matrix, width, height, image_name):
    print(f"Brightness matrix for image: {image_name}")

    demo_matrix = []

    for x in range (3):
        row = []
        for y in range (3):
            row.append(str(brightness_matrix[x][y]))

        row.append('...')

        for x in range (3):
            row.append(str(brightness_matrix[x][height - 1 - (2 - y)]))
        
        row_str = ' '.join(row)
        demo_matrix.append(row_str)

    demo_matrix.append('...')

    for x in range (3):
        row = []
        for y in range (3):
            row.append(str(brightness_matrix[width - 1 - (2 - x)][y]))

        row.append('...')

        for y in range (3):
            row.append(str(brightness_matrix[width - 1 - (2 - x)][height - 1 - (2 - y)]))
        
        row_str = ' '.join(row)
        demo_matrix.append(row_str)

    for i in range(len(demo_matrix)):
        print(f"[ {demo_matrix[i]} ]")
    print()

def print_histogram(cv2_image, image_name):
    # matplotlib histogram
    plt.hist(cv2_image.ravel(), 256, [0,256])

    plt.title(f"Histogram of image {image_name}")
    plt.xlabel('Pixel brightness')
    plt.ylabel('Number of pixels')
    plt.show()

def get_sorted_images():
    sorted_images = []
    folders_list = []

    for item in os.listdir('.'):
        if os.path.isdir(item) and 'imgs' in item:
            folders_list.append(item)

    for folder in folders_list:
        sorted_folder = ["", "", "", "", ""]
        files_list = os.listdir(f"./{folder}")

        for file in files_list:
            if not '%' in file:
                sorted_folder[0] = f"./{folder}/{file}"
            elif '100%' in file:
                sorted_folder[1] = f"./{folder}/{file}"
            elif '50%' in file:
                sorted_folder[2] = f"./{folder}/{file}"
            elif '10%' in file:
                sorted_folder[3] = f"./{folder}/{file}"
            elif '1%' in file:
                sorted_folder[4] = f"./{folder}/{file}"

        sorted_images.append(sorted_folder)

    return sorted_images     

if __name__ == '__main__':
    main()