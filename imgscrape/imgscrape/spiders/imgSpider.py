import scrapy
  
class ImageSpider(scrapy.Spider):
    name = 'imagespider' # Name identifies the spider
    start_urls = ['https://www.gettyimages.co.uk/photos/golf-swing-technique?license=rf&phrase=golf%20swing%20technique&sort=best']


#    def start_requests(self):
 #       urls = ['https://www.gettyimages.co.uk/photos/golf-swing-technique?license=rf&phrase=golf%20swing%20technique&sort=best',
  #      ]
   #     for url in urls: # Must return an iterable of Requests
    #        yield scrapy.Request(url=url, callback=self.parse) # Scrapy uses requests to ask for a page and gets responses from the webserver.
   
    def parse(self, response):
        for img in response.xpath('//img[@class="gallery-asset__thumb gallery-mosaic-asset__thumb"]/@src').getall():
            yield {'URL': img}
        

