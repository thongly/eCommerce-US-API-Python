import time
import USmpgClasses

host = "esplusqa.moneris.com"
store_id = "monusqa002"
api_token = "qatoken"

order_id = "test_python-" + str(time.time())
amount = "10.30"
track2 = ";4242424242424242=15102012602213899076?"
pan = ""
expiry_date = ""
pos_code = "00"

p = USmpgClasses.USTrack2Purchase (order_id, amount , track2, pan, expiry_date, pos_code)
p.setCustId ("cust 1")
p.setDynamicDescriptor("INVOICE 001")
p.setCommcardInvoice("COM INVOICE 1")
p.setCommcardTaxAmount("0.10")
avs = USmpgClasses.AvsInfo("123", "Main St", "a1a2b2")
p.setAvsInfo(avs)

req = USmpgClasses.mpgHttpsPost(host, store_id , api_token, p)
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
#print ("CvdResultCode: " + resp.getCvdResultCode())
#print ("\n\nStatus Check:")
#req.postStatus()
#resp = req.getResponse()
#print ("Status Code: " + resp.getStatusCode()) 
#print ("Status Message: " + resp.getStatusMessage())
