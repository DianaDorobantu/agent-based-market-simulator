import random
from agents.base_trader import BaseTrader
from order_book import Order


class SpoofTrader(BaseTrader):

    def __init__(self, agent_id):
        super().__init__(agent_id)
        self.active_spoofs = []

    def act(self, order_book):

        # Cancel previous spoof orders
        for oid in self.active_spoofs:
            order_book.cancel_order(oid)

        self.active_spoofs = []

        base_price = random.uniform(99, 101)

        # Place multiple layered spoof orders
        for i in range(3):

            side = random.choice(["buy", "sell"])
            price = base_price + (i * 0.2 if side == "sell" else -i * 0.2)
            quantity = random.randint(50, 100)

            order = Order(self.agent_id, side, price, quantity)
            order_book.place_order(order)

            self.active_spoofs.append(order.id)