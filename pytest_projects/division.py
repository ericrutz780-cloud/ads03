def make_division(dividend, divisor):
	try:
		result = dividend/divisor
		return "[INFO:] Das Ergebnis von %s / %s der Division ist %s" % (dividend, divisor, result)
	except ZeroDivisionError:
		return"[FEHLER:] Fehler bei der Berechnung %s / %s" % (dividend, divisor)

if __name__ == "__main__":
	n = 6
	for dividend in range (-5, n, 5):
		for divisor in range (-5, n, 5):
			log = make_division(dividend, divisor)
			print(log)
