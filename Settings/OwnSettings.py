import smtplib

def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('pisivasa@gmail.com', 'V24P01.2006G')            #replace with master/sender email id and app-password generated from email provider
    server.sendmail('pisivasa@gmail.com', to, content)
    server.close()