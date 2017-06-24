from django.contrib import admin
from .models import Post    # importujemy (dołączamy) model Post, który zdefiniowałyśmy w models.py

admin.site.register(Post)   # Aby nasz model był widoczny w panelu admina, musimy go zarejestrować