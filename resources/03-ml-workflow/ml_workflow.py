import os
import random
import shutil
import stat
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import layers, models
from prefect import flow, task
import logging

logging.basicConfig(level=logging.INFO)

# Define base paths
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "img-lab3")
TRAIN_DIR = os.path.join(DATA_DIR, "train")
VAL_DIR = os.path.join(DATA_DIR, "validation")
TEST_DIR = os.path.join(DATA_DIR, "test")

# Function to ensure permissions on a path
def ensure_write_permission(path):
    """Ensures that the specified directory has write permissions."""
    if not os.access(path, os.W_OK):
        os.chmod(path, stat.S_IWUSR | stat.S_IWGRP | stat.S_IWOTH)

# Function to split data into train, validation, and test sets
def split_data(source_dir, train_dir, val_dir, test_dir, split_ratio=(0.8, 0.1, 0.1)):
    """Splits data into train, validation, and test sets."""
    # Ensure target directories exist
    for directory in [train_dir, val_dir, test_dir]:
        os.makedirs(directory, exist_ok=True)
        ensure_write_permission(directory)
    
    for category in os.listdir(source_dir):
        category_path = os.path.join(source_dir, category)
        if not os.path.isdir(category_path):
            continue
        
        images = [img for img in os.listdir(category_path) if os.path.isfile(os.path.join(category_path, img))]
        random.shuffle(images)

        train_split = int(len(images) * split_ratio[0])
        val_split = int(len(images) * (split_ratio[0] + split_ratio[1]))

        train_images = images[:train_split]
        val_images = images[train_split:val_split]
        test_images = images[val_split:]

        # Move images to corresponding folders
        for img_set, target_dir in zip([train_images, val_images, test_images], [train_dir, val_dir, test_dir]):
            category_target_dir = os.path.join(target_dir, category)
            os.makedirs(category_target_dir, exist_ok=True)
            ensure_write_permission(category_target_dir)
            for img in img_set:
                src_path = os.path.join(category_path, img)
                dest_path = os.path.join(category_target_dir, img)
                try:
                    shutil.copy(src_path, dest_path)
                except PermissionError as e:
                    logging.error(f"Permission denied when copying {src_path} to {dest_path}: {e}")
                except Exception as e:
                    logging.error(f"Unexpected error when copying {src_path} to {dest_path}: {e}")

# Task 1: Organize Data
@task
def organize_data():
    """Organizes images into training, validation, and testing directories."""
    try:
        split_data(DATA_DIR, TRAIN_DIR, VAL_DIR, TEST_DIR)
        logging.info("Data organization complete.")
    except Exception as e:
        logging.error(f"Error organizing data: {e}")
        raise

# Task 2: Preprocess Data
@task
def preprocess_data():
    """Preprocesses the images for training."""
    try:
        train_datagen = ImageDataGenerator(rescale=1.0/255, shear_range=0.2, zoom_range=0.2, horizontal_flip=True)
        val_datagen = ImageDataGenerator(rescale=1.0/255)

        train_gen = train_datagen.flow_from_directory(
            TRAIN_DIR,
            target_size=(150, 150),
            batch_size=32,
            class_mode='categorical'  # Change to categorical for multi-class classification
        )
        val_gen = val_datagen.flow_from_directory(
            VAL_DIR,
            target_size=(150, 150),
            batch_size=32,
            class_mode='categorical'  # Change to categorical for multi-class classification
        )

        return train_gen, val_gen
    except Exception as e:
        logging.error(f"Error during data preprocessing: {e}")
        raise
#test
# Task 3: Build Model
@task
def build_model(): # --
    """Builds a CNN model."""
    try:
        model = models.Sequential([
            layers.Conv2D(32, (3, 3), activation='relu', input_shape=(150, 150, 3)),
            layers.MaxPooling2D(2, 2),
            layers.Conv2D(64, (3, 3), activation='relu'),
            layers.MaxPooling2D(2, 2),
            layers.Conv2D(128, (3, 3), activation='relu'),
            layers.MaxPooling2D(2, 2),
            layers.Flatten(),
            layers.Dense(512, activation='relu'),
            layers.Dense(5, activation='softmax')  # Change to 5 output units for 5 classes
        ])
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
        logging.info("Model built successfully.")
        return model
    except Exception as e:
        logging.error(f"Error building model: {e}")
        raise

# Task 4: Train Model
@task
def train_model(model, train_gen, val_gen):
    """Trains the model using the provided data generators."""
    try:
        history = model.fit(
            train_gen,
            steps_per_epoch=train_gen.samples // train_gen.batch_size,
            epochs=10,
            validation_data=val_gen,
            validation_steps=val_gen.samples // val_gen.batch_size
        )
        logging.info("Model training complete.")

        # Save the trained model
        model_file = "trained_model.h5"
        model.save(model_file)
        logging.info(f"Model saved to {model_file}")
        
        return model_file
    except Exception as e:
        logging.error(f"Error during model training: {e}")
        raise

# Task 5: Evaluate Model
@task
def evaluate_model(model_file, test_gen):
    """Evaluates the model on the test set."""
    try:
        model = tf.keras.models.load_model(model_file)
        test_loss, test_acc = model.evaluate(test_gen, steps=test_gen.samples // test_gen.batch_size)
        logging.info(f"Test accuracy: {test_acc}, Test loss: {test_loss}")
    except Exception as e:
        logging.error(f"Error during model evaluation: {e}")
        raise

# Flow: ML Pipeline
@flow(name="ml-pipeline")
def ml_pipeline():
    """The main ML pipeline."""
    organize_data()
    train_gen, val_gen = preprocess_data()
    model = build_model()
    model_file = train_model(model, train_gen, val_gen)

    # Preprocess the test data
    test_datagen = ImageDataGenerator(rescale=1.0/255)
    test_gen = test_datagen.flow_from_directory(
        TEST_DIR,
        target_size=(150, 150),
        batch_size=32,
        class_mode='categorical'
    )

    # Evaluate the model
    evaluate_model(model_file, test_gen)

if __name__ == "__main__":
    ml_pipeline()