#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# ----------------------------------------------------------------------------
# "THE BEER-WARE LICENSE" (Revision 42):
# <c.mignanti@gmail.com> wrote this file.  As long as you retain this notice you
# can do whatever you want with this stuff. If we meet some day, and you think
# this stuff is worth it, you can buy me a beer in return.
# ----------------------------------------------------------------------------
#

import sys

from provider.digikey import *
from provider.mouser import *

if __name__ == "__main__":
	for line in sys.stdin:

		# don't read commented lines
		if line.strip()[0] == '#':
			continue

		d = None
		# parse barcode 1786439000000040970571
		sys.stderr.write('info: code readed: {}\n'.format(line))

		if len(line) == 23: # digikey bag code
			prod_id = line[0:7]
			qnt = line[8:16]

			d = digikey2data(id2digi_pn(prod_id))
		elif '-ND' in line: # digikey part/number
			d = digikey2data(line.strip())
		elif '-' in line:	# mouser code
			d = mouser2data(line.strip())
		else:
			sys.stderr.write('info: cannot parse code, no valid format : {}\n'.format(line))

		if d is not None:
			print "%s, %s, %s, %s" % (d['provider'], d['provider_pn'], d['manufacturer_pn'], d['description'])
