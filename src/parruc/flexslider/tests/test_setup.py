# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from parruc.flexslider.testing import PARRUC_FLEXSLIDER_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that parruc.flexslider is properly installed."""

    layer = PARRUC_FLEXSLIDER_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if parruc.flexslider is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'parruc.flexslider'))

    def test_browserlayer(self):
        """Test that IParrucFlexsliderLayer is registered."""
        from parruc.flexslider.interfaces import (
            IParrucFlexsliderLayer)
        from plone.browserlayer import utils
        self.assertIn(IParrucFlexsliderLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = PARRUC_FLEXSLIDER_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['parruc.flexslider'])

    def test_product_uninstalled(self):
        """Test if parruc.flexslider is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'parruc.flexslider'))

    def test_browserlayer_removed(self):
        """Test that IParrucFlexsliderLayer is removed."""
        from parruc.flexslider.interfaces import IParrucFlexsliderLayer
        from plone.browserlayer import utils
        self.assertNotIn(IParrucFlexsliderLayer, utils.registered_layers())
