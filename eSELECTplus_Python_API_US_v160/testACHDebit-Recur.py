import time
import USmpgClasses

host = "esplusqa.moneris.com"
store_id = "monusqa002"
api_token = "qatoken"

order_id = "test_python-" + str(time.time())
amount = "1.00"

sec = "ppd" #ppd|ccd|web|pop|arc|boc
routing_num = "011000015"
account_num = "490000018"
account_type = "savings" #savings|checking
chkInfo = USmpgClasses.ACHInfo(sec, routing_num, account_num, account_type)

ach = USmpgClasses.ACHDebit (order_id, amount, chkInfo)
ach.setCustId("Customer 1")

recur_unit = "month" #valid values are (day,week,month,eom)
start_now = "true"
start_date = "2015/12/01"
num_recurs = "12"
period = "1"
recur_amount = "1.00"


recur = USmpgClasses.Recur(recur_unit, start_now, start_date, num_recurs, period, recur_amount)
ach.setRecur(recur)


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
print ("AvsResultCode: " + resp.getAvsResultCode())
print ("CvdResultCode: " + resp.getCvdResultCode())
#print ("\n\nStatus Check:")
#req.postStatus()
#resp = req.getResponse()
#print ("Status Code: " + resp.getStatusCode()) 
#print ("Status Message: " + resp.getStatusMessage()) 

