# Notes

  source projectname/bin/activate
  deactivate - quits virtualenv

  import django
  django.VERSION

  python manage.py migrate
  python manage.py runserver

  python manage.py startapp blog
  python manage.py makemigrations blog
  python manage.py sqlmigrate blog 0001
  python manage.py migrate
  python manage.py createsuperuser
  python manage.py shell

  # command line work
  from django.contrib.auth.models import User
  from blog.models import Post

  post.save()

  Post.Objects.filter(publish__year=2016, author__name='admin')

  Post.objects.filter(publish__year=2016)\
... .filter(author__username='tharnid')

    .exclude

    Post.objects.order_by('title')

    -title would be descending order
