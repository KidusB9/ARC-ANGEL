from tensorflow.keras.layers import Dropout
from tensorflow.keras.callbacks import ModelCheckpoint

model = Sequential()
model.add(LSTM(128, input_shape=(maxlen, len(chars)), return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(128))
model.add(Dropout(0.2))
model.add(Dense(len(chars), activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer=RMSprop(lr=0.01))

# Add model checkpoints
filepath = "weights.best.hdf5"
checkpoint = ModelCheckpoint(filepath, monitor='loss', verbose=1, save_best_only=True, mode='min')
callbacks_list = [print_callback, checkpoint]

model.fit(X, y, batch_size=128, epochs=25, callbacks=callbacks_list)
