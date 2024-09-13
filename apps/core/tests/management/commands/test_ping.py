from io import StringIO

from django.core.management import call_command


def test_command_output():
    out = StringIO()
    call_command("ping", stdout=out)
    assert out.getvalue() == "pong\n"
