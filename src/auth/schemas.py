from pydantic import BaseModel, EmailStr, ValidationError, field_validator


class RegistrationForm(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    doc_number: int = 1_234_567
    password: str

    @field_validator("doc_number")
    def validate_doc_number(cls, value):
        if value < 1000000:
            raise ValidationError(
                "doc_number must be greater than or equal to 1,000,000"
            )

        return value


class LoginForm(BaseModel):
    doc_number: int
    password: str

    @field_validator("doc_number")
    def validate_doc_number(cls, value):
        if value < 1000000:
            raise ValidationError(
                "doc_number must be greater than or equal to 1,000,000"
            )

        return value
