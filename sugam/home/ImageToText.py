
class ImageToText:
    def __init__(self, image_path):
        self.image_path = image_path

    def start(self):
        extracted_txt = ""
        return extracted_txt
    
if __name__ == "__main__":
    test =  ImageToText("img.png")
    extracted_txt = test.start()
    print(extracted_txt)