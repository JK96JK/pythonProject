import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.callbacks import Callback
import matplotlib.pyplot as plt

# Load and preprocess the MNIST dataset
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalize the pixel values to [0, 1] and reshape the images to 784-dimensional vectors
x_train = x_train.reshape(x_train.shape[0], 784).astype('float32') / 255
x_test = x_test.reshape(x_test.shape[0], 784).astype('float32') / 255

# Convert labels to one-hot encoding
y_train = tf.keras.utils.to_categorical(y_train, 10)
y_test = tf.keras.utils.to_categorical(y_test, 10)

# Define a custom callback to suppress output
class SilentCallback(Callback):
    def on_epoch_end(self, epoch, logs=None):
        pass

# Define the neural network model
model = Sequential()
# Hidden layer with 128 neurons, increasing neurons increases accuracy, but too many may cause overfitting and it will not work as
# well on anything but training data it was trained on. Too low and it cant capture enough information from data to be accurate.
model.add(Dense(128, input_dim=784, activation='sigmoid'))
# Output layer for 10 classes
model.add(Dense(10, activation='softmax'))

#Define learing rate for optimizer,
optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)
# Compile the model
model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model with a silent callback
#add ,callbacks=[SilentCallback()] as last argument after verbose=2 to mute epochs, also set verbose=0
#Increacing epochs increases accuracy untill its too high, when it will start to work poorly on other data than training one (overfitting).
# Too low epochs and it underfits and it cant learn enough.
# Lower batch_size makes training slower, higher makes it faster but more memory hungry and if it is too high may overfit. So choose correctly for your data, I left it to 64.
history = model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=20 , batch_size=64, verbose=2)

# Evaluate the model on training data
train_loss, train_accuracy = model.evaluate(x_train, y_train, verbose=0)
print(f'Training Accuracy: {train_accuracy * 100:.2f}%')

# Evaluate the model on test data
test_loss, test_accuracy = model.evaluate(x_test, y_test, verbose=0)
print(f'Test Accuracy: {test_accuracy * 100:.2f}%')

# Plot the training loss curve
plt.figure(figsize=(8, 6))
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Training and Validation Loss Curve')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.grid()
plt.show()