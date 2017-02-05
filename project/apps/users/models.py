from django.contrib.auth.models import User
from django.db import models
from taggit.managers import TaggableManager

import json


class Profile(models.Model):
    user = models.OneToOneField(User)
    date_birth = models.DateField(null=True, blank=True)
    education = models.CharField(max_length=50, null=True, blank=True)
    tech_stack = TaggableManager()
    about = models.TextField(max_length=250, default='')
    links = models.TextField(default='{}')
    is_subscribe = models.BooleanField(default=True)
    online = models.DateTimeField(auto_now_add=True)
    # rating = models.IntegerField(default=10)
    gender = models.CharField(max_length=1, default='M', choices=[
        ('M', 'Мужской'),
        ('F', 'Женский'),
    ])

    # def set_links(self, links):
    #     available_values = {
    #         'vk_id': int,
    #         'github_username': str,
    #         'bitbucket_username': str,
    #         'gitlab_username': str,
    #     }
    #
    #     serialized_links = {}
    #     for key in links:
    #         if key not in available_values:
    #             continue
    #
    #         serialized_links[links[key]]
    #
    #     links = json.loads(self.links)
    #     links.append(link)
    #     self.links = json.dump(links)

    def get_links(self):
        return json.loads(self.links)

    def serialized(self):
        return {
            'id': self.user.id,
            'username': self.user.username,
            'email': self.user.email,
            'first_name': self.user.first_name,
            'last_name': self.user.last_name,
            'last_login': self.user.last_login,
            'date_joined': self.user.date_joined,
        }
