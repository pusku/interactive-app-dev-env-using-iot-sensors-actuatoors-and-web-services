from django.db import models
from datetime import datetime
from django.utils import timezone


class Actuator(models.Model):
    topic = models.CharField(max_length=100, null=True)
    value = models.CharField(max_length=100, null=True)
    time = models.DateTimeField(auto_now_add=True, null=True)
    name = models.CharField(max_length=60, null=True)

    class Meta:
        verbose_name_plural = 'Actuators'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.time = timezone.now()
        return super(Actuator, self).save(*args, **kwargs)


class Sensor(models.Model):
    topic = models.CharField(max_length=100, null=True)
    value = models.CharField(max_length=100, null=True)
    time = models.DateTimeField(default=datetime.now, null=True)
    name = models.CharField(max_length=60, null=True)

    class Meta:
        verbose_name_plural = 'Sensors'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.time = timezone.now()
        return super(Sensor, self).save(*args, **kwargs)


class ServiceRegistry(models.Model):
    name = models.CharField(max_length=100, unique=True)
    service_type = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Service Registry'

    def __str__(self):
        return self.name


class MailBox(models.Model):
    name = models.CharField(max_length=100, null=True)
    api = models.FileField(upload_to="mailbox", null=True, blank=True)

    class Meta:
        verbose_name_plural = 'MailBox'

    def __str__(self):
        return self.name


class API(models.Model):
    name = models.CharField(max_length=100, null=True)
    api = models.CharField(max_length=100, null=True)
    fields = models.TextField(max_length=500, null=True)
    connection = models.TextField(max_length=500, null=True)

    class Meta:
        verbose_name_plural = 'API'

    def __str__(self):
        return self.name


class Interactive(models.Model):
    name = models.CharField(max_length=100, null=True)
    fields = models.TextField(max_length=500, null=True)

    class Meta:
        verbose_name_plural = 'Interactive'

    def __str__(self):
        return self.name
