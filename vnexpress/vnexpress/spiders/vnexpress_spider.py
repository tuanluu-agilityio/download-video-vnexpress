# system
import os

# lib
import scrapy
import urllib.request
from scrapy.utils.project import get_project_settings

# project
from vnexpress.core import utils as services

settings = get_project_settings()

VIDEOS_PATH = os.path.join(settings.get('BOT_NAME'), 'mp4')


class VnExpressSpider(scrapy.Spider):
    name = "video_vnexpress"
    start_urls = [
        'https://vnexpress.net/infographics/ngoi-sao-lon-gap-1-400-lan-mat-troi-co-the-sap-phat-no-4033020.html',
        'https://vnexpress.net/infographics/su-ra-doi-cua-nhung-ngoi-sao-dau-tien-trong-vu-tru-4033285.html'
    ]

    def parse(self, response):
        print('Start download')
        # parse video from vnexpress
        url = response.xpath('//video[@type]/@src').get()

        # convert .m3u8 to .mp4 file
        new_url, file_name = services.get_new_url(url)

        # save file to mp4/
        fullfilename = os.path.join(VIDEOS_PATH, file_name)

        # execute download file
        urllib.request.urlretrieve(str(new_url), fullfilename)

        print('Download {0} finish!!!'.format(file_name))
