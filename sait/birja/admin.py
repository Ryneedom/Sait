from django.contrib import admin
from .models import Applicant, Company, Post, ListPost, Vacancy

admin.site.register(Applicant)
admin.site.register(Company)
admin.site.register(Post)
admin.site.register(ListPost)
admin.site.register(Vacancy)
