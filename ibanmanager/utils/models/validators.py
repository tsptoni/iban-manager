from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from stdnum.exceptions import ValidationError as stdnumValidationError

from stdnum import iban

def validate_iban(value):

    try:
        iban.validate(value)
        return True
    except stdnumValidationError as e:
            raise ValidationError(
                _('%(value)s is not valid format'),
                params={'value': value},
            )