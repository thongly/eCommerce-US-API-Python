import time
import USmpgClasses

host = "esplusqa.moneris.com"
store_id = "monusqa002"
api_token = "qatoken"

order_id = "test_python-" + str(time.time())
amount = "1.00"
pan = "4242424242424242"
expiry_date = "1611"
crypt = "7"

p = USmpgClasses.USPurchase (order_id, amount, pan, expiry_date, crypt)
p.setCustId ("cust 1")

cust = USmpgClasses.CustInfo()
billing = USmpgClasses.BillingInfo("first_name", "last_name", "company_name", "address", "city", "province", "postal_code", "country", "phone_number", "fax", "tax1", "tax2", "tax3", "shipping_cost")
shipping = USmpgClasses.ShippingInfo("first_name", "last_name", "company_name", "address", "city", "province", "postal_code", "country", "phone_number", "fax", "tax1", "tax2", "tax3", "shipping_cost")
email = "email@abc.com"
instruction = "take it slow"
cust.setBilling(billing)
cust.setShipping(shipping)
cust.setEmail(email)
cust.setInstruction(instruction)
cust.addItem(USmpgClasses.Item("item 123", "1", "4527182-90123", "5.00"))
cust.addItem(USmpgClasses.Item("item 234", "2", "4527182-90234", "4.00"))
cust.addItem(USmpgClasses.Item("item 345", "3", "4527182-90345", "3.00"))

p.setCustInfo (cust)

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


