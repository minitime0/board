from django.db import models

#   seconapp_armyshop
class ArmyShop(models.Model):
  id = models.IntegerField(primary_key=True)
  year = models.IntegerField()
  month = models.IntegerField()
  type = models.CharField(max_length=10)
  name = models.CharField(max_length=30)

  class Meta:  # 내부 클래스 inner
    db_table = 'army_shop'
    managed = False



class Course(models.Model):
  name = models.CharField(max_length=255)
  cnt = models.IntegerField()