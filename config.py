AUTH = {
    'login': 'LOGIN',
    'password': 'PASSWORD'
}


def return_url(server):
    return f'https://{server}.darkorbit.com/indexInternal.es?action='


def clean_data(s):
    result = s.replace('.', '').replace(',', '')
    return int(result)
