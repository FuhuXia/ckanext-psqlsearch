import pytest

from ckan.plugins import plugin_loaded

import ckanext.psqlsearch.plugin as plugin


@pytest.mark.ckan_config("ckan.plugins", "psqlsearch")
@pytest.mark.usefixtures("with_plugins")
def test_plugin_loads():
    assert plugin_loaded("psqlsearch")


def test_actions_are_registered():
    actions = plugin.PsqlsearchPlugin().get_actions()

    assert "package_search" in actions
    assert "package_autocomplete" in actions
