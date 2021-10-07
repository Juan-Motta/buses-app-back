from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class UserManager(BaseUserManager):
    """Representacion del manager que contiene los metodos para realizar las consultas a la base de datos"""

    def _create_user(self, email, name, last_name, password, document, birth, phone, is_staff, is_superuser, **extra_fields):
        """Metodo que crea el registro de usuario en la base de datos"""
        user = self.model(
            name=name,
            last_name=last_name,
            email=email,
            document=document,
            birth=birth,
            phone=phone,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, email, name, last_name, document, birth, phone, password=None, **extra_fields):
        """Metodo que crea un usuario"""
        return self._create_user(email, name, last_name, password, document, birth, phone, False, False, **extra_fields)

    def create_superuser(self, email, name, last_name, document, birth, phone, password=None, **extra_fields):
        """Metodo que crea un superusuario"""
        return self._create_user(email, name, last_name, password, document, birth, phone, True, True, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """Representacion del modelo para Usuarios"""

    name = models.CharField(
        'Nombres',
        max_length=254,
    )

    last_name = models.CharField(
        'Apellidos',
        max_length=254,
    )

    email = models.EmailField(
        'Correo Electrónico',
        max_length=254,
        unique=True,
    )

    document = models.CharField(
        'Documento',
        max_length=50,
        unique=True,
    )

    birth = models.DateField(
        'Fecha de nacimiento (YYYY-MM-DD)',
        auto_now=False,
        auto_now_add=False,
    )

    phone = models.CharField(
        'Celular',
        max_length=50,
        unique=True,
    )

    is_active = models.BooleanField(
        default=True
    )

    is_staff = models.BooleanField(
        default=False
    )

    objects = UserManager()

    def save(self, **kwargs):
        self.name = self.name.upper()
        self.last_name = self.last_name.upper()
        super().save(*kwargs)

    class Meta:
        """Definicion de los Metadatos para el modelo de Usuarios"""
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'last_name', 'document', 'birth', 'phone']

    def __str__(self):
        """Representacion Unicode del Usuario"""
        return f'{self.name} {self.last_name} - {self.document} - {self.email}'
