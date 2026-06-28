from django.core.exceptions import ValidationError


def validate_summary_length(value):
    if len(value) < 3:
        raise ValidationError("Краткое описание должно быть не менее 3 символов.")


def validate_exlude_words(value):
    exclude_word = '404'
    if exclude_word in value.lower():
        raise ValidationError(f"Описание содержит недопустимое слово: '{exclude_word}'")