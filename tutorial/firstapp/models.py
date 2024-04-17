from django.db import models

class Curriculum(models.Model):
  name = models.CharField(max_length=255)

class Emp(models.Model):
  # 자동 증가(숫자), 기본키
  id = models.AutoField(primary_key=True)

class Member(models.Model):
  email = models.CharField(max_length=255)
  pwd = models.CharField(max_length=255)
  name = models.CharField(max_length=255)