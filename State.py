from collections import namedtuple
import numpy as np

class State():
    """
    Base class for state
    """
    def __init__(self, ):
        """
        Initializes the model

        :param state_variable: list(str) - state variable dimension names
        :param decision_variable: list(str) - decision variable dimension names
        :param state_0: dict - needs to contain at least the information to populate initial state using state_names
        :param exog_info_fn: function - calculates relevant exogenous information
        :param transition_fn: function - takes in decision variables and exogenous information to describe how the state
               evolves
        :param objective_fn: function - calculates contribution at time t
        :param seed: int - seed for random number generator
        """

    def build_state(self, info):
        """
        this function gives a state containing all the state information needed

        :param info: dict - contains all state information
        :return: namedtuple - a state object
        """
        return self.State(*[info[k] for k in self.state_variable])

    def transition_fn(self, decision, exog_info):
        """
        this function takes in the decision and exogenous information to update the state

        :param decision: namedtuple - contains all decision info
        :param exog_info: any exogenous info (in this asset selling model,
               the exogenous info does not factor into the transition function)
        :return: dict - updated resource
        """
        new_resource = 0 if decision.sell is 1 else self.state.resource
        return {"resource": new_resource}
