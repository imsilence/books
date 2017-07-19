#encoding: utf-8
import ftplib

def login(host, user, password, port=21):
    try:
        _client = ftplib.FTP()
        _client.connect(host, port)
        _client.login(user, password)
        _client.quit()
        return True
    except BaseException as e:
        return False

def anonymous_login(host, user='anonymous'):
    return login(host, user, '')

if __name__ == '__main__':
    print anonymous_login(host='localhost')
    print anonymous_login(host='localhost', user='anyone')
    print anonymous_login(host='localhost', user='silence')
