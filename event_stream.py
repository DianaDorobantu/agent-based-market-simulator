"""
Standardized event logging for L3 surveillance research.
"""
import pandas as pd

class EventLogger:

    def __init__(self):
        self.events = []

    def log_new(self, order):
        self.events.append({
            "timestamp": order.timestamp,
            "event_type": "NEW",
            "order_id": order.id,
            "agent_id": order.agent_id,
            "side": order.side,
            "price": order.price,
            "quantity": order.quantity
        })

    def log_cancel(self, order):
        self.events.append({
            "timestamp": order.timestamp,
            "event_type": "CANCEL",
            "order_id": order.id,
            "agent_id": order.agent_id,
            "side": order.side,
            "price": order.price,
            "quantity": order.quantity
        })

    def log_trade(self, trade):
        self.events.append({
            "timestamp": trade["timestamp"],
            "event_type": "TRADE",
            "buy_agent": trade["buy_agent"],
            "sell_agent": trade["sell_agent"],
            "price": trade["price"],
            "quantity": trade["quantity"]
        })

    def save(self, filename="events.parquet"):

        df = pd.DataFrame(self.events)

        # Ensure timestamp column exists
        if "timestamp" not in df.columns:
            raise ValueError("No timestamp column found in events.")

        # Force everything to datetime with UTC
        df["timestamp"] = pd.to_datetime(
            df["timestamp"],
            errors="coerce",
            utc=True
        )

        # Drop rows with invalid timestamps (optional but safe)
        df = df.dropna(subset=["timestamp"])

        df.to_parquet(filename, index=False)