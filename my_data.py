class VkData:
    f = open('../data.txt', 'r')
    f.readline().rstrip()
    MY_USER_ID = f.readline().rstrip()
    DUROV_USER_ID = '1'
    API_URL = 'https://api.vk.com/method/'
    APP_ID = f.readline().rstrip()
    LOGIN = f.readline().rstrip()
    f.close()

    #print(MY_USER_ID)
    #print(APP_ID)
    #print(LOGIN)
    @staticmethod
    def GET_PAS():
        f = open('../data.txt','r')

        pas=f.readline().rstrip()

        f.close()
        return pas
if __name__ == '__main__':
    pas = VkData.GET_PAS()
    #print(pas)