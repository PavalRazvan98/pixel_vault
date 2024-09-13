import pytest
from django.contrib.auth import get_user_model
from django.core.management import call_command
from faker import Faker

User = get_user_model()

f = Faker()


@pytest.mark.django_db
def test_populate_users_database():
    assert User.objects.count() == 0
    call_command("populate_users_database")
    assert User.objects.filter(is_superuser=False, is_staff=False).count() == 15


@pytest.mark.django_db
def test_populate_users_database_already_exist():
    User.objects.create(
        username=f.user_name(),
        first_name=f.first_name(),
        last_name=f.last_name(),
        email=f.email(),
    )

    assert User.objects.filter(is_superuser=False, is_staff=False).count() == 1
    call_command("populate_users_database")
    assert User.objects.filter(is_superuser=False, is_staff=False).count() == 1
