from django.db import migrations

class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0003_post_tags'),
    ]
    operations = [
        migrations.RunSQL('CREATE EXTENSION IF NOT EXISTS pg_trgm'),
    ]