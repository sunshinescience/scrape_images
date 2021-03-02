import scrapy
  
class golfimgspider(scrapy.Spider):
    name = 'golfimg'
    start_urls = ['https://www.google.com/search?q=golf+swing+images&client=firefox-b-e&sxsrf=ALeKk02GLeeXfjkKI7QpEHryzmSD-CnX2w:1609934027493&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjg6cfOn4fuAhXUOcAKHUyrAoEQ_AUoAXoECBEQAw&biw=990&bih=768']

    