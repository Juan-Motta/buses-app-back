from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from simple_history.models import HistoricalRecords


class UserManager(BaseUserManager):
    def _create_user(self, email, name, last_name, password, document, birth, phone, is_staff, is_superuser, **extra_fields):
        user = self.model(
            email=email,
            name=name,
            last_name=last_name,
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
        return self._create_user(email, name, last_name, password, document, birth, phone, False, False, **extra_fields)

    def create_superuser(self, email, name, last_name, document, birth, phone, password=None, **extra_fields):
        return self._create_user(email, name, last_name, password, document, birth, phone, True, True, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        'Correo Electrónico',
        max_length=255,
        unique=True,
        blank=False,
        null=False
    )
    name = models.CharField(
        'Nombres',
        max_length=255,
        blank=True,
        null=True
    )
    last_name = models.CharField(
        'Apellidos',
        max_length=255,
        blank=True,
        null=True
    )
    image = models.ImageField(
        'Imagen de perfil',
        upload_to='perfil/',
        max_length=255,
        null=True,
        blank=True
    )
    document = models.CharField(
        'Documento',
        max_length=50,
        unique=True,
        blank=True,
        null=True
    )
    birth = models.DateField(
        'Fecha de nacimiento (YYYY-MM-DD)',
        auto_now=False,
        auto_now_add=False,
        name=False,
        blank=True,
        null=True
    )
    phone = models.CharField(
        'Celular',
        max_length=50,
        unique=True,
        blank=True,
        null=True
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    historical = HistoricalRecords()
    objects = UserManager()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'last_name', 'document', 'birth', 'phone']

    def __str__(self):
        return f'{self.name} {self.last_name}'
