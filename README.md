# Agent-Based Market Simulator

An agent-based L3 LOB (Level 3 Limit Order Book) simulator designed for market microstructure research and market surveillance experimentation.

## Overview
It is designed for:

- Market microstructure research
- Manipulation pattern simulation (spoofing, layering, wash trading, etc.)
- Surveillance model development
- High-frequency trading experiments
- Academic experimentation with synthetic order flow

The simulator produces realistic order-level event logs compatible with downstream detection systems.

## Key Features
- Full Level 3 order book (individual order tracking)
- Price-time priority matching
- Partial fills and cancellations
- Agent-based order generation
- Manipulative behavior simulation
- Standardized event logging (CSV / Parquet)
- Modular and extensible architecture


## Research Motivation

Modern electronic markets operate at microsecond resolution.
Understanding order-level dynamics is essential for studying
market manipulation, liquidity formation and surveillance systems.


## Steps to Replicate Results

1. Clone the repository to your local machine.
2. Setup the environment by ensuring that Python and the required libraries are installed, as specified in the `requirements.txt` file.
3. Open and run `run_simulation.py` to perform the simulation.
5. Open and run `inspect_parquet.py` in order to review the data.
