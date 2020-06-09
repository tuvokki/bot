from django.contrib import admin

from BotApp.models import IntentPointer, Intent

admin.site.register([Intent, IntentPointer])
