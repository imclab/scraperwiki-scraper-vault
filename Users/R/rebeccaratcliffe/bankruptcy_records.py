# Data stored on individual pages not accessible from one single page
# typical URL is http://www.london-gazette.co.uk/id/issues/60115/notices/1572287
# Need to cycle through an array of those codes, created by using the =JOIN formula in Google Docs

#If you want to understand this scraper - start at the bottom where it says 'base_url' (line 47)

import scraperwiki
#import urlparse
import lxml.html

#Create a function called 'scrape_table' which is called in the function 'scrape_page' below
#The 'scrape_page' function also passed the contents of the page to this function as 'root'
def scrape_table(root):
    #Use cssselect to find the contents of a particular HTML tag, and put it in a new object 'rows'
    #there's more than one table, so we need to specify the class="destinations", represented by the full stop
    rows = root.cssselect("table.destinations tr")
    for row in rows:
        #Create a new empty record
        record = {}
        #Assign the contents of <td> to a new object called 'table_cells'
        table_cells = row.cssselect("td")
        #If there's anything
#TO ADD: AN ELSE FOR THOSE PAGES THAT SEEM TO HAVE BEEN SKIPPED? STORE ID AND 'NOT SCRAPED'?        
        if table_cells: 
            #Put the contents of the first <td> into a record in the column 'BKRPT'
            record['BKRPT'] = table_cells[0].text
            #this takes the ID number, which has been named item in the for loop below
            record['ID'] = item
            print record, '------------'
            #Save in the SQLite database, with the ID code to be used as the unique reference
            scraperwiki.sqlite.save(["ID"], record)


#this creates a new function and (re)names whatever parameter is passed to it - i.e. 'next_link' below - as 'url'
def scrape_page(url):
    #now 'url' is scraped with the scraperwiki library imported above, and the contents put into a new object, 'html'
    html = scraperwiki.scrape(url)
    print html
    #now we use the lxml.html function imported above to convert 'html' into a new object, 'root'
    root = lxml.html.fromstring(html)
    #now we call another function on root, which we write - above
    scrape_table(root)

