import requests
import hashlib


def sha512(input):
    hashed_input = hashlib.sha512(input.encode('utf-8'))
    hex_dig = hashed_input.hexdigest()
    return hex_dig


merchantId = "2547916"
apiKey = "1946"
rrr = "240008240803"

liveEnvironment= "https://login.remita.net/remita/ecomm/"
demoEnvironment= "https://remitademo.net/remita/ecomm/"


apiHash = sha512(rrr + apiKey + merchantId)
print('')
print(apiHash)
print('')
checkStatus = demoEnvironment + merchantId + "/" + rrr + "/" + apiHash + "/status.reg"
print('')
print(checkStatus)

response = requests.get(checkStatus)
print(response.text)