
import tesserocr
from PIL import Image
image = Image.open('./simple/imgs/1.jpg')
result = tesserocr.image_to_text(image)
print(result)