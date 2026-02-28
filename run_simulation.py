from order_book import OrderBook
from agents.noise_trader import NoiseTrader
from agents.manipulative_trader import SpoofTrader
from event_stream import EventLogger


def main():

    logger = EventLogger()
    order_book = OrderBook(event_logger=logger)

    agents = [NoiseTrader(f"noise_{i}") for i in range(5)]
    agents.append(SpoofTrader("spoof_1"))

    for step in range(500):
        for agent in agents:
            agent.act(order_book)

    logger.save("data/simulation_events.parquet")

    print("Simulation complete.")
    print("Events saved to simulation_events.parquet")


if __name__ == "__main__":
    main()