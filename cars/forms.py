# Junção dos forms dessa app com ajuda do django (validação, etc)
from django import forms
from cars.models import Brand, Car

class CarForm(forms.Form):
    model = forms.CharField(max_length=200)
    # Busca-se todas as marcas do banco de dados e fornece uma 
    # lista com esse valores para se escolher...
    brand = forms.ModelChoiceField(Brand.objects.all())
    factory_year = forms.IntegerField()
    model_year = forms.IntegerField()
    plate = forms.CharField(max_length=10)
    value = forms.FloatField()
    photo = forms.ImageField()


    def save(self):
        car = Car(
            model = self.cleaned_data['model'],
            brand = self.cleaned_data['brand'],
            factory_year = self.cleaned_data['factory_year'],
            model_year = self.cleaned_data['model_year'],
            plate = self.cleaned_data['plate'],
            value = self.cleaned_data['value'],
            photo = self.cleaned_data['photo'],
        )

        car.save()
        return car


class CarModelForm(forms.ModelForm):
    
    class Meta():
        model = Car
        fields = '__all__' # pega todos os campos da tabela Car

    # Abaixo é criada uma validação para o campo "value" da tabela Car
    def clean_value(self):
        value = self.cleaned_data.get('value') # dados limpos
        if value < 20000:
            self.add_error('value', 'O valor minimo do carro é R$ 20.000,00!')
        return value

    # Abaixo é criada uma validação para o campo "factory_year" da tabela Car
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 1990:
            self.add_error('factory_year', 'Carros fabricados antes de 1990 não são permitidos!')
        return factory_year