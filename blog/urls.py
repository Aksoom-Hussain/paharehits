from django.conf.urls import urls
from django.views.generic import ListView
from blog.models import Post

urlpatterns =['',
    url(r'^',ListView.as_view(
        queryset = Post.objects.all().order_by(-date)[:10],
        template_name = "blog.html"
    )),
    
]