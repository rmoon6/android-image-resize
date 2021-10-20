from PIL import Image
import glob
import os
import shutil

INPUT_PATH = os.path.join(".", "input")
OUTPUT_PATH = os.path.join(".", "output")

def get_png_images():
    return [ Image.open(filename) for filename in glob.glob(os.path.join(INPUT_PATH, "*.png")) ]

def clean_up_file_structure():
    if os.path.isdir(OUTPUT_PATH):
        shutil.rmtree(OUTPUT_PATH)
    os.mkdir(OUTPUT_PATH)
    os.mkdir(os.path.join(OUTPUT_PATH, "drawable-mdpi"))
    os.mkdir(os.path.join(OUTPUT_PATH, "drawable-hdpi"))
    os.mkdir(os.path.join(OUTPUT_PATH, "drawable-xhdpi"))
    os.mkdir(os.path.join(OUTPUT_PATH, "drawable-xxhdpi"))

def resize_image_from_multiplier(image, multiplier):
    new_size = (int(image.size[0] * multiplier), int(image.size[1] * multiplier))
    return image.resize(new_size)

def main():

    clean_up_file_structure()

    for image in get_png_images():

        base_filename = os.path.basename(image.filename)

        mdpi_image = resize_image_from_multiplier(image, 1/3)
        hdpi_image = resize_image_from_multiplier(image, 1/2)
        xhdpi_image = resize_image_from_multiplier(image, 2/3)
        xxhdpi_image = image

        mdpi_path = os.path.join(OUTPUT_PATH, "drawable-mdpi", base_filename)
        hdpi_path = os.path.join(OUTPUT_PATH, "drawable-hdpi", base_filename)
        xhdpi_path = os.path.join(OUTPUT_PATH, "drawable-xhdpi", base_filename)
        xxhdpi_path = os.path.join(OUTPUT_PATH, "drawable-xxhdpi", base_filename)

        print(f"saving file: {base_filename}")
        print(f"mdpi image size: ${mdpi_image.size}\tpath: {mdpi_path}")
        print(f"hdpi image size: ${hdpi_image.size}\tpath: {hdpi_path}")
        print(f"xhdpi image size: ${xhdpi_image.size}\tpath: {xhdpi_path}")
        print(f"xxhdpi image size: ${xxhdpi_image.size}\tpath: {xxhdpi_path}")
        print()

        mdpi_image.save(mdpi_path)
        hdpi_image.save(hdpi_path)
        xhdpi_image.save(xhdpi_path)
        xxhdpi_image.save(xxhdpi_path)

if __name__ == '__main__':
    main()
