import vk
import time
from my_data import VkData
session = vk.AuthSession(app_id=VkData.APP_ID, user_login=VkData.LOGIN,user_password=VkData.GET_PAS(), scope='messages')
vkapi = vk.API(session)
#MESSAGE = 'привет. Приходи на двухдневный workshop по свадебной фотографии Сергея Рожнова в СПб. 1й день - теория+обработка+пресеты и экшены, 2й - полноценная съемка для портфолио. Подробнее в группе https://vk.com/mkwedspb'
MESSAGE = 'МК свадебного фотографа Сергея Рожнова в СПб будет проходить два дня, 1-2 апреля. 1й день - теория+обработка+пресеты и экшены, 2й - полноценная съемка для портфолио. Подробнее в группе https://vk.com/mkwedspb'
f = open('../ph.txt','r')
i=1
name=''
for line in f:
    print(line.strip())
    time.sleep(0.25)
    g=vkapi.users.get(user_id=line.strip(),fields='first_name,can_write_private_message')
    print(g)
    for fild in g:
        can = fild['can_write_private_message']
        print(can)
        name = fild['first_name']
        print(name)

    if can==1:
        print((name+', '+MESSAGE))
        out=vkapi.messages.getHistory(count=1,user_id=line.strip())
        if out[0]==0:
            print("можно отправить")
            vkapi.messages.send(user_id=line.strip(), message=(name+', '+MESSAGE))
            time.sleep(30)
        else:
            print("Уже писали этому пользователю")
            time.sleep(30)
    i+=1
    if i>9: break
f.close()


