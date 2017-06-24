from django.db import models
from django.utils import timezone


class Post(models.Model):           # oznacza, że nasz obiekt Post jest modelem Django (dziedziczymy po tej klasie)
                                    # ta linijka definiuje nasz model (jest on obiektem, czyli object)
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)    # tak definiujemy tekst z ograniczoną liczbą znaków
    text = models.TextField()   # do dłuższych tekstów bez ograniczeń w ilości znaków
    created_date = models.DateTimeField(default=timezone.now)   # data i godzina
    published_date = models.DateTimeField(blank=True, null=True)    # odnośnik do innego modelu

    def publish(self):      # metoda publikujaca wpis
        self.published_date = timezone.now()
        self.save()

    def __str__(self):      # zwraca tekst (string) zawierający tytuł wpisu
        return self.title
