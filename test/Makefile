
all:
	cat test.txt | coverage run ../digi-reader.py > test_digikey.csv
	#test 609-1041-ND
	grep MOSFET test_digikey.csv
	#test 2531105000000020464850 
	grep 'USB TypeA' test_digikey.csv
	#test 603-AC0402FR-071ML
	grep 'SMD 1/16W 1M ohm 1%' test_digikey.csv

	# export coverage file
	cp .coverage ../
