import pytest
from app import app


def test_header_present():
    layout = app.layout
    assert any(c.id == "header" for c in layout.children if hasattr(c, "id"))


def test_graph_present():
    layout = app.layout
    assert any(c.id == "sales-chart" for c in layout.children if hasattr(c, "id"))


def test_region_picker_present():
    layout = app.layout
    assert any(c.id == "region-filter" for c in layout.children if hasattr(c, "id"))