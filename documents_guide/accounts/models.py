from django.contrib.auth.models import AbstractUser, BaseUserManager, Group, Permission
from django.db import models

class UserProfileManager(BaseUserManager):
    """
    Kullanıcı modelini yönetmek için özel bir manager sınıfı.
    """
    def create_user(self, email, first_name, last_name, password=None, **extra_fields):
        """
        Yeni bir kullanıcı oluşturur ve kaydeder.
        """
        if not email:
            raise ValueError("Kullanıcının e-posta adresi zorunludur.")
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password=None, **extra_fields):
        """
        Süper kullanıcı oluşturur.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, first_name, last_name, password, **extra_fields)


class UserProfile(AbstractUser):
    """
    Proje için özelleştirilmiş kullanıcı profili modeli.
    """
    email = models.EmailField(unique=True)  # E-posta adresi benzersiz olacak
    first_name = models.CharField(max_length=30)  # İsim
    last_name = models.CharField(max_length=30)  # Soyisim
    is_verified = models.BooleanField(default=False)  # E-posta doğrulama durumu

    # USERNAME_FIELD ve REQUIRED_FIELDS'ı güncelleyeceğiz.
    USERNAME_FIELD = 'email'  # Kullanıcı adı olarak e-posta kullanılacak
    REQUIRED_FIELDS = ['first_name', 'last_name']  # Manuel üye olma sırasında zorunlu alanlar

    # groups ve user_permissions için related_name ekliyoruz
    groups = models.ManyToManyField(
        Group,
        related_name='userprofile_groups',  # Farklı ilişkilerle çakışmayı engellemek için
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='userprofile_permissions',  # Farklı ilişkilerle çakışmayı engellemek için
        blank=True,
    )

    objects = UserProfileManager()  # Kullanıcıyı yönetmek için özel manager

    def __str__(self):
        return self.email


class UserProfileDetails(models.Model):
    """
    Kullanıcı bilgileri ile ilgili ek alanlar ve ilişkiler.
    """
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)  # UserProfile ile ilişkilendirildi
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"Profile of {self.user.email}"
