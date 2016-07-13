# -*- coding: utf-8 -*-
from zope.interface import implements

from plone.dexterity.content import Item

from .interfaces import ISlide


class Slide(Item):
    implements(ISlide)
