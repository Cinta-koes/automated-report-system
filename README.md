# Automated Report Delivery System

A Python-based system that automatically queries a SQL database, generates business reports in multiple formats, and delivers them via scheduled email — simulating a real-world data reporting pipeline.

## Overview

This project was built to demonstrate an end-to-end reporting workflow: from querying raw transactional data, transforming it into meaningful business insights, generating formatted reports, and delivering them automatically on a recurring schedule — without any manual intervention.

## What It Does

The system generates two types of reports:

**1. Weekly Sales Summary**
Aggregates total sales by region and category, giving management a clear view of performance across the business. Delivered every Monday.

**2. Delayed Shipment Alert**
Flags orders where shipping time exceeds a 7-day SLA threshold, helping the fulfillment team quickly identify and investigate delays. Delivered daily.

## How It Works
1. **`setup_db.py`** — Loads raw data into a SQLite database
2. **`query_data.py`** — Runs SQL queries to aggregate data for each report type
3. **`generate_report.py`** — Converts query results into CSV, Excel, or PDF files
4. **`send_email.py`** — Emails the generated report with the file attached
5. **`main.py`** — Schedules and orchestrates the entire pipeline to run automatically

## Tech Stack

- **Python** — core logic
- **SQLite** — database
- **Pandas** — data querying and transformation
- **ReportLab** — PDF generation
- **OpenPyXL** — Excel export
- **smtplib** — email delivery
- **schedule** — task scheduling

## Key Features

- SQL-based data aggregation using `GROUP BY` and date calculations
- Multi-format report generation (CSV, Excel, PDF) with custom PDF styling
- Automated email delivery with file attachments
- Scheduled execution (no manual triggering required)
- Environment-variable based credential handling (no hardcoded secrets)

## Getting Started

```bash
# Clone the repo
git clone https://github.com/[username]/automated-report-system.git
cd automated-report-system

# Set up virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Set up the database
python setup_db.py

# Set email credentials (as environment variables)
export EMAIL_SENDER="your-email@gmail.com"
export EMAIL_PASSWORD="your-app-password"

# Run the scheduler
python main.py
```

## Project Structure
automated-report-system/
├── data/ # Source data & database
├── reports/ # Generated report outputs
├── setup_db.py # Database initialisation
├── query_data.py # SQL queries for report data
├── generate_report.py # Report generation (CSV/Excel/PDF)
├── send_email.py # Email delivery logic
├── main.py # Scheduler & orchestration
└── requirements.txt # Python dependencies
