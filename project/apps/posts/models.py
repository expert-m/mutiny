from django.contrib.auth.models import User
from django.db import models
from taggit.managers import TaggableManager


class Post(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, null=True, blank=True)
    tags = TaggableManager()
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'app_post'


class PostImage(models.Model):
    image = models.ImageField(upload_to='post_images/%Y/%m/%d')
    info = models.CharField(max_length=140)
    created = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post)
    user = models.ForeignKey(User)

    def save(self, *args, **kwargs):
        try:
            this_img = PostImage.objects.get(id=self.id)
            if this_img.data != self.data:
                this_img.data.delete(save=False)
        except:
            pass

        super(PostImage, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.data.delete(save=False)
        super(PostImage, self).delete(*args, **kwargs)

    def __str__(self):
        return self.data.name

    class Meta:
        db_table = 'app_post_image'
