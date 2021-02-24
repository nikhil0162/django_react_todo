# nopep8
import django
import random
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo.settings')
django.setup()

from faker import Faker
from blog.models import Category, Post
from django.contrib.auth import get_user_model

User = get_user_model()

fakegen = Faker()
from faker import providers

category = ['electric', 'cloths', 'django', 'insurance', 'security']


def add_category():
    c = Category.objects.get_or_create(name=random.choice(category))[0]
    c.save()
    return c


def populate(num=5):
    user = User.objects.get(id=2)
    for entry in range(num):
        category = add_category()
        fake_title = fakegen.name()
        fake_excerpt = fakegen.name()
        fake_content = fakegen.text()
        fake_slug = fakegen.slug()
        # fake_published = providers.date_time
        fake_author = user
        fake_status = fakegen.sentence()

        Post.objects.get_or_create(category=category,
                                          title=fake_title,
                                          excerpt=fake_excerpt,
                                          content=fake_content,
                                          slug=fake_slug,
                                        #   published=fake_published,
                                          status=fake_status,
                                          author=fake_author
                                          )


if __name__ == '__main__':
    print("populating data, please wait...")
    populate(20)
    print("data populated successfully")
