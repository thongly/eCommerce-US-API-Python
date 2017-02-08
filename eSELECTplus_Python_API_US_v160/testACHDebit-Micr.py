import time
import USmpgClasses

host = "esplusqa.moneris.com"
store_id = "monusqa002"
api_token = "qatoken"

order_id = "test_python-" + str(time.time())
amount = "1.00"

sec = "pop" #ppd|ccd|web|pop|arc|boc

### micr version of chkInfo
micr = "t071000013t742941347o125"
dl_num = "CO-12312312"
magstripe = "no"
image_front = "1234567890123456789012345678" #Full image is required
image_back = "12345678901234567890123456789" # Full image is required

chkInfo = USmpgClasses.ACHInfo(sec, micr, dl_num, magstripe, image_front, image_back) ### When ACHInfo is obtained from MICR reader

chkInfo.setCheckNum("100")
chkInfo.setCustAddress1("3300 Bloor Street West")
chkInfo.setCustAddress2("West Tower")
chkInfo.setCustCity("Toronto")
chkInfo.setCustFirstName("FirstName")
chkInfo.setCustLastName("LastName")
chkInfo.setCustState("ON")
chkInfo.setCustZip("12345")

ach = USmpgClasses.ACHDebit (order_id, amount, chkInfo)
ach.setCustId("Customer 1")

req = USmpgClasses.mpgHttpsPost(host, store_id, api_token, ach)
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
#print ("\n\nStatus Check:")
#req.postStatus()
#resp = req.getResponse()
#print ("Status Code: " + resp.getStatusCode()) 
#print ("Status Message: " + resp.getStatusMessage()) 

