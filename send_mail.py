
import smtplib
from email.mime.text import MIMEText


def send_mail(customer,dealer,rating,comments):
    port=2525
    smpt_server="smpt.mailtrap.io"
    login="603df197f90b1a"
    password="dcd477fb987166"
    message=f"<h3> new feedback submission </h3><ul><li> customer:{customer}</li><li> dealer:{dealer}</li><li> rating:{rating}</li><li> comments:{comments}</li></ul>"
    sender_email="ashokroyal36@gmail.com"
    recevier_email="bogemnarendra8@gmail.com"
    msg=MIMEText(message,"html")
    msg["Subject"]="lexus feedback"
    msg["From"]=sender_email
    msg["To"]=recevier_email

    with smtplib.SMTP(smpt_server,port ) as server :
        server.login(login,password)
        server.sendmail(sender_email,recevier_email,msg.as_string())


