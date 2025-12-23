from django.core.management.base import BaseCommand

from shop.models import Category, Product


class Command(BaseCommand):
    help = "Seed default categories and sample products."

    def handle(self, *args, **options):
        categories = [
            ('paintings', 'Paintings'),
            ('pencil', 'Pencil Drawings'),
            ('caricature', 'Caricatures'),
            ('stencil', 'Stencil Artworks'),
            ('mural', 'Kerala Mural'),
        ]
        created = 0
        for key, label in categories:
            cat, was_created = Category.objects.get_or_create(name=key, defaults={'description': label})
            if was_created:
                created += 1
        if created:
            self.stdout.write(self.style.SUCCESS(f'Created {created} categories'))
        if not Product.objects.exists():
            for idx, (key, label) in enumerate(categories, start=1):
                Product.objects.create(
                    title=f'Sample {label} #{idx}',
                    description=f'Beautiful {label.lower()} artwork.',
                    category=Category.objects.get(name=key),
                    price=1000 + idx * 100,
                    stock=5,
                    slug=f'sample-{key}-{idx}',
                )
            self.stdout.write(self.style.SUCCESS('Created sample products'))
        else:
            self.stdout.write('Products already exist; skipping samples.')



















