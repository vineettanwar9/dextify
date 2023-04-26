import re
import Raw
import os
import numpy as np
import matplotlib as plt
import tensorflow as tf



new_model = tf.keras.models.load_model("model_final")
new_model1 = tf.keras.models.load_model("my_model_final")
new_model2 = tf.keras.models.load_model("final_save.h5",custom_objects={"CTCLayer": CTCLayer})

import re
def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)

path = "segmented/"

counter = sorted_alphanumeric(os.listdir('segmented'))

for x in range(len(counter)):
    counter[x] = os.path.join(path, counter[x])

num = len(counter)

ocr_test_img_path = counter

test_ds1 = prepare_dataset1(ocr_test_img_path)

for batch in test_ds1.take(1):
    batch_images = batch["image"]
    _, ax = plt.subplots(5, 5, figsize=(15, 8))

    print(batch_images.shape)
    new_model.summary()
    batch_labels = np.zeros((num, 90))

    preds = new_model.predict([batch_images,batch_labels])
    pred_texts = decode_batch_predictions(preds)
    for i in range(25):
        img = batch_images[i]
        img = tf.image.flip_left_right(img)
        img = tf.transpose(img, perm=[1, 0, 2])
        img = (img * 255.0).numpy().clip(0, 255).astype(np.uint8)
        img = img[:, :, 0]

        title = f"Prediction: {pred_texts[i]}"
        ax[i // 5, i % 5].imshow(img, cmap="gray")
        ax[i // 5, i % 5].set_title(title)
        ax[i // 5, i % 5].axis("off")
plt.show()

print(len(pred_texts))