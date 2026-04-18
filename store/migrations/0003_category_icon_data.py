from django.db import migrations


ICON_RULES = [
    # (từ khóa trong tên, fa class)
    ('để bàn',   'fa-solid fa-desktop'),
    ('xách tay', 'fa-solid fa-laptop'),
    ('bảng',     'fa-solid fa-tablet-screen-button'),
    ('màn hình', 'fa-solid fa-display'),
    ('loa',      'fa-solid fa-volume-high'),
    ('tai nghe', 'fa-solid fa-headphones'),
    ('chuột',    'fa-solid fa-computer-mouse'),
    ('bàn phím', 'fa-solid fa-keyboard'),
    ('gaming',   'fa-solid fa-gamepad'),
    ('pc',       'fa-solid fa-microchip'),
    ('linh kiện','fa-solid fa-microchip'),
    ('ổ cứng',   'fa-solid fa-hard-drive'),
    ('ram',      'fa-solid fa-memory'),
    ('nguồn',    'fa-solid fa-plug'),
    ('case',     'fa-solid fa-server'),
    ('vga',      'fa-solid fa-tv'),
    ('card',     'fa-solid fa-tv'),
    ('webcam',   'fa-solid fa-camera'),
    ('máy in',   'fa-solid fa-print'),
    ('usb',      'fa-solid fa-usb'),
    ('mạng',     'fa-solid fa-wifi'),
]


def assign_icons(apps, schema_editor):
    Category = apps.get_model('store', 'Category')
    for cat in Category.objects.all():
        name_lower = cat.name.lower()
        for keyword, icon_class in ICON_RULES:
            if keyword in name_lower:
                cat.icon = icon_class
                break
        else:
            cat.icon = 'fa-solid fa-tag'
        cat.save()


def reverse_icons(apps, schema_editor):
    Category = apps.get_model('store', 'Category')
    Category.objects.all().update(icon='fa-solid fa-tag')


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_category_icon'),
    ]

    operations = [
        migrations.RunPython(assign_icons, reverse_icons),
    ]
