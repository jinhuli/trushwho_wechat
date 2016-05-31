# -*- coding: utf-8 -*-

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext_lazy as _

FLATTEXT_MARKUPS = (
    'flattext.markups.HTML',
    'flattext.markups.PlainText',
    'flattext.markups.MarkDown',
    'flattext.markups.DjangoTemplate',
    )

def dynamic_import(names):
    imported = []
    for name in names:
        modname, attrname = name.rsplit('.', 1)  # python2.4+
        mod = __import__(modname, {}, {}, [''])
        imported.append(getattr(mod, attrname))
    return imported

class FlatText(models.Model):
    # Store registered markup languages.
    _markups = dynamic_import(getattr(settings, 'FLATTEXT_MARKUPS', FLATTEXT_MARKUPS))
    TEXT_TYPE_CHOICES = map(lambda x: (getattr(x, 'text_type'), getattr(x, 'text_type_display')), _markups)
    _markups_dict = dict(map(lambda c: (c.text_type, c), _markups))

    # fields
    slug = models.SlugField(max_length=255, db_index=True, unique=True)
    text_type = models.CharField(max_length=128, choices=TEXT_TYPE_CHOICES, default=TEXT_TYPE_CHOICES[0][0])
    text = models.TextField(blank=True)
    processed_text = models.TextField(blank=True, editable=False)  # rely on obj cache instead of standalone template-like cache
    note = models.CharField(blank=True, max_length=200)
    related_url = models.CharField(blank=True, max_length=400)

    class Meta:
        verbose_name = _('flattext')
        verbose_name_plural = _('flattexts')

    @property
    def markup(self):  # get the markup controller
        return self._markups_dict[self.text_type]

    def clean_fields(self, *arg, **kw):
        super(FlatText, self).clean_fields(*arg, **kw)  # does not mix errors on self.text, not a big problem
        if hasattr(self.markup, 'validate'):
            try:
                self.markup.validate(self.text)
            except ValidationError, e:
                raise ValidationError({'text':e.messages})

    def __unicode__(self):
        return self.slug

    def get_absolute_url(self):
        return self.related_url

    def save(self):
        # only for one-pass markup processor w/o any variable dependence
        # exception raise from markup.render will not be captured
        self.processed_text = self.markup.is_one_pass and self.markup.render(self.text) or ''
        super(FlatText, self).save()

    def render(self):
        if self.markup.is_one_pass:
            return self.processed_text
        return self.markup.render(self.text, self=self)
