from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
import os
from django.core import management

from project.apps.meetings.models import Meeting
from project.apps.posts.models import Post
from project.apps.projects.models import Project
from project.apps.users.models import Profile


class Command(BaseCommand):
    help = 'Clean old migrations and create new db'

    def remove_migrations(self):
        print('Removing migrations...')
        os.remove(os.path.join('.', 'db.sqlite3'))

        for root, dirs, files in os.walk('./project/apps', topdown=False):
            if '/migrations' not in root:
                continue
            for name in files:
                if name == '__init__.py':
                    continue
                print('Removing "%s"...' % os.path.join(root, name))
                os.remove(os.path.join(root, name))

    def create_data(self):
        print('Creating test users...')
        admin = User.objects.create_user('admin', password='test1010')
        admin.is_superuser = True
        admin.is_staff = True
        admin.save()
        Profile.objects.create(user=admin).save()  # todo recievers

        user1 = User.objects.create_user('user', password='test1010')
        Profile.objects.create(user=user1).save()

        user2 = User.objects.create_user('smith', password='smith1010')
        Profile.objects.create(user=user2).save()

        print('Creating test posts...')
        post1 = Post.objects.create(
            title='Test',
            content='Bla bla...\n[b]test[/b] [u]bbcode[/u]',
            author=admin
        )

        post1.tags.add('C++', 'Python3', 'Go')
        post1.save()

        post2 = Post.objects.create(
            title='Lorem ipsum dolor sit amet',
            content='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut '
                    'labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco '
                    'laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in '
                    'voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat '
                    'non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
            author=admin
        )

        post2.tags.add('Java', 'News')
        post2.save()

        print('Creating test projects...')
        project1 = Project.objects.create(
            title='Lorem ipsum dolor sit amet',
            description='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut '
                        'labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco '
                        'laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in '
                        'voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat '
                        'non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
            author=admin,
            is_published=True
        )
        project1.members.add(user1)
        project1.members.add(user2)
        project1.tech_stack.add('C++', 'Django')
        project1.save()

        print('Creating test meetings...')
        meeting1 = Meeting.objects.create(
            title='Lorem ipsum dolor sit amet',
            description='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut '
                        'labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco '
                        'laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in '
                        'voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat '
                        'non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
            author=admin,
            is_published=True
        )
        meeting1.members.add(user1)
        meeting1.members.add(user2)
        meeting1.projects.add(project1)
        meeting1.save()

    def handle(self, *args, **options):
        self.remove_migrations()

        print('Create DB...')
        management.call_command('makemigrations')
        management.call_command('migrate')

        self.create_data()
