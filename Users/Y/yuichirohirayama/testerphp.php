<?php

# Blank PHP
$html = scraperWiki::scrape("https://www.fostercareer.com/job/detail/JB0000000105");
print $html . "\n";

require 'scraperwiki/simple_html_dom.php';
$dom = new simple_html_dom();
$dom->load($html);
foreach($dom->find("div[@align='left'] tr") as $data){
    $tds = $data->find("td");
    if(count($tds)==12){
        $record = array(
            'country' => $tds[0]->plaintext, 
            'years_in_school' => intval($tds[4]->plaintext)
        );
        scraperwiki::save(array('country'), $record);

    }
}



?>
<?php

# Blank PHP
$html = scraperWiki::scrape("https://www.fostercareer.com/job/detail/JB0000000105");
print $html . "\n";

require 'scraperwiki/simple_html_dom.php';
$dom = new simple_html_dom();
$dom->load($html);
foreach($dom->find("div[@align='left'] tr") as $data){
    $tds = $data->find("td");
    if(count($tds)==12){
        $record = array(
            'country' => $tds[0]->plaintext, 
            'years_in_school' => intval($tds[4]->plaintext)
        );
        scraperwiki::save(array('country'), $record);

    }
}



?>
