# financial_modeling

Visualizing Different Financial Modeling Techniques

This repository contains a minimal Python script that demonstrates how to:

- Install `yfinance`
- Fetch historical closing prices from Yahoo Finance
- Print those prices to the console

## Setup

1. Clone the repo:
   ```bash
   git clone https://github.com/<your‐username>/financial_modeling.git
   cd financial_modeling
   ```

## Running via Docker

You can build and run this project in a container—no need to install anything except Docker itself.

1. **Build the Docker image**  
   From the repo root (where `Dockerfile` lives), run:
   ```bash
   docker build -t financial_modeling .
   ```

In total the workflow will look like this:

git clone https://github.com/Samir0051/financial_modeling.git
cd financial_modeling
docker build -t financial_modeling .
docker run --rm financial_modeling
