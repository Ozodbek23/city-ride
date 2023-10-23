from django.core.validators import RegexValidator

phone_validator = RegexValidator(
    regex=r'^\d{9}$',
    message="Phone number must be exactly 9 digits long!",
)
