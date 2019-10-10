from auth.auth import auth
from parser.account_info_parser import get_account_info
from parser.skylab_parser import get_skylab_info
from config import auth_params

auth_session = auth(auth_params['login'], auth_params['password'])

account_info = get_account_info(auth_session)
print(account_info.get_info())

skylab_info = get_skylab_info(auth_session)
print(skylab_info.get_info())
