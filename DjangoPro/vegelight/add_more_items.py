import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vegelight.settings')
django.setup()

from delivery.models import Restaurant, Item

def add_items():
    print("Adding more veg items to menus...")

    # Green Leaf Cafe
    try:
        r_green = Restaurant.objects.get(name="Green Leaf Cafe")
        Item.objects.get_or_create(
            restaurant=r_green,
            name="Mango Kale Smoothie Bowl",
            defaults={
                'description': 'Fresh kale and mango blended smooth, topped with chia seeds and granola.',
                'price': 12.50,
                'vegeterian': True,
                'picture': 'https://images.unsplash.com/photo-1494597564530-871f2b93ac55?auto=format&fit=crop&q=80&w=800'
            }
        )
        Item.objects.get_or_create(
            restaurant=r_green,
            name="Vegan Wrap",
            defaults={
                'description': 'Whole wheat wrap stuffed with hummus, mixed greens, and roasted peppers.',
                'price': 9.50,
                'vegeterian': True,
                'picture': 'https://images.unsplash.com/photo-1628840042765-356cda07504e?auto=format&fit=crop&q=80&w=800'
            }
        )
    except Restaurant.DoesNotExist:
        pass

    # Govinda's Pure Veg
    try:
        r_govinda = Restaurant.objects.get(name="Govinda's Pure Veg")
        Item.objects.get_or_create(
            restaurant=r_govinda,
            name="Palak Paneer",
            defaults={
                'description': 'Fresh spinach puree cooked with soft paneer cubes and mild spices.',
                'price': 12.00,
                'vegeterian': True,
                'picture': 'https://images.unsplash.com/photo-1601050690597-df0568f70950?auto=format&fit=crop&q=80&w=800'
            }
        )
        Item.objects.get_or_create(
            restaurant=r_govinda,
            name="Veg Biryani",
            defaults={
                'description': 'Aromatic basmati rice cooked with mixed vegetables and rich spices.',
                'price': 14.00,
                'vegeterian': True,
                'picture': 'https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8?auto=format&fit=crop&q=80&w=800'
            }
        )
    except Restaurant.DoesNotExist:
        pass

    # The Golden Spoon
    try:
        r_golden = Restaurant.objects.get(name="The Golden Spoon")
        Item.objects.get_or_create(
            restaurant=r_golden,
            name="Mushroom Ravioli",
            defaults={
                'description': 'Handmade ravioli stuffed with ricotta and wild mushrooms in garlic butter sauce.',
                'price': 19.50,
                'vegeterian': True,
                'picture': 'https://images.unsplash.com/photo-1588013273468-315fd88ea34c?auto=format&fit=crop&q=80&w=800'
            }
        )
    except Restaurant.DoesNotExist:
        pass

    # Spice Route
    try:
        r_spice = Restaurant.objects.get(name="Spice Route")
        Item.objects.get_or_create(
            restaurant=r_spice,
            name="Chana Masala",
            defaults={
                'description': 'Spicy and tangy chickpea curry served with bhatura.',
                'price': 11.50,
                'vegeterian': True,
                'picture': 'https://images.unsplash.com/photo-1606850025988-75c1a7051ce9?auto=format&fit=crop&q=80&w=800'
            }
        )
    except Restaurant.DoesNotExist:
        pass

    print("Added new items successfully!")

if __name__ == '__main__':
    add_items()
