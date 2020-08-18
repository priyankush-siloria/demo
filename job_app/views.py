from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import login, logout, authenticate
from rest_framework.authentication import TokenAuthentication
from .models import *
from .serializers import *
from rest_framework import generics
import uuid, re,os
import requests ,sqlite3
import scrapy 
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerRunner
from scraper.scraper.items import SearchedItem
from scraper.scraper.pipelines import  SearchPipeline

searched = ""


class ExtractUrls(scrapy.Spider): 
      
    # This name must be unique always 
    name = "extract"  

    def __init__(self, key):
        print(key,'--------------------keykey')
        self.key = key
        urls = "https://www.bing.com/search?q=" + key
        self.url = urls
        # print(urls,'-----------------urls') 
        # for url in urls: 
        #     print(url,'=----------------------urlurl')
        #     yield scrapy.Request(url = url, callback = self.parse) 

    def start_requests(self): 
        print(self.url,'---------------------searched')
        # enter the URL here 
        yield scrapy.Request(url = self.url, callback=self.parse, dont_filter=True)
        # u = "https://www.bing.com/search?q=" + str(searched)
        # # search_req = request.session.get('searched_value')
        # urls =  [u,]
        # print(urls,'-----------------urls') 
        # for url in urls: 
        #     print(url,'=----------------------urlurl')
        #     yield scrapy.Request(url = url, callback = self.parse) 

     # Parse function 
    def parse(self, response): 
        print(response,'------------------------response')
        # Extra feature to get title 
        title = response.css('title::text').extract_first()  
        # print(title,'------------------------title')
        # Get anchor tags 
        links = response.css('a::attr(href)').extract()      
        # print(links,'------------------------links')
        for link in links: 
            item = SearchedItem()
            item['keyword'] = "bcci"
            item["link"] = link
            
            print(self.key,link,'--------------------------link')
            SearchPipeline()
            SearchedLinks.objects.create(keyword = self.key,link = link)
            yield item
        # print("done-----------------------doneee")



class SearchData(APIView):
    def get(self, request):
        context = {}
        searched = request.GET.get('q')
        request.session['searched_value'] = searched
        crawler_settings = get_project_settings()
        crawler = CrawlerProcess(crawler_settings)
        print(searched,">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        crawler.crawl(ExtractUrls, key=searched)
        crawler.start()

        data = SearchedLinks.objects.filter(keyword = searched)
        if data:
            serializer = SearchedLinksSerializer(data, many=True)
            context['success'] = True
            context['data'] = serializer.data

        else:
            context['success'] = True
            context['message'] = "No data found."
        return Response(context)

   
# crawler_settings = get_project_settings()
# crawler = CrawlerProcess(crawler_settings)
# crawler.crawl(ExtractUrls, key=searched)
# crawler.start()
