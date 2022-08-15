from django.db import models

from wagtail.models import Page

from wagtail.core.fields import RichTextField

from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel

from wagtail.images.edit_handlers import ImageChooserPanel


class HomePage(Page):
    pass
