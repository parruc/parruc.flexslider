# -*- coding: utf-8 -*-

from plone import api
from plone.app.layout.viewlets import common as base


class SliderViewlet(base.ViewletBase):

    def slides(self):
        return self.context.slides
