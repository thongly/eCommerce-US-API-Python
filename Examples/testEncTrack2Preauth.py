import time
import USmpgClasses

host = "esplusqa.moneris.com"
store_id = "monusqa002"
api_token = "qatoken"

order_id = "test_python-" + str(time.time())
amount = "1.00"
enc_track2 = "02D901801F4F2800039B%*4924********3444^TESTCARD/MONERIS^*****************************************?*;4924********3444=********************?*FACA5317D3572BDCFFC6BF46D88C1328477510B988A6ECC9978527A92389F3E76362F57DA4874C64209109024563883A0C4A3706ABCBA687D2E72528AA2339E724572CFE24CD264F16350BCB2B6C22E31F3377698D7953FF25263FBFF45CDAD6B5197FB3136FB63FC3D823CA27417305DE8597CDDEA47AABBA281CCC6B6158CF8EB67350510CF4618D76E76FE3ADCFB5642EBFDDCD927E59BB1DCBF281CE8BC2FFFF314159200420005D332903"
pos_code = "00"
device_type = "idtech"

p = USmpgClasses.USEncTrack2Preauth (order_id, amount, enc_track2, pos_code, device_type)

p.setCustId ("cust 1")
p.setDynamicDescriptor("INVOICE 001")

p.setCommcardInvoice("COM INVOICE 1")
p.setCommcardTaxAmount("0.10")

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
#print ("AvsResultCode: " + resp.getAvsResultCode())
#print ("CvdResultCode: " + resp.getCvdResultCode())
#print ("\n\nStatus Check:")
#req.postStatus()
#resp = req.getResponse()
#print ("Status Code: " + resp.getStatusCode()) 
#print ("Status Message: " + resp.getStatusMessage())
