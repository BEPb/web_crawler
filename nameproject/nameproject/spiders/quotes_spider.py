import scrapy


class QuotesSpider(scrapy.Spider):
    '''идентифицирует Паука. Оно должно быть уникальным в пределах проекта, то есть вы не можете задать одно и то же
    имя для разных Пауков. '''
    name = "quotes"


    '''должен возвращать итерацию Запросов (вы можете вернуть список запросов или написать функцию-генератор), 
    с которых Паук начнет сканировать. Последующие запросы будут генерироваться последовательно из этих 
    первоначальных запросов.  '''
    # def start_requests(self):
    #     urls = [
    #         'https://quotes.toscrape.com/page/1/',
    #         'https://quotes.toscrape.com/page/2/',
    #     ]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)


    '''метод, который будет вызываться для обработки ответа, загруженного для каждого из сделанных запросов. 
    Параметр ответа является экземпляром TextResponse, который содержит содержимое страницы и имеет дополнительные 
    полезные методы для его обработки. '''
    # def parse(self, response):
    #     page = response.url.split("/")[-2]
    #     filename = f'quotes-{page}.html'
    #     with open(filename, 'wb') as f:
    #         f.write(response.body)
    #     self.log(f'Saved file {filename}')



    start_urls = [
        'https://quotes.toscrape.com/page/1/',
        'https://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }