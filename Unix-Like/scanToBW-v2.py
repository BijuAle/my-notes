import os
from pdf2image import convert_from_path
from PIL import Image, ImageEnhance
import pytesseract
import numpy as np
import cv2

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
            print(f"Processing page {i + 1}...")

            # Convert to grayscale
            gray_image = image.convert("L")  # Convert to grayscale
            np_image = np.array(gray_image)

            # Enhance image contrast
            enhancer = ImageEnhance.Contrast(gray_image)
            enhanced_image = enhancer.enhance(2)  # Increase contrast to improve text clarity

            # Convert the enhanced image to a NumPy array for processing
            enhanced_np_image = np.array(enhanced_image)

            # Calculate optimal threshold using Otsu's binarization method
            _, otsu_threshold_image = cv2.threshold(enhanced_np_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

            # Convert back to a PIL Image
            otsu_image = Image.fromarray(otsu_threshold_image)

            # Optionally apply OCR to each page (uncomment the next lines if needed)
            # text = pytesseract.image_to_string(otsu_image)
            # print(f"OCR Text from Page {i + 1}:")
            # print(text)

            # Save processed black-and-white image
            bw_image_path = os.path.join(output_dir, f"bw_page_{i + 1}.png")
            otsu_image.save(bw_image_path, "PNG")
            bw_images.append(otsu_image)

        # Save all black-and-white images as a new PDF
        output_pdf_path = os.path.join(output_dir, "bw_output.pdf")
        print(f"Saving processed PDF to {output_pdf_path}...")
        bw_images[0].save(output_pdf_path, save_all=True, append_images=bw_images[1:])
        print("Conversion to true black-and-white completed successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")