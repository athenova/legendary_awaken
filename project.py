from simple_blogger import CommonBlogger
#from simple_blogger.generators.OpenAIGenerator import OpenAITextGenerator
from simple_blogger.generators.YandexGenerator import YandexImageGenerator
from datetime import datetime
from datetime import timedelta
from simple_blogger.senders.TelegramSender import TelegramSender
from simple_blogger.senders.InstagramSender import InstagramSender


class Project(CommonBlogger):
    def _example_task_creator(self):
        return [
            {
                "name": "Name",
                "country": "Country",
            }
        ]

    def _get_category_folder(self, task):
        return f"{task['country']}"
                    
    def _get_topic_folder(self, task):
        return f"{task['name']}"

    def _system_prompt(self, task):
        return "Ты - блогер с 1000000 миллионном подписчиков"

    def _task_converter(self, idea):
        return { 
                    "name": idea['name'],
                    "country": idea['country'],
                    "topic_prompt": f"Расскажи интересный факт про '{idea['name']}' из '{idea['country']}', используй не более {self.topic_word_limit} слов, используй смайлики",
                    "topic_image": f"Нарисуй рисунок, вдохновлённый '{idea['name']}' из '{idea['country']}'",
                }

    def __init__(self, **kwargs):
        super().__init__(
            first_post_date=datetime(2025, 3, 9),
            #days_to_review=timedelta(2),
            days_between_posts=timedelta(7),
            image_generator=YandexImageGenerator(),
            #text_generator=OpenAITextGenerator(),
            reviewer=TelegramSender(),
            senders=[TelegramSender(channel_id=f"@lux_nexus"), InstagramSender(channel_token_name='LUX_NEXUS_TOKEN')],
            topic_word_limit=100,
            shuffle_tasks=False,
            **kwargs
        )