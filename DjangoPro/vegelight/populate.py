import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vegelight.settings')
django.setup()

from delivery.models import Restaurant, Item

def populate():
    print("Populating databases...")

    # Restaurant 1
    r1, _ = Restaurant.objects.get_or_create(
        name="The Golden Spoon",
        defaults={
            'picture': 'https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?auto=format&fit=crop&q=80&w=800',
            'cuisine': 'Fine Dining & Continental',
            'rating': 4.9
        }
    )

    Item.objects.get_or_create(
        restaurant=r1,
        name="Truffle Risotto",
        defaults={
            'description': 'Creamy arborio rice with wild mushrooms and black truffle shavings.',
            'price': 24.99,
            'vegeterian': True,
            'picture': 'https://images.unsplash.com/photo-1476124369491-e7addf5db371?auto=format&fit=crop&q=80&w=800'
        }
    )

    Item.objects.get_or_create(
        restaurant=r1,
        name="Wagyu Steak",
        defaults={
            'description': 'Premium A5 Wagyu beef served with garlic herb butter and asparagus.',
            'price': 89.99,
            'vegeterian': False,
            'picture': 'https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&q=80&w=800'
        }
    )

    # Restaurant 2
    r2, _ = Restaurant.objects.get_or_create(
        name="Spice Route",
        defaults={
            'picture': 'https://images.unsplash.com/photo-1552566626-52f8b828add9?auto=format&fit=crop&q=80&w=800',
            'cuisine': 'Authentic Indian',
            'rating': 4.7
        }
    )

    Item.objects.get_or_create(
        restaurant=r2,
        name="Paneer Butter Masala",
        defaults={
            'description': 'Soft paneer cubes simmered in a rich tomato and butter gravy.',
            'price': 14.50,
            'vegeterian': True,
            'picture': 'https://images.unsplash.com/photo-1631452180519-c014fe946bc0?auto=format&fit=crop&q=80&w=800'
        }
    )

    Item.objects.get_or_create(
        restaurant=r2,
        name="Chicken Tikka Masala",
        defaults={
            'description': 'Roasted marinated chicken chunks in a spiced curry sauce.',
            'price': 16.50,
            'vegeterian': False,
            'picture': 'https://images.unsplash.com/photo-1565557623262-b51c2513a641?auto=format&fit=crop&q=80&w=800'
        }
    )

    # Restaurant 3
    r3, _ = Restaurant.objects.get_or_create(
        name="Zen Sushi Bar",
        defaults={
            'picture': 'https://images.unsplash.com/photo-1579027989536-b7b1f875659b?auto=format&fit=crop&q=80&w=800',
            'cuisine': 'Japanese Sushi & Sashimi',
            'rating': 4.8
        }
    )

    Item.objects.get_or_create(
        restaurant=r3,
        name="Dragon Roll",
        defaults={
            'description': 'Eel and cucumber topped with avocado and sweet eel sauce.',
            'price': 18.00,
            'vegeterian': False,
            'picture': 'https://images.unsplash.com/photo-1579871494447-9811cf80d66c?auto=format&fit=crop&q=80&w=800'
        }
    )

    Item.objects.get_or_create(
        restaurant=r3,
        name="Vegetable Tempura",
        defaults={
            'description': 'Lightly battered and crispy fried assorted seasonal vegetables.',
            'price': 12.00,
            'vegeterian': True,
            'picture': 'https://images.unsplash.com/photo-1615486171346-63d1ed7f0c5a?auto=format&fit=crop&q=80&w=800'
        }
    )

    print("Successfully populated databases with hotels and menus!")

if __name__ == '__main__':
    populate()
