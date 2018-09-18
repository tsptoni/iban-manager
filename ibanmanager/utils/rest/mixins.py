from django.core.exceptions import ObjectDoesNotExist
from django.utils.encoding import smart_text
from rest_framework import mixins
from django.utils.translation import ugettext as _
from rest_framework.viewsets import GenericViewSet


class FromPrivateKeyMixin(object):
    """Allow to provide the PK of the model to retrieve it instead of creating a new instance with fields from data."""

    default_error_messages = {
        'does_not_exist': _('Invalid pk "{pk_value}" - object does not exist.'),
        'incorrect_type': _('Incorrect type. Expected pk value, received {data_type}.'),
    }

    def to_internal_value(self, data):
        """Transform the *incoming* primitive data into a native value."""
        if data is None or isinstance(data, dict):
            return super(FromPrivateKeyMixin, self).to_internal_value(data)
        elif data == '':
            self.fail('does_not_exist', pk_value=smart_text(data))
        else:
            try:
                return self.Meta.model.objects.get(pk=data)
            except ObjectDoesNotExist:
                self.fail('does_not_exist', pk_value=smart_text(data))
            except (TypeError, ValueError):
                self.fail('incorrect_type', data_type=type(data).__name__)

    def create(self, validated_data):
        if isinstance(validated_data, self.Meta.model):
            return validated_data
        return super(FromPrivateKeyMixin, self).create(validated_data)


class PartialUpdateModelMixin(mixins.UpdateModelMixin):

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super(PartialUpdateModelMixin, self).update(request, *args, **kwargs)


class CustomModelViewSet(mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin,
                       PartialUpdateModelMixin,
                       mixins.DestroyModelMixin,
                       mixins.ListModelMixin,
                       GenericViewSet):

    pass
