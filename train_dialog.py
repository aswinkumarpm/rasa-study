import logging
from rasa_core import training
from rasa_core.actions import Action
from rasa_core.agent import Agent
from rasa_core.domain import Domain
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.featurizers import MaxHistoryTrackerFeaturizer, BinarySingleStateFeaturizer
from rasa_core.interpreter import RegexInterpreter
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.policies import FallbackPolicy, KerasPolicy, MemoizationPolicy, FormPolicy
fallback = FallbackPolicy(fallback_action_name="utter_default",
                          core_threshold=0.2,
                          nlu_threshold=0.1)
from rasa_core import config as policy_config
policies = policy_config.load("policy.yml")

# - name: KerasPolicy
# epochs: 100
# max_history: 3
# - name: MemoizationPolicy
# max_history: 3
# - name: FallbackPolicy
# nlu_threshold: 0.1
# core_threshold: 0.2
# fallback_action_name: 'utter_default'
# - name: FormPolicy


# Function
#------------
def train_dialog(dialog_training_data_file, domain_file, path_to_model = 'models/dialogue'):
    logging.basicConfig(level='INFO')

    agent = Agent(domain_file,
              policies=[KerasPolicy(epochs=100, max_history=3), MemoizationPolicy(max_history=3), fallback, FormPolicy()])
    training_data = agent.load_data(dialog_training_data_file)
    agent.train(
        training_data)
    agent.persist(path_to_model)

# Train
#--------
train_dialog('data/stories.md', 'domain.yml')

rasaNLU = RasaNLUInterpreter("models/nlu/default/chat")
agent = Agent.load("models/dialogue", interpreter= rasaNLU)

# asking question
agent.handle_text('Hi')


# once more
agent.handle_text('How many days in January')

# once more
agent.handle_text('How many days in April')


# once more
agent.handle_text('Bye')