import sys, time, os
import mechanize
import lxml.html
import string
import scraperwiki

LOGIN_URL = 'https://www.johnlewisgiftlist.com/giftint/JSPs/GiftList/BuyGifts/GuestFindAList.jsp'
NEW_URL = 'https://www.johnlewisgiftlist.com/giftint/buylist'
GIFTLISTNO = '442551'

br = mechanize.Browser()                # Create a browser
br.open(LOGIN_URL)            # Open the login page
print br.geturl()
br.select_form(nr=0)  # Find the login form
br['giftListNumber'] = GIFTLISTNO # Set the form values
br.submit()            # Submit the form

# Automatic redirect sometimes fails, follow manually when needed
#if 'Redirecting' in br.title():
#    resp = br.follow_link(text_regex='click here')

allforms = list(br.forms())
print "There are %d forms" % len(allforms)

#forms = mechanize.ParseResponse(response, backwards_compat=False)
#listForm = br.forms[0]

#print listForm

#listForm.set_all_readonly(False) # allow changing the .value of all controls


br.select_form(nr=0)  # Find the login form
br.set_all_readonly(False)
br['Action'] = 'showEverything' # Set the form values
br['PageNumber'] = '1' # Set the form values
br.submit()            # Submit the form

datasheet = br.response().read()

#print datasheet

root = lxml.html.fromstring(datasheet)



prodstring = root.cssselect("tr.item")


prodcatno = root.cssselect("td.catno")
prodqty = root.cssselect("td.qty")
prodprice = root.cssselect("td.price")

print "There are %d items on your shopping list" % len(prodstring)

#print "Their corresponding attributes are:", [tr.attrib  for tr in prodname ]
#print lxml.html.tostring(prodname[0])

scraperwiki.sqlite.execute("drop table if exists swdata")


for index, item in enumerate(prodstring):
    
    #root = Element(prodname, width="7%")
    #print root.tostring(root)

    #for child in prodname:
    #    print(child.tag)
    if not index == 0:
        prodstringBig = lxml.html.tostring(item)
        prodstringBig = string.join(string.split(prodstringBig), " ")
        prodstringBig = string.split(prodstringBig, "</td>")
        #print prodstringBig
        
        # price, quantity, catNo, image, productName
        prodfav = prodstringBig[0]
        prodfav = string.replace(prodfav, '<tr class="item"><td width="2%"> <img src="/giftint/assets/star.gif">', '1')
        prodfav = string.replace(prodfav, '<tr class="item"><td width="2%">', '0')
        print prodfav

        prodprice = prodstringBig[5]
        prodprice = string.replace(prodprice, ' <td width="10%" class="centre">', '')
        prodprice = string.replace(prodprice, ' ', '')
      #  print prodprice

        prodquantitywip = prodstringBig[4]
        prodquantitywip = string.replace(prodquantitywip, ' <td width="12%" class="centre">', '')
        prodquantitywip = string.replace(prodquantitywip, ' ', '')
        prodquantitywip = string.split(prodquantitywip, "of")
        prodquantity = prodquantitywip[0]
        prodquantitymax = prodquantitywip[1]
      #  print prodquantity
      #  print prodquantitymax

        prodcatno = prodstringBig[2]
        prodcatno = string.replace(prodcatno , ' <td width="10%" class="centre">', '')
        prodcatno = string.replace(prodcatno , ' ', '')
      #  print prodcatno

        productURL = "https://shop.johnlewisgiftlist.com/Corp/ProductInfo.aspx?Prodcode=" + prodcatno
        #productRoot = lxml.html.parse(productURL).getroot()
        
       # newbr = mechanize.Browser()

       # newbr.open(productURL)
       # proddatasheet = newbr.response().read()
       # print proddatasheet
       # proddatasheetroot = lxml.html.fromstring(proddatasheet)
       # imgTag = proddatasheetroot.cssselect("img#imgProductImage")[0]
       # imgSrc = imgTag.attrib.get("src")
       # prodimage = string.replace(imgSrc, '$product$', '$preview$')
        prodimage = "http://www.danandcaroline.co.uk/wp-content/themes/fadelicious/style/images/giftlist-missingproduct.png"
       # print prodimage

        prodname = prodstringBig[3]
        prodname = string.replace(prodname, ' <td width="49%"> ', '')
        prodname = " ".join([s.capitalize() for s in prodname.split(" ")])
        prodname = string.replace(prodname, '/', '&#47;')
       # print prodname

        dataArray = { "productName":prodname, "catNo":prodcatno, "quantity":prodquantity, "quantitymax":prodquantitymax, "price":prodprice, "image":prodimage}
        print dataArray
    

        scraperwiki.sqlite.save(unique_keys=["catNo", "productName"], data=dataArray)
   
