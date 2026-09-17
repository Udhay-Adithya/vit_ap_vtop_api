"""Sphinx configuration.

The endpoint reference is generated from the app's own OpenAPI schema rather
than written out, so a route or a model that changes cannot leave the docs
behind. Prose that explains *why* the API is shaped the way it is lives in
guide/ and is written by hand.
"""

import json
import os
import sys
import tomllib
from pathlib import Path

_root = Path(__file__).parent.parent
sys.path.insert(0, str(_root))

_pyproject = tomllib.loads((_root / "pyproject.toml").read_text())

project = "VIT-AP VTOP API"
author = "Udhay Adithya"
copyright = "%Y, Udhay Adithya"
release = _pyproject["tool"]["poetry"]["version"]
version = ".".join(release.split(".")[:2])


def _dump_openapi() -> None:
    """Writes the app's OpenAPI schema for sphinxcontrib-openapi to render.

    Importing the app needs a settings value, and the docs build has no real
    one -- nothing here talks to VTOP, the key is only read to compare against
    an incoming header.
    """
    os.environ.setdefault("API_KEY", "docs-build-placeholder")
    from src.main import app

    (Path(__file__).parent / "openapi.json").write_text(
        json.dumps(app.openapi(), indent=2)
    )


_dump_openapi()

extensions = [
    "sphinxcontrib.openapi",
    "sphinx.ext.intersphinx",
    "sphinx_copybutton",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

intersphinx_mapping = {"python": ("https://docs.python.org/3", None)}

html_theme = "furo"
html_title = f"VIT-AP VTOP API {release}"
html_static_path = ["_static"]
# Copied verbatim into the build. Holds .nojekyll, which stops GitHub Pages
# running Jekyll -- Jekyll drops directories beginning with an underscore, and
# Sphinx puts every asset in _static.
html_extra_path = ["_extra"]
html_theme_options = {
    "source_repository": "https://github.com/Udhay-Adithya/vit_ap_vtop_api/",
    "source_branch": "main",
    "source_directory": "docs/",
}
