import yaml
import json
import os
import numpy as np
import tensorflow as tf
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import LSTM, Dense
from keras import utils

## Reading a data

data = yaml.safe_load(open('train.yml').read())
inputs, entities, actions = [], [], []


for command in data['commands']:
    inputs.append(str(command['input'].lower()))
    entities.append(str(command['entity'].lower()))
    actions.append(str(command['action'].lower()))

print(inputs)
print(entities)
print(actions)
print(inputs[5], entities[5], actions[5])
''''## Creating a data set

chars = set()

## Reading all chars from dataset:

for i in inputs + outputs:
    for ch in i:
        if ch not in chars:
            chars.add(ch)

## Map each character to an index

chr2idx = {}
idx2chr = {}

for k, ch in enumerate(chars):
    chr2idx[ch]
    idx2chr[k]

## Create input data

print(inputs)
max_sent = max([len(x) for x in inputs]) ## max input sequence
print(max_sent)
print(len(chars))

## Create arrays

input_data = np.zeros((len(inputs), max_sent, len(chars)), dtype='int32')

for i, input in enumerate(inputs):
    for k, ch in enumerate(input):
        input_data[i, k, chr2idx[ch]] = 1 ## one-hot encoding

print(input_data.shape)

input_data = np.zeros((len(inputs), max_sent, len(chars)), dtype='int32')
print(input_data.shape)
'''
