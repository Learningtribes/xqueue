from django.conf.urls import include, url

urlpatterns = [
    url(r'^xqueue/', include('lt_queue.urls')),
]
