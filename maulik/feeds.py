from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from blog.models import Blog
from django.urls import reverse


class BlogFeed(Feed):
    title = "My blog"
    link = ""
    description = "New posts of my blog."

    def items(self):
        return Blog.objects.filter(id=1)

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.content, 30)
