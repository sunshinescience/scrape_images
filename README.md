## Setting up the project
### Install Scrapy
In the command line, type `conda install -c conda-forge scrapy`. Type y to proceed with necessary packages.

### Start a new project
In the command line, type `scrapy startproject project_name` amd in this case it would be:
`scrapy startproject imgscrape`

This created a imgscrape directory.

You can start your first spider with:
    `cd imgscrape`
    `scrapy genspider example example.com`

### Create a spider
Define a class, called a spider, which Scrapy uses to scrape information from a website. They must subclass scrapy.Spider and define the initial requests to make. In this example, we have created a file called imgSpider.py in the imgscrape/spiders directory.

#### Get a list of start url’s
The spider will start to crawl from a list of the URLs, called `start_urls`. For now, we will use the page https://www.gettyimages.co.uk/photos/golf-swing-technique?license=rf&phrase=golf%20swing%20technique&sort=best.

#### Construct the selectors
You need to extract the data from the HTML source. Querying responses using both XPath and CSS includes two shortcuts to use: `response.xpath()` and `response.css()`. In this instance, we will use the XPath selectors. CSS selectors can select text or attribute nodes using CSS3 pseudo-elements (i.e., ::).

Let's use the Scrapy shell to practice writing the selectors. Open up the command line. And type `scrapy shell website_url`, for example:
`scrapy shell https://www.gettyimages.co.uk/photos/golf-swing-technique?license=rf&phrase=golf%20swing%20technique&sort=best`. However, when I tried using the shell on this address, I wasn't able to. So I tried using `scrapy shell https://www.gettyimages.co.uk/photos/golf-swing-technique` and it worked. But then I found that you need to just enclose the url in quotes, because characters like & will not work if you don't. So, this works now:
`scrapy shell 'https://www.gettyimages.co.uk/photos/golf-swing-technique?license=rf&phrase=golf%20swing%20technique&sort=best'`

This is the class for the image tag to scrape the thumbnail images:
"gallery-asset__thumb gallery-mosaic-asset__thumb"

To get all of the src attributes from the img tag, use the XPath selector: 
response.xpath('//img[@class="gallery-asset__thumb gallery-mosaic-asset__thumb"]/@src').getall()

#### Scrape URLs in the spider
`
import scrapy
  
class ImageSpider(scrapy.Spider):
    name = 'imagespider' # Name identifies the spider
    start_urls = ['https://www.gettyimages.co.uk/photos/golf-swing-technique?license=rf&phrase=golf%20swing%20technique&sort=best']

    def parse(self, response):
        for img in response.xpath('//img[@class="gallery-asset__thumb gallery-mosaic-asset__thumb"]/@src').getall():
            yield {'URL': img}
`

In the directory, in the command line, type `scrapy crawl imagespider -o golf_images.csv` to save a spreadsheet with the scraped URL's.

### Install pillow
The Images Pipeline requires Pillow 4.0.0 or greater. Its used for thumbnailing and normalizing images to JPEG/RGB format. To install the [pillow](https://anaconda.org/conda-forge/pillow) package with conda, run `conda install -c conda-forge pillow`.

### Enable the media pipeline
An advantage of using the [ImagesPipeline](https://docs.scrapy.org/en/latest/topics/media-pipeline.html#using-the-images-pipeline) for image files is that some extra functions can be made to generate thumbnails and filter the images based on their size. 

In the settings.py file, two updates are needed:
The first update is to uncomment (if commented out) the ITEM_PIPELINES. And include the following code:
`ITEM_PIPELINES = {'scrapy.pipelines.images.ImagesPipeline': 1}`

The second update can be appended to the bottom of the file. This value, FILES_STORE, is simply the path to the output directory where the download images will be stored. Configure the target storage setting to a valid value that will be used for storing the downloaded images in order to enable the pipeline, use the code:
In that settings.py file, add in a valid path name to save your images:
`IMAGES_STORE = '/path/to/valid/dir'`

In the items.py file, add the code:
`
import scrapy

class ImgscrapeItem(scrapy.Item):
    image_urls = scrapy.Field()
    images = scrapy.Field()
`

### Get the spider to scrape images
At the top of our spider file, we want to import the data object model (in this case, called ImgscrapeItem) from the items.py file, so its in the folder imgscrape in this case. Add the code to the imgSpider.py file: 
`from imgscrape.items import ImgscrapeItem`

The complete code for one page of thumbnail images in the spider file is:
import scrapy
from imgscrape.items import ImgscrapeItem

class ImageSpider(scrapy.Spider):
    name = 'imagespider' # Name identifies the spider
    start_urls = ['https://www.gettyimages.co.uk/photos/golf-swing-technique?license=rf&phrase=golf%20swing%20technique&sort=best']

    def parse(self, response):
        for img in response.xpath('//img[@class="gallery-asset__thumb gallery-mosaic-asset__thumb"]/@src'):
            # yield {'URL': img}
            imageURL = img.extract()
            yield ImgscrapeItem(image_urls=[imageURL])
    
To download images, run the command in the command line:
scrapy crawl imagespider -o output.json

And the images will be downloaded in the folder imgscrape/images/full.

### Crawl to the next pages
The class we want is:
search-pagination__button search-pagination__button--next

response.xpath('//a[@class="search-pagination__button search-pagination__button--next"]').get() 
