import smtplib

my_email = "appbrewerytesting@gmail.com"
password = "fwviehfiewcjypkr"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="appbreweryinfo@gmail.com", msg="Subject:Hello\n This is the body of my email")
    connection.close()