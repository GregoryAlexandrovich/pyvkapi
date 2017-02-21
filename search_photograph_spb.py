import vk
import time
from my_data import VkData
session = vk.AuthSession(app_id=VkData.APP_ID, user_login=VkData.LOGIN,user_password=VkData.GET_PAS(), scope='messages')
vkapi = vk.API(session)

#MESSAGE = 'Привет!Это сообщение отправлено из скрипта. Если это читаешь, значит скрипт работает)'

#AGE_FROM = 18
#AGE_TO = 27
#CITY = 2 #SPb
#SEARCH = "фотограф"
#users = vkapi.users.search(q=SEARCH,city=CITY,has_photo=1,sort=0,fields='domain',count=1000)
#users_count = users[0]
#print('Кол-во человек: %d'%(users_count))
#users = users[1:]
#[print(user) for user in users]
#i=0
#f = open('../ph2.txt','w')
#f2 = open('../ph_mk.txt','r')

#MESSAGE = 'Привет! Приходи на двухдневный workshop Сергея Рожнова в СПб. Подробнее в группе https://vk.com/mkwedspb'

users = f2.read()
#print(users)
f2.close()
for user in users:
    UID=user['uid']
#    friends = vkapi.friends.get(user_id=UID)
    #i+=1
    #print(i)
    #print(len(friends))
    time.sleep(0.3)
#    if len(friends) <= 1500:
    f.write(str(UID) + '\n')
        #print(UID)
f.close()