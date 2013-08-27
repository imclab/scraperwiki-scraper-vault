import scraperwiki
import urlparse
import lxml.html

# scrape_table function: gets passed an individual page to scrape
def scrape_divs(url):
    html = scraperwiki.scrape(url)
    print html
    root = lxml.html.fromstring(html)
#MAY BE BETTER TO USE     rows = root.cssselect("article div")  
#ALSO CAN THEN ADD alltext = row[0].text_content()
    #line below selects all <div class="block size3of4"> - note that because there is a space in the value of the div class, we need to put it in inverted commas as a string
    rows = root.cssselect("div.'block size3of4'") 
#ERROR generated by line 21 below can be corrected by changing above to rows = root.cssselect("article") or by using if statements below to test presence of h4, etc.
    for row in rows:
        # Set up our data record - we'll need it later
        print row
        record = {}
        #grab all <h4> tags within our <div>
        h4s = row.cssselect("h4")
        if h4s:
            membername = h4s[0].text
        #repeat process for <h4><span>, and further down, the last [-1] <p>
        spans = row.cssselect("h4 span")
        if spans:
            membertitle = spans[0].text
        ps = row.cssselect("p")
        if ps:
            memberbiog = ps[-1].text_content()
        record['URL'] = url
        record['Name'] = membername
        record['Title'] = membertitle
        record['Description'] = memberbiog
        print record, '------------'
        # Finally, save the record to the datastore - 'Name' is our unique key
#MAY BE WORTH USING A DIFFERENT KEY?
        scraperwiki.sqlite.save(["Name"], record)
        
#list of URLs with similar CMS compiled with this advanced search on Google:
#inurl:about-us/board.aspx CCG
#https://www.google.co.uk/search?q=ccg+nhs+uk+board&channel=linkdoctor&safe=on#hl=en&safe=active&sclient=psy-ab&q=inurl:about-us%2Fboard.aspx+CCG&oq=inurl:about-us%2Fboard.aspx+CCG

ccglist = ['www.brentccg.nhs.uk/', 'www.ealingccg.nhs.uk/', 'www.hounslowccg.nhs.uk/', 'www.westlondonccg.nhs.uk/', 'www.centrallondonccg.nhs.uk/', 'www.harrowccg.nhs.uk/', 'www.hammersmithfulhamccg.nhs.uk/']
for ccg in ccglist:
    scrape_divs('http://'+ccg+'about-us/board.aspx')
import scraperwiki
import urlparse
import lxml.html

# scrape_table function: gets passed an individual page to scrape
def scrape_divs(url):
    html = scraperwiki.scrape(url)
    print html
    root = lxml.html.fromstring(html)
#MAY BE BETTER TO USE     rows = root.cssselect("article div")  
#ALSO CAN THEN ADD alltext = row[0].text_content()
    #line below selects all <div class="block size3of4"> - note that because there is a space in the value of the div class, we need to put it in inverted commas as a string
    rows = root.cssselect("div.'block size3of4'") 
#ERROR generated by line 21 below can be corrected by changing above to rows = root.cssselect("article") or by using if statements below to test presence of h4, etc.
    for row in rows:
        # Set up our data record - we'll need it later
        print row
        record = {}
        #grab all <h4> tags within our <div>
        h4s = row.cssselect("h4")
        if h4s:
            membername = h4s[0].text
        #repeat process for <h4><span>, and further down, the last [-1] <p>
        spans = row.cssselect("h4 span")
        if spans:
            membertitle = spans[0].text
        ps = row.cssselect("p")
        if ps:
            memberbiog = ps[-1].text_content()
        record['URL'] = url
        record['Name'] = membername
        record['Title'] = membertitle
        record['Description'] = memberbiog
        print record, '------------'
        # Finally, save the record to the datastore - 'Name' is our unique key
#MAY BE WORTH USING A DIFFERENT KEY?
        scraperwiki.sqlite.save(["Name"], record)
        
#list of URLs with similar CMS compiled with this advanced search on Google:
#inurl:about-us/board.aspx CCG
#https://www.google.co.uk/search?q=ccg+nhs+uk+board&channel=linkdoctor&safe=on#hl=en&safe=active&sclient=psy-ab&q=inurl:about-us%2Fboard.aspx+CCG&oq=inurl:about-us%2Fboard.aspx+CCG

ccglist = ['www.brentccg.nhs.uk/', 'www.ealingccg.nhs.uk/', 'www.hounslowccg.nhs.uk/', 'www.westlondonccg.nhs.uk/', 'www.centrallondonccg.nhs.uk/', 'www.harrowccg.nhs.uk/', 'www.hammersmithfulhamccg.nhs.uk/']
for ccg in ccglist:
    scrape_divs('http://'+ccg+'about-us/board.aspx')
import scraperwiki
import urlparse
import lxml.html

# scrape_table function: gets passed an individual page to scrape
def scrape_divs(url):
    html = scraperwiki.scrape(url)
    print html
    root = lxml.html.fromstring(html)
#MAY BE BETTER TO USE     rows = root.cssselect("article div")  
#ALSO CAN THEN ADD alltext = row[0].text_content()
    #line below selects all <div class="block size3of4"> - note that because there is a space in the value of the div class, we need to put it in inverted commas as a string
    rows = root.cssselect("div.'block size3of4'") 
#ERROR generated by line 21 below can be corrected by changing above to rows = root.cssselect("article") or by using if statements below to test presence of h4, etc.
    for row in rows:
        # Set up our data record - we'll need it later
        print row
        record = {}
        #grab all <h4> tags within our <div>
        h4s = row.cssselect("h4")
        if h4s:
            membername = h4s[0].text
        #repeat process for <h4><span>, and further down, the last [-1] <p>
        spans = row.cssselect("h4 span")
        if spans:
            membertitle = spans[0].text
        ps = row.cssselect("p")
        if ps:
            memberbiog = ps[-1].text_content()
        record['URL'] = url
        record['Name'] = membername
        record['Title'] = membertitle
        record['Description'] = memberbiog
        print record, '------------'
        # Finally, save the record to the datastore - 'Name' is our unique key
#MAY BE WORTH USING A DIFFERENT KEY?
        scraperwiki.sqlite.save(["Name"], record)
        
#list of URLs with similar CMS compiled with this advanced search on Google:
#inurl:about-us/board.aspx CCG
#https://www.google.co.uk/search?q=ccg+nhs+uk+board&channel=linkdoctor&safe=on#hl=en&safe=active&sclient=psy-ab&q=inurl:about-us%2Fboard.aspx+CCG&oq=inurl:about-us%2Fboard.aspx+CCG

ccglist = ['www.brentccg.nhs.uk/', 'www.ealingccg.nhs.uk/', 'www.hounslowccg.nhs.uk/', 'www.westlondonccg.nhs.uk/', 'www.centrallondonccg.nhs.uk/', 'www.harrowccg.nhs.uk/', 'www.hammersmithfulhamccg.nhs.uk/']
for ccg in ccglist:
    scrape_divs('http://'+ccg+'about-us/board.aspx')
