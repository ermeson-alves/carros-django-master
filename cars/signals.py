from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver
from cars.models import Car, CarInventory
from django.db.models import Sum


def car_inventory_update():
    cars_count = Car.objects.all().count()
    cars_value = Car.objects.aggregate(
        total_value=Sum('value')
    )['total_value']
    CarInventory.objects.create( # criando os registros
        cars_count=cars_count,
        cars_value=cars_value
    )   


# @receiver(pre_save, sender=Car)
# def car_pre_save(sender, instance, **kwargs):
#     """ Processamento antes de salvar dados.

#     Args:
#         sender: Model, Objeto, Quem envia os dados...
#         instance: "Dados" do objeto novo a serem armazenados.
#         ao realizar um print, obtem o mesmo retorno da função 
#         __str__ do model.
#     """
#     if not instance.bio:
#         instance.bio = 'Bio gerada automaticamente!'


@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    """
    Quando um carro novo é salvo, este signal calcula o cars_count e o 
    cars_value.
    """
    car_inventory_update()
    

# @receiver(pre_delete, sender=Car)
# def car_pre_delete(sender, instance, **kwargs):
#     print('-'*30, '\npre-delete signal\n', '-'*30)


@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    car_inventory_update()


