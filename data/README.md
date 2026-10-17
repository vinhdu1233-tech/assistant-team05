# Data Documentation

## Overview
This directory contains sample office information
used by the Smart Virtual Assistant project
developed by Team 05.

## Data Source
The `offices.csv` dataset is based on the sample
data provided for CSC10014 Lab 1.

The records are for demonstration and testing
purposes, not verified official university information.

## Dataset
- `offices.csv`: Contains office names, room
  locations, and opening hours.

## Data Structure

| Column | Description | Example |
|--------|-------------|---------|
| `name` | Name of the campus office | IT Helpdesk |
| `room` | Office room number | E.005 |
| `hours` | Office opening hours | Mon-Fri 08:00-17:00 |

## Data Ownership
Member 4 (dmdung2520) of Team 05 is responsible for maintaining
the sample dataset and documenting its structure.

## Data Management Guidelines
- Maintain the column names `name`, `room`, and `hours`.
- Keep the CSV format consistent.
- Do not include sensitive or personal information.
- Review dataset changes to maintain compatibility
  with the assistant backend and automated tests.

## Current Status
The sample dataset is included as part of
the initial Lab 1 project setup.

### Adding New Records
1. Open the `data/offices.csv` file.
2. Add a new row following the format: `name,room,hours`.
3. Ensure all required fields contain valid, non-empty values.
4. Verify that the office name is not duplicated.

### Sample Data Disclaimer
The current records in `data/offices.csv` are **sample/mock data** intended for system testing and demonstration purposes only. They have not been fully verified against real-time administrative records.