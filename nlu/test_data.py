import yaml
import json

data = yaml.safe_load(open('train.yml', 'r'))

print(data)
print(data['commands'][1])
print(type(data['commands'][1]))
print(type(data))