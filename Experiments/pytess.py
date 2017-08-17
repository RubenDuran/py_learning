try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract as pts
# from tesseract import image_to_string

print pts.image_to_string(Image.open('test.png'))
# print image_to_string(Image.open('test-english.jpg'), lang='eng')
