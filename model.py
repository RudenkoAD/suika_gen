import keras

class RecursiveModel(keras.Model):
    def __init__(self):
        super().__init__()
        self.recursive = keras.layers.Bidirectional(
            keras.layers.GRU(20)
        )
        self.base = keras.Sequential()
        self.base.add(keras.layers.Dense(40, activation="relu"))
        self.base.add(keras.layers.Dense(20, activation="relu"))
        self.base.add(keras.layers.Dense(4))
        self.base.add(keras.layers.Softmax())

    def call(self, inputs):
        x = self.recursive(inputs)
        x = self.base(x)
        return x