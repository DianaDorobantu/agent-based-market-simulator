"""
Level 3 order book implementation.

Features:
- Individual order tracking
- Full price level depth
- Partial fills
- Proper cancellation
- Event callbacks for logging
"""

import heapq
import uuid
from collections import defaultdict
from datetime import datetime, timezone


class Order:
    """
    Single L3 order.
    """

    def __init__(self, agent_id, side, price, quantity):
        self.id = str(uuid.uuid4())
        self.agent_id = agent_id
        self.side = side  
        self.price = price
        self.quantity = quantity
        self.timestamp = datetime.now(timezone.utc)


class OrderBook:
    """
    Level 3 Order Book.
    """

    def __init__(self, event_logger=None):
        '''
        Sets up:
            - a dictionary for active orders
            - price-level groupings for buy and sell orders
            - heaps for quick best-price access
            - a trade history list
            - optional event logger (dependency injection)
        '''

        self.active_orders = {}

        self.buy_levels = defaultdict(list)
        self.sell_levels = defaultdict(list)

        self.buy_prices = []   
        self.sell_prices = []  

        self.trade_history = []

        self.event_logger = event_logger



    def place_order(self, order: Order):

        self.active_orders[order.id] = order

        if order.side == "buy":
            if order.price not in self.buy_levels:
                heapq.heappush(self.buy_prices, -order.price)
            self.buy_levels[order.price].append(order)

        else:
            if order.price not in self.sell_levels:
                heapq.heappush(self.sell_prices, order.price)
            self.sell_levels[order.price].append(order)

        # Log NEW event
        if self.event_logger:
            self.event_logger.log_new(order)

        self.match_orders()



    def cancel_order(self, order_id):

        if order_id not in self.active_orders:
            return

        order = self.active_orders.pop(order_id)

        levels = self.buy_levels if order.side == "buy" else self.sell_levels

        levels[order.price] = [
            o for o in levels[order.price] if o.id != order_id
        ]

        if not levels[order.price]:
            del levels[order.price]

        # Log CANCEL event
        if self.event_logger:
            self.event_logger.log_cancel(order)

  
  
    def match_orders(self):

        while self.buy_prices and self.sell_prices:

            # Clean stale buy prices
            while self.buy_prices:
                best_bid = -self.buy_prices[0]
                if best_bid in self.buy_levels and self.buy_levels[best_bid]:
                    break
                heapq.heappop(self.buy_prices)

            # Clean stale sell prices
            while self.sell_prices:
                best_ask = self.sell_prices[0]
                if best_ask in self.sell_levels and self.sell_levels[best_ask]:
                    break
                heapq.heappop(self.sell_prices)

            if not self.buy_prices or not self.sell_prices:
                break

            best_bid = -self.buy_prices[0]
            best_ask = self.sell_prices[0]

            if best_bid < best_ask:
                break

            buy_order = self.buy_levels[best_bid][0]
            sell_order = self.sell_levels[best_ask][0]

            trade_qty = min(buy_order.quantity, sell_order.quantity)
            trade_price = best_ask

            trade = {
                "timestamp": datetime.utcnow(),
                "buy_agent": buy_order.agent_id,
                "sell_agent": sell_order.agent_id,
                "price": trade_price,
                "quantity": trade_qty
            }

            self.trade_history.append(trade)

            if self.event_logger:
                self.event_logger.log_trade(trade)

            buy_order.quantity -= trade_qty
            sell_order.quantity -= trade_qty

            if buy_order.quantity == 0:
                self.buy_levels[best_bid].pop(0)
                del self.active_orders[buy_order.id]

            if sell_order.quantity == 0:
                self.sell_levels[best_ask].pop(0)
                del self.active_orders[sell_order.id]