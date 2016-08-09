"""
importing user model and serializer model
"""
from django.contrib.auth.models import User
from rest_framework import serializers
from signup.utiles import send_twilio_message


class UserSerializer(serializers.ModelSerializer):
    """
    User Validation
    """
    password = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)
    confirm_password = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)
    mobile_number = serializers.CharField(write_only=True)

    def validate_password(self, value):
        """
        validate length of the password
        """
        # pylint: disable=no-self-use
        if len(value) < 4:
            raise serializers.ValidationError("Short Password!")
        return value

    def validate_confirm_password(self, value):
        """
        validate length of confirm password
        """
        # pylint: disable=no-self-use
        if len(value) < 4:
            raise serializers.ValidationError("Short Password!")
        else:
            return value

    def validate(self, data):
        """
        validate for same password
        """
        if data['confirm_password'] != data['password']:
            raise serializers.ValidationError("Passwords don't match")
        return data

    def create(self, validated_data):
        """
        create user
        """
        number = validated_data['mobile_number']
        body = 'Welocom User'

        send_twilio_message(number, body)
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )

        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        """
        user model
        """
        model = User
        fields = ('id', 'username', 'email', 'password',
                  'confirm_password', 'mobile_number')


class UpdateSerializer(serializers.ModelSerializer):
    """
    for user update put and patch
    """
    user = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = User
        fields = ('user', 'username', 'email', 'password')
