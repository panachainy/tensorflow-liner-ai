
# TF for image classification model

import tensorflow
import numpy
from PIL import Image

model_path = './models/gesture'

model = tensorflow.saved_model.load(model_path)
classes = ["gesture_2",  "gesture_4",  "gesture_3",  "gesture_1", ]

img = Image.open(model_path + "/ex_image.jpg").convert('RGB')
img = img.resize(
    (300, 300 * img.size[1] // img.size[0]), Image.Resampling.LANCZOS)
inp_numpy = numpy.array(img)[None]


inp = tensorflow.constant(inp_numpy, dtype='float32')

class_scores = model(inp)[0].numpy()


print("")
print("class_scores", class_scores)
print("Class : ", classes[class_scores.argmax()])