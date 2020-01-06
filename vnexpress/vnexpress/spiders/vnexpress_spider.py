# system
import os

# lib
import scrapy
import urllib.request
from scrapy.utils.project import get_project_settings

from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging

# project
from vnexpress.core import utils as services

settings = get_project_settings()

VIDEOS_PATH = os.path.join(settings.get('BOT_NAME'), 'mp4')
URLS_PATH = os.path.join(settings.get('BOT_NAME'), 'urls')


class VnExpressSpider(scrapy.Spider):
    name = "video_vnexpress"

    def start_requests(self):
        urls = []
        url_file = os.path.join(URLS_PATH, 'urls.txt')
        with open(url_file) as fp:
            line = fp.readline()
            cnt = 1
            while line:
                print("Line {}: {}".format(cnt, line.strip()))
                line = fp.readline()
                cnt += 1
                urls.append(line)

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

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


class KhoaHocSpider(scrapy.Spider):
    name = "khoahoc_vnexpress"
    starts_urls = [
        'https://vnexpress.net/khoa-hoc/thuong-thuc'
    ]

    def parse(self, response):
        print('Start extract')
        urls = response.css('h4.title_news a.icon_commend::attr(href)').getall()

        url_file = os.path.join(URLS_PATH, 'urls.txt')
        with open(url_file, 'a') as file:
            for url in urls:
                file.write(url + '\n')

        next_page = response.css('a.next::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            print('Next_page: ', next_page)
            yield scrapy.Request(next_page, callback=self.parse)

        print('Finished extract')
