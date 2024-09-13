import os

import pytest
from django.contrib.auth import get_user_model
from django.core.management import call_command

User = get_user_model()


@pytest.mark.django_db
def test_create_superuser_from_env_variables():
    assert User.objects.filter(is_superuser=True).count() == 0
    call_command("create_pixel_vault_superuser")
    assert User.objects.filter(is_superuser=True).count() == 1
    assert os.environ.get("PIXEL_VAULT_USERNAME") == "admin"
    assert os.environ.get("PIXEL_VAULT_EMAIL") == "admin@gmail.com"


@pytest.mark.django_db
def test_superuser_already_created():
    User.objects.create_superuser(
        username="ion",
        password="ion",
        email="ion@gmail.com",
    )
    assert User.objects.filter(is_superuser=True).count() == 1
    call_command("create_pixel_vault_superuser")
    assert User.objects.filter(is_superuser=True).count() == 1
    s_user = User.objects.filter(is_superuser=True).first()
    assert s_user.username == "ion"
    assert s_user.email == "ion@gmail.com"


@pytest.mark.django_db
def test_superuser_create_from_flags():
    assert User.objects.filter(is_superuser=True).count() == 0
    call_command(
        "create_pixel_vault_superuser",
        "--username",
        "test",
        "--password",
        "test",
        "--email",
        "test@gmail.com",
    )
    assert User.objects.filter(is_superuser=True).count() == 1
    s_user = User.objects.filter(is_superuser=True).first()
    assert s_user.username == "test"
    assert s_user.email == "test@gmail.com"
