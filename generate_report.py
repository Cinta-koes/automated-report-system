import pandas as pd
from datetime import datetime
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import os

def generate_csv(df, filepath):
    filepath = f"reports/{filepath}.csv"
    os.makedirs("reports", exist_ok=True)
    df.to_csv(filepath, index=False)
    print(f"CSV report generated: {filepath}")
    return filepath

def generate_excel(df, filepath):
    filepath = f"reports/{filepath}.xlsx"
    os.makedirs("reports", exist_ok=True)
    df.to_excel(filepath, index=False)
    print(f"Excel report generated: {filepath}")
    return filepath

def generate_pdf(df, filepath, title="Report"):
    filepath = f"reports/{filepath}.pdf"
    os.makedirs("reports", exist_ok=True)
    
    doc = SimpleDocTemplate(filepath, pagesize=letter)
    elements = []
    styles = getSampleStyleSheet()
    
    # Add a title
    elements.append(Paragraph(title, styles['Title']))
    elements.append(Paragraph(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}", styles['Normal']))
    elements.append(Spacer(1, 12))

    # Convert DataFrame to a list of lists
    data = [df.columns.tolist()] + df.values.tolist()
    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    elements.append(table)

    doc.build(elements)
    print(f"PDF report generated: {filepath}")
    return filepath

# Testing
if __name__ == "__main__":
    from query_data import weekly_sales_summary, delayed_shipment_alert
    
    # Report 1: Weekly Sales Summary
    df_sales = weekly_sales_summary()
    generate_excel(df_sales, "weekly_sales_summary")
    generate_pdf(df_sales, "weekly_sales_summary", "Weekly Sales Summary")
    
    # Report 2: Delayed Shipment Report
    df_shipment = delayed_shipment_alert()
    generate_csv(df_shipment, "delayed_shipment_alert")