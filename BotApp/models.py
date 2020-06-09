from django.db import models


class Intent(models.Model):
    name = models.CharField(max_length=200, null=False)
    answer = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class IntentPointer(models.Model):
    pointer = models.CharField(max_length=200)
    intent = models.ForeignKey(Intent, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.pointer
