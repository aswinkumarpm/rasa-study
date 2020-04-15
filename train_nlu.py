import json

from rasa_nlu.training_data import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer
from rasa_nlu import config
from rasa_nlu.model import Metadata, Interpreter



training_data = load_data("data/nlu.md")

# trainer to educate our pipeline
trainer = Trainer(config.load("test_config.yml"))

# train the model!
interpreter = trainer.train(training_data)

# store it for future use
model_directory = trainer.persist("./models/nlu", fixed_model_name="current")

def pprint(o):
   print(json.dumps(o, indent=2))
pprint(interpreter.parse("I am unhappy"))

# Functions
#------------
def train (data, config_file, model_dir):
    training_data = load_data(data)
    trainer = Trainer(config.load(config_file))
    trainer.train(training_data)
    model_directory = trainer.persist(model_dir, fixed_model_name = 'chat')

# Training
#------------
train('data/nlu_train.md', 'nlu_config.yml', 'models/nlu')