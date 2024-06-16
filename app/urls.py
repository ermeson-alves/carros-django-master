from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cars.views import cars_views, new_car_view, CarsView, NewCarView, \
    CarsListView, NewCreateCarView, CarDetailView, CarUpdateView, CarDeleteView
from accounts.views import register_view, login_view, logout_view


urlpatterns = [
    path('admin/', admin.site.urls), # responsável pela visão de administrador
    path('cars/', CarsListView.as_view(), name='cars_list'),
    path('new_car/', NewCreateCarView.as_view(), name='new_car'), # aula de forms 
    path('register/', register_view, name='register'), # aula de autenticação
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    # A sintaxe abaixo indica que cada carro tem uma rota diferente sendo
    # /car seguido de um valor inteiro que foi denominado pk e isso faz com que
    # o django automaticamente passe a chave primária do objeto em questão nessa parte da rota.
    path('car/<int:pk>/', CarDetailView.as_view(), name='car_detail'),
    # É necessário passar ainda essa parte anterior da rota para que a view tenha informações
    # sobre qual carro editar.
    path('car/<int:pk>/update', CarUpdateView.as_view(), name='car_update'),
    path('car/<int:pk>/delete', CarDeleteView.as_view(), name='car_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        