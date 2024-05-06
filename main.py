from kavenegar import *
try:
    api = KavenegarAPI('50574345306438544B4737793548544C6C37362F6B41785A794762352B4E5174')
    params = {
        'sender': '10008663',#optional
        'receptor': '+989129494759',#multiple mobile number, split by comma
        'message': 'test',
    } 
    response = api.sms_send(params)
    print(response)
except:
    print("sms sent")    
# except APIException as e: 
#     print(e)
# except HTTPException as e: 
#     print(e)


    