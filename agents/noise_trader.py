import random
from agents.base_trader import BaseTrader
from order_book import Order


class NoiseTrader(BaseTrader):

    def act(self, order_book):

        side = random.choice(["buy", "sell"])
        price = random.uniform(95, 105)
        quantity = random.randint(1, 5)

        order = Order(self.agent_id, side, price, quantity)
        order_book.place_order(order)