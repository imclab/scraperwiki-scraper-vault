import scraperwiki          
import lxml.html
import uuid
import datetime
# Here's the original blog post that explains how to set up IFTTT to alert you to ebook deals: 
# http://markhawker.tumblr.com/post/39433120371/amazon-wish-lists-scraperwiki-and-ifttt

# Variables

# Put Your Wishlist Code Below
wishlist = "WISHLISTCODE"
# Put the price below which you want to be alerted (I put $10 to be alerted when ebooks are $9.99 or less)
limit = 10
asins = []

# Functions

def is_cheap(price):
    if(price < float(limit)):
        cheap = "Is going cheap!" # Text to search for within IFTTT
    elif(price == 9999999):
        cheap = "We can't get a price."
    else:
        cheap = "Is not going cheap."
    return cheap

def save(title, link, description):
    now = datetime.datetime.now()
    data = {
        "title": title,
        "link": link,
        "description": description,
        "guid": link + "&uuid=" + str(uuid.uuid1()),
        "pubDate": str(now)
    }
    scraperwiki.sqlite.save(unique_keys=['link'], data=data)
    return "Saved!"

try: # Try and get ASINs from your Amazon Wish List
    url = "http://www.amazon.ca/wishlist/" + wishlist + "/ref=cm_wl_act_print_o?_encoding=UTF8&disableNav=1&items-per-page=2500&layout=standard-print&page=1&visitor-view=1"
    html = scraperwiki.scrape(url)
    root = lxml.html.fromstring(html)
    for element in root.cssselect("tbody[class='itemWrapper']"):
        string = element.attrib["name"]
        pieces = string.split(".")
        asins.append(pieces[3])
except:
    print "There was an error. Did you provide a working Amazon Wish List identifier?"
    exit;

# Process ASINs for further details

for asin in asins:
    price = 9999999
    url = "http://www.amazon.ca/dp/" + asin
    html = scraperwiki.scrape(url)
    root = lxml.html.fromstring(html)
    title = root.cssselect("span[id='btAsinTitle']")[0].text_content()
    if(title.find("Kindle Edition") > 0): # Check if this is an item for the Amazon Kindle
        for element in root.cssselect("div[class='buying'] input"):
            if(element.attrib["name"] == "displayedPrice"):
                price = float(element.attrib["value"])
        cheap = is_cheap(price)
    else:
        try: # Try and get the price of the item. Some items throw back garbage so the price is listed as cannot be found.
            price = float(root.cssselect("span[id='actualPriceValue'] b")[0].text_content()[1:])
        except(IndexError):
            print "We can't get a price for: " + title
            print "Try camelcamelcamel: http://uk.camelcamelcamel.com/product/" + asin
        cheap = is_cheap(price)
    print save(title, url, cheap)import scraperwiki          
import lxml.html
import uuid
import datetime
# Here's the original blog post that explains how to set up IFTTT to alert you to ebook deals: 
# http://markhawker.tumblr.com/post/39433120371/amazon-wish-lists-scraperwiki-and-ifttt

# Variables

# Put Your Wishlist Code Below
wishlist = "WISHLISTCODE"
# Put the price below which you want to be alerted (I put $10 to be alerted when ebooks are $9.99 or less)
limit = 10
asins = []

# Functions

def is_cheap(price):
    if(price < float(limit)):
        cheap = "Is going cheap!" # Text to search for within IFTTT
    elif(price == 9999999):
        cheap = "We can't get a price."
    else:
        cheap = "Is not going cheap."
    return cheap

def save(title, link, description):
    now = datetime.datetime.now()
    data = {
        "title": title,
        "link": link,
        "description": description,
        "guid": link + "&uuid=" + str(uuid.uuid1()),
        "pubDate": str(now)
    }
    scraperwiki.sqlite.save(unique_keys=['link'], data=data)
    return "Saved!"

try: # Try and get ASINs from your Amazon Wish List
    url = "http://www.amazon.ca/wishlist/" + wishlist + "/ref=cm_wl_act_print_o?_encoding=UTF8&disableNav=1&items-per-page=2500&layout=standard-print&page=1&visitor-view=1"
    html = scraperwiki.scrape(url)
    root = lxml.html.fromstring(html)
    for element in root.cssselect("tbody[class='itemWrapper']"):
        string = element.attrib["name"]
        pieces = string.split(".")
        asins.append(pieces[3])
except:
    print "There was an error. Did you provide a working Amazon Wish List identifier?"
    exit;

# Process ASINs for further details

for asin in asins:
    price = 9999999
    url = "http://www.amazon.ca/dp/" + asin
    html = scraperwiki.scrape(url)
    root = lxml.html.fromstring(html)
    title = root.cssselect("span[id='btAsinTitle']")[0].text_content()
    if(title.find("Kindle Edition") > 0): # Check if this is an item for the Amazon Kindle
        for element in root.cssselect("div[class='buying'] input"):
            if(element.attrib["name"] == "displayedPrice"):
                price = float(element.attrib["value"])
        cheap = is_cheap(price)
    else:
        try: # Try and get the price of the item. Some items throw back garbage so the price is listed as cannot be found.
            price = float(root.cssselect("span[id='actualPriceValue'] b")[0].text_content()[1:])
        except(IndexError):
            print "We can't get a price for: " + title
            print "Try camelcamelcamel: http://uk.camelcamelcamel.com/product/" + asin
        cheap = is_cheap(price)
    print save(title, url, cheap)