from django.shortcuts import render
from .models import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializer import *
from django.contrib.auth import authenticate, login , logout
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .permissions import*
from datetime import date, timedelta
from django.utils import timezone
        


# Creating tokens manually
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

# Create your views here.
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>USER REGISTRATIONS<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
class UserRegistration(APIView):
    def post(self, request ):
        data = request.data
        serializers = UserSerializer(data=data)
        serializers.is_valid(raise_exception=True)
        a = request.data['password']
        b = request.data['confirm_password']
        if a == b :
            # User.objects.create(name=request.data['name'], email=request.data['email'], password=request.data['password'])
            serializers.save()
            return Response({'message' : 'you have succefully created done your registration' , 'data' : serializers.data }, status=status.HTTP_200_OK)
        else:
            return Response({'message' : 'password didnt matched please try again' , 'data' : serializers.data }, status=status.HTTP_400_BAD_REQUEST)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>USER LOGIN<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
class UserLogin(APIView):
    def post(self, request, format=None):
        data = request.data
        serializers = LoginSerializer(data=data)
        serializers.is_valid(raise_exception=True)
        username = serializers.data.get('username')
        password = serializers.data.get('password')
        user = authenticate(username=username , password=password)
        if user is not None:
            login(request, user)
            token = get_tokens_for_user(user)
            return Response({'token' : token ,'msg': 'Login Success'}, status=status.HTTP_200_OK)
        return Response({'errors': {'non_field_errors': ['Email or Password is not valid']}}, status=status.HTTP_404_NOT_FOUND)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>BOOK VIEW<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
class BookView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, id=None, format=None):
        id = id
        if id is not None:
            book =Book.objects.get(id=id)
            serializer = BookSerializer(book)
            return Response(serializer.data)
        book = Book.objects.all()
        serializer = BookSerializer(book, many=True)
        return Response(serializer.data)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>BOOK ENTRY<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
class BookEntryView(APIView):
    permission_classes = [AuthorAllStaffAllButEditOrReadOnly]
    def put(self, request):
        # user = User.objects.filter(username = request.user).first()
        # if user.type == "admin":
            # print("🚀 ~ file: views.py ~ line 72 ~ user")
        data=request.data
        serializers = BookSerializer(data=data)
        if serializers.is_valid():
            serializers.save()
            return Response({'msg': 'data Created' , "data":serializers.data}, status=status.HTTP_200_OK)
        return Response({'message' : 'please input your data and Try again!!' , "data" : serializers.errors }, status=status.HTTP_400_BAD_REQUEST)
        # else:
        #     return Response({'message' : 'only admin can add book!!'})
            
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>BOOK PARTIALLY UPDATE<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
class BookUpdate(APIView):
    permission_classes = [IsAuthenticated]
    def patch(self, request , id = None):
        book = Book.objects.get(id=id)
        data = request.data
        serializers = BookSerializer(book, data=data , partial = True)
        if serializers.is_valid():
            serializers.save()
            return Response({'message' : "your data updated Sucessfully" , "data" : serializers.data} , status=status.HTTP_200_OK)
        return Response({'message' : "Update your Data" , "data" : serializers.errors} , status=status.HTTP_400_BAD_REQUEST)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>DELETE BOOK<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
class BookDelete(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self, request , id=None):
        book = Book.objects.get(id=id)
        book.delete()
        return Response({'message' : "your Data Deleted"})

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>LEND BOOK<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
class LendBookView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        get_book_on = LendBook.objects.filter(user = request.user).values_list('issued_date',flat=True)[0]
        return_book_on = (datetime.date.today() - get_book_on.date())
        # dates = return_book_on.days
        dates=8
        print("🚀 ~ file: views.py ~ line 113 ~ dates", dates)
        student = LendBook.objects.filter(user= request.user)
        serializers = LendBookSerializer(student , many=True)
        fi = 30
        if dates > 7:
            a = dates - 7
            daily_fine = fi * a
            print("🚀 ~ file: views.py ~ line 119 ~ daily_fine", daily_fine)
            fine  = LendBook.objects.update(fine=daily_fine)
            return Response({'msg': 'please find the details of the student' , 'data': serializers.data })
        else:
            fine  = LendBook.objects.update(fine=0)
            return Response(serializers.data)
        # return Response({'msg': 'please enter correct data' })
            

    def post(self, request):
        data = request.data
        serializers = LendBookSerializer(data=data)
        book = request.data.get('book')
        user = list(LendBook.objects.filter(user=request.user).values_list('book_id',flat=True))
        # user = LendBook.objects.filter(user=request.user , book = request.data.get('book'))
        print("🚀 ~ file: views.py ~ line 131 ~ user", user)
        print("🚀 ~ file: views.py ~ line 131 ~ book", book)
        serializers.is_valid(raise_exception=True)    
        # if user:
        if book in user:
            return Response({'message' : 'you cannot added duplicate book'} , status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            tc = request.data.get('tc')
            if tc == True:  
                serializers.save(user=request.user)
                return Response({'msg': 'Ok !!!!!!! You can now take the book but You have to return it within 7 days otherwise You will be Penalized' , "data":serializers.data}, status=status.HTTP_200_OK)
            else:
                return Response({'msg' : 'You have to Select Terms and Condition Only True if you want to take the book'})





        

