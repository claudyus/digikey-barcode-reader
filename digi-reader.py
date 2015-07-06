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

from bs4 import BeautifulSoup

import urllib2
import urllib
import sys

def id2digi_pn(prod_id):

	try:
		url="https://startpage.com/do/search"
		data = urllib.urlencode({'query' : 'digikey {}'.format(prod_id)})
		req = urllib2.Request(url, headers={'User-Agent' : "electronic-parser"}, data=data)
		page = urllib2.urlopen(req)

		soup = BeautifulSoup(page.read(), 'html.parser')
		u=soup.find_all('div',id='first-result')

		#print "h3(r)", u
		#[<h3 class="r"><a href="/url?q=http://www.digikey.it/product-detail/it/GRPB031VWVN-RC/S9014E-03-ND/1786439&amp;sa=U&amp;ei=B66WVfPZOMursAGTxoDIDQ&amp;ved=0CCsQFjAA&amp;usg=AFQjCNGcHGKcXod2fw4CWYyhglKdQPpFXQ">S9014E-03-ND - <b>Digikey</b></a></h3>]

		#print u[0].a['href']
		#/url?q=http://www.digikey.it/product-detail/it/GRPB031VWVN-RC/S9014E-03-ND/1786439&sa=U&ei=7LCWVcewNoPIyAPox4G4Aw&ved=0CCwQFjAA&usg=AFQjCNGrvndBviWTutyW_mT6MarGdlJV7w
		url = u[0].a['href'].split('/')[-2]
		return url
	except Exception as e:
		sys.stderr.write('error: analizing code: {} reason: {}\n'.format(prod_id, e))
		return None

def digikey2data(digi_pn):

	data = None

	if digi_pn is not None:
		digi_url = "http://search.digikey.com/scripts/DkSearch/dksus.dll?Detail&name={}".format(digi_pn)
		req2 = urllib2.Request(digi_url, headers={'User-Agent' : "electronic-parser"})
		page2 = urllib2.urlopen(req2)
		soup2 = BeautifulSoup(page2.read(), 'html.parser')
		u = soup2.find_all('table', class_='product-details')

		data = {
			"digi_pn": digi_pn,
			"manufacturer_pn": u[0].find_all('h1', itemprop="model")[0].contents[0].encode('utf-8'),
			"description": u[0].find_all('td', itemprop="description")[0].contents[0].encode('utf-8')
		}
		return data
	else:
		return None


if __name__ == "__main__":
	for line in sys.stdin:
		# parse barcode 1786439000000040970571
		sys.stderr.write('info: code readed: {}\n'.format(line))

		prod_id = line[0:7]
		qnt = line[8:16]

		d = digikey2data(id2digi_pn(prod_id))
		#print d
		if d is not None:
			print "%s, %s, %d, %s, %s" % (prod_id, d['digi_pn'], int(qnt), d['manufacturer_pn'], d['description'])
