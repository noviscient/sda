"""
Model class
"""
import numpy as np

class Model():
    """
    Base class for exogenous information
    """

    def __init__(self):
        pass


    def contribution_fn(state, decision):
        """
        this function calculates the contribution, which depends on the decision and ...

        :param state: contains all decision info
        :param decision: contains all decision info
        :param exog_info: any exogenous info 
        :return: float - calculated contribution
        """
        sell_size = 1 if decision.sell is 1 and state.resource != 0 else 0
        contribution =  state.price * sell_size
        return contribution

    def step(self, decision):
        """
        this function steps the process forward by one time increment by updating the sum of the contributions, the
        exogenous information and the state variable

        :param decision: contains all decision info
        :return: none
        """
        exog_info = self.exog_info_fn()
        self.objective += self.objective_fn(decision, exog_info)
        exog_info.update(self.transition_fn(decision, exog_info))
        self.state = self.build_state(exog_info)