# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup as bs
from dotenv import load_dotenv
import os
from ..items import LyricscrawlItem

class MetrolyricsSpider(scrapy.Spider):
    name = 'metrolyrics'
    allowed_domains = ['www.metrolyrics.com']
    start_urls = ['http://www.metrolyrics.com/']
    
    def start_requests(self):
        load_dotenv()
        singers = os.getenv("singers").replace(' ','-').split(',')
        for singer in singers:
            meta = {
                'singer':singer.replace('-',' ')
            }
            yield scrapy.Request("http://www.metrolyrics.com/"+  singer + "-lyrics.html",callback=self.parse, meta=meta)

    def parse(self, response):
        start_r_meta = response.meta
        source = bs(response.text, 'lxml')
        a_tags = source.select('tr td a.title')
        for href in a_tags:
            url = href.get('href')
            meta = {
                'singer':start_r_meta['singer'],
                'title':href.text.replace(' Lyrics','').strip(),
                'url':url
            }
            yield scrapy.Request(url ,callback=self.lyrics_parse, meta=meta)
    
    def lyrics_parse(self, response):
        item = LyricscrawlItem()
        meta = response.meta
        source = bs(response.text, 'lxml')
        verse_tags = source.select('div#lyrics-body-text p.verse')
        lyrics =''
        for verse in verse_tags:
            lyrics += verse.text
        item['title'] = meta['title']
        item['url'] = meta['url']
        item['lyrics'] = lyrics        
        item['singer'] = meta['singer']
        return item