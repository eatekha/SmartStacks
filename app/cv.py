# from transformers import TrOCRProcessor, VisionEncoderDecoderModel
# from PIL import Image
# import torch

# img = Image.open('C:/Users/surya/test_img.jpg')
# image = img.convert('RGB')

# processor = TrOCRProcessor.from_pretrained('microsoft/trocr-base-handwritten')
# model = VisionEncoderDecoderModel.from_pretrained('microsoft/trocr-base-handwritten')
# pixel_values = processor(images=image, return_tensors="pt").pixel_values

# generated_ids = model.generate(pixel_values, max_new_tokens=512)
# generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]

# print(generated_text)

from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image
import requests

# load image from the IAM database
image = Image.open("C:/Users/surya/img_1.png")
image = image.convert('RGB')

processor = TrOCRProcessor.from_pretrained('microsoft/trocr-base-handwritten')
model = VisionEncoderDecoderModel.from_pretrained('microsoft/trocr-base-handwritten')
pixel_values = processor(images=image, return_tensors="pt").pixel_values

generated_ids = model.generate(pixel_values)
generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]

print('hello' + generated_text)