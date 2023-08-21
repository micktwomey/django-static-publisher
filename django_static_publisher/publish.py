from pathlib import Path
from typing import Iterable

from django.conf import settings
from django.test import Client

from .patterns import PATTERNS, Patterns


def url_path_to_path(prefix: Path, url_path: str) -> Path:
    path = Path(url_path)
    if path.is_absolute():
        path = path.relative_to("/")
    return prefix / path / "index.html"


def render_to_path(destination: Path, client: Client, url: str):
    response = client.get(url)
    assert response.status_code == 200, (response.status_code, response)
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("wb") as fp:
        fp.write(response.content)


def publish(destination_path: Path, patterns: Patterns = PATTERNS) -> Iterable[Path]:
    settings.ALLOWED_HOSTS = ["testserver"]
    settings.STATIC_ROOT = str(destination_path / "static")
    # TODO: allow override setting for prefix for reversed urls in rendered templates
    # when writing out
    # TODO: Would it be worth spinning up a server and using HTTP requests?
    client = Client(raise_request_exception=True)
    for query, reverser in patterns:
        if query is None:
            url_path = reverser(None)
            rendered_path = url_path_to_path(destination_path, url_path)
            render_to_path(rendered_path, client, url_path)
            yield rendered_path
        else:
            for model in query().all():
                url_path = reverser(model)
                rendered_path = url_path_to_path(destination_path, url_path)
                render_to_path(rendered_path, client, url_path)
                yield rendered_path

    # Defer import to ensure settings from above take
    from django.contrib.staticfiles.management.commands import collectstatic

    cmd = collectstatic.Command()
    cmd.dry_run = False
    cmd.symlink = False
    cmd.clear = False
    cmd.ignore_patterns = []
    cmd.verbosity = 2
    cmd.post_process = True
    cmd.collect()
