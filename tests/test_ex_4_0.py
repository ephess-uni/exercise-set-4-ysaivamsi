import pytest
from src.ex_4_0 import get_shutdown_events
from textwrap import dedent


@pytest.mark.parametrize(
    'logfile',
    [
        'data/messages.log',
        'tests/fixtures/messages.log',
    ]
)
def test___get_shutdown_events___returns_list(logfile,feedback):
    md = dedent("""
    # Feedback
    Assure that get_shutdown_events() returns a *list* type.
    """
    )
    feedback(md)

    assert isinstance(get_shutdown_events(logfile), list)


@pytest.mark.parametrize(
    'logfile,expected_length',
    [
        ('data/messages.log', 2),
        ('tests/fixtures/messages.log', 4),
    ]
)
def test___get_shutdown_events___returns_correct_number_of_lines(logfile, expected_length, feedback):
    md = dedent(
        """
        # Feedback
        get_shutdown_events should only collect log events where shutdowns were initiated.
        
        This tests the number of events returned by your function.  For the default logfile, 
        this should be 2.
        """
    )
    feedback(md)
    assert len(get_shutdown_events(logfile)) == expected_length


@pytest.mark.parametrize(
    'logfile',
    [
        'data/messages.log',
        'tests/fixtures/messages.log',
    ]
)
def test___get_shutdown_events___collects_only_shutdown_initiated(logfile, feedback):
    md = dedent(
        """
        # Feedback
        get_shutdown_events should only collect log events where shutdowns were initiated.

        This tests the content of each list and asserts that *Shutdown initiated* is present.
        """
    )
    feedback(md)
    actual = get_shutdown_events(logfile)
    assert all(['Shutdown initiated'.lower() in s.lower() for s in actual])