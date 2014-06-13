def getCheckDigit(barcode):
	strBarcode = str(barcode)
	
	firstSum = 0
	SecondSum = 0

	for i in range(6):
		firstSum += int(strBarcode[2*i])
		SecondSum += int(strBarcode[2*i+1])
	
	checkDigit = (10 -  ((firstSum+(SecondSum*3))%10))

	return checkDigit
