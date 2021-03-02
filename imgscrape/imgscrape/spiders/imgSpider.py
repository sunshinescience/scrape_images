import scrapy
from imgscrape.items import ImgscrapeItem

class ImageSpider(scrapy.Spider):
    name = 'imagespider' # Name identifies the spider
    start_urls = ['https://www.gettyimages.co.uk/photos/golf-swing-technique?license=rf&phrase=golf%20swing%20technique&sort=best']

    for i in range(2, 84):
        url_first_part = "https://www.gettyimages.co.uk/photos/golf-swing-technique?license=rf&page="
        url_last_part = "&phrase=golf%20swing%20technique&sort=best"
        start_urls.append(url_first_part + str(i) + url_last_part)               
    
    def parse(self, response):
        for img in response.xpath('//img[@class="gallery-asset__thumb gallery-mosaic-asset__thumb"]/@src'):
            # yield {'URL': img}
            imageURL = img.extract()
            yield ImgscrapeItem(image_urls=[imageURL])
        