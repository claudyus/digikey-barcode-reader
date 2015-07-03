#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

import urllib2
import urllib
import sys

def id2digi_pn(prod_id):

	url="https://startpage.com/do/search"
	data = urllib.urlencode({'query' : 'digikey {}'.format(prod_id)})
	req = urllib2.Request(url, headers={'User-Agent' : "MagicBrowser2"}, data=data) 
	page = urllib2.urlopen(req)

	soup = BeautifulSoup(page.read(), 'html.parser')
	u=soup.find_all('div',id='first-result')

	#print "h3(r)", u
	#[<h3 class="r"><a href="/url?q=http://www.digikey.it/product-detail/it/GRPB031VWVN-RC/S9014E-03-ND/1786439&amp;sa=U&amp;ei=B66WVfPZOMursAGTxoDIDQ&amp;ved=0CCsQFjAA&amp;usg=AFQjCNGcHGKcXod2fw4CWYyhglKdQPpFXQ">S9014E-03-ND - <b>Digikey</b></a></h3>]

	#print u[0].a['href']
	#/url?q=http://www.digikey.it/product-detail/it/GRPB031VWVN-RC/S9014E-03-ND/1786439&sa=U&ei=7LCWVcewNoPIyAPox4G4Aw&ved=0CCwQFjAA&usg=AFQjCNGrvndBviWTutyW_mT6MarGdlJV7w
	return u[0].a['href'].split('/')[-2]


def digikey2data(digi_pn):

	digi_url = "http://search.digikey.com/scripts/DkSearch/dksus.dll?Detail&name={}".format(digi_pn)
	req2 = urllib2.Request(digi_url, headers={'User-Agent' : "MagicBrowser2"}) 
	page2 = urllib2.urlopen(req2)
	soup2 = BeautifulSoup(page2.read(), 'html.parser')
	u = soup2.find_all('table', class_='product-details')

	data = {
		"digi_pn": digi_pn,
		"manufacturer_pn": u[0].find_all('h1', itemprop="model")[0].contents[0].encode('utf-8'),
		"description": u[0].find_all('td', itemprop="description")[0].contents[0].encode('utf-8')
	}
	return data


if __name__ == "__main__":
	for line in sys.stdin:
		# parse barcode 1786439000000040970571
		prod_id = line[0:7]
		qnt = line[8:16]

		d = digikey2data(id2digi_pn(prod_id))
		#print d
		print "%s, %s, %d, %s, %s" % (prod_id, d['digi_pn'], int(qnt), d['manufacturer_pn'], d['description'])
