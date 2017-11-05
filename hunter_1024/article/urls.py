from django.conf.urls import url
from .views import article_list
from .views import article_create
# from .views import ArticleDetailView
# from .views import ArticleCreateView

urlpatterns = [
    url(r'^list/(?P<block_id>\d+)', article_list),
    # url(r'^detail/(?P<block_id>\d+)', article_detail),
    url(r'^create/(?P<block_id>\d+)', article_create),
    # url(r'^detail_s/(?P<pk>\d+)$', ArticleDetailView.as_view()),
    # url(r'^create/(?P<block_id>\d+)', ArticleCreateView.as_view()),
    #url(r'^article/', include('article.urls')),
	#url(r'^static/(?P<path>.*)$',django.contrib.staticfiles.views.serve),
	#url(r'^$',views.index),
]
