# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import parruc.flexslider


class ParrucFlexsliderLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=parruc.flexslider)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'parruc.flexslider:default')


PARRUC_FLEXSLIDER_FIXTURE = ParrucFlexsliderLayer()


PARRUC_FLEXSLIDER_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PARRUC_FLEXSLIDER_FIXTURE,),
    name='ParrucFlexsliderLayer:IntegrationTesting'
)


PARRUC_FLEXSLIDER_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PARRUC_FLEXSLIDER_FIXTURE,),
    name='ParrucFlexsliderLayer:FunctionalTesting'
)


PARRUC_FLEXSLIDER_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        PARRUC_FLEXSLIDER_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='ParrucFlexsliderLayer:AcceptanceTesting'
)
