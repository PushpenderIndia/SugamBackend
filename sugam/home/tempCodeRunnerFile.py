import pytesseract
from PIL import Image

class ImageToText:
    def __init__(self, image_path):
        self.image_path = image_path

    def start(self):
        extracted_txt = ""
        try:
            # Open the image file
            with Image.open(self.image_path) as image:
                # Use pytesseract to extract text from the image
                extracted_txt = pytesseract.image_to_string(image)
        except Exception as e:
            print("Unable to open image file: ", e)

        return extracted_txt

if __name__ == "__main__":
    test = ImageToText("images.png")
    extracted_txt = test.start()
    print(extracted_txt)
