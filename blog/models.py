from django.db import models


class Employee(models.Model):
    img = models.ImageField(upload_to='employee/', verbose_name="изображение")
    name = models.CharField(max_length=25)
    facebook = models.URLField()
    instagram = models.URLField()
    linkedin = models.URLField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'сотрудника'
        verbose_name_plural = 'кол.работников'


class FeedBack(models.Model):
    img = models.ImageField(upload_to='FeedBack/')
    text = models.CharField(max_length=50)

    def __str__(self):
        return self.img

    class Meta:
        ordering = ['text']
        verbose_name = 'отзыв'
        verbose_name_plural = 'кол отзывов'


class Contact(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'сотрудников'
        verbose_name_plural = 'список сотрудников'


class Spam(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email

    class Meta:
        ordering = ['email']
        verbose_name = 'обратная связь'
        verbose_name_plural = 'поддержка:'


