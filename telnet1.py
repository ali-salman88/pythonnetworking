import email. message, email.utils, email.policy, sys
from pprint import pprint
import socket

info=socket.getaddrinfo('www.google.com','telnet',0,socket.SOCK_STREAM,0,socket.AI_PASSIVE)
pprint(info)
respons=str (info)
message=email.message.EmailMessage(email.policy.SMTP)
message['To']="alisalmanhussein@yahoo.com"
message['From']='Test message <alisalmanhussein@gmail.com>'
message['Subject']='this is test using python'
message['Date']=email.utils.formatdate(localtime=True)
message['message-id']=email.utils.make_msgid()
message.set_content(respons)
sys.stdout.buffer.write(message.as_bytes())

