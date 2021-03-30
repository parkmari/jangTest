from django.db import models
from django.urls import reverse
# Create your models here.
#글의 종류 (유머, 일상, 정보 등)
class Category(models.Model):
    name = models.CharField(max_length=50, help_text="블로그 글의 분류를 입력하시오")

    def __str__(self):
        return self.name

# 블로그 글, 제목, 작정, 대표이미지 정도
class Post(models.Model):
    title = models.CharField(max_length=200)
    title_image = models.ImageField(blank=True)
    content = models.TextField()
    createDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now_add=True)
    # 하나의 글을 여러자기의 분류에 해당 될 수 있다(정보, 유머), 하나의 분류의 여러 글 포함 가능
    category = models.ManyToManyField(Category, help_text="글의 분류를 설정하시오.")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post", args=[str(self.id)])

    def is_content_more45(self):
        return len(self.content) > 45

    def get_content_under45(self):
        return self.content[:45]