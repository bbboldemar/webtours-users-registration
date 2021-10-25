import requests
port = int(input('Номер порта: '))
user_base_size = int(input('Количество пользователей: '))
sign_up = 'http://localhost:'+str(port)+'/cgi-bin/login.pl'


try:
    for i in range (1, user_base_size + 1):
        new_user = {
        'username' : 'user'+str(i),
        'password' : 'pass'+str(i),
        'passwordConfirm' : 'pass'+str(i),
        'firstName' : 'FirstName'+str(i),
        'lastName' : 'LastName'+str(i),
        'address1' : 'Str'+str(i),
        'address2' :'0'+str(i),
        'register.x' : '26',
        'register.y' : '1'}
        requests.post(sign_up, new_user)
        print ('user № ' + str(i) + ' created')
    print (new_user['username'])
    print (new_user['password'])
    print ('Типовой логин/пароль: user*/pass*, где * - цифра от 1 до введеного колличества пользователей.')
except:
    print ('Некорректные введенные данные')    