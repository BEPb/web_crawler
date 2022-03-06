![Profile views](https://gpvc.arturio.dev/BEPb) 
![GitHub top language](https://img.shields.io/github/languages/top/BEPb/web_crawler) 
![GitHub language count](https://img.shields.io/github/languages/count/BEPb/web_crawler)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/BEPb/web_crawler)
![GitHub repo size](https://img.shields.io/github/repo-size/BEPb/web_crawler) 
![GitHub](https://img.shields.io/github/license/BEPb/web_crawler) 
![GitHub last commit](https://img.shields.io/github/last-commit/BEPb/web_crawler)
![GitHub User's stars](https://img.shields.io/github/stars/BEPb?style=social)
<p align="left">
<img src="https://visitor-badge.laobi.icu/badge?page_id=BEPb.github-contributions" alt="visitors"/>
</p>


![](./example/i_l_p.png)


Read this in other languages: [Russian](README.ru.md), [हिन्दी](README.hindi.md), [中國人](README.chinese.md)


<div align="center">


<img src="img/web_crawler_header.jpg" alt="Bot logo" width="800" height="156.5">

## Fast and simple crawler

</div>

## How it works?

Вit's very simple: your bot massively signs your account in response, people follow you.

## The order of preparation and work with the bot

1. Clone the repository or download the archive from github or using the following commands on the command line
   ```commandline
   $ cmd
   $ git clone https://github.com/BEPb/github_bot
   $ cd github_bot
   ```
2. Create a Python virtual environment.
3. Install all necessary packages for our code to work using the following command:

    ```
    pip install -r requirements.txt
    ```


4. create a project called nameproject
```command line
scrapy startproject nameproject
```

5. after which you will have a folder with the name of this project and in it the minimum necessary files and dependencies
```command line

    scrapy.cfg #deploy configuration file
    nameproject/ # project's Python module, you'll import your code from here
        __init__.py
        items.py # project items definition file
        middlewares.py # project middlewares file
        pipelines.py # project pipelines file
        settings.py # project settings file
        spiders/ # a directory where you'll later put your spiders
            __init__.py
```
6. go to our project folder
```command line
cd nameproject
```

7. create a quotes_spider.py file in the spiders/ folder and write in it who and how we cheat
8. launch our crawler
```command line
scrapy crawl quotes
```
9. as a result of the execution, two new files were created: quotes-1.html and quotes-2.html with content for
  the corresponding URLs, as our parse method specifies.
10. use shell selectors
```command line
scrapy shell 'https://quotes.toscrape.com/page/1/'
```
11. view all 'title' objects using css. The result of executing response.css('title') is similar to
  list object named SelectorList which is a list of Selector objects that wrap
  XML/HTML elements and allow you to perform additional queries to refine the selection or retrieve data.
```command line
response.css('title')
```
12. and in order to view the list, specify the getall () method
```command line
response.css('title::text').getall()
```
13. the same can be done with xpath
```command line
response.xpath('//title/text()').get()
```
14. and now take div tags with class quote
```command line
response.css("div.quote")
```

15. take only the first element in the list
```command line
response.css("div.quote")[0]
```

16. in order to get the class in the tag, use the following command:
```command line
quote.css("span.text::text").get()
quote.css("small.author::text").get()
```
17. and this is how we will display the complete list of the class of the div tag
```command line
response.css("div.quote").css("div.tags a.tag::text").getall()
```
18. this is how we save the result in json format, where the `-O` command line switch overwrites any existing
  file;
```command line
scrapy crawl quotes -O quotes.json
```
19. and this is how we save the result in csv format
```command line
scrapy crawl quotes -O quotes.csv
```
20. The following command writes line by line using the .jl format
```command line
scrapy crawl quotes -o quotes.jl
```
<img src="img/spyder.jpg" alt="Bot logo" width="800" height="356.5">