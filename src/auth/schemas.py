from pydantic import BaseModel, EmailStr, SecretStr, ValidationError, field_validator


class RegistrationForm(BaseModel):
    fname: str
    lname: str
    email: EmailStr
    doc_number: str
    password: SecretStr

    @field_validator("doc_number")
    def validate_doc_number(cls, value):
        if not value.isdigit():
            raise ValidationError("doc_number must contain only digits")

        doc_number_int = int(value)
        if doc_number_int < 1000000:
            raise ValidationError("doc_number must be greater than or equal to 1,000,000")

        return value


class LoginForm(BaseModel):
    doc_number: str
    password: SecretStr

    @field_validator("doc_number")
    def validate_doc_number(cls, value):
        if not value.isdigit():
            raise ValidationError("doc_number must contain only digits")

        doc_number_int = int(value)
        if doc_number_int < 1000000:
            raise ValidationError("doc_number must be greater than or equal to 1,000,000")

        return value
