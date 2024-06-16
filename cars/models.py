from django.db import models



class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name



class Car(models.Model):
    '''Essa classe representa a tabela Car dentro do
    banco de dados.
    
    Importante lembrar das restrições de integridade da
    cadeira de banco de dados.
    '''
    # campo que é a chave primária da tabela
    id = models.AutoField(primary_key=True)
    # campo para o modelo do carro
    model = models.CharField(max_length=200)
    # campo da marca:
    # ON DELETE PROTECT impede deletar a marca se 
    # existir Carros associados a ela. 
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand')
    # campo de ano de fabricação:
    # blank e null iguais a True implicam campos opicionais.max_length=200
    factory_year = models.IntegerField(blank=True, null=True)
    model_year = models.IntegerField(blank=True, null=True)
    plate = models.CharField(max_length=10, blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    # Isso implica armazenar a referencia para a imagem dentre de 
    # uma pasta de uploads em cars/
    photo = models.ImageField(upload_to='cars/', blank=True, null=True)
    # Descrição do carro:
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.model
    


class CarInventory(models.Model):
    cars_count = models.IntegerField()
    cars_value = models.FloatField()
    # DateTimeField armazena data e horário 
    # e auto_now_add implica que esse campo é atualizado
    # automaticamente:
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Ordenação decrescente dos registros via campo created_at."""
        ordering = ['-created_at']

    def __str__(self):
        # Isso exibe a soma dos campos dessas colunas:
        return f'{self.cars_count} - {self.cars_value}'

