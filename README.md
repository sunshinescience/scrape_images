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

#### Construct the selectors
You need to extract the data from the HTML source. Querying responses using both XPath and CSS includes two shortcuts to use: `response.xpath()` and `response.css()`. In this instance, we will use the XPath selectors. CSS selectors can select text or attribute nodes using CSS3 pseudo-elements (i.e., ::).

Let's use the Scrapy shell to practice writing the selectors. Open up the command line. And type `scrapy shell website_url`, for example:
`scrapy shell https://www.gettyimages.co.uk/photos/golf-swing-technique?license=rf&phrase=golf%20swing%20technique&sort=best`. However, when I tried using the shell on this address, I wasn't able to. So I tried using `scrapy shell https://www.gettyimages.co.uk/photos/golf-swing-technique` and it worked. But then I found that you need to just enclose the url in quotes, because characters like & will not work if you don't. So, this works now:
`scrapy shell 'https://www.gettyimages.co.uk/photos/golf-swing-technique?license=rf&phrase=golf%20swing%20technique&sort=best'`

This is the class for the image tag to scrape the thumbnail images:
"gallery-asset__thumb gallery-mosaic-asset__thumb"

To get all of the src attributes from the img tag, use the XPath selector: 
response.xpath('//img[@class="gallery-asset__thumb gallery-mosaic-asset__thumb"]/@src').getall()

### Install pillow
The Images Pipeline requires Pillow 4.0.0 or greater. Its used for thumbnailing and normalizing images to JPEG/RGB format. To install the [pillow](https://anaconda.org/conda-forge/pillow) package with conda, run `conda install -c conda-forge pillow`.

### Get a list of start url’s
The spider will start to crawl from a list of the URLs, called `start_urls`. For now, we will use: https://www.gettyimages.co.uk/photos/golf-swing-technique?license=rf&phrase=golf%20swing%20technique&sort=best

### Enable the media pipeline
An advantage of using the ImagesPipeline for image files is that some extra functions can be made to generate thumbnails and filter the images based on their size. 


