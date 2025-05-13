- Used a convolutional neural network (CNN)
- ResNet50 and partially fine-tuned the model
- Lower layers are frozen to retain low-level features.
- Higher layers (layer3, layer4) are trained
- Preprocessing to remove very skewed latitude and longitude in the coordinates of the train set
- Scaled the coordinates to between 0 and 1 for easier training
- Higher emphasis on latlong prediction and lower on angle prediction.

https://drive.google.com/drive/folders/1RBIM7ZCr3ibeXbmw0_USlmbIex0MgtbG?usp=sharing
