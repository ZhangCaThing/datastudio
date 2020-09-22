import json
from unittest.mock import patch

from nose.tools import eq_

from example.commons import Faker
from pyecharts import options as opts
from pyecharts.charts import Map


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_map_base(fake_writer):
    c = Map().add(
        "商家A", [list(z) for z in zip(Faker.provinces, Faker.values())], "china"
    )
    c.render()
    _, content = fake_writer.call_args[0]
    eq_(c.theme, "white")
    eq_(c.renderer, "canvas")


def test_map_emphasis():
    c = Map().add(
        "商家A",
        [list(z) for z in zip(Faker.provinces, Faker.values())],
        "china",
        emphasis_label_opts=opts.LabelOpts(is_show=False),
        emphasis_itemstyle_opts=opts.ItemStyleOpts(border_color="white"),
    )
    options = json.loads(c.dump_options())
    expected = {
        "label": {"show": False, "position": "top", "margin": 8},
        "itemStyle": {"borderColor": "white"},
    }
    eq_(expected, options["series"][0]["emphasis"])