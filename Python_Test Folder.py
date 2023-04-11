import requests
import hashlib
import random


def sha512(inputString):
    hashed_input = hashlib.sha512(inputString.encode('utf-8'))
    hex_dig = hashed_input.hexdigest()
    return hex_dig


def formatResponse(input):
    response = input.text
    return response[7:87]


liveEnvironment= "https://login.remita.net/remita/exapp/api/v1/send/api/echannelsvc/merchant/api/paymentinit"
demoEnvironment= "https://remitademo.net/remita/exapp/api/v1/send/api/echannelsvc/merchant/api/paymentinit"

#url= "https://remitademo.net/remita/exapp/api/v1/send/api/echannelsvc/merchant/api/paymentinit"
merchantId = "2547916"
apiKey = "1946"
serviceTypeId = "4430731"
orderId = str(random.random() * 1000000000)
print(orderId)
totalAmount = "20000"

apiHash = sha512(merchantId + serviceTypeId + orderId + totalAmount + apiKey)
print(apiHash)

headers = {'Content-Type': 'application/json',
           'Authorization': 'remitaConsumerKey=' + merchantId + ',remitaConsumerToken=' + apiHash
           }

payload = {
    'serviceTypeId': serviceTypeId,
    'amount': totalAmount,
    'orderId': orderId,
    'payerName': 'Michael Alozie',
    'payerEmail': 'alozie@systemspecs.com.ng',
    'payerPhone': '09062067384',
    'description': 'Payment for Donation 3'
}

response = requests.post(demoEnvironment, headers=headers, json=payload)
response = formatResponse(response)
print(response)