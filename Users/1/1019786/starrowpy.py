###############################################################################
# START HERE: Tutorial 1: Getting used to the ScraperWiki editing interface.
# Follow the actions listed with -- BLOCK CAPITALS below.
###############################################################################

# -----------------------------------------------------------------------------
# 1. Start by running a really simple Python script, just to make sure that 
# everything is working OK.
# -- CLICK THE 'RUN' BUTTON BELOW
# You should see some numbers print in the 'Console' tab below. If it doesn't work, 
# try reopening this page in a different browser - Chrome or the latest Firefox.
# -----------------------------------------------------------------------------

import turtle
def stars(n):
  if(n==0):
   return
  else:
    print('*')
    stars(n-1)
if __name__ == '__main__':
    n= input("Please enter a number")
    stars(n)
    


# -----------------------------------------------------------------------------
# 2. Next, try scraping an actual web page and getting some raw HTML.
# -- UNCOMMENT THE THREE LINES BELOW (i.e. delete the # at the start of the lines)
# -- CLICK THE 'RUN' BUTTON AGAIN 
# You should see the raw HTML at the bottom of the 'Console' tab. 
# Click on the 'more' link to see it all, and the 'Sources' tab to see our URL - 
# you can click on the URL to see the original page. 
# -----------------------------------------------------------------------------

#import scraperwiki
#html = scraperwiki.scrape('http://scraperwiki.com/hello_world.html')
#print html

# -----------------------------------------------------------------------------
# In the next tutorial, you'll learn how to extract the useful parts
# from the raw HTML page.
# -----------------------------------------------------------------------------###############################################################################
# START HERE: Tutorial 1: Getting used to the ScraperWiki editing interface.
# Follow the actions listed with -- BLOCK CAPITALS below.
###############################################################################

# -----------------------------------------------------------------------------
# 1. Start by running a really simple Python script, just to make sure that 
# everything is working OK.
# -- CLICK THE 'RUN' BUTTON BELOW
# You should see some numbers print in the 'Console' tab below. If it doesn't work, 
# try reopening this page in a different browser - Chrome or the latest Firefox.
# -----------------------------------------------------------------------------

import turtle
def stars(n):
  if(n==0):
   return
  else:
    print('*')
    stars(n-1)
if __name__ == '__main__':
    n= input("Please enter a number")
    stars(n)
    


# -----------------------------------------------------------------------------
# 2. Next, try scraping an actual web page and getting some raw HTML.
# -- UNCOMMENT THE THREE LINES BELOW (i.e. delete the # at the start of the lines)
# -- CLICK THE 'RUN' BUTTON AGAIN 
# You should see the raw HTML at the bottom of the 'Console' tab. 
# Click on the 'more' link to see it all, and the 'Sources' tab to see our URL - 
# you can click on the URL to see the original page. 
# -----------------------------------------------------------------------------

#import scraperwiki
#html = scraperwiki.scrape('http://scraperwiki.com/hello_world.html')
#print html

# -----------------------------------------------------------------------------
# In the next tutorial, you'll learn how to extract the useful parts
# from the raw HTML page.
# -----------------------------------------------------------------------------