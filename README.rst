Digikey barcode reader
=========================

A python script to retrieve information about digikey components using bag barcode

Usage
-------

Scan your digikey barcode using a barcode scanner and save it in a text file, the barcode
should be saved one-per-line. See digi_example.txt for example

Than pipe the scanned file to digi-reader.py (linux)::

  cat digi_example.txt | python digi-reader.py >> digi_parts.csv


Windows usage::

  type digi_example.txt | python digi-reader.py >> digi_parts.csv


This will output a CSV in the format::

  product_id, digikey_part_number, qnty, manufacter_part_number, description

Background of this script
----------------------------

Often I have to organize bags of digikey parts bought over the time. I have around 200 bags of parts around that should be classify.
I start to look at the barcode always present on the bag label [1] and I start to thought about it format, unfortunately nothing can be found online so after a while I was able to recognize a pattern inside the barcode.
The first 7 digits are the product_id (used internally by digikey, it is not the p/n), the following digits are the shipped quantity, and the last 6 digits are still unknown (package information? or shipping information?)

On digikey website there is no way, as I know, to retrieve part information using the
unique product_id, it is only exposed as part of the URI on the webpage related to a given part.

So I start to write a simple web scraper that is looking for a given product_id, retrieve the digikey page from startpage.com (google cannot be used due to bot recognition system), than open 
the digikey page and retrieve information about the electronic parts. Than all the infos are
printed as CSV.

ATM there is no configuration, you can easily modify the output format at the end of the script itself.


1. here an example http://ch00ftech.com/wp-content/uploads/2013/02/IMG_1777.jpg

LICENSE
---------
This work is release under BEER-WARE LICENSE
