from NorenRestApiPy.NorenApi import NorenApi
import logging
import pyotp

class ShoonyaApiPy(NorenApi):
    def __init__(self):
        super().__init__(host='https://api.shoonya.com/NorenWClientTP/', 
                         websocket='wss://api.shoonya.com/NorenWSTP/',
                         eodhost='https://api.shoonya.com/NorenEODTP/')
        global api
        api = self

    def login(self, userid, password, twoFA, vendor_code, api_secret, imei):
        ret = super().login(userid=userid, password=password, twoFA=twoFA, vendor_code=vendor_code, api_secret=api_secret, imei=imei)
        if ret and ret.get('stat') == 'Ok':
            self.__username = userid
        return ret

# Enable debug to see request and responses
logging.basicConfig(level=logging.DEBUG)

# Generate OTP
token = "63637365DV2ZW244WZV5M32L2R5P5Y75"
otp = pyotp.TOTP(token).now()

# Instantiate API
api = ShoonyaApiPy()

# User credentials and other details
user = 'FA68357'
pwd = 'P@a93149'
factor2 = otp
vc = 'FA68357_U'
apikey = '8d49c5a4fab22d91b097b246b1c64d2f'
imei = 'abc1234'

# Login
try:
    ret = api.login(userid=user, password=pwd, twoFA=factor2, vendor_code=vc, api_secret=apikey, imei=imei)
    if ret:
        print(ret)
        if ret.get('stat') == 'Ok':
            # Get limits only if login is successful
            a = api.get_holdings()
            print(a)
        else:
            print(f"Login failed: {ret.get('emsg')}")
    else:
        print("Login failed: No response received")
except Exception as e:
    print(f"An error occurred during login: {str(e)}")
