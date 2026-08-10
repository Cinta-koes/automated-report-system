import schedule
import time
from send_email import send_report_email
from generate_report import generate_excel, generate_pdf, generate_csv
from query_data import weekly_sales_summary, delayed_shipment_alert

MANAGER_EMAIL = "cinta.koes15@gmail.com"
FULFILLMENT_EMAIL = "cinta.koes15@gmail.com"

def run_weekly_sales_report():
    """Job 1: Generate & kirim Weekly Sales Summary — tiap Senin."""
    print("Running weekly sales report job...")
    
    df = weekly_sales_summary()
    filepath = generate_excel(df, "weekly_sales_summary")
    
    send_report_email(
        filepath=filepath,
        recipient_email=MANAGER_EMAIL,
        subject="Weekly Sales Summary Report",
        body="Please find attached this week's sales summary, broken down by region and category."
    )
    
    print("Weekly sales report job completed.\n")


def run_delayed_shipment_alert():
    """Job 2: Generate & kirim Delayed Shipment Alert — setiap hari."""
    print("Running delayed shipment alert job...")
    
    df = delayed_shipment_alert()
    
    if df.empty:
        print("No delayed shipments found today. Skipping email.\n")
        return
    
    filepath = generate_csv(df, "delayed_shipment_alert")
    
    send_report_email(
        filepath=filepath,
        recipient_email=FULFILLMENT_EMAIL,
        subject="Delayed Shipment Alert",
        body=f"There are {len(df)} orders with shipping delays exceeding 7 days. Please review and investigate."
    )
    
    print("Delayed shipment alert job completed.\n")


# Jadwal
schedule.every().monday.at("08:00").do(run_weekly_sales_report)
schedule.every().day.at("09:00").do(run_delayed_shipment_alert)

print("Scheduler started. Waiting for scheduled jobs...")
print("Weekly Sales Report: every Monday at 08:00")
print("Delayed Shipment Alert: every day at 09:00")

while True:
    schedule.run_pending()
    time.sleep(60)
