from django.db import models


# Сейчас этот класс не используется и основное название храниться в
# классе MangaInfo, но позже будет вынесено отдельно.
class MangaTitle(models.Model):
    """
    Класс для хранения основного и альтернативного названия манги.
    """
    pass


class MangaInfo(models.Model):
    """
    Клвсс хранящий основную информацию об конкретной манге.
    """
    title = models.CharField(max_length=255)


class MangaLib(models.Model):
    """
    Класс для хранения рейтинга, оценки пользователей с сайта
    https://mangalib.me
    """
    pass


class MangaRead(models.Model):
    """
    Класс для хранения рейтинга, оценки пользователей с сайта
    https://readmanga.live
    """
    pass
