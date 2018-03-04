from django.contrib.auth.models import User

from rest_framework.serializers import (
    CharField,
    EmailField,
    ModelSerializer,
    ValidationError
)

class UserLoginSerializer(ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    username = CharField()
    # email = EmailField()
    class Meta:
        model = User
        fields = [
            'username',
            # 'email',
            'password',
            'token',
        ]
        extra_kwargs = {"password":
                            {"write_only": True}
                        }
    def validate(self, data):
        # username = data['username']
        username = data.get("username", None)
        password = data.get("password", None)

        user_qs = User.objects.filter(username=username)

        if user_qs.exists() and user_qs.count() == 1:
            user = user_qs.first()
        else:
            raise ValidationError("This username is not exist")

        if user:
            if not user.check_password(password):
                raise ValidationError("Incorrect credentials please try again")

        return data