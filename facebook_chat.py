from fbchat import Client
import fbchat

client1=Client("Your Email or Phone","Facebook Password")
#Logging into facebook
checklogin=client1.isLoggedIn()
#Login successfully return True
print(checklogin)
#o/p: True

####Find Top 5 users with same name with different User-Id
Tot_Users_with_same_name=client1.searchForUsers("Rajeev Kumar",5)
for user in Tot_Users_with_same_name:
    print(user)
###o/p:
####<USER Rajeev Kumar (100003149965719)>
####<USER Rajeev Kumar (100002938065104)>
####<USER Rajeev Kumar (100001330735025)>
####<USER Rajeev Kumar (100003575685008)>
####<USER Rajeev Kumar (100003679172501)>

#Getting User name and Id of Rajeev Kumar
friends=client1.searchForUsers("Rajeev Kumar")
print(friends[0])
#o/p:<USER Rajeev Kumar (100003149965719)>

print(friends[0].uid)
#o/p:100003149965719

#Getting Fb User Id of Rajeev Kumar
uiid=friends[0].uid
#Sending message to Rajeev Kumar
client1.send(fbchat.models.Message("Hello ...."),uiid)
client1.send(fbchat.models.Message(":) Smile"),uiid)

##Getting Page id of the Fabebook page
pageid=client1.searchForPages("Krishna Kumar Gupta")
print(pageid[0])
#o/p:1472339113054688
uiid=pageid[0].uid
#Sending message to FB Page
client1.send(fbchat.models.Message("Hello ...."),uiid)
