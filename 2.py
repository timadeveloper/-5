

import json

class Model:
    def __init__(self, title, author, other_attribute):
        self.title = title
        self.author = author
        self.other_attribute = other_attribute

    def save(self, filename):
        data = {attr: getattr(self, attr) for attr in dir(self) if not attr.startswith('_') and not callable(getattr(self, attr))}
        with open(filename, 'w') as json_file:
            json.dump(data, json_file, indent=2)

model_instance = Model(title='Какой-то заголовок', author='Какой-то автор', other_attribute='Другой атрибут')

model_instance.save('model_data.json')
