from django.conf import settings
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Post(models.Model):
    CATEGORY_CHOICES = [
        ('JPN', '和食'),
        ('LOCAL', '郷土料理'),
        ('SUSHI', '寿司'),
        ('RAMEN', 'ラーメン類'),
        ('CURRY', 'カレー'),
        ('FA', 'ファミレス・ファストフード'),
        ('MEAT', '焼肉・ステーキ等の肉関連'),
        ('BAR', '居酒屋・バー'),
        ('CHN', '中華'),
        ('WES', '洋食'),
        ('ITA', 'イタリアン'),
        ('FRA', 'フレンチ'),
        ('ASIA', 'アジア・エスニック'),
        ('CAFE', 'カフェ'),
        ('SWEETS', 'スイーツ'),
        ('OTHER', 'その他'),
    ]
    editable = models.BooleanField(default=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    img =models.ImageField("Uploaded image", null=True)
    name = models.CharField(max_length=50)
    area = models.CharField(max_length=50)
    address = models.CharField(max_length=50, blank=True)
    dish = models.CharField(max_length=100, blank=True)
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES
    )
    expense = models.IntegerField(blank=True)
    note = models.TextField(blank=True)
    rating = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )

    def __str__(self):
        return self.name
