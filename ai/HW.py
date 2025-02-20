import numpy as np
from PIL import Image
import base64,io
def detectHW(imagePath):
    import tensorflow
    import cv2
    # print(imagePath)  
    # Remove data URI prefix if present
    if ',' in imagePath:
        imagePath = imagePath.split(',')[1]
    # Decode the Base64 string
    image_bytes = base64.b64decode(imagePath)
    # Create a BytesIO object and load the image
    image_stream = io.BytesIO(image_bytes)
    
    image = Image.open(image_stream).convert('L')
    
    img = np.invert(np.array(image))
    img = np.reshape(img, (1, 28, 28, 1))
    # Convert to numpy array
    # img_array = np.array(image)
    
    # print(img_array)
    # # Load the model
    loaded_model = tensorflow.keras.models.load_model('HWRModel.hdf5')
    pred = loaded_model.predict(img)
    return np.argmax(pred)