require 'nokogiri'
require 'mechanize'


@br = Mechanize.new { |b|
  b.user_agent_alias = 'Linux Firefox'
  b.read_timeout = 1200
  b.max_history=0
  b.retry_change_requests = true
  b.verify_mode = OpenSSL::SSL::VERIFY_NONE

}

class Array
  def pretty
    self.collect{|a| a.strip.to_i}
  end
end

Mechanize.html_parser = Nokogiri::HTML

BASE_URL = "http://tnbear.tn.gov/Ecommerce/"

def get_metadata(key, default)
    begin
      ScraperWiki.get_var(key, default)
    rescue Exception => e
        puts "ERROR: #{e.inspect} during get_metadata(#{key}, #{default})"
        retry
    end
end

def save_metadata(key, value)
    begin
      ScraperWiki.save_var(key, value)
    rescue Exception => e
        puts "ERROR: #{e.inspect} during save_metadata(#{key}) :: #{e.backtrace}"
        retry
    end
end

def text(str)
  begin
      return (str.nil? or str.text.nil?) ? "" : str.text.gsub(/\n|\t|^\s+|:|\s+$/,"")
  rescue Exception => e
      return str.text unless str.nil? 
      puts e.backtrace
  end
end

def attributes(t,attr)
  return (t.nil? or t.first.nil? or t.first.attributes.nil?) ? "" : t.first.attributes[attr].value
end

def exists(num)
    return ScraperWiki.sqliteexecute("select count(*) from swdata where scraped_number=?",[num])['data'][0][0]
end

def scrape(data,action,num)
  if action == "list"
    records = {}
      Nokogiri::HTML(data).xpath(".//*[@id='ctl00_MainContent_SearchResultList']/table/tr[position()>1]").each{|tr|
        td = tr.xpath("td")
        records = {
          "ENTITY_NUMBER" => text(td[0]),
          "URL" => BASE_URL + attributes(td[0].xpath("a"),"href"),
          "TYPE" => text(td[1]),
          "ENTITY_NAME" => text(td[2]),
          "ENTITY_TYPE" => text(td[3]),
          "STATUS" => text(td[4]),
          "DOF" => text(td[5]),
          "ENTITY_STATUS" => text(td[6]),
          "SCRAPED_NUMBER"=>num,"DOC"=>Time.now.to_s
        }
        #puts records.inspect
        
        ScraperWiki.save_sqlite(unique_keys=["ENTITY_NUMBER","ENTITY_TYPE","STATUS"],records)
        return (records['ENTITY_NUMBER'].nil? or records['ENTITY_NUMBER'].empty?)? nil : 0 
      }
  end 
  return nil
end

def action(index)
  begin
    params = {
      "ctl00$MainContent$txtSearchValue" =>"",
      "ctl00$MainContent$searchOpt"=>"chkSearchStartWith",
      "__EVENTTARGET"=>"ctl00$MainContent$SearchButton",
      "__EVENTARGUMENT" => "",
      "ctl00$MainContent$txtFilingId"=> index
    }
    @pg.form_with(:name => "aspnetForm") do |f|
      params.each{|k,v|
        f[k] = v
      }
      @pg =  f.submit
    end unless @pg.nil? or @pg.form_with(:name=>"aspnetForm").nil? 
    re = scrape(@pg.body,"list",index)
    #save_metadata("INDEX",index.next) unless re.nil? 
  end 
end

s_url = BASE_URL + "FilingSearch.aspx"
@pg = @br.get(s_url)

start = ScraperWiki.sqliteexecute("select max(scraped_number) from swdata")['data'].flatten.first.to_i
(start..start+500).each{|strt|
  action(strt)
  sleep(5)
}
require 'nokogiri'
require 'mechanize'


@br = Mechanize.new { |b|
  b.user_agent_alias = 'Linux Firefox'
  b.read_timeout = 1200
  b.max_history=0
  b.retry_change_requests = true
  b.verify_mode = OpenSSL::SSL::VERIFY_NONE

}

class Array
  def pretty
    self.collect{|a| a.strip.to_i}
  end
end

Mechanize.html_parser = Nokogiri::HTML

BASE_URL = "http://tnbear.tn.gov/Ecommerce/"

def get_metadata(key, default)
    begin
      ScraperWiki.get_var(key, default)
    rescue Exception => e
        puts "ERROR: #{e.inspect} during get_metadata(#{key}, #{default})"
        retry
    end
end

def save_metadata(key, value)
    begin
      ScraperWiki.save_var(key, value)
    rescue Exception => e
        puts "ERROR: #{e.inspect} during save_metadata(#{key}) :: #{e.backtrace}"
        retry
    end
end

def text(str)
  begin
      return (str.nil? or str.text.nil?) ? "" : str.text.gsub(/\n|\t|^\s+|:|\s+$/,"")
  rescue Exception => e
      return str.text unless str.nil? 
      puts e.backtrace
  end
end

def attributes(t,attr)
  return (t.nil? or t.first.nil? or t.first.attributes.nil?) ? "" : t.first.attributes[attr].value
end

def exists(num)
    return ScraperWiki.sqliteexecute("select count(*) from swdata where scraped_number=?",[num])['data'][0][0]
end

def scrape(data,action,num)
  if action == "list"
    records = {}
      Nokogiri::HTML(data).xpath(".//*[@id='ctl00_MainContent_SearchResultList']/table/tr[position()>1]").each{|tr|
        td = tr.xpath("td")
        records = {
          "ENTITY_NUMBER" => text(td[0]),
          "URL" => BASE_URL + attributes(td[0].xpath("a"),"href"),
          "TYPE" => text(td[1]),
          "ENTITY_NAME" => text(td[2]),
          "ENTITY_TYPE" => text(td[3]),
          "STATUS" => text(td[4]),
          "DOF" => text(td[5]),
          "ENTITY_STATUS" => text(td[6]),
          "SCRAPED_NUMBER"=>num,"DOC"=>Time.now.to_s
        }
        #puts records.inspect
        
        ScraperWiki.save_sqlite(unique_keys=["ENTITY_NUMBER","ENTITY_TYPE","STATUS"],records)
        return (records['ENTITY_NUMBER'].nil? or records['ENTITY_NUMBER'].empty?)? nil : 0 
      }
  end 
  return nil
end

def action(index)
  begin
    params = {
      "ctl00$MainContent$txtSearchValue" =>"",
      "ctl00$MainContent$searchOpt"=>"chkSearchStartWith",
      "__EVENTTARGET"=>"ctl00$MainContent$SearchButton",
      "__EVENTARGUMENT" => "",
      "ctl00$MainContent$txtFilingId"=> index
    }
    @pg.form_with(:name => "aspnetForm") do |f|
      params.each{|k,v|
        f[k] = v
      }
      @pg =  f.submit
    end unless @pg.nil? or @pg.form_with(:name=>"aspnetForm").nil? 
    re = scrape(@pg.body,"list",index)
    #save_metadata("INDEX",index.next) unless re.nil? 
  end 
end

s_url = BASE_URL + "FilingSearch.aspx"
@pg = @br.get(s_url)

start = ScraperWiki.sqliteexecute("select max(scraped_number) from swdata")['data'].flatten.first.to_i
(start..start+500).each{|strt|
  action(strt)
  sleep(5)
}
