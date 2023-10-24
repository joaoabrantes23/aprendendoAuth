from rest_framework import viewsets, status
from .models import User
from .serializers import UserSerializer
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        data = request.data
        user = User.objects.create(
            email=data['email'],
            role=data['role'],
            nome=data['nome'],
            telefone=data['telefone'],
            cpf_cnpj=data['cpf_cnpj'],
            data_nascimento=data['data_nascimento'],
            endereco=data['endereco'],
            registroProfissional=data['registroProfissional']
        )

        # Use set_password para definir a senha de forma segura
        user.set_password(data['password'])
        user.save()

        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
