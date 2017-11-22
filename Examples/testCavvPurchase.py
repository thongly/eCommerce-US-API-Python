import time
import USmpgClasses

host = "esplusqa.moneris.com"
store_id = "monusqa002"
api_token = "qatoken"

order_id = "test_python-" + str(time.time())
amount = "10.30"
pan = "4242424242424242"
expiry_date = "1611"
cavv = "CAACCJIGVSZTUSI0JgZVAAAAAAA="

p = USmpgClasses.USCavvPurchase (order_id, amount, pan, expiry_date, cavv)
p.setCustId ("cust 1")
cvd = USmpgClasses.CvdInfo("1", "123")
avs = USmpgClasses.AvsInfo("123", "Main St", "a1a2b2")

p.setCvdInfo(cvd)
p.setAvsInfo(avs)

req = USmpgClasses.mpgHttpsPost(host, store_id, api_token, p)
req.postRequest()
resp = req.getResponse()
print ("ReceiptId: " + resp.getReceiptId()) 
print ("ReferenceNum: " + resp.getReferenceNum()) 
print ("ResponseCode: " + resp.getResponseCode()) 
print ("AuthCode: " + resp.getAuthCode()) 
print ("TransTime: " + resp.getTransTime()) 
print ("TransDate: " + resp.getTransDate()) 
print ("TransType: " + resp.getTransType()) 
print ("Complete: " + resp.getComplete()) 
print ("Message: " + resp.getMessage()) 
print ("TransAmount: " + resp.getTransAmount()) 
print ("CardType: " + resp.getCardType()) 
print ("TransID: " + resp.getTransID()) 
print ("TimedOut: " + resp.getTimedOut()) 
print ("BankTotals: " + resp.getBankTotals()) 
print ("Ticket: " + resp.getTicket()) 
print ("AvsResultCode: " + resp.getAvsResultCode())
print ("CvdResultCode: " + resp.getCvdResultCode())
print ("CAVVResultCode: " + resp.getCavvResultCode())
#print ("\n\nStatus Check:")
#req.postStatus()
#resp = req.getResponse()
#print ("Status Code: " + resp.getStatusCode()) 
#print ("Status Message: " + resp.getStatusMessage()) 

