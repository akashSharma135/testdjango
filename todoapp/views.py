from .models import ManagerAssigned, NewUser
from .serializers import NewUserSerializer
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import authenticate
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class UserRegisterView(APIView):
    
        def post(self, request):
            try:
                user = NewUser.objects.create_user(
                    username = request.data.get('username'),
                    email = request.data.get('email'),
                    name = request.data.get('name'),
                    password = request.data.get('password'),
                    role = request.data.get('role'),
                    is_staff = request.data.get('is_staff'))
                
                user.save()
                
                if user is not None:
                    token = Token.objects.create(user=user)
                    print(token.key)
                    return Response(token.key, status=status.HTTP_200_OK)

                else:
                    return Response([], status=status.HTTP_400_BAD_REQUEST)

            except:
                return Response({"error": "username already taken"}, status=status.HTTP_400_BAD_REQUEST)
        
        
class LoginView(APIView):
    def post(self, request):
        user = authenticate(username=request.data.get("username"), password=request.data.get("password"))
        if user is not None:
            # A backend authenticated the credentials
            try:
                token = Token.objects.get(user=user)
            except Token.DoesNotExist:
                token = Token.objects.create(user=user)
            return Response(token.key)
        else:
            # No backend authenticated the credentials
            return Response([], status=status.HTTP_401_UNAUTHORIZED)
        
        
class ProfileView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self, request):
        ser = NewUserSerializer(request.user)
        return Response(ser.data)
    
    
class AllManagersView(APIView):
    permission_classes=[IsAdminUser]
    def get(self, request):
        try:
            users = NewUser.objects.filter(role='manager')
            serializer = NewUserSerializer(users, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except NewUser.DoesNotExist:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
class AllSimpleUserView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self, request):
        try:
            users = NewUser.objects.filter(role='user')
            serializer = NewUserSerializer(users, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except NewUser.DoesNotExist:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
class UserDetailView(APIView):
    permission_classes=[IsAdminUser]
    def get_object(self, pk):
        try:
            return NewUser.objects.get(pk=pk)
        except NewUser.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        user = self.get_object(pk=pk)
        serializer = NewUserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk, format=None):
        user = NewUser.objects.get(username=request.user)
        if user.is_superuser is False:
            return Response({"msg": "You do not have permission to perform delete operation"}, status=status.HTTP_400_BAD_REQUEST)
        user = self.get_object(pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class AssignManagerView(APIView):
    permission_classes=[IsAdminUser]
    def post(self, request):
        try:
            if request.user.role != 'admin':
                return Response({"msg": "You do not have permission to perform delete operation"}, status=status.HTTP_400_BAD_REQUEST)
            
            manager_username = request.data.get('manager_username')
            user_username = request.data.get('user_username')
            
            manager = NewUser.objects.filter(username=manager_username).first()
            user = NewUser.objects.filter(username=user_username).first()
            
            assigned = ManagerAssigned.objects.create(manager=manager, user=user)
            print(assigned)
            assigned.save()

            return Response({"msg": "manager assigned!"}, status=status.HTTP_200_OK)
        except:
            return Response({"error": "manager already assigned to this user!"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
 
 
# class AssignTaskView(APIView):
#     def post(self, request):
#         task_id = request.data.get('task_id')
        
#         print(ManagerAssigned.objects.get(user_id=7))
#         return Response("success")