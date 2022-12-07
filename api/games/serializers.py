from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import CustomUser, Game, GameUser
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        return token

class CustomUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField(min_length=3, write_only=True)

    class Meta:
        model = CustomUser
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)  # as long as the fields are the same, we can just use this
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class GameSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Game
        fields = '__all__'

class GameUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameUser
        fields = '__all__'
