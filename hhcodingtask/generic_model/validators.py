from django.core.exceptions import ValidationError


def clean_and_validate(data, scheme):
    cleaned_data = {}
    errors = {}

    if not isinstance(data, dict):
        raise ValidationError('Data is not dict')

    for name, value in data.items():
        if name not in scheme:
            continue

        try:
            cleaned_data[name] = scheme[name](value)
        except Exception as e:
            errors[name] = str(e)

    if errors:
        raise ValidationError(errors)

    return cleaned_data
