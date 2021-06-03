from django.urls import path, include
from rest_framework.authtoken import views
from .views import home

urlpatterns = [
    path('', home, name='api.home'),
    # go and ask the api inside the foledr category urls
    path('category/', include('api.category.urls')),
    path('product/', include('api.product.urls')),
    path('user/', include('api.user.urls')),
    path('order/', include('api.order.urls')),
    path('payment/', include('api.payment.urls')),
    # The line is added from Django rest after creating the API django app
    path('api-token-auth/', views.obtain_auth_token,
         name='api_token_auth')  # <-- And here
]
