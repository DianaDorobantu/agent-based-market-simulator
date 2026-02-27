# Agent-Based Market Simulator

An agent-based L3 LOB (Level 3 Limit Order Book) simulator designed for market microstructure research and market surveillance experimentation.

This project implements a fully event-driven L3 LOB with individual order tracking.

## 📖 Overview
It is designed for:

- Market microstructure research
- Manipulation pattern simulation (spoofing, layering, wash trading, etc.)
- Surveillance model development
- High-frequency trading experiments
- Academic experimentation with synthetic order flow

The simulator produces realistic order-level event logs compatible with downstream detection systems.

## 🧠 Key Features
- Full Level 3 order book (individual order tracking)
- Price-time priority matching
- Partial fills and cancellations
- Agent-based order generation
- Manipulative behavior simulation
- Standardized event logging (CSV / Parquet)
- Modular and extensible architecture


## 🔬 Research Motivation

Modern electronic markets operate at microsecond resolution.
Understanding order-level dynamics is essential for studying
market manipulation, liquidity formation and surveillance systems.

This simulator provides a controlled environment to study
L3 LOB behavior and agent interactions.

Use Cases:
- Market manipulation detection
- Order cancellation analysis
- Liquidity modeling
- Order flow imbalance studies
- Anomaly detection in high-frequency markets

## 🚀 Quick Start
```sh
git clone https://github.com/DianaDorobantu/agent-based-market-simulator.git
cd agent-based-market-simulator
pip install -r requirements.txt
python experiments/run_simulation.py
```
