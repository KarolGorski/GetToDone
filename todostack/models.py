from django.db import models
from django.utils import timezone
from colorfield.fields import ColorField


class Category(models.Model):
    name = models.CharField(max_length=100)
    color = ColorField(default='#FF0000')

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Difficulty(models.Model):
    name = models.CharField(max_length=100)
    current_multiplier = models.FloatField()
    color = ColorField(default='#FF0000')

    class Meta:
        verbose_name = "Difficulty"
        verbose_name_plural = "Difficulties"

    def __str__(self):
        return self.name


class Priority(models.Model):
    name = models.CharField(max_length=100)
    priority_num = models.IntegerField()
    color = ColorField(default='#FF0000')

    class Meta:
        verbose_name = "Priority"
        verbose_name_plural = "Priorities"

    def __str__(self):
        return self.name


class ToDo(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(blank=True)
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    category = models.ForeignKey(Category, default="general", on_delete=models.PROTECT)
    difficulty = models.ForeignKey(Difficulty, default=3, on_delete=models.PROTECT)
    priority = models.ForeignKey(Priority, default=3, on_delete=models.PROTECT)
    estimatedTime = models.CharField(max_length=10)

    class Meta:
        ordering = ["created"]

    def __str__(self):
        return self.title






# difficulty = (
#     'No Problem!',
#     'Easy',
#     'Medium',
#     'Hard',
#     'Very hard',
#     'Is it even possible?'
# )
# importance = {
#     'Daily habit'
#     'It can wait',
#     'Near future',
#     'Urgent',
#     'TODAY!',
#     'BLOCKER'
# }



