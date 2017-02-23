import vk
import time
from my_data import VkData
session = vk.AuthSession(app_id=VkData.APP_ID, user_login=VkData.LOGIN,user_password=VkData.GET_PAS(), scope='messages')
vkapi = vk.API(session)

#AGE_FROM = 18
#AGE_TO = 27
CITY = 2 #SPb
SEARCH = "фотограф"
users = vkapi.users.search(q=SEARCH,city=CITY,has_photo=1,sort=0,fields='domain',count=2000)
users_count = users[0]
print('Кол-во человек: %d'%(users_count))
users = users[1:]
#[print(user) for user in users]

file = open('../ph1500.txt','w')
i=0
for user in users:
    UID=user['uid']
    #friends = vkapi.friends.get(user_id=UID)
    #print(len(friends))
    time.sleep(0.3)
    #if ((len(friends) >= 1500)and(len(friends)<=3000)):
    out = vkapi.messages.getHistory(count=1, user_id=UID)
    print(out)
    if out[0] == 0:
       # print("можно отправить")
        file.write(str(UID) + '\n')
        print(UID)
        i=i+1
print(i)
file.close()