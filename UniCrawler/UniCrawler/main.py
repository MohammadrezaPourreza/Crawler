from scrapy import cmdline

cmdline.execute("scrapy crawl courses -o courses.csv -t csv".split())
# cmdline.execute("scrapy crawl courses -o courses.json".split())