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


Read this in other languages: [Russian](README.ru.md), [English](README.md), [中國人](README.chinese.md)


<div align="center">


<img src="img/web_crawler_header.jpg" alt="Bot logo" width="800" height="156.5">

## तेज और सरल क्रॉलर
</div>

## यह काम किस प्रकार करता है?
यह बहुत आसान है: आपका बॉट बड़े पैमाने पर आपके खाते की सदस्यता लेता है, लोग आपकी सदस्यता लेते हैं।
## बॉट के साथ तैयारी और काम करने का क्रम
. रिपॉजिटरी को क्लोन करें या जिथब से आर्काइव डाउनलोड करें या कमांड लाइन पर निम्न कमांड का उपयोग करें
   ```commandline
   $ cmd
   $ git clone https://github.com/BEPb/github_bot
   $ cd github_bot
   ```

2. एक पायथन वर्चुअल वातावरण बनाएं।
3. निम्नलिखित कमांड का उपयोग करके हमारे कोड के काम करने के लिए सभी आवश्यक पैकेज स्थापित करें:
    ```
    pip install -r requirements.txt
    ```

4. nameproject . नामक एक प्रोजेक्ट बनाएं
```commandline
scrapy startproject nameproject
```

5. जिसके बाद आपके पास इस प्रोजेक्ट के नाम के साथ एक फोल्डर होगा और उसमें न्यूनतम आवश्यक फाइलें और निर्भरताएँ होंगी
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
6. हमारे प्रोजेक्ट फोल्डर में जाएं
```commandline
cd nameproject
```

7. स्पाइडर/फोल्डर में एक Quotes_spider.py फाइल बनाएं और उसमें लिखें कि हम किसे और कैसे धोखा देते हैं
8. हमारा क्रॉलर लॉन्च करें
```commandline
scrapy crawl quotes
```
9. निष्पादन के परिणामस्वरूप, दो नई फाइलें बनाई गईं: उद्धरण-1.एचटीएमएल और उद्धरण-2.एचटीएमएल के लिए सामग्री के साथ
  संबंधित URL, जैसा कि हमारी पार्स विधि निर्दिष्ट करती है।
10. शेल चयनकर्ताओं का उपयोग करें
```commandline
scrapy shell 'https://quotes.toscrape.com/page/1/'
```
11. सीएसएस का उपयोग करके सभी 'शीर्षक' ऑब्जेक्ट देखें। प्रतिक्रिया निष्पादित करने का परिणाम। सीएसएस ('शीर्षक') समान है
  चयनकर्ता सूची नामक सूची वस्तु जो चयनकर्ता वस्तुओं की एक सूची है जो लपेटती है
  एक्सएमएल/एचटीएमएल तत्व और आपको चयन को परिष्कृत करने या डेटा पुनर्प्राप्त करने के लिए अतिरिक्त क्वेरी करने की अनुमति देता है। 
```commandline
response.css('title')
```
12. और सूची देखने के लिए, getall () विधि निर्दिष्ट करें
```commandline
response.css('title::text').getall()
```
13. वही xpath . के साथ किया जा सकता है
```commandline
response.xpath('//title/text()').get()
```
14. और अब क्लास कोट के साथ डिव टैग लें
```commandline
response.css("div.quote")
```

15. सूची में केवल पहला तत्व लें
```commandline
response.css("div.quote")[0]
```

16. टैग में वर्ग प्राप्त करने के लिए, निम्न आदेश का उपयोग करें:
```commandline
quote.css("span.text::text").get()
quote.css("small.author::text").get()
```
17. और इस प्रकार हम div टैग के वर्ग की पूरी सूची प्रदर्शित करेंगे
```commandline
response.css("div.quote").css("div.tags a.tag::text").getall()
```
18. इस प्रकार हम परिणाम को जोंस प्रारूप में सहेजते हैं, जहां `-O` कमांड लाइन स्विच किसी भी मौजूदा . को अधिलेखित कर देता है
  फ़ाइल;
```commandline
scrapy crawl quotes -O quotes.json
```
19. और इस तरह हम परिणाम को csv प्रारूप में सहेजते हैं
```commandline
scrapy crawl quotes -O quotes.csv
```
20. निम्न कमांड .jl फॉर्मेट का प्रयोग करते हुए लाइन दर लाइन लिखता है
```commandline
scrapy crawl quotes -o quotes.jl
```
<img src="img/spyder.jpg" alt="Bot logo" width="800" height="356.5">