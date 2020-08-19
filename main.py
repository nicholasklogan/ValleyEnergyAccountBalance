import re

import requests


def get_gas_balance():
    sess = requests.Session()

    y = sess.get('https://myfuelaccount.com/valleyenergy')
    for i in y.text.split('\r\n'):
        if '__RequestVerificationToken' in i:
            token_matched = re.match('.*?<input name="__RequestVerificationToken" type="hidden" value="(?P<token>.*?)" />.*?', i)
            if token_matched:
                token = token_matched.groupdict()['token']
                break
    Go = False
    for i in sess.post('https://myfuelaccount.com/valleyenergy', data={
                '__RequestVerificationToken': token,
                'Email': '', # ENTER EMAIL ADDRESS HERE
                'Password': '', # ENTER PASSWORD HERE
                'RememberMe': False
            }).text.split('\r\n'):
        if Go:
            return i.strip()
        if 'Balance:  <br />' in i:
            Go = True

print(get_gas_balance())
