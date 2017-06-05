import scrapy
from itertools import islice
#import json

class DescriptionTextSpider(scrapy.Spider):
    name = "description_text"

    def start_requests(self):
        #--- Returns the next url every call
        #urls = ['https://www.kickstarter.com/projects/599092525/the-order-of-the-stick-reprint-drive?ref=category_recommended','https://www.kickstarter.com/projects/469955675/jump-start-kindergarten-toolkit?ref=category','https://www.kickstarter.com/projects/1469579873/auntie-dis-music-time-sign-asl-for-hearing-and-hoh/']
        #for url in urls:
        with open("webrobot_dataset_parsed.txt", "r") as f:
            for line in islice(f, 800, 1000): #skip first number lines, stop after second number lines
                url = line.split()[0]
                yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        imgCount = len( response.css('div.col.col-8.description-container').css('div.full-description.js-full-description.responsive-media.formatted-lists').css('div.template.asset').extract() )
        descText = ''.join( response.css('div.col.col-8.description-container').css('div.full-description.js-full-description.responsive-media.formatted-lists').css('::text').extract() ) +\
                   ''.join( response.css('div.col.col-8.description-container').css('div.js-risks').css('::text').extract() )
        descText = ' '.join(descText.split()) # Remove newlines and extra spaces
        duration = int(' '.join(response.css('div.NS_campaigns__funding_period').css('::text').extract()[-2].split()).strip('( days)'))
     
        yield {'descText': descText,'imgCount': imgCount,'duration': duration}






        #page = response.url.split("/")[-2]
        #filename = 'quotes-%s.html' % page
        # with open("test.txt", "a") as f:
        #     #f.write(response.body)
        #     #f.write(''.join( response.css('div.col.col-8.description-container').css('div.full-description.js-full-description.responsive-media.formatted-lists').css('::text').extract() ) +\
        #     #        ''.join( response.css('div.col.col-8.description-container').css('div.js-risks').css('::text').extract() ) + ' ' +\
        #     #        )
        #     imgCount = str( len( response.css('div.col.col-8.description-container').css('div.full-description.js-full-description.responsive-media.formatted-lists').css('div.template.asset').extract() ) )
        #     descText = ''.join( response.css('div.col.col-8.description-container').css('div.full-description.js-full-description.responsive-media.formatted-lists').css('::text').extract() ) +\
        #                ''.join( response.css('div.col.col-8.description-container').css('div.js-risks').css('::text').extract() )
            

        #     #mydict = {'len': descLen}
        #     #json.dump(descLen, f)
        #     f.write(d)

        #self.log('Saved file %s' % filename)
        #self.log('Saved')

        ##TEXT
        ##1-only description (no risks):
        # ''.join( response.css('div.col.col-8.description-container').css('div.full-description.js-full-description.responsive-media.formatted-lists').css('::text').extract() )
        ##2-risks:
        # ''.join( response.css('div.col.col-8.description-container').css('div.js-risks').css('::text').extract() )
        ##3-complete description:
        # ''.join( response.css('div.col.col-8.description-container').css('::text').extract() )
        ## Best to combine result of 1 and 2 with + operator

        ##NR OF IMG
        #len( response.css('div.col.col-8.description-container').css('div.full-description.js-full-description.responsive-media.formatted-lists').css('div.template.asset').extract() )

        ##FUNDING PERIOD
        #response.css('div.NS_campaigns__funding_period').css('::text').extract()[-2]