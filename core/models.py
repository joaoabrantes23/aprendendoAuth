from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from datetime import date

# Create your CustomUserManager here.
class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, role, nome, telefone, cpf_cnpj, data_nascimento, endereco, registroProfissional, **extra_fields):
        if not email:
            raise ValueError("Email must be provided")
        if not password:
            raise ValueError('Password is not provided')

        user = self.model(
            email = self.normalize_email(email),
            role = role,
            nome = nome,
            telefone = telefone,
            cpf_cnpj = cpf_cnpj,
            data_nascimento = data_nascimento,
            endereco = endereco,
            registroProfissional = registroProfissional,
            **extra_fields
        )
        
        user.set_password(password)
        user.save()
        return user

    def create_user(self, email, password, role, nome, telefone, cpf_cnpj, data_nascimento, endereco, registroProfissional, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',False)
        return self._create_user(email, password, role, nome, telefone, cpf_cnpj, data_nascimento, endereco, registroProfissional, **extra_fields)

    def create_superuser(self, email, password, role, nome, telefone, cpf_cnpj, data_nascimento, endereco, registroProfissional, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',True)
        return self._create_user(email, password, role, nome, telefone, cpf_cnpj, data_nascimento, endereco, registroProfissional, **extra_fields)

def upload_image_pessoa(instance, filename):
    return f"user_images/{instance.cpf_cnpj}/{filename}"

# Create your User Model here.
class User(AbstractBaseUser,PermissionsMixin):
    # Abstractbaseuser has password, last_login, is_active by default

    TYPE_CHOICES = (
        ('ADMINISTRADOR', 'Administrador'),
        ("COORDENADOR", "Coordenador"),
        ("SUPERVISOR", "Supervisor"),
        ("AVALIADOR", "Avaliador")
    )
    role = models.CharField(max_length=25, choices=TYPE_CHOICES, default="Avaliador")
    image_url = models.ImageField(upload_to = upload_image_pessoa, null = True, blank=True, default= 'media/admin_image/generic_profile.png')
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(max_length=150, unique=True)
    cpf_cnpj = models.CharField(max_length=20)
    data_nascimento = models.DateField(default=date.today)
    endereco = models.CharField(max_length = 255, blank=True, null=True)
    registroProfissional = models.CharField(max_length = 30, blank=True, null=True)

    is_staff = models.BooleanField(default=True) # must needed, otherwise you won't be able to loginto django-admin.
    is_active = models.BooleanField(default=True) # must needed, otherwise you won't be able to loginto django-admin.
    is_superuser = models.BooleanField(default=False) # this field we inherit from PermissionsMixin.

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome','telefone','role', 'cpf_cnpj', 'data_nascimento', 'endereco', 'registroProfissional']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'