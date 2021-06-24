import tensorflow as tf
from keras.layers import (LSTM, Dense, Conv1D, Embedding, Concatenate, \
                          Bidirectional, TimeDistributed, GlobalMaxPooling1D)

MAX_LEN_CHAR = 20
MAX_LEN_SENT = 128
WORD_EMBEDDING_SIZE = 300

KERNEL = 3
FILTERS = 15
CHAR_EMBEDDING_SIZE = 15

NEURONS_LSTM = 64
NUERONS_DENSE = 64


class BiLSTM(tf.keras.Model):
    def __init__(self, word_size, char_size, n_class):
        super(BiLSTM, self).__init__()
        # branch word embedding
        self.word = Embedding(input_dim=word_size,
                              input_length=MAX_LEN_SENT,
                              output_dim=WORD_EMBEDDING_SIZE
                             )

        # branch char embedding
        self.char = TimeDistributed(Embedding(input_dim=char_size,
                                              input_length=MAX_LEN_CHAR,
                                              output_dim=CHAR_EMBEDDING_SIZE
                                              ))
        self.conv1d = TimeDistributed(Conv1D(padding='valid',
                                             filters=FILTERS,
                                             kernel_size=KERNEL,
                                             activation='relu'))
        self.pool = TimeDistributed(GlobalMaxPooling1D())
        
        # join branchs
        self.concat = Concatenate(axis=-1)

        self.bilstm = Bidirectional(LSTM(NEURONS_LSTM, return_sequences=True))
        
        self.dense = Dense(64, activation='tanh')
        self.softmax = Dense(n_class, activation='softmax')

    def call(self, inputs, training=False):
        """
         Forward pass
        """
        
        # branch word embedding
        word_embeddings = self.word(inputs[1])

        # branch char embedding
        c = self.char(inputs[0])
        c = self.conv1d(c)
        char_embeddings = self.pool(c)

        # join branchs
        x = self.concat([word_embeddings, char_embeddings])
        
        x = self.bilstm(x)

        if training:
            pass
        
        x = self.dense(x)
        x = self.softmax(x)
        return x
