import scrapy
  
class ImageSpider(scrapy.Spider):
    name = 'imagespider' # Name identifies the spider

    def start_requests(self):
        urls = ['https://www.gettyimages.co.uk/photos/golf-swing-technique?license=rf&phrase=golf%20swing%20technique&sort=best',
        ]
        for url in urls: # Must return an iterable of Requests
            yield scrapy.Request(url=url, callback=self.parse) # Scrapy uses requests to ask for a page and gets responses from the webserver.
    
    def parse(self, response):
              

