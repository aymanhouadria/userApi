from rest_framework import serializers
from users_api.models import User, Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('id', 'street', 'state', 'city', 'country', 'zip')


class UserSerializer(serializers.ModelSerializer):
    address = AddressSerializer(read_only=False)

    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'birthdate', 'address')

    def create(self, validated_data):
        address, user, address_data = Address(), User(), validated_data.get('address')
        user = create_address_and_user(user, validated_data, address_data, address)

        return user

    def update(self, instance, validated_data):
        user_instance, address_data = instance, validated_data.get('address')
        address = user_instance.address
        user = create_address_and_user(user_instance, validated_data, address_data, address)

        return user



def create_address_and_user(user_instance, validated_data, address_data, address):
    for address_attr, address_value in address_data.items():
        setattr(address, address_attr, address_value)
    address.save()

    for attr, value in validated_data.items():
        if attr != 'address':
            setattr(user_instance, attr, value)
    user_instance.address = address
    user_instance.save()

    return user_instance
