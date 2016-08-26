# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from . import _
from plone.app.vocabularies.catalog import CatalogSource
from plone.namedfile.field import NamedBlobImage
from plone.supermodel import model
from z3c.relationfield.schema import RelationChoice
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


launches = CatalogSource(portal_type=("Document", "News Item"))


class IParrucFlexsliderLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class ISlide(model.Schema):

    image = NamedBlobImage(
        title=_("Immagine slide"),
        required=True,
    )

    link = RelationChoice(
        title=_(u"Contenuto dal linkare nella slide"),
        source=launches,
        required=False,
    )
    model.primary('image')
