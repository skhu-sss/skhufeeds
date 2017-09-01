from crawlers.models import NewsFeed,Source
from settings.models import Subscribed
from django.contrib.auth.models import User

def query_news(user):
    newsfeeds = ""
    sub_list = Subscribed.objects.filter(User=user)
    last_pull = user.profile.last_pull
    for sub in sub_list:
        feeds = NewsFeed.objects.filter(source=sub.source, time__gte=last_pull)
        if(len(feeds)==0):
            feeds = NewsFeed.objects.filter(source=sub.source).order_by('-time')[:5]
        for feed in feeds:
            newsfeeds = newsfeeds + "{}\n{}\n----------\n".format(feed.title, feed.url)

    return newsfeeds