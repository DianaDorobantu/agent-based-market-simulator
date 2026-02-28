"""
Defines the base class for all agents in the simulation.
"""

from abc import ABC, abstractmethod

class BaseTrader(ABC):
    """
    Abstract class for a trading agent.
    All traders must implement the act() method.
    """

    def __init__(self, agent_id):
        """
        agent_id : str
            Unique identifier for this trader.
        """
        self.agent_id = agent_id

    @abstractmethod
    def act(self, order_book):
        """
        Define the trading action for this agent.
        
        order_book : OrderBook
            Reference to the market order book.

        This method should place or cancel orders.
        """
        pass