from django.db import models
from django.utils.translation import ugettext_lazy as _

from ckeditor_uploader.fields import RichTextUploadingField


class Blog(models.Model):
    title = models.CharField(
        max_length=256,
        verbose_name=_('Title :'),
        unique=True,
        null=False,
        blank=False
    )
    slug = models.SlugField(
        max_length=256,
        verbose_name=_('Slug :'),
        unique=True,
        null=False,
        blank=False
    )
    thumbnail = models.ImageField(
        upload_to='content/blog/thumbnail/',
        verbose_name=_('Thumbnail :')
    )
    publish = models.BooleanField(
        verbose_name=_('Publish :'),
        default=True,
        help_text=_('Will this post be published?')
    )
    create_time = models.DateTimeField(
        verbose_name=_('Create Time'),
        auto_now_add=True,
        null=False,
        blank=False,
        editable=False
    )
    last_update_time = models.DateTimeField(
        verbose_name=_('Last Update Time'),
        auto_now=True,
        null=False,
        blank=False,
        editable=False
    )
    content = RichTextUploadingField()

    class Meta:
        verbose_name = _('Blog')
        verbose_name_plural = _('Blogs')

    def __str__(self):
        return self.title


class Skill(models.Model):
    title = models.CharField(
        max_length=256,
        verbose_name=_('Title :'),
        unique=True,
        null=False,
        blank=False
    )
    description = models.TextField(
        verbose_name=_('Description :'),
        null=False,
        blank=False
    )
    icon = models.CharField(
        max_length=30,
        verbose_name=_('Icon name :'),
        null=False,
        blank=False
    )

    class Meta:
        verbose_name = _('Skill')
        verbose_name_plural = _('Skills')

    def __str__(self):
        return self.title


class ContactUs(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name=_('Name'),
        null=False,
        blank=False
    )
    email = models.EmailField(
        verbose_name=_('Email'),
        null=False,
        blank=False
    )
    message = models.TextField(
        verbose_name=_('Message'),
        null=False,
        blank=False
    )
    create_time = models.DateTimeField(
        verbose_name=_('Create Time'),
        auto_now_add=True,
        null=False,
        blank=False,
        editable=False
    )

    class Meta:
        verbose_name = _('Contact Us')
        verbose_name_plural = _('Contact Us')

    def __str__(self):
        return str(self.pk)
