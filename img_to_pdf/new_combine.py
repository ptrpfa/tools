from PIL import Image
from PyPDF2 import PdfWriter
from natsort import natsorted
import os, sys
import shutil
import tempfile

Image.MAX_IMAGE_PIXELS = None

def split_image(image_path, height):
    img = Image.open(image_path)
    img_width, img_height = img.size
    
    if img_height <= height:
        return [img]  # No need to split if the image height is less than or equal to the split height
    
    num_splits = img_height // height

    image_parts = []

    for i in range(num_splits):
        box = (0, i * height, img_width, (i + 1) * height)
        image_parts.append(img.crop(box))
    
    # Append the last part (might have different height due to integer division)
    box = (0, num_splits * height, img_width, img_height)
    image_parts.append(img.crop(box))

    return image_parts

def save_images(image_parts, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for i, image in enumerate(image_parts):
        image_path = os.path.join(output_folder, f"part_{i+1}.png")
        image.save(image_path)

def combine_images_to_pdf(image_parts, pdf_path):
    with PdfWriter(pdf_path) as pdf_writer:
        for image in image_parts:
            img_pdf = Image.new("RGB", image.size, "WHITE")
            img_pdf.paste(image, (0, 0))
            with tempfile.NamedTemporaryFile(delete=False) as temp:
                img_pdf.save(temp, "PDF", quality=100)
                pdf_writer.append(temp.name)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <folder_path> <output_name>")
        sys.exit(1)

    folder_path = sys.argv[1]
    output_name = sys.argv[2]

    if not os.path.isdir(folder_path):
        print("Error: Invalid folder path.")
        sys.exit(1)

    # Find all PNG and JPG files in the folder
    image_files = natsorted(
        [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    )
    image_paths = [os.path.join(folder_path, f) for f in image_files]

    output_folder = "image_parts"  # Folder to store the split images
    output_pdf_path = f"{output_name}.pdf"  # Output PDF file

    # Load images
    image_parts = [Image.open(image_path) for image_path in image_paths]

    # Save the images into the output folder
    save_images(image_parts, output_folder)

    # Combine images into a PDF
    combine_images_to_pdf(image_parts, output_pdf_path)

    print("PDF file created successfully.")

    # Define the Downloads folder path
    downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")

    # Move the PDF file to the Downloads folder
    shutil.move(output_pdf_path, os.path.join(downloads_folder, output_pdf_path))

    # Remove the image_parts folder after creating the PDF
    shutil.rmtree(output_folder)
