import smtplib

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

login_result = server.login("your_email@gmail.com", "your_password")  # App password
if "235" in str(login_result):   # 235 means Authentication successful
    message = "Subject: Test Mail\n\nThis is a test email."
    send_result = server.sendmail("your_email@gmail.com", "receiver_email@gmail.com", message)
    if send_result == {}:   # Empty dict means success
        print("Email sent successfully")
    else:
        print("Email sending failed")
else:
    print("Login failed")

server.quit()
