import os
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import (
    GlobalAveragePooling2D, Flatten,
    Dense, Dropout, BatchNormalization
)
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import VGG16
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping


DATA_DIR = "ai_engine/data"
TRAIN_DIR = os.path.join(DATA_DIR, "train")
VAL_DIR = os.path.join(DATA_DIR, "val")
MODEL_PATH = "ai_engine/model.h5"


def get_number_of_classes():
    return len([
        f for f in os.listdir(TRAIN_DIR)
        if os.path.isdir(os.path.join(TRAIN_DIR, f))
    ])


def train_model():
    print("🔍 Checking GPU")
    print("GPU Available:", tf.config.list_physical_devices('GPU'))

    train_datagen = ImageDataGenerator(
        rescale=1.0 / 255,
        rotation_range=30,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest'
    )

    val_datagen = ImageDataGenerator(rescale=1.0 / 255)

    train_generator = train_datagen.flow_from_directory(
        TRAIN_DIR,
        target_size=(150, 150),
        batch_size=16,
        class_mode='categorical'
    )

    val_generator = val_datagen.flow_from_directory(
        VAL_DIR,
        target_size=(150, 150),
        batch_size=16,
        class_mode='categorical'
    )

    base_model = VGG16(
        weights='imagenet',
        include_top=False,
        input_shape=(150, 150, 3)
    )
    base_model.trainable = False

    num_classes = get_number_of_classes()
    print("📊 Total classes:", num_classes)

    model = Sequential([
        base_model,
        GlobalAveragePooling2D(),
        Flatten(),
        Dense(128, activation='relu'),
        BatchNormalization(),
        Dropout(0.5),
        Dense(num_classes, activation='softmax')
    ])

    model.compile(
        optimizer=Adam(learning_rate=0.0001),
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )

    early_stop = EarlyStopping(
        monitor='val_loss',
        patience=10,
        restore_best_weights=True
    )

    model.fit(
        train_generator,
        validation_data=val_generator,
        epochs=10,
        callbacks=[early_stop]
    )

    model.save(MODEL_PATH)
    print("✅ Model trained & saved:", MODEL_PATH)
