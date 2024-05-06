import random
from kavenegar import KavenegarAPI

class SMSService:
    def __init__(self, api_key, sender, receptor):
        self.api = KavenegarAPI(api_key)
        self.sender = sender
        self.receptor = receptor

    def send_sms(self, message):
        #print(message)
        try:
            params = {
                'sender': self.sender,  # optional
                'receptor': self.receptor,  # multiple mobile numbers, split by comma
                'message': message,
            }
            response = self.api.sms_send(params)
            print(response)
        except Exception as e:
            print(f"An error occurred: {e}")


    def generate_random_number():
        return random.randint(10000000, 99999999)

# Example usage
api_key = '50574345306438544B4737793548544C6C37362F6B41785A794762352B4E5174'
sender = '10008663'
receptor = '+989129494759'
sms_service = SMSService(api_key, sender, receptor)
token = sms_service.generate_random_number()
sms_service.send_sms(f'Hello, your code is {token}')



# import random
# from kavenegar import KavenegarAPI

# def send_sms(api_key, sender, receptor, message):
#     try:
#         api = KavenegarAPI(api_key)
#         print(message)
#         params = {
#             'sender': sender,#optional
#             'receptor': receptor,#multiple mobile number, split by comma
#             'message': message,
#         } 
#         response = api.sms_send(params)
#         print(response)
#     except:
#         print("sent")    

# def rand_num():
#     randint = random.randint(10000000, 99999999)
#     return randint

# token=rand_num()
# send_sms('50574345306438544B4737793548544C6C37362F6B41785A794762352B4E5174', '10008663', '+989129494759', 'hello your code in {}'.format(token))
