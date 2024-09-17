import pytest


def test_system_requirement_memory(system_requirement_factory):
    assert system_requirement_factory.build(memory_mb=1).memory == "1 MB"
    assert system_requirement_factory.build(memory_mb=1024).memory == "1.0 GB"
    assert system_requirement_factory.build(memory_mb=8540).memory == "8.33984375 GB"
    assert system_requirement_factory.build(memory_mb=50000).memory == "48.828125 GB"
    assert system_requirement_factory.build(memory_mb=0).memory == "None"
    assert system_requirement_factory.build(memory_mb=None).memory == "None"


def test_system_requirement_storage(system_requirement_factory):
    assert system_requirement_factory.build(storage_mb=1).storage == "1 MB"
    assert system_requirement_factory.build(storage_mb=1024).storage == "1.0 GB"
    assert system_requirement_factory.build(storage_mb=8540).storage == "8.33984375 GB"
    assert system_requirement_factory.build(storage_mb=50000).storage == "48.828125 GB"
    assert system_requirement_factory.build(storage_mb=0).storage == "None"
    assert system_requirement_factory.build(storage_mb=None).storage == "None"


@pytest.mark.django_db
def test_game_str(game):
    assert str(game) == f"{game.title} ({game.release_year})"


@pytest.mark.django_db
def test_system_requirement_str(system_requirement):
    valid = f"{system_requirement.game} {system_requirement.type} run on {system_requirement.os}"
    assert str(system_requirement) == valid
