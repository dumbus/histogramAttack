from PIL import Image

def main():
    image = Image.open('./imgs-06/6.bmp')

    width = image.size[0]
    height = image.size[1]

    brightness_matrix = get_brightness_matrix(image, width, height)
    print_brightness_matrix(brightness_matrix, width, height)


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

def print_brightness_matrix(brightness_matrix, width, height):
    print("Brightness matrix for image:")

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


def get_histogram_data():
    im = Image.open('./imgs-06/6.bmp').convert('L')
    h = im.histogram()
    # Print histogram
    for idx, val in enumerate(h):
        print(idx,val)

if __name__ == '__main__':
    main()