import USmpgClasses

host = "esplusqa.moneris.com"
store_id = "monusqa002"
api_token = "qatoken"

order_id = "ORDER_ID_FROM_ORIGINAL_TXN"

#The following fields can be updated for a CC, ACH or Pinless Debit transaction
cust_id = "cust 2"
recur_amount = "1.00"
add_num = "1"
total_num ="20"
hold = 'false';
terminate = 'false'

#The pan & expdate can be updated for a Credit Card or Pinless Debit transaction
pan = "4242424242424242"
expdate = "1611"

#The AVS details can only be updated for a Credit Card transaction
avs_street_number = '112'
avs_street_name = 'lakeshore blvd'
avs_zipcode = '123123'

#The p_account_number & presentation_type can only be updated for a Pinless Debit transaction
#p_account_number="Account a12345678 9876543"
#presentation_type = "X"

p = USmpgClasses.USRecurUpdate(order_id)
p.setCustId (cust_id)
p.setRecurAmount(recur_amount)
p.setPan(pan)
p.setExpDate(expdate)
p.setAddNumRecurs(add_num)
p.setTotalNumRecurs(total_num)
p.setHold(hold)
p.setTerminate(terminate)
p.setAvsStreetNumber(avs_street_number)
p.setAvsStreetName(avs_street_name)
p.setAvsZipcode(avs_zipcode)
#p.setPAccountNumber(p_account_number)
#p.setPresentationType(presentation_type)

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
print ("RecurUpdateSuccess: " + resp.getRecurUpdateSuccess())
print ("NextRecurDate: " + resp.getNextRecurDate())
print ("RecurEndDate: " + resp.getRecurEndDate())

