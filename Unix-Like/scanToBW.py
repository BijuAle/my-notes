import os
from pdf2image import convert_from_path
from PIL import Image
import pytesseract

# Specify the PDF file name
pdf_filename = "a.pdf"

# Check if the PDF file exists in the current directory
if not os.path.isfile(pdf_filename):
    print(f"{pdf_filename} not found in the current directory.")
else:
    try:
        # Create output directory
        output_dir = "output_images"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Convert PDF to images (large-size pages may take a while)
        print("Converting PDF pages to images...")
        images = convert_from_path(pdf_filename, dpi=300, thread_count=4)  # Adjust DPI and use multiple threads

        bw_images = []
        for i, image in enumerate(images):
            # Convert to grayscale
            print(f"Processing page {i + 1}...")
            gray_image = image.convert("L")  # Convert to grayscale

            # Apply threshold to convert the grayscale image to true black and white
            threshold = 128  # You can adjust this threshold value
            bw_image = gray_image.point(lambda p: 255 if p > threshold else 0, mode='1')  # True B&W
            
            # Optionally apply OCR to each page
            # Uncomment the next two lines if OCR is desired
            # text = pytesseract.image_to_string(bw_image)
            # print(f"OCR Text from Page {i + 1}:")
            # print(text)

            # Save processed black-and-white image
            bw_image_path = os.path.join(output_dir, f"bw_page_{i + 1}.png")
            bw_image.save(bw_image_path, "PNG")
            bw_images.append(bw_image)

        # Save all black-and-white images as a new PDF
        output_pdf_path = os.path.join(output_dir, "bw_output.pdf")
        print(f"Saving processed PDF to {output_pdf_path}...")
        bw_images[0].save(output_pdf_path, save_all=True, append_images=bw_images[1:])
        print("Conversion to true black-and-white completed successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")