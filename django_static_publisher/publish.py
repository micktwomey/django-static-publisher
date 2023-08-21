from pathlib import Path

from django.conf import settings
from django.test import Client

from .patterns import PATTERNS


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


def publish(destination_path: Path, patterns=PATTERNS):
    settings.ALLOWED_HOSTS = ["testserver"]
    # TODO: allow override setting for prefix for reversed paths when writing out
    client = Client()
    for query, reverser in patterns:
        if query is None:
            url_path = reverser(None)
            rendered_path = url_path_to_path(destination_path, url_path)
            print(rendered_path)
            render_to_path(rendered_path, client, url_path)
        else:
            for model in query().all():
                url_path = reverser(model)
                rendered_path = url_path_to_path(destination_path, url_path)
                print(rendered_path)
                render_to_path(rendered_path, client, url_path)