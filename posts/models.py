from django.db import models
from django.utils import timezone

from clients.models import Client
# Create your models here.


class Posts(models.Model):
    title = models.CharField(
        verbose_name="название поста",
        max_length=200,



    )
    description = models.TextField(
        verbose_name="описание поста",
        max_length=5000,
    )
    date_publication=models.DateTimeField(
        verbose_name="дата публикации",
        default=timezone.now,
    )
    user=models.ForeignKey(
        to=Client,
        on_delete=models.CASCADE,
        default="Unknown author",
        related_name="posts",
        verbose_name="client_name",

    )

    likes=models.PositiveBigIntegerField(
        verbose_name="лайки",
        default=0,

    )
    dislikes=models.PositiveBigIntegerField(
        verbose_name="дизлайки",
        default=0,

    )

    class Meta:
        ordering=("id",)
        verbose_name="статья"
        verbose_name_plural="статьи"

    def __str__(self):
        return f"{self.title} | {self.date_publication}"
class Images(models.Model):
    image=models.ImageField(
        verbose_name="изображение",
        upload_to="images/posts/",
    )
    post=models.ForeignKey(
        to=Posts,
        on_delete=models.CASCADE,
        related_name="post_images",
        verbose_name="статья",
    )
    class Meta:
        ordering=("id",)
        verbose_name="изоображение"
        verbose_name_plural="изоображения"

    def __str__(self):
        return f"{self.image} | {self.pk}"
class Categories(models.Model):
    title=models.CharField(
        verbose_name="название категории",
        max_length=200,
    )
    post=models.ManyToManyField(
        to=Posts,
        related_name="categories",
        verbose_name="статьи",
    )
    class Meta:
        ordering=("id",)
        verbose_name="категория"
        verbose_name_plural="категории"
    def __str__(self):
        return f"{self.title} | {self.pk}"

