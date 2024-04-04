import scrapy
from myproject.items import UserItem

class UserSpider(scrapy.Spider):
    name = "userspider"
    start_urls = ['https://stackoverflow.com/users']

    custom_settings = {
        'ITEM_PIPELINES': {
            'myproject.pipelines.SaveToJsonPipeline': 300,
        }
    }

    def parse(self, response):
        # Извлекаем информацию о каждом пользователе
        for user_info in response.css('.grid--item.user-info'):
            user = UserItem()
            user['username'] = user_info.css('.user-details a::text').get()
            user['location'] = user_info.css('.user-location::text').get()
            user['reputation'] = user_info.css('.reputation-score::text').get().strip()
            # user['tags'] = user_info.css('.user-tags a::text').getall()
            yield user


# scrapy crawl userspider
# source .\.venv\Scripts\activate     # для Windows