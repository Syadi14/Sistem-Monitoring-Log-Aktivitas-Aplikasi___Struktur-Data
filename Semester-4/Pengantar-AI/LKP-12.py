import numpy as np

class SimpleNeuralNetwork:
    

    def __init__(self, input_size, hidden_size, output_size):

        # Inisialisasi bobot dan bias
        self.W1 = np.random.randn(input_size, hidden_size) * 0.01
        self.b1 = np.zeros((1, hidden_size))

        self.W2 = np.random.randn(hidden_size, output_size) * 0.01
        self.b2 = np.zeros((1, output_size))

    # Fungsi aktivasi ReLU
    def relu(self, x):
        return np.maximum(0, x)

    # Turunan ReLU
    def relu_derivative(self, x):
        return (x > 0).astype(float)

    # Forward propagation
    def forward(self, X):

        self.z1 = np.dot(X, self.W1) + self.b1   # hidden input
        self.a1 = self.relu(self.z1)             # hidden output
        self.z2 = np.dot(self.a1, self.W2) + self.b2   # output layer

        return self.z2

    # Backward propagation
    def backward(self, X, y, y_pred, lr):

        # Hitung error
        error = y_pred - y

        # Gradien output layer
        dW2 = np.dot(self.a1.T, error) / X.shape[0]
        db2 = np.sum(error, axis=0, keepdims=True) / X.shape[0]

        # Propagasi ke hidden layer
        dA1 = np.dot(error, self.W2.T)
        dZ1 = dA1 * self.relu_derivative(self.z1)

        # Gradien hidden layer
        dW1 = np.dot(X.T, dZ1) / X.shape[0]
        db1 = np.sum(dZ1, axis=0, keepdims=True) / X.shape[0]

        # Update bobot
        self.W2 -= lr * dW2
        self.b2 -= lr * db2

        self.W1 -= lr * dW1
        self.b1 -= lr * db1

    # Training
    def train(self, X, y, epochs, lr):

        for epoch in range(epochs):

            # Forward
            y_pred = self.forward(X)

            # Hitung loss
            loss = np.mean((y - y_pred) ** 2)

            # Backward
            self.backward(X, y, y_pred, lr)

            if epoch % 100 == 0:
                print(f"Epoch {epoch}, Loss: {loss}")