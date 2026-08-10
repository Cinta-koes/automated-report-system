import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import os

def send_report_email(filepath, recipient_email, subject, body):
    """Kirim file report sebagai attachment lewat email."""
    
    # Ambil kredensial dari environment variable (JANGAN hardcode password di kode!)
    sender_email = os.environ.get("EMAIL_SENDER")
    sender_password = os.environ.get("EMAIL_PASSWORD")
    
    if not sender_email or not sender_password:
        raise ValueError("EMAIL_SENDER dan EMAIL_PASSWORD belum di-set sebagai environment variable")
    
    # Bikin email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'plain'))
    
    # Attach file report
    with open(filepath, "rb") as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
    
    encoders.encode_base64(part)
    filename = os.path.basename(filepath)
    part.add_header('Content-Disposition', f'attachment; filename={filename}')
    msg.attach(part)
    
    # Kirim email lewat Gmail SMTP
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
    
    print(f"✅ Email sent to {recipient_email} with attachment: {filename}")


# Testing
if __name__ == "__main__":
    send_report_email(
        filepath="reports/weekly_sales_summary.xlsx",
        recipient_email="cinta.koes15@gmail.com",
        subject="Weekly Sales Summary Report",
        body="Please find attached this week's sales summary report."
    )