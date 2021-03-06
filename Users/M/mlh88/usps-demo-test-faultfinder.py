import scraperwiki


# Blank Python

import scraperwiki,urllib2,lxml.html,unicodedata
#data = scraperwiki.scrape("https://sites.google.com/site/mlhdatadump/addresslookup/AddrTest.csv")
data = scraperwiki.scrape("https://sites.google.com/site/mlhdatadump/addresslookup/BadAddrTest.csv")

import csv           
reader = csv.reader(data.splitlines())

for row in reader:           
    LookupAddr = row[0]
    LookupCity = row[1]
    LookupState = row[2]
#print LookupAddr, LookupCity, LookupState
    
    url='https://tools.usps.com/go/ZipLookupResultsAction!input.action?resultMode=0&companyName=&address1='+LookupAddr+'&address2=&city='+LookupCity+'&state='+LookupState+'&urbanCode=&postalCode=&zip='

# Below is my attempt at searching for the message that indicates a non-deliverable address
    html=urllib2.urlopen(url).read()
    print html
    nondel = html.find('The address you provided is not recognized')
    #print nondel
    if nondel != -1:
        #print 'The address you entered is invalid'
        data={'The address you entered is invalid,'}
            #print data
        scraperwiki.sqlite.save(table_name='address',data=data,unique_keys=["1"])
  # else:
  #      print 'The address you entered is valid'
  #      data = nondel
  #      scraperwiki.sqlite.save(table_name='address',data=data,unique_keys=[])
    else:
        root = lxml.html.fromstring(html).get_element_by_id('result-list')
        for cdata in root.cssselect("[class='data']"):
            data={}
            for addressbit in cdata.cssselect("[class='std-address'] span"): # the assertion that these are unique is FALSE; erases names.
                bitname=addressbit.attrib['class']
                bittext=addressbit.text_content()
                bitname=unicodedata.normalize('NFKD', unicode(bitname)).encode('ascii','ignore').replace('/','-')
                data[bitname]=bittext
            for hiddenbit in cdata.cssselect("dl[class='details'] dt"):
                bitname=hiddenbit.text_content()
                bittext=hiddenbit.getnext().text_content()
                bitname=unicodedata.normalize('NFKD', unicode(bitname)).encode('ascii','ignore').replace('/','-')
                data[bitname]=bittext
            print data
        scraperwiki.sqlite.save(table_name='address',data=data,unique_keys=[])
#nondel = html.find('The address you provided is not recognized by the US Postal Service')
#print nondel
import scraperwiki


# Blank Python

import scraperwiki,urllib2,lxml.html,unicodedata
#data = scraperwiki.scrape("https://sites.google.com/site/mlhdatadump/addresslookup/AddrTest.csv")
data = scraperwiki.scrape("https://sites.google.com/site/mlhdatadump/addresslookup/BadAddrTest.csv")

import csv           
reader = csv.reader(data.splitlines())

for row in reader:           
    LookupAddr = row[0]
    LookupCity = row[1]
    LookupState = row[2]
#print LookupAddr, LookupCity, LookupState
    
    url='https://tools.usps.com/go/ZipLookupResultsAction!input.action?resultMode=0&companyName=&address1='+LookupAddr+'&address2=&city='+LookupCity+'&state='+LookupState+'&urbanCode=&postalCode=&zip='

# Below is my attempt at searching for the message that indicates a non-deliverable address
    html=urllib2.urlopen(url).read()
    print html
    nondel = html.find('The address you provided is not recognized')
    #print nondel
    if nondel != -1:
        #print 'The address you entered is invalid'
        data={'The address you entered is invalid,'}
            #print data
        scraperwiki.sqlite.save(table_name='address',data=data,unique_keys=["1"])
  # else:
  #      print 'The address you entered is valid'
  #      data = nondel
  #      scraperwiki.sqlite.save(table_name='address',data=data,unique_keys=[])
    else:
        root = lxml.html.fromstring(html).get_element_by_id('result-list')
        for cdata in root.cssselect("[class='data']"):
            data={}
            for addressbit in cdata.cssselect("[class='std-address'] span"): # the assertion that these are unique is FALSE; erases names.
                bitname=addressbit.attrib['class']
                bittext=addressbit.text_content()
                bitname=unicodedata.normalize('NFKD', unicode(bitname)).encode('ascii','ignore').replace('/','-')
                data[bitname]=bittext
            for hiddenbit in cdata.cssselect("dl[class='details'] dt"):
                bitname=hiddenbit.text_content()
                bittext=hiddenbit.getnext().text_content()
                bitname=unicodedata.normalize('NFKD', unicode(bitname)).encode('ascii','ignore').replace('/','-')
                data[bitname]=bittext
            print data
        scraperwiki.sqlite.save(table_name='address',data=data,unique_keys=[])
#nondel = html.find('The address you provided is not recognized by the US Postal Service')
#print nondel
