from django.core.validators import RegexValidator


start_with_letter_validator = RegexValidator(regex=r'^[A-Za-z_]',
                                             message="Name must start with a letter or _.")

contains_only_letters_dash_underscore_validator = RegexValidator(regex=r'^[-\w]*$',
                                                                 message="Name must contain only alphanumeric characters, _'s, or -'s.")
