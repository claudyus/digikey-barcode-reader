Digikey barcode reader
=========================

This script is used to retrieve information from the web using the digikey tag barcode.


Usage
-------

Scan your digikey barcode using a barcode scanner and save it in a text file, the barcode
should be saved one-per-line. See digi_example.txt for example

Than pipe yhe scanned file to digi-reader.py::

  cat digi_example.txt | pyhon digi-reader.py

This will output a CSV in the fomat::

  product_id, digikey_part_number, qnty, manufacter_part_number, description
