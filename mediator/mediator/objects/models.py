import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

#
# Models will be references to tModelhe actual files on the sftp server and will contain only needed metadata
#


class Media(models.Model):
    class MediaType(models.TextChoices):
        BOOKS = 'BK', _('Books')
        TV = 'TV', _('Television')
        MISC = 'XX', _('Miscellaneous')

    id = models.CharField(max_length=2, choices=MediaType.choices, default=MediaType.MISC)
    mType = models.CharField(max_length=15)
    attribs = models.JSONField()
    pos_ref = models.FilePathField(path='media')

    def get_mtype(self):
        return self.mType

    def get_full_mtype(self):
        return Media.MediaType(self.id)

    def get_dir(self):
        return self.pos_ref


class Book(models.Model):
    class Format(models.TextChoices):
        PDF = 'P', _('PDF')
        MOBI = 'M', _('MOBI')
        EPUB = 'E', _('EPUB')
        TEXT = 'T', _('TXT')

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    topic = models.ManyToManyField("Topics", through="Topics", on_delete=models.PROTECT())
    format = models.CharField(max_length=4, choices=Format.choices, default=Format.PDF)
    favorite = models.BooleanField(default=False)
    # date = models.SmallIntegerField()
    # tags = models.ManyToManyField("Tags", through="Tags", on_delete=models.PROTECT)
    pos_ref = models.FilePathField(path="media/books")

    def get_format(self):
        return self.format

    def __str__(self):
        return self.title


class Topics(models.Model):
    topicId = models.SmallIntegerField(primary_key=True)
    topicName = models.CharField(max_length=20)
    topicPath = models.FilePathField(path="media/books/topics")


    def __str__(self):
        return self.topicName



class TV(models.Model):

    id = models.UUIDField()
    title = models.CharField(max_length=200)
    season = models.CharField(max_length=50)
    # date = models.SmallIntegerField()
    # tags = models.ManyToManyField("Tags", through="Tags", on_delete=models.PROTECT)
    pos_ref = models.FilePathField(path="media/tv")

    def __str__(self):
        return self.title



# TODO: Attach tagging system
#
# class Tags(models.Model):
#     tag = models.CharField(20)
#     taggedBooks = models.ManyToManyField("Book")
#     taggedTv = models.ManyToManyField("TV")
#

