from django.contrib import admin
from django.urls import path , re_path
# add for slice01 
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import login , logout
from karajna.core import views as core_views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ar/', core_views.home, name='home'),
    path('ar/my-account/login/', auth_views.login, {'template_name': 'login.html'}, name='login'),
    path('ar/my-account/logout/', auth_views.logout, {'next_page': 'login'}, name='logout'),
    path('ar/my-account/signup/', core_views.signup, name='signup'),
    path('account_activation_sent/', core_views.account_activation_sent, name='account_activation_sent'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',core_views.activate, name='activate'),

    path('password_reset/', auth_views.password_reset, name='password_reset'),
    path('password_reset/done/', auth_views.password_reset_done, name='password_reset_done'),
    re_path('reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', 
          auth_views.password_reset_confirm,name='password_reset_confirm'),
    path('reset/done/', auth_views.password_reset_complete, name='password_reset_complete'),

    path('ar/my-account/bef-sell-car/', core_views.before_sell, name='before_sell'),
    path('ar/my-account/sell-car/', core_views.CarCreateView.as_view(), name='car_add'),

    path('ar/my-account/delete-car/<int:pk>', core_views.CarDelete.as_view(), name='car_delete'),
    path('<int:pk>/', core_views.CarUpdateView.as_view(), name='car_change'),
    path('ajax/load-versions/', core_views.load_versions, name='ajax_load_versions'),
    #path('', core_views.CarListView.as_view(), name='car_changelist'),
    path('ar/my-account/my-cars', core_views.carlist, name='carlist'),
    path('ar/my-account/show-car/<int:pk>/', core_views.cardata, name='cardata'),
    #path('ar/my-account/del-car/<int:pk>', core_views.car_delete, name='car_delete'),





]# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

