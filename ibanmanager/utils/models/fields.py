from django.db import models
from django.conf import settings


class FirstRegistry(object):
    _registry = {}

    def add_field(self, model, field):
        reg = self.__class__._registry.setdefault(model,[])
        reg.append(field)

    def get_fields(self, model):
        return self.__class__._registry.get(model, [])

    def __contains__(self, model):
        return model in self.__class__._registry


class LastRegistry(object):
    _registry = {}

    def add_field(self, model, field):
        reg = self.__class__._registry.setdefault(model,[])
        reg.append(field)

    def get_fields(self, model):
        return self.__class__._registry.get(model, [])

    def __contains__(self, model):
        return model in self.__class__._registry


class FirstUserField(models.ForeignKey):
    def __init__(self, to=settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL, **kwargs):
        super(FirstUserField, self).__init__(to=to, blank=blank, null=null, on_delete=on_delete, **kwargs)

    def contribute_to_class(self, cls, name, **kwargs):
        super(FirstUserField, self).contribute_to_class(cls, name)
        registry = FirstRegistry()
        registry.add_field(cls, self)



class LastUserField(models.ForeignKey):
    def __init__(self, to=settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL, **kwargs):
        super(LastUserField, self).__init__(to=to, blank=blank, null=null, on_delete=on_delete, **kwargs)

    def contribute_to_class(self, cls, name, **kwargs):
        super(LastUserField, self).contribute_to_class(cls, name)
        registry = LastRegistry()
        registry.add_field(cls, self)