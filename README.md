### Быстрый и простой краулер
* устанавливаем зависомости

* создаем проект с названием nameproject
```commandline
scrapy startproject nameproject
```

* после чего у вас появится папка с названием этого проекта а в ней минимально необходимые файлы и зависимости
```commandline

    scrapy.cfg            #  deploy configuration file
    nameproject/             # project's Python module, you'll import your code from here
        __init__.py
        items.py          # project items definition file
        middlewares.py    # project middlewares file
        pipelines.py      # project pipelines file
        settings.py       # project settings file
        spiders/          # a directory where you'll later put your spiders
            __init__.py
```
* переходим в папку нашего проекта
```commandline
cd nameproject
```

* создаем файл quotes_spider.py в папке spiders/ и прописываем в нем кого и как кравлим
* запускаем наш краулер
```commandline
scrapy crawl quotes
```
* в результате выполнения были созданы два новых файла: quotes-1.html и quotes-2.html с содержимым для 
  соответствующих URL-адресов, как parseуказывает наш метод. 
* используем селекторы оболочки 
```commandline
scrapy shell 'https://quotes.toscrape.com/page/1/'
```
* просмотрим все объекты 'title' используя css. Результатом выполнения response.css('title')является похожий на 
  список объект с именем SelectorList, который представляет собой список Selectorобъектов, которые обертывают 
  элементы XML/HTML и позволяют выполнять дополнительные запросы для детализации выборки или извлечения данных.  
```commandline
response.css('title')
```
* а для того что бы просмотреть список укзаываем метод getall()
```commandline
response.css('title::text').getall()
```
* тоже самое можно и сделать и при помощи xpath
```commandline
response.xpath('//title/text()').get()
```
* а теперь возьмем теги div с классом quote 
```commandline
response.css("div.quote")
```

* возьмем только первый элемент в списке
```commandline
response.css("div.quote")[0]
```

* для того что бы достать в теге класс используем следующую команду:
```commandline
quote.css("span.text::text").get()
quote.css("small.author::text").get()
```
* а вот так мы выведем полный список класса тега div
```commandline
response.css("div.quote").css("div.tags a.tag::text").getall()
```
* так мы сохраним результат в формат json, где Переключатель `-O` командной строки перезаписывает любой существующий 
  файл;
```commandline
scrapy crawl quotes -O quotes.json
```
* а так мы сохраним результат в формат csv
```commandline
scrapy crawl quotes -O quotes.csv
```
* следующая команда осуществляет запись по строчно за счет формата .jl
```commandline
scrapy crawl quotes -o quotes.jl
```
