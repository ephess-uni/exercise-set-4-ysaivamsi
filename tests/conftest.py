import pytest
from rich import print
from rich.panel import Panel
from rich.markdown import Markdown


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"

    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture
def feedback(request):
    md_message = []

    def _feedback(message_):
        nonlocal md_message
        md_message.append(message_)

    yield _feedback

    if request.node.rep_call.failed:
        feedback_panel = Panel(
            Markdown(md_message[0]),
        )
        print(feedback_panel)
