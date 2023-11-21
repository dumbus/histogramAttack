from PIL import Image

def main():
    print("Hello world!")

def get_histogram_data():
    im = Image.open('./imgs-06/6.bmp').convert('L')
    h = im.histogram()
    # Print histogram
    for idx, val in enumerate(h):
        print(idx,val)

if __name__ == '__main__':
    main()