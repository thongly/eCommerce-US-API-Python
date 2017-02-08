import USmpgClasses

host = "esplusqa.moneris.com"
store_id = "monusqa002"
api_token = "qatoken"
ecr_no = "64000003"

ot = USmpgClasses.USBatchClose(ecr_no)

req = USmpgClasses.mpgHttpsPost(host, store_id, api_token, ot)
req.postRequest()

resp = req.getResponse()
ecrs = resp.getECRs()
for termid in ecrs.keys():
	print ("ecr is: "+ termid )
	cardTypes = resp.getCardTypes(termid)
	for card in cardTypes:
		print ("Card Type is : " + card)
		print ("\tPurchase Count: " + resp.getPurchaseCount(termid, card))
		print ("\tPurchase Amount: " + resp.getPurchaseAmount(termid, card))
		print ("\tRefund Count: " + resp.getRefundCount(termid, card))
		print ("\tRefund Amount: " + resp.getRefundAmount(termid, card))
		print ("\tCorrection Count: " + resp.getCorrectionCount(termid, card))
		print ("\tCorrection Amount: " + resp.getCorrectionAmount(termid, card))	
		print ("\n\n")
	print ("------------------------------\n\n")
