from django.urls import path
from .views import signin, signup, signout, ajax_reg, profile


urlpatterns = [
    path('signin', signin),
    path('signup', signup),
    path('signout', signout),
    path('ajax_reg', ajax_reg),
    path('profile', profile)
]