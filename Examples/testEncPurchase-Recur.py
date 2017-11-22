import time
import USmpgClasses

host = "esplusqa.moneris.com"
store_id = "monusqa002"
api_token = "qatoken"

order_id = "test_python-" + str(time.time())
amount = "1.00"
enc_track2 = "02840085000000000416F08AFACC95B5ABE3C30BF8420389C9179AADEDB5B993948A9BED3E4D1A791C3F4FC61C1800486A8A6B6CCAA00431353131FFFF314159200420005C726003"
crypt = "7"
device_type = "idtech"


p = USmpgClasses.USEncPurchase (order_id, amount, enc_track2, crypt, device_type)
p.setCustId ("cust 1")
p.setDynamicDescriptor("INVOICE 001")

recur_unit = "month" #valid values are (day,week,month,eom)
start_now = "true"
start_date = "2015/12/01"
num_recurs = "12"
period = "1"
recur_amount = "30.00"


recur = USmpgClasses.Recur(recur_unit, start_now, start_date, num_recurs, period, recur_amount)
p.setRecur(recur)

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
print ("Masked Pan: " + resp.getMaskedPan())
print ("RecurSuccess: " + resp.getRecurSuccess())

