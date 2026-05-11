import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vegelight.settings')
django.setup()

from delivery.models import Restaurant, Item

def update_db():
    print("Deleting non-veg items...")
    Item.objects.filter(vegeterian=False).delete()

    print("Deleting empty restaurants...")
    # Find restaurants with 0 items
    for restaurant in Restaurant.objects.all():
        if restaurant.items.count() == 0:
            print(f"Deleting empty restaurant: {restaurant.name}")
            restaurant.delete()

    print("Adding new purely vegetarian restaurants...")
    
    # New Veg Restaurant 1
    r4, _ = Restaurant.objects.get_or_create(
        name="Green Leaf Cafe",
        defaults={
            'picture': 'https://images.unsplash.com/photo-1555396273-367ea4eb4db5?auto=format&fit=crop&q=80&w=800',
            'cuisine': 'Healthy Salads & Bowls',
            'rating': 4.8
        }
    )

    Item.objects.get_or_create(
        restaurant=r4,
        name="Quinoa Buddha Bowl",
        defaults={
            'description': 'Roasted sweet potatoes, avocado, chickpeas, and quinoa with tahini dressing.',
            'price': 15.00,
            'vegeterian': True,
            'picture': 'https://images.unsplash.com/photo-1512621776951-a57141f2eefd?auto=format&fit=crop&q=80&w=800'
        }
    )

    Item.objects.get_or_create(
        restaurant=r4,
        name="Avocado Toast",
        defaults={
            'description': 'Smashed avocado on sourdough with cherry tomatoes and microgreens.',
            'price': 10.50,
            'vegeterian': True,
            'picture': 'https://images.unsplash.com/photo-1541519227354-08fa5d50c44d?auto=format&fit=crop&q=80&w=800'
        }
    )

    # New Veg Restaurant 2
    r5, _ = Restaurant.objects.get_or_create(
        name="Govinda's Pure Veg",
        defaults={
            'picture': 'https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?auto=format&fit=crop&q=80&w=800',
            'cuisine': 'Authentic Indian Thali',
            'rating': 4.6
        }
    )

    Item.objects.get_or_create(
        restaurant=r5,
        name="Deluxe Thali",
        defaults={
            'description': 'A massive platter featuring paneer, dal makhani, 3 rotis, rice, and sweet gulab jamun.',
            'price': 18.00,
            'vegeterian': True,
            'picture': 'https://images.unsplash.com/photo-1546833999-b9f581a1996d?auto=format&fit=crop&q=80&w=800'
        }
    )
    
    Item.objects.get_or_create(
        restaurant=r5,
        name="Masala Dosa",
        defaults={
            'description': 'Crispy crepe made from rice and lentils filled with spiced potatoes.',
            'price': 8.50,
            'vegeterian': True,
            'picture': 'https://images.unsplash.com/photo-1589301760014-d929f39ce9b0?auto=format&fit=crop&q=80&w=800'
        }
    )

    print("Database update complete!")

if __name__ == '__main__':
    update_db()
