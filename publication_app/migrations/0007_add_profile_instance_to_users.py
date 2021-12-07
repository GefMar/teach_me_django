from django.db import migrations, models


def create_profiles_to_user(apps, schemas_editor):
    user_model = apps.get_model('auth', "User")
    profile_model = apps.get_model('publication_app', "Profile")
    users = user_model.objects.filter(profile__isnull=True).all()
    for user in users:
        profile = profile_model(user=user)
        profile.save()


class Migration(migrations.Migration):
    dependencies = [
        ('publication_app', '0006_profile'),
    ]

    operations = [
        migrations.RunPython(create_profiles_to_user),

    ]


# TODO: Страница регистрации
# TODO: Старница Авторизации
# TODO: Просмотр своего профиля
# TODO: Редактирование своего профиля
# не может изменять username
# TODO: Форма публикации Поста

