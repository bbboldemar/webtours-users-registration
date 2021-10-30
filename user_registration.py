def install_and_import(package):
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        import subprocess
        import sys
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", package]
        )
    finally:
        globals()[package] = importlib.import_module(package)


def settings(port, localhost):
    if port == "":
        port = '1080'
    print('port: {}'.format(port))

    if localhost == "":
        localhost = 'localhost'
    print('url: {}'.format(localhost))
    return {'localhost': localhost, 'port': port}


if __name__ == "__main__":
    try:
        import requests
    except:
        install = input(
            'Install Requests — 3-rd party library for Python (Y/N)?'
        )
        if install in ["y", "Y", ""]:
            install_and_import('requests')
        else:
            print('Exit')
            raise SystemExit

    port = input(
        'port: (by default "1080", press enter to skip)'
    )
    localhost = input(
        'server url: (by default "localhost", press enter to skip)'
    )
    user_base_size = input(
        'Number of created users: '
    )

    data = settings(port, localhost)
    sign_up = 'http://{}:{}/cgi-bin/login.pl'.format(
        data['localhost'],
        data['port']
    )
    welcome_page = 'http://{}:{}/webtours/'.format(
        data['localhost'],
        data['port']
    )
    try:
        requests.get(welcome_page)
    except:
        print("Can't reach 'WebTours' server")
        raise SystemExit

    try:
        user_base_size = int(user_base_size)
        for i in range(1, user_base_size + 1):
            new_user = {
                'username': 'user{}'.format(i),
                'password': 'pass{}'.format(i),
                'passwordConfirm': 'pass{}'.format(i),
                'firstName': 'FirstName{}'.format(i),
                'lastName': 'LastName{}'.format(i),
                'address1': 'City{}'.format(i),
                'address2': 'Str{}'.format(i),
                'register.x': '1',
                'register.y': '1'}
            requests.post(sign_up, new_user)
            print('User №{} created. Login/Password: user{}/pass{}'.format(
                i, i, i
            ))
        print('Users created!')
    except:
        print('Your "number of created users" is not a number')
        
