# first neural network with keras tutorial
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense, Conv2D,MaxPooling2D,Flatten
from tensorflow.keras.preprocessing.image import ImageDataGenerator 
from tensorflow.keras.preprocessing import image
import numpy as np
import os
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense
def retrain_network(img_width, img_height):
    train_datagen = ImageDataGenerator(rescale=1. / 255, 
                                       rotation_range = 30, 
                                       width_shift_range=0.1,
                                       height_shift_range=0.1,
                                       shear_range=0.1,
                                       zoom_range=0.1,
                                       horizontal_flip=True, 
                                       fill_mode='nearest')
    val_datagen = ImageDataGenerator(rescale=1. / 255)

    val_generator = \
        val_datagen.flow_from_directory('data/validation_set'
            , target_size=(img_width, img_height), batch_size=16, class_mode='categorical')

    train_generator = \
        train_datagen.flow_from_directory('data/training_set'
            , target_size=(img_width, img_height), batch_size=16, class_mode='categorical')

    # Configure the CNN (Convolutional Neural Network).
    classifier = Sequential()
    
    # ------------------ YOUR CODE HERE-------------------------------------------------#
    base_model = ResNet50(weights='imagenet', include_top=False, input_shape=(128, 128, 3))

# Load the ResNet50 model pretrained on ImageNet data
    base_model = ResNet50(weights='imagenet', include_top=False, input_shape=(128, 128, 3))

    classifier = Sequential([
           base_model,  
           Conv2D(16, (3, 3), input_shape=(128, 128, 3), activation='relu', padding='valid'),
           Conv2D(32, (5, 5), activation='relu', padding='valid'),
           MaxPooling2D(pool_size=(3, 3)),
           Flatten(),
           Dense(units=256, activation='relu'),
           Dense(units=128, activation='relu'),
           Dense(units=3, activation='softmax')
       ])

    # Unfreeze some of the top layers of the base model for fine-tuning
   # Freeze the pretrained layers so they are not trained during fine-tuning
    for layer in base_model.layers:
       layer.trainable = True

    
    # Compile the model
    classifier.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    # Print model summary
    print(classifier.summary())

    
    optimizer = Adam(learning_rate=0.001)
    classifier.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['accuracy'])

    
    # Define early stopping
    early_stopping = EarlyStopping(monitor='val_loss', patience=20, restore_best_weights=True)
    
    # Train the model
    history = classifier.fit(train_generator, epochs=100,
                             validation_data=val_generator,
                         validation_steps=30, verbose=2,
                         callbacks=[early_stopping])

    # -------------------YOUR CODE ENDS HERE---------------------------------------------#
    
    # list all data in history
    print(history.history.keys())
    import matplotlib.pyplot as plt
    # import matplotlib.image as mpimg
    
    plt.plot(history.history['loss'][:])
    plt.legend(['train'], loc='upper left')
    plt.ylabel('MSE loss')
    plt.xlabel('epoch')
    plt.title('Loss function MSE')
    plt.show()
    
    plt.plot(history.history['accuracy'])
    plt.legend(['train', 'val'], loc='upper left')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.title('Training and Validation Accuracy')
    plt.show()

    classifier.save("classifier.h5")
    return classifier


def load_saved_model(model_name):
    classifier=load_model(model_name)  
    print(classifier.summary())
    return classifier

def test_trained_network(classifier,img_width, img_height):
    test_datagen = ImageDataGenerator(rescale=1. / 255)
    val_datagen = ImageDataGenerator(rescale=1. / 255)


    val_generator = \
        val_datagen.flow_from_directory('data/validation_set'
            , target_size=(img_width, img_height), batch_size=32, class_mode='categorical')


    test_generator = \
        test_datagen.flow_from_directory('data/test'
            , target_size=(img_width, img_height), batch_size=32, class_mode='categorical')

    test_per_class=20

    test_generator = test_datagen.flow_from_directory(
        directory='data/test',
        target_size=(img_width, img_height),
        color_mode="rgb",
        batch_size=test_per_class,
        class_mode="categorical",
        shuffle=False)

    STEP_SIZE_VAL=val_generator.n//val_generator.batch_size
    scores_val = classifier.evaluate(val_generator, steps=STEP_SIZE_VAL)
    print("validation accuracy = ", scores_val[1])

    STEP_SIZE_TEST=test_generator.n//test_generator.batch_size
    scores_test=classifier.evaluate(test_generator, steps=STEP_SIZE_TEST)
    print("test accuracy = ", scores_test[1])


def predict_class_file(classifier,img_str,img_width, img_height):
    
    # PREDICT THE CLASS OF ONE IMAGE
    img = image.load_img(img_str, target_size=(img_width, img_height))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    images = np.vstack([x])
    classes = np.argmax(classifier.predict(images,batch_size=1),axis=1)
    class_names=("Cylinder","Square","Rectangle")
    print ("predicted the class:",classes[0],"code:",class_names[classes[0]])
    return classes[0],class_names[classes[0]]

def main():
    if os.path.exists("classifier.h5"):
        os.remove("classifier.h5")
    img_width=128 
    img_height=128
    # ------------------ YOUR CODE HERE-------------------------------------------------#

#   UNCOMMENT WHEN YOU WAN TO LOAD A MODEL INSTEAD OF TRAINING A NEW ONE
    #classifier=load_saved_model("classifier.h5") 
#   UNCOMMENT WHEN YOU WANT TO TRAIN A MODEL INSTEAD OF LOADING
    classifier=retrain_network(img_width, img_height) 
    
    # -------------------YOUR CODE ENDS HERE---------------------------------------------#
    test_trained_network(classifier,img_width, img_height)
    class_code,class_name=predict_class_file(classifier,"data/test_image.png",img_width, img_height)


if __name__ == '__main__':
    main()  