from django.conf.urls import include, url

urlpatterns = [
    url(r'^', 'calculator.views.doOperation'),
]
