
from time import sleep
import scrapy
from sqlalchemy import table
import w3lib.html

from combo.items import ComboItem


class Sitemap1Spider(scrapy.Spider):
    name = 'sitemap1'
    with open("E:\\Work\\Web Development\\Python\\uptodown\\combo\\combo\\spiders\\urls1.csv", "rt") as f:
        start_urls = [url.strip() for url in f]

   

    def parse(self, response):
       
        item = ComboItem()
        item["title"] = response.css(".box-title::text").extract_first().replace("\n","").strip()
      
        item["version_name"] = response.css(".htlgb::text").extract_first()
        item["category"] = response.css('a[rel="category tag"]::text').getall()
        item["short_desc"] = response.css(".descripcion::text").get()
        # item["developer"] = response.css(".box-data-app>.left.data-app>span::text").extract()[0]
        
        # updated = str(response.css(".box-data-app>.left.data-app>span>div").extract()[1])
        # item["updated"]= w3lib.html.remove_tags(updated)
        
        # requirement = response.css(".box-data-app>.left.data-app>span>div").extract()[2]
        # item["requirement"] = w3lib.html.remove_tags(requirement)
        
        # size = response.css(".box-data-app>.left.data-app>span>div").extract()[3]
        # item["size"] =   w3lib.html.remove_tags(size)
        
        description = response.css(".entry-limit").get()
        item["description"] = w3lib.html.remove_tags(description).strip().replace("\n","")
        
        item["gallery_images"] = response.css(".px-carousel-item>img::attr(data-big-src)").getall()
        yield item
        # yield {
        #     "title":title,
        #     "version":version,
        #     "category":category,
        #     "short_dec":short_desc,
        #     "developer":developer,
        #     "updated":updatd_value,
        #     "requirement":requirement_value,
        #     "size":size_value,
        #     "description":description_value,
        #     "gallery":gallery_images
        # }
