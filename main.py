from PIL import Image

def main():
    image = Image.open('./imgs-06/6.bmp')

    width = image.size[0]
    height = image.size[1]

    brightness_matrix = get_brightness_matrix(image, width, height)
    # print_brightness_matrix(brightness_matrix)


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

# def print_brightness_matrix(brightness_matrix):
#     print("Brightness matrix for image:")

#     for i in range (3):


def get_histogram_data():
    im = Image.open('./imgs-06/6.bmp').convert('L')
    h = im.histogram()
    # Print histogram
    for idx, val in enumerate(h):
        print(idx,val)

if __name__ == '__main__':
    main()