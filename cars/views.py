from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from cars.models import Car # é necessário ter acesso ao arquivo de models, pois as views realizam as querys baseadas nele
from cars.forms import CarForm, CarModelForm
from django.views import View
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
def cars_views(request):
    cars = Car.objects.all()
    search = request.GET.get('search')
    if search:
        # SELECT model FROM Car WHERE model contém search...
        # field__icontains ignora upercase e lowercase, em relação ao field__contains
        cars = cars.filter(model__icontains=search)
        # .order_by(), permite ordenar as intancias que representam a relação do bd 
        # baseado no valor entre os ()                                               
        cars = cars.order_by('-model') 
                                                    
    return render(request, 
        'templatedoadm.html', # não precisa dizer que está dentro da pasta ./templates (o django identifica isso)
        context={'cars': cars}
    )



class CarsView(View):

    def get(self, request):
        cars = Car.objects.all()
        search = request.GET.get('search')
        if search:
            cars = cars.filter(model__icontains=search)                                                 
            cars = cars.order_by('-model')    
        return render(request, 'templatedoadm.html', context={'cars': cars})



class CarsListView(ListView):
    model = Car
    template_name = 'templatedoadm.html' # Para a listagem de carros
    context_object_name = 'cars'
    
    # função adequada para realizar filtro's:
    def get_queryset(self):
        # A get_queryet da classe superior retorna todos os registros da tabela
        # por padrão.
        cars = super().get_queryset().order_by('model')
        # Captura o valor do parâmetro search da requisião:
        search = self.request.GET.get('search')
        if search:
            cars = cars.filter(model__icontains=search)
        return cars



def new_car_view(request):
    # request.POST pega todos os dados da requisição
    if request.method == 'POST':
        # new_car_form = CarForm(request.POST, request.FILES)
        # Forma mais dificil:
                # if new_car_form.is_valid():
                #     new_car_form.save()
                #     return redirect('cars_list')
        # O campo files é por conta de dados como imagens...
        new_car_form = CarModelForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list')
        
    else:
        # new_car_form = CarForm()
        new_car_form = CarModelForm()
        # render serve para renderizar um arquivo html (necessário contexto)
        # o contexto ajuda na transição de dados para o html;
    return render(request, 'newcaradm.html', {'new_car_form': new_car_form})


class NewCarView(View):

    def get(self, request):
        new_car_form = CarModelForm()
        return render(request, 'newcaradm.html', {'new_car_form': new_car_form})

    def post(self, request):
        new_car_form = CarModelForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list')
        return render(request, 'newcaradm.html', {'new_car_form': new_car_form})
    

# Necessário indicar qual método da classe vai ser decorado (dispatch nesse caso)
# Obs: saber qual método da class based views decorar. 
@method_decorator(login_required(login_url='login'), name='dispatch')
class NewCreateCarView(CreateView):
    # Isso passa para o template a variavel com nome "form"
    model = Car
    form_class = CarModelForm
    template_name = 'newcaradm.html'
    success_url = '/cars'



class CarDetailView(DetailView):
    model = Car
    template_name = 'cardetailadm.html'



@method_decorator(login_required(login_url='login'), name='dispatch')
class CarUpdateView(UpdateView):
    model = Car
    form_class = CarModelForm
    template_name = 'car_update_adm.html'

    # aplicar o redirecionamento para a view detail do carro atual
    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs={'pk': self.object.pk})



@method_decorator(login_required(login_url='login'), name='dispatch')
class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_deleteadm.html'
    # MUDAR ISSO:
    success_url = '/cars'