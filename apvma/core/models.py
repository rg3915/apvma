from django.contrib.auth.models import User
from django.db import models

from apvma.accounts.validators import validate_cpf


class Resident(models.Model):
    POSTS = (
        ('CL', 'Coronel'),
        ('TCL', 'Tenente-Coronel'),
        ('MJ', 'Major'),
        ('CP', 'Capitão'),
        ('1T', '1º Tenente'),
        ('2T', '2º Tenente')
    )

    post = models.CharField('posto', max_length=4, choices=POSTS)
    full_name = models.CharField('nome completo', max_length=100)
    war_name = models.CharField('nome de guerra', max_length=20)
    cpf = models.CharField('CPF', max_length=11, validators=[validate_cpf])
    email = models.EmailField('email intraer')
    apartment = models.OneToOneField(User, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name = 'morador'
        verbose_name_plural = 'moradores'

    def __str__(self):
        return '{} {}'.format(self.post, self.war_name)


# class Apartment not in use. Using User for apartment.
# class Apartment(models.Model):
#     BLOCKS = (
#         ('RN', 'Rio Negro'),
#         ('RS', 'Rio Solimões'),
#         ('RA', 'Rio Amazonas'),
#         ('RJ', 'Rio Japurá')
#     )
#
#     NUMBERS = (
#         ('101', '101'), ('102', '102'), ('103', '103'), ('104', '104'),
#         ('201', '201'), ('202', '202'), ('203', '203'), ('204', '204'),
#         ('301', '301'), ('302', '302'), ('303', '303'), ('304', '304'),
#         ('401', '401'), ('402', '402'), ('403', '403'), ('404', '404'),
#         ('501', '501'), ('502', '502'), ('503', '503'), ('504', '504'),
#         ('601', '601'), ('602', '602'), ('603', '603'), ('604', '604'),
#     )
#
#     block = models.CharField('bloco', max_length=2, choices=BLOCKS)
#     number = models.CharField('número', max_length=3, choices=NUMBERS)
#
#     class Meta:
#         unique_together = ('block', 'number')
#         verbose_name = 'apartamento'
#         verbose_name_plural = 'apartamentos'
#
#     def __str__(self):
#         return '{}-{}'.format(self.block, self.number)