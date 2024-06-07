from django.contrib import admin
from .models import comment, User, category, bid, watchlist, list_item

# Register your models here.

admin.site.register(comment)
admin.site.register(User)
admin.site.register(category)
admin.site.register(bid)
admin.site.register(watchlist)
admin.site.register(list_item)