from rest_framework import serializers
from .models import *

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>USER REGISTRATIONS<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(max_length=20, write_only=True)

    class Meta:
        model = User
        fields = ('username','email', 'type','password', 'confirm_password')

    def create(self, validated_data):
        validated_data.pop("confirm_password")
        user = User(
            # email=validated_data['email'],
            # username=validated_data['username'],
            **validated_data

        )
        user.set_password(validated_data['password'])
        user.save()
        return user
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>USER LOGIN<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=200)
    password = serializers.CharField()
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>BOOK<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('book_id', 'book_name', 'book_price', 'book_author', 'book_dateofpublication', 'book_in_language', 'add_by')
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>LEND BOOK<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
class LendBookSerializer(serializers.ModelSerializer):
    book = serializers.ReadOnlyField(source='book.book_name')

    class Meta:
        model = LendBook
        fields = ['book', 'tc' , 'fine' ]
        # depth =1
class PaymentDoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentDone
        fields = ('payment_done' ,)

    