#START HERE: This is the part of the URL which all our pages share
base_url = 'http://www.london-gazette.co.uk/id/issues/60115/notices/'
#And these are the numbers which we need to complete that URL to make each individual URL
#This array has been compiled using the =JOIN formula in Google Docs on a column of bankruptcy codes
BKRPTIDs =
['1572292','1572287','1572295','1572220','1572269','1572218','1572243','1572267','1572293','1572291','1572273','1572227','1572231','1572233','1572261','1572266','1572249','1572228','1572241','1572274','1572265','1572254','1572255','1572319','1572320','1572235','1572223','1572299','1572214','1572213','1572288','1572276','1572316','1572317','1572239','1572290','1572229','1572258','1572321','1572306','1572215','1572302','1572234','1572264','1572270','1572282','1572262','1572278','1572219','1572328','1572230','1572307','1572305','1572326','1572272','1572309','1572242','1572245','1572247','1572263','1572240','1572318','1572308','1572232','1572238','1572323','1572226','1572313','1572300','1572244','1572257','1572222','1572221','1572277','1572275','1572286','1572322','1572312','1572315','1572327','1572310','1572311','1572296','1572256','1572259','1572325','1572294','1572285','1572260','1572271','1572217','1572284','1572251','1572297','1572301','1572225','1572224','1572298','1572314','1572324','1572268','1572279','1572250','1572237','1572303','1572248','1572289','1572283','1572236','1572253','1572216','1572252','1572280','1572281','1572304','1572246','1570598','1570718','1570762','1570592','1570633','1570626','1570600','1570599','1570601','1570673','1570683','1570634','1570747','1570617','1570662','1570680','1570697','1570682','1570759','1570658','1570660','1570614','1570663','1570712','1570745','1570603','1570699','1570702','1570719','1570668','1570714','1570628','1570678','1570667','1570757','1570684','1570632','1570640','1570659','1570656','1570602','1570732','1570758','1570704','1570590','1570700','1570698','1570645','1570711','1570610','1570728','1570705','1570750','1570639','1570619','1570695','1570605','1570737','1570709','1570642','1570641','1570607','1570671','1570657','1570638','1570615','1570720','1570716','1570670','1570664','1570736','1570690','1570652','1570752','1570623','1570612','1570733','1570730','1570701','1570681','1570606','1570621','1570654','1570715','1570708','1570651','1570743','1570613','1570636','1570637','1570648','1570609','1570627','1570596','1570754','1570691','1570625','1570749','1570723','1570744','1570740','1570706','1570721','1570756','1570687','1570618','1570666','1570746','1570726','1570653','1570620','1570595','1570710','1570688','1570689','1570672','1570707','1570717','1570713','1570703','1570696','1570693','1570643','1570646','1570622','1570677','1570647','1570655','1570661','1570692','1570685','1570729','1570738','1570755','1570629','1570630','1570694','1570608','1570635','1570722','1570735','1570676','1570594','1570742','1570686','1570725','1570724','1570731','1570761','1570665','1570739','1570679','1570675','1570674','1570669','1570591','1570748','1570751','1570753','1570734','1570760','1570597','1570604','1570741','1570727','1570611','1570649','1570650','1570644','1570593','1570624','1570616','1570631','1569625','1569622','1569621','1569570','1569611','1569588','1569579','1569540','1569598','1569587','1569575','1569641','1569606','1569596','1569581','1569639','1569638','1569605','1569650','1569541','1569545','1569586','1569536','1569634','1569635','1569559','1569535','1569620','1569601','1569531','1569552','1569615','1569592','1569643','1569549','1569557','1569573','1569637','1569623','1569626','1569585','1569646','1569607','1569577','1569547','1569628','1569539','1569612','1569613','1569627','1569636','1569630','1569571','1569537','1569597','1569589','1569528','1569527','1569616','1569544','1569565','1569568','1569542','1569521','1569603','1569584','1569651','1569543','1569645','1569556','1569555','1569534','1569550','1569608','1569523','1569632','1569566','1569522','1569624','1569580','1569594','1569567','1569578','1569574','1569648','1569618','1569576','1569530','1569569','1569652','1569546','1569583','1569593','1569647','1569591','1569548','1569595','1569609','1569614','1569561','1569604','1569619','1569529','1569582','1569617','1569599','1569524','1569526','1569572','1569525','1569560','1569610','1569633','1569640','1569631','1569644','1569563','1569564','1569642','1569538','1569600','1569553','1569590','1569554','1569558','1569649','1569532','1569629','1569602','1569562','1569551','1569533','1568529','1568613','1568537','1568593','1568532','1568614','1568541','1568546','1568523','1568560','1568590','1568611','1568573','1568518','1568530','1568524','1568526','1568558','1568516','1568574','1568547','1568515','1568565','1568575','1568549','1568536','1568610','1568597','1568527','1568578','1568501','1568500','1568545','1568604','1568602','1568555','1568543','1568506','1568520','1568519','1568534','1568600','1568608','1568581','1568569','1568598','1568514','1568513','1568508','1568601','1568571','1568512','1568585','1568603','1568521','1568584','1568589','1568511','1568596','1568582','1568591','1568570','1568612','1568544','1568553','1568595','1568588','1568583','1568522','1568504','1568542','1568594','1568567','1568617','1568579','1568561','1568548','1568556','1568554','1568507','1568538','1568503','1568599','1568592','1568577','1568607','1568539','1568586','1568576','1568535','1568531','1568609','1568499','1568517','1568572','1568564','1568563','1568618','1568498','1568540','1568528','1568525','1568559','1568580','1568552','1568562','1568587','1568566','1568551','1568550','1568510','1568502','1568606','1568616','1568568','1568509','1568605','1568615','1568496','1568533','1568557','1567665','1567688','1567627','1567700','1567621','1567636','1567674','1567675','1567704','1567679','1567617','1567685','1567643','1567678','1567645','1567693','1567673','1567628','1567699','1567638','1567654','1567640','1567631','1567702','1567646','1567701','1567708','1567676','1567672','1567637','1567660','1567711','1567618','1567681','1567648','1567655','1567657','1567694','1567677','1567624','1567639','1567691','1567707','1567706','1567698','1567623','1567689','1567668','1567705','1567656','1567692','1567669','1567632','1567666','1567690','1567614','1567658','1567712','1567663','1567697','1567670','1567649','1567686','1567653','1567687','1567713','1567683','1567684','1567635','1567695','1567619','1567667','1567671','1567634','1567642','1567696','1567714','1567710','1567709','1567630','1567703','1567652','1567651','1567680','1567629','1567661','1567664','1567644','1567641','1567659','1567620','1567622','1567613','1567616','1567633','1567650','1567615','1567662','1567682','1567647','1567626','1567625','1566760','1566714','1566762','1566698','1566764','1566756','1566687','1566774','1566773','1566707','1566741','1566748','1566723','1566729','1566728','1566745','1566769','1566768','1566772','1566783','1566730','1566681','1566746','1566766','1566721','1566739','1566738','1566715','1566718','1566685','1566706','1566726','1566709','1566712','1566710','1566702','1566780','1566688','1566680','1566770','1566731','1566742','1566720','1566724','1566758','1566727','1566696','1566695','1566497','1566757','1566782','1566737','1566740','1566725','1566767','1566692','1566775','1566686','1566744','1566699','1566701','1566787','1566683','1566776','1566749','1566704','1566682','1566736','1566781','1566716','1566684','1566778','1566759','1566752','1566751','1566733','1566711','1566785','1566719','1566679','1566761','1566771','1566700','1566765','1566735','1566784','1566708','1566763','1566676','1566678','1566677','1566755','1566743','1566786','1566779','1566777','1566690','1566693','1566750','1566754','1566753','1566697','1566722','1566691','1566703','1566713','1566717','1566705','1566747','1566734','1566694','1566732','1566689','1565557','1565484','1565468','1565469','1565497','1565514','1565525','1565567','1565457','1565522','1565523','1565459','1565467','1565505','1565451','1565502','1565561','1565533','1565569','1565499','1565440','1565494','1565482','1565439','1565507','1565535','1565527','1565564','1565543','1565544','1565529','1565443','1565462','1565449','1565461','1565472','1565460','1565441','1565503','1565446','1565565','1565518','1565574','1565520','1565553','1565493','1565555','1565560','1565576','1565515','1565475','1565488','1565566','1565568','1565573','1565551','1565496','1565504','1565552','1565537','1565466','1565530','1565526','1565546','1565528','1565517','1565532','1565437','1565456','1565558','1565577','1565508','1565476','1565442','1565579','1565477','1565498','1565509','1565559','1565479','1565538','1565516','1565458','1565485','1565519','1565563','1565542','1565450','1565471','1565455','1565575','1565501','1565500','1565473','1565548','1565444','1565550','1565562','1565506','1565512','1565511','1565556','1565554','1565487','1565513','1565524','1565481','1565510','1565465','1565570','1565571','1565464','1565534','1565447','1565486','1565578','1565448','1565470','1565572','1565491','1565581','1565531','1565490','1565478','1565536','1565453','1565463','1565547','1565545','1565489','1565580','1565438','1565521','1565483','1565436','1565435','1565452','1565495','1565549','1565492','1565480','1565539','1565540','1565445','1565541','1565454','1565474','1564406','1564459','1564508','1564414','1564411','1564514','1564418','1564440','1564428','1564426','1564443','1564409','1564476','1564404','1564473','1564457','1564468','1564455','1564454','1564432','1564477','1564438','1564423','1564518','1564390','1564439','1564442','1564474','1564435','1564512','1564467','1564452','1564401','1564486','1564494','1564503','1564516','1564484','1564421','1564483','1564396','1564436','1564488','1564447','1564491','1564448','1564419','1564410','1564400','1564479','1564391','1564501','1564482','1564431','1564460','1564515','1564481','1564492','1564398','1564461','1564434','1564490','1564502','1564397','1564495','1564389','1564388','1564466','1564392','1564499','1564449','1564500','1564497','1564496','1564504','1564469','1564517','1564465','1564513','1564464','1564471','1564403','1564475','1564402','1564415','1564412','1564441','1564505','1564433','1564385','1564420','1564493','1564446','1564417','1564416','1564462','1564463','1564387','1564487','1564451','1564437','1564405','1564399','1564444','1564425','1564394','1564470','1564445','1564510','1564393','1564478','1564509','1564450','1564427','1564489','1564480','1564498','1564472','1564395','1564386','1564424','1564506','1564507','1564458','1564453','1564407','1564485','1564429','1564430','1564456','1564413','1564408','1564511','1564422','1563770','1563666','1563714','1563659','1563811','1563756','1563755','1563748','1563699','1563707','1563682','1563744','1563777','1563768','1563673','1563824','1563745','1563670','1563695','1563829','1563704','1563838','1563819','1563710','1563749','1563759','1563837','1563674','1563723','1563669','1563686','1563698','1563796','1563763','1563804','1563803','1563814','1563662','1563722','1563773','1563685','1563660','1563781','1563677','1563752','1563806','1563702','1563730','1563817','1563816','1563732','1563731','1563706','1563696','1563832','1563668','1563676','1563823','1563784','1563786','1563818','1563747','1563746','1563717','1563709','1563794','1563822','1563826','1563815','1563810','1563785','1563780','1563754','1563721','1563691','1563767','1563757','1563719','1563790','1563689','1563713','1563712','1563831','1563828','1563800','1563833','1563834','1563839','1563825','1563812','1563813','1563716','1563753','1563769','1563665','1563836','1563703','1563827','1563835','1563687','1563718','1563779','1563715','1563711','1563690','1563801','1563799','1563663','1563758','1563680','1563742','1563700','1563809','1563708','1563733','1563802','1563720','1563672','1563783','1563750','1563774','1563791','1563787','1563728','1563684','1563692','1563727','1563681','1563661','1563775','1563697','1563788','1563694','1563705','1563766','1563683','1563793','1563701','1563765','1563778','1563760','1563735','1563738','1563743','1563664','1563693','1563805','1563688','1563725','1563820','1563795','1563830','1563821','1563807','1563741','1563737','1563789','1563675','1563729','1563798','1563772','1563771','1563797','1563726','1563776','1563751','1563808','1563762','1563679','1563782','1563678','1563671','1563734','1563764','1563736','1563724','1563739','1563740','1563761','1563792','1563667','1562836','1562837','1562886','1562885','1562834','1562896','1562840','1562859','1562854','1562934','1562968','1562899','1562941','1562905','1562973','1562975','1562956','1562911','1562951','1562833','1562921','1562974','1562869','1562907','1562900','1562906','1562877','1562876','1562875','1562889','1562919','1562966','1562977','1562917','1562918','1562888','1562923','1562937','1562938','1562851','1562893','1562891','1562871','1562939','1562963','1562920','1562962','1562972','1562936','1562860','1562872','1562970','1562930','1562890','1562915','1562909','1562908','1562943','1562942','1562967','1562957','1562873','1562933','1562865','1562883','1562842','1562976','1562935','1562979','1562850','1562922','1562880','1562884','1562852','1562926','1562832','1562856','1562855','1562892','1562931','1562830','1562952','1562945','1562959','1562903','1562902','1562864','1562867','1562910','1562950','1562904','1562868','1562913','1562846','1562978','1562949','1562928','1562829','1562947','1562841','1562955','1562954','1562878','1562898','1562981','1562980','1562870','1562874','1562857','1562858','1562838','1562882','1562929','1562831','1562924','1562948','1562894','1562827','1562916','1562881','1562969','1562897','1562853','1562961','1562863','1562964','1562940','1562879','1562848','1562965','1562845','1562927','1562849','1562861','1562960','1562826','1562958','1562914','1562971','1562828','1562843','1562862','1562866','1562925','1562835','1562944','1562839','1562953','1562895','1562932','1562847','1562912','1562946','1562901','1562844','1562887']
#go through the bankruptIDs array above, and for each ID...
for item in :
    #show it in the console
    print item
    #create a URL called 'next_link' which adds that ID to the end of the base_url variable
    next_link = base_url+item
    #pass that new concatenated URL to a function, 'scrape_page', which is scripted above
    scrape_page(next_link)

#In each page puts contents of all <a> tags in <div class="Result"> into a list,
#Then loops through and puts the first 'about' attribute of each into a table
#Then finds 'next' link, and does the same for that linked page

#http://www.london-gazette.co.uk/issues/recent/10/personal-insolvency/bankruptcy/start=1
#HTML:
#<div id="divResult" class="Result">
#<dl class="Details">
# <dt class="PubDate">Date:</dt>
# <dd class="PubDate">
#<p class="summary">
# <strong class="highlight">60112</strong> 
#<ul class="Links">                       
# <li class="lteIE6_first-child" about="http://www.london-gazette.co.uk/id/issues/60112" typeof="g:Issue" property="g:hasPublicationDate" content="2012-04-10" rel="g:hasNotice"><a href="/issues/60112/notices/1568613/recent=10;category=personal-insolvency;subcategory=bankruptcy" about="http://www.london-gazette.co.uk/id/issues/60112/notices/1568613" typeof="g:Notice"><img alt="See full notice" title="See full notice" src="/styles/styleimages/button_seeFullNotice.gif" /></a></li>
# <li about="http://www.london-gazette.co.uk/id/issues/60112/notices/1568613" typeof="g:Notice" rel="foaf:page"><a target="_blank" href="/issues/60112/pages/6994" typeof="foaf:Document"><img alt="See PDF" title="See PDF" src="/styles/styleimages/button_seePDF.gif" /></a></li><li><a target='_blank' href='https://www.tsoshop.co.uk/bookstore.asp?FO=1159966&amp;Action=AddItem&amp;ExternalRef=60112'>