print scraperwiki.sqlite.select("* from swdata")import sys, time, os
import mechanize
import lxml.html
import string
import scraperwiki

LOGIN_URL = 'https://www.johnlewisgiftlist.com/giftint/JSPs/GiftList/BuyGifts/GuestFindAList.jsp'
NEW_URL = 'https://www.johnlewisgiftlist.com/giftint/buylist'
GIFTLISTNO = '442551'

br = mechanize.Browser()                # Create a browser
br.open(LOGIN_URL)            # Open the login page
print br.geturl()
br.select_form(nr=0)  # Find the login form
br['giftListNumber'] = GIFTLISTNO # Set the form values
br.submit()            # Submit the form

# Automatic redirect sometimes fails, follow manually when needed
#if 'Redirecting' in br.title():
#    resp = br.follow_link(text_regex='click here')

allforms = list(br.forms())
print "There are %d forms" % len(allforms)

#forms = mechanize.ParseResponse(response, backwards_compat=False)
#listForm = br.forms[0]

#print listForm

#listForm.set_all_readonly(False) # allow changing the .value of all controls


br.select_form(nr=0)  # Find the login form
br.set_all_readonly(False)
br['Action'] = 'showEverything' # Set the form values
br['PageNumber'] = '1' # Set the form values
br.submit()            # Submit the form

datasheet = br.response().read()

#print datasheet

root = lxml.html.fromstring(datasheet)



prodstring = root.cssselect("tr.item")


prodcatno = root.cssselect("td.catno")
prodqty = root.cssselect("td.qty")
prodprice = root.cssselect("td.price")

print "There are %d items on your shopping list" % len(prodstring)

#print "Their corresponding attributes are:", [tr.attrib  for tr in prodname ]
#print lxml.html.tostring(prodname[0])

scraperwiki.sqlite.execute("drop table if exists swdata")


for index, item in enumerate(prodstring):
    
    #root = Element(prodname, width="7%")
    #print root.tostring(root)

    #for child in prodname:
    #    print(child.tag)
    if not index == 0:
        prodstringBig = lxml.html.tostring(item)
        prodstringBig = string.join(string.split(prodstringBig), " ")
        prodstringBig = string.split(prodstringBig, "</td>")
        #print prodstringBig
        
        # price, quantity, catNo, image, productName
        prodfav = prodstringBig[0]
        prodfav = string.replace(prodfav, '<tr class="item"><td width="2%"> <img src="/giftint/assets/star.gif">', '1')
        prodfav = string.replace(prodfav, '<tr class="item"><td width="2%">', '0')
        print prodfav

        prodprice = prodstringBig[5]
        prodprice = string.replace(prodprice, ' <td width="10%" class="centre">', '')
        prodprice = string.replace(prodprice, ' ', '')
      #  print prodprice

        prodquantitywip = prodstringBig[4]
        prodquantitywip = string.replace(prodquantitywip, ' <td width="12%" class="centre">', '')
        prodquantitywip = string.replace(prodquantitywip, ' ', '')
        prodquantitywip = string.split(prodquantitywip, "of")
        prodquantity = prodquantitywip[0]
        prodquantitymax = prodquantitywip[1]
      #  print prodquantity
      #  print prodquantitymax

        prodcatno = prodstringBig[2]
        prodcatno = string.replace(prodcatno , ' <td width="10%" class="centre">', '')
        prodcatno = string.replace(prodcatno , ' ', '')
      #  print prodcatno

        productURL = "https://shop.johnlewisgiftlist.com/Corp/ProductInfo.aspx?Prodcode=" + prodcatno
        #productRoot = lxml.html.parse(productURL).getroot()
        
       # newbr = mechanize.Browser()

       # newbr.open(productURL)
       # proddatasheet = newbr.response().read()
       # print proddatasheet
       # proddatasheetroot = lxml.html.fromstring(proddatasheet)
       # imgTag = proddatasheetroot.cssselect("img#imgProductImage")[0]
       # imgSrc = imgTag.attrib.get("src")
       # prodimage = string.replace(imgSrc, '$product$', '$preview$')
        prodimage = "http://www.danandcaroline.co.uk/wp-content/themes/fadelicious/style/images/giftlist-missingproduct.png"
       # print prodimage

        prodname = prodstringBig[3]
        prodname = string.replace(prodname, ' <td width="49%"> ', '')
        prodname = " ".join([s.capitalize() for s in prodname.split(" ")])
        prodname = string.replace(prodname, '/', '&#47;')
       # print prodname

        dataArray = { "productName":prodname, "catNo":prodcatno, "quantity":prodquantity, "quantitymax":prodquantitymax, "price":prodprice, "image":prodimage}
        print dataArray
    

        scraperwiki.sqlite.save(unique_keys=["catNo", "productName"], data=dataArray)
   
print scraperwiki.sqlite.select("* from swdata")