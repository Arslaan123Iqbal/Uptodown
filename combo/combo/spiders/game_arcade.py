from time import sleep
from weakref import proxy
from combo.items import ComboItem
import w3lib.html
import scrapy



class ArcadeSpider(scrapy.Spider):
    name = 'game-arcade'
    page_number =2
    start_urls = ['https://en.uptodown.com/android/arcade']

    def parse(self, response):
        for item in response.css('.name'):
            link = item.css('div.name> a::attr(href)').get()
           
            yield scrapy.Request(url=link,callback=self.parseInnerPage )
        next_page = "https://en.uptodown.com/android/arcade/"+str(ArcadeSpider.page_number)+"/"
        
        if next_page is not None:
            
            ArcadeSpider.page_number +=1
            sleep(7)
            
            yield scrapy.Request(url=next_page,callback=self.parse,meta={proxy:"http://170.155.5.235"})
           
    
    
    def parseInnerPage(self,response):
        item = ComboItem()
      
        
       
    
        item["icon"] = response.css(".icon>img::attr(src)").extract_first()
       
        item["title"] = response.css("#detail-app-name::text").extract_first()
        
        item["version_name"] = response.css(".version::text").extract_first()
        item["short_desc"] = response.css(".detail>h2::text").extract_first()
        item["gallery_images"] = response.css(".gallery>div>img::attr(data-src-large)").getall()
      
        
        # description
        text_description = response.css(".text-description").extract_first()
      
        ad= response.css(".text-description>div>div.ad.text").extract_first() 
        out = text_description.replace(ad or "","") 
        replace = out.replace("\n","")
        item["description"] =w3lib.html.remove_tags(replace).strip().rstrip()
        # More Information
       # table data
      
        table = response.css('table')
              
        result = {}
        
        for tr in table.css('tr'):
            row_header = tr.css('th::text').extract_first()
            row_value = tr.css('td::text').extract_first() or tr.css('td>a::text').extract_first()
           
            if row_value is not None:
           
                replace_value = row_value.replace("\n","")
            else:
                row_value ="" 
           
            replace_row_header = row_header.replace("Package Name","package_name") 
            replace_row_header_again =replace_row_header.replace("Why is this app published on Uptodown?","") and replace_row_header.replace("Op. System","type")
            replace_with_content = replace_row_header_again.replace("Content Rating","content_rating")
            result[replace_with_content.lower()] = replace_value
   
        
    
    
        item["information"] = result

       
        item["type"] = result["type"]
        item["update_date"] = result["date"]
        rating =response.css(".score::text").extract_first()
        if rating is not None:  
          rating_replace=  rating.replace("\n","")
          item["rating"]= rating_replace
        reviews =response.css("#more-comments-rate-section").extract_first()
        if reviews is not None: 
            reviews_remove =(w3lib.html.remove_tags(reviews)) 
            review_replace = reviews_remove.replace("\n","")
            item["reviews"] = str(review_replace)

        # Download page
        download_link = response.css("a.button.last::attr(href)").extract_first()
        sleep(1)
        request= scrapy.Request(url=download_link,callback=self.download_page,meta={'dont_redirect': True,proxy:["http://170.155.5.235"]})
        request.meta["item"] = item
   
        yield request
 
   # download page function
    def download_page(self,response):
       
        item = response.meta["item"]
        item["latest_download_link"] = response.css("a.button.download::attr(href)").extract_first()
        return item
        
        
           
           



    



    