import os, django, random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.implement.models import UrlModel
from core.common.utils import crawling, get_short_url



def main():
    urls = [
        'https://www.elegantthemes.com/blog/marketing/types-of-blogs',
        'https://neilpatel.com/how-to-start-a-blog/',
        'https://djbook.ru/examples/77/',
        'https://itnext.io/simple-multi-tenancy-with-django-running-on-openshift-b5859a94dd52',
        'https://medium.com/@muiruri.samuel/implementing-a-chatbot-in-django-af004f46ad8',
        'https://scotch.io/tutorials/django-authentication-with-facebook-instagram-and-linkedin',
        'https://www.techiediaries.com/python-django-ajax/',
        'https://www.techiediaries.com/django-rest-image-file-upload-tutorial/',
        'https://books.agiliq.com/projects/django-api-polls-tutorial/en/latest/',
        'https://pythondigest.ru/view/2223/',
        'https://expertvagabond.com/travel-blogs/',
        'https://www.travelblog.org/North-America/Canada/Manitoba/Winnipeg/blog-1034661.html',
        'https://www.themeditationblog.com/be-friends-with-your-wandering-mind/',
        'https://tinybuddha.com/blog/find-your-rat-people-the-best-advice-for-people-pleasers/',
        'https://addicted2success.com/motivation/a-step-by-step-process-that-will-help-you-make-the-impossible-possible/',
        'https://www.dumblittleman.com/interesting-gardening-facts/',
        'http://www.insidehighered.com/news/2019/05/23/rejecting-requirement-publish-dissertations-online',
        'http://www.insideworldfootball.com/2019/05/23/ahmad-fifa-investigation-financial-corruption-say-reports/',
        'https://www.geeksforgeeks.org/combining-iot-and-machine-learning-makes-our-future-smarter/',
        'https://www.linuxfoundation.org/blog/2019/04/lf-forms-laminas-project/',
        'https://dzone.com/articles/streaming-machine-learning-pipeline-for-sentiment-1',
        'https://www.hackerearth.com/blog/developers/reactjs-vs-vuejs/',
        'https://developers.googleblog.com/2019/05/increasing-diversity-cloud-study-jam.html',
        'https://www.w3schools.com/howto/howto_css_dropdown.asp'
    ]

    for url in urls:
        UrlModel.objects.create(
            full_url = url,
            short_url = get_short_url(url),
            text = crawling(url)
        )

if __name__ == '__main__':
    main()
    print('Finish All.')