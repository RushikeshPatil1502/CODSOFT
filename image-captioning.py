import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from tensorflow.keras.applications.vgg16 import decode_predictions
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import Model
from PIL import Image

# Here we Load the VGG16 feature extractor

base_model = VGG16(weights="imagenet")
model = base_model
print("✅ VGG16 loaded")


# Feature extraction - will extract important features from image

def extract_features(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    features = model.predict(img_array, verbose=0)
    return features

 #Caption generator using VGG ImageNet predictions

def generate_caption(preds):
    # Convert VGG features back to classification-style prediction
    # Decode top prediction
    decoded = decode_predictions(preds, top=1)[0][0]

    label = decoded[1].replace("_", " ")
    confidence = decoded[2]

    # Build natural sentence
    if confidence > 0.5:
        caption = f"a photo of a {label}"
    elif confidence > 0.2:
        caption = f"an image that may contain a {label}"
    else:
        caption = f"an unclear image possibly showing a {label}"

    return caption


img_path = "1.HomePage.png"
features = extract_features(img_path)
caption = generate_caption(features)
img = Image.open(img_path)

plt.imshow(img)
plt.axis("off")
plt.title("Caption: " + caption)
plt.show()

print("Generated Caption:", caption)
