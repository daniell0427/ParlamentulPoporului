from random import *
from twilio.rest import Client 


account_sid = 'ACfd8f42b2319e166669e54f00026c5def' 
auth_token = '45f6a03597ba738beeb6fe0557f774c4' 
client = Client(account_sid, auth_token) 
a=randint(1000,9999)
message = client.messages.create(  
                            messaging_service_sid='MGa91850e937131d1178348517855ca354', 
                            body=a,      
                            to=
                        ) 