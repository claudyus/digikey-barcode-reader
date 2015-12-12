from bs4 import BeautifulSoup

import urllib2
import urllib
import sys

def mouser2data(part_num):
	data = None

	try:
		if part_num is not None:
			digi_url = "http://www.mouser.com/Search/Refine.aspx?Keyword={}".format(part_num)
			req2 = urllib2.Request(digi_url, headers={'User-Agent' : "electronic-parser"})
			page2 = urllib2.urlopen(req2)
			soup2 = BeautifulSoup(page2.read(), 'html.parser')
			u = soup2.find_all('div', id='product-desc')

			data = {
				"provider": "mouser",
				"provider_pn": part_num,
				"manufacturer_pn": u[0].find_all('div', itemprop="ProductID")[0].contents[1].contents[1].contents[0].encode('utf-8').strip(),
				"description": u[0].find_all('span', itemprop="description")[0].contents[1].contents[0].encode('utf-8').strip()
			}
			return data
	except Exception as e:
		sys.stderr.write('error: reading mouser page for {} reason: {}\n'.format(part_num, e))
		return None
