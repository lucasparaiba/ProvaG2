from django.db import models

class Eleicao(models.Model): #classe configurações
    h_entrada = models.TimeField(blank=True, null=True)
    h_saida = models.TimeField(blank=True, null=True)
    #funcionario = models.ForeignKey(Funcionario, null=True, blank=False)

    def __str__(self):
        return str(self.h_entrada) + " - " + str(self.h_saida)

class Eleitor(models.Model):
    nome = models.CharField(max_length=128)
    token = models. CharField(max_length=14)

    def __str__(self):
        return self.nome + self.token

class Candidatos(models.Model):
    nome = models.CharField(max_length=128)
    numero = models.CharField(max_length=10)

    def __str__(self):
        return self.nome + self.numero

class Vagas(models.Model):
    candidato = models.ForeignKey(Candidatos, related_name='candidatos', null=True, blank=False)
    cargo = models.CharField(max_length=128)

    def __str__(self):
        return self.candidato + self.cargo

class Votar(models.Model):
    TIPO_CHOICES = (
        ('sim', 'Sim'),
        ('nao', 'Não'),
    )
    eleitor = models.ForeignKey(Eleitor, null=True, blank=False)
    numeroCandidato = models.ForeignKey(Candidatos, null=True, blank=False)
    Votou = models.CharField(max_length=7, choices=TIPO_CHOICES, blank=False, null=False)
    votouemBranco = models.BooleanField("Consistência da frequência!?",default=False) #True: Consistente, False: Incosistente


    def __str__(self):
        return self.eleitor.nome + ": votou: " + self.votou
