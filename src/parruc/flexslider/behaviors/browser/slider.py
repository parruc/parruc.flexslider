# -*- coding: utf-8 -*-

from Acquisition import aq_parent
from plone.app.layout.viewlets import common as base


class SliderViewlet(base.ViewletBase):

    def slides(self):
        return self.context.slides


class ParentSliderViewlet(base.ViewletBase):

    def slides(self):
        parent = aq_parent(self.context)
        if hasattr(parent, "slides") and parent.slides:
            return parent.slides
