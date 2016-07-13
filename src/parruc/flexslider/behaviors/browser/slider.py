# -*- coding: utf-8 -*-

from plone import api
from plone.app.layout.viewlets import common as base


class SliderViewlet(base.ViewletBase):

    def slides(self):
        import pdb; pdb.set_trace()
        return self.context.slides
