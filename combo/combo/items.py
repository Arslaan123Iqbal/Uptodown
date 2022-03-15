# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html



import scrapy


class ComboItem(scrapy.Field):
    # define the fields for your item here like:

    type = scrapy.Item()
  
    icon = scrapy.Item()
    
    title= scrapy.Item()
    version_name = scrapy.Item()
    category = scrapy.Item()
    short_desc = scrapy.Item()
    developer = scrapy.Item()
    gallery_images = scrapy.Item()
    video= scrapy.Item()
    
    description = scrapy.Item()
    requirement =scrapy.Item()
    size = scrapy.Item()
    information = scrapy.Item()
    rating = scrapy.Item()
    updated = scrapy.Item()
    change_log = scrapy.Item()
    video = scrapy.Item()
    reviews = scrapy.Item()
    latest_download_link = scrapy.Item()
  
    
    
    


    