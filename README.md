 # Cargo Stowage Management System

## Overview
This project is a Cargo Stowage Management System designed for the National Space Hackathon 2025. It aims to optimize cargo placement, retrieval, and waste management in a space station environment.

## Features
- Placement recommendations
- Item search and retrieval
- Rearrangement optimization
- Waste management
- Time simulation

## Setup
1. Clone the repository.
2. Run `generate_samples.py` to create sample item data.
3. Run `generate_containers.py` to create sample container data.
4. Build the Docker image:
   ```bash
   docker build -t cargo-stowage-management .
