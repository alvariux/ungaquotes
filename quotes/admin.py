from django.contrib import admin
from .models import Quote
from .models import QuoteDetail

admin.site.register(Quote)
admin.site.register(QuoteDetail)

