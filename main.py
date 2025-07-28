# from Project_OCR import extraction_file
from Project_OCR.extraction_file import ExtractPanDetails
import config

if __name__ == "__main__":
    obj = ExtractPanDetails(config.file_path,config.pytesseract_path)
    result = obj.get_pan_details()
    print(result)

