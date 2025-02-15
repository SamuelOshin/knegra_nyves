# Generated by Django 5.1.2 on 2025-01-03 15:51

import multiselectfield.db.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_cartitem_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='color',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('#000000', 'Black'), ('#FFFFFF', 'White'), ('#FF0000', 'Red'), ('#00FF00', 'Green'), ('#0000FF', 'Blue'), ('#FFFF00', 'Yellow'), ('#FFA500', 'Orange'), ('#800080', 'Purple'), ('#FFC0CB', 'Pink'), ('#A52A2A', 'Brown'), ('#808080', 'Gray'), ('#00FFFF', 'Cyan'), ('#008000', 'Dark Green'), ('#FFD700', 'Gold'), ('#4B0082', 'Indigo'), ('#ADD8E6', 'Light Blue'), ('#800000', 'Maroon'), ('#000080', 'Navy'), ('#808000', 'Olive'), ('#FF4500', 'Orange Red'), ('#DA70D6', 'Orchid'), ('#EEE8AA', 'Pale Goldenrod'), ('#98FB98', 'Pale Green'), ('#AFEEEE', 'Pale Turquoise'), ('#DB7093', 'Pale Violet Red'), ('#FFEFD5', 'Papaya Whip'), ('#FFDAB9', 'Peach Puff'), ('#CD853F', 'Peru'), ('#FFC0CB', 'Pink'), ('#DDA0DD', 'Plum'), ('#B0E0E6', 'Powder Blue'), ('#BC8F8F', 'Rosy Brown'), ('#4169E1', 'Royal Blue'), ('#8B4513', 'Saddle Brown'), ('#FA8072', 'Salmon'), ('#F4A460', 'Sandy Brown'), ('#2E8B57', 'Sea Green'), ('#FFF5EE', 'Sea Shell'), ('#A0522D', 'Sienna'), ('#C0C0C0', 'Silver'), ('#87CEEB', 'Sky Blue'), ('#6A5ACD', 'Slate Blue'), ('#708090', 'Slate Gray'), ('#FFFAFA', 'Snow'), ('#00FF7F', 'Spring Green'), ('#4682B4', 'Steel Blue'), ('#D2B48C', 'Tan'), ('#008080', 'Teal'), ('#D8BFD8', 'Thistle'), ('#FF6347', 'Tomato'), ('#40E0D0', 'Turquoise'), ('#EE82EE', 'Violet'), ('#F5DEB3', 'Wheat'), ('#F5F5F5', 'White Smoke'), ('#9ACD32', 'Yellow Green')], max_length=439),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra Large'), ('2XL', 'Extra Extra Large'), ('6', 'Size 6'), ('7', 'Size 7'), ('8', 'Size 8'), ('9', 'Size 9'), ('10', 'Size 10'), ('11', 'Size 11'), ('12', 'Size 12')], max_length=29),
        ),
    ]