import scraperwiki
import urlparse
import lxml.html

# scrape_table function: gets passed an individual page to scrape
def scrape_links(root):
#    print root.cssselect("div.Result p"), 'AGHHH'
    links = root.cssselect("div.Result a")  # selects all <a> links in <div class="Result">
    for link in links:
        # Set up data record
        record = {}
        aboutattr = link.attrib.get('about')
        if aboutattr:
            record['link'] = aboutattr
            print record, '------------'
            scraperwiki.sqlite.save(["link"], record)
        
# scrape_and_look_for_next_link function: calls the scrape_table
# function, then hunts for a 'next' link: if one is found, calls itself again
def scrape_and_look_for_next_link(url):
    html = scraperwiki.scrape(url)
    print html
    root = lxml.html.fromstring(html)
    scrape_links(root)
    next_link = root.cssselect("a.Next")
    print next_link
    if next_link:
        next_url = urlparse.urljoin(base_url, next_link[0].attrib.get('href'))
        print next_url
        scrape_and_look_for_next_link(next_url)

# START HERE: define your starting URL - then 
base_url = 'http://www.london-gazette.co.uk'
starting_url = urlparse.urljoin(base_url, '/issues/recent/10/personal-insolvency/bankruptcy/start=1')
scrape_and_look_for_next_link(starting_url)