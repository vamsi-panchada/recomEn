from django.db import models

# Create your models here.

class transactions(models.Model):
    transactionId
    userId
    merchantId
    amount
class merchantDetails(models.Model):
    merchantId
    merchantName
    catogary
    location

class offers(models.Model):
    offerId
    merchantId
    coupenCode
    description

class userDetails(models.Model):
    userId=models.
    userName
    userAge
    userIncome
    userHometown

class Disease(models.Model):
    disname = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.disname


class Record(models.Model):
    aadharp = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='patientaadhar', to_field='aadhar_no')
    aadhard = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='docpatient')
    disid = models.ForeignKey(Disease, on_delete=models.CASCADE, related_name='disease')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.created)


class Symptom(models.Model):
    symptom = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.symptom


class Relation(models.Model):
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE, related_name='Disease')
    symptom = models.ForeignKey(Symptom, on_delete=models.CASCADE, related_name='Symptom')

    def __str__(self):
        return str(self.symptom) + " : "+str(self.disease)



