from tensorflow.keras.preprocessing.image import ImageDataGenerator # type: ignore
from tensorflow.keras.models import Sequential # type: ignore
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense # pyright: ignore[reportMissingModuleSource]

train = ImageDataGenerator(rescale=1./255)

dataset = train.flow_from_directory(
    "C:/Users/saini/ewaste_ai/dataset",
    target_size=(224,224),
    batch_size=16,
    class_mode='categorical'
)

model = Sequential()

model.add(Conv2D(32,(3,3),activation='relu',input_shape=(224,224,3)))
model.add(MaxPooling2D())

model.add(Conv2D(64,(3,3),activation='relu'))
model.add(MaxPooling2D())

model.add(Flatten())

model.add(Dense(128,activation='relu'))
model.add(Dense(4,activation='softmax'))

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

model.fit(dataset, epochs=5)

model.save("../model/ewaste_classifier.h5")
