
all:
	cat test.txt | python ../digi-reader.py > test_digikey.csv
	#test 609-1041-ND
	grep MOSFET test_digikey.csv
	#test 2531105000000020464850 
	grep 'USB TypeA' test_digikey.csv
