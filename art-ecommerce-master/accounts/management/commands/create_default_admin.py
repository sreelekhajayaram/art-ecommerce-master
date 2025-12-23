from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create default admin user if missing."

    def handle(self, *args, **options):
        User = get_user_model()
        email = 'admin123@gmail.com'
        username = email
        password = 'admin@123'
        user_qs = User.objects.filter(email__iexact=email)
        if user_qs.exists():
            user = user_qs.first()
            try:
                user.set_password(password)
                user.is_staff = True
                user.is_superuser = True
                user.username = username
                user.save()
                self.stdout.write(self.style.SUCCESS(f'Updated password for existing admin user {user.username}'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Failed to update existing admin user: {e}'))
            return

        try:
            user = User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f'Created admin user {user.username}'))
        except TypeError:
            # Fallback if custom user model uses email as USERNAME_FIELD
            user = User.objects.create_superuser(email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f'Created admin user {getattr(user, "username", email)}'))



