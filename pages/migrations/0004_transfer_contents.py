from django.db import migrations
from django.utils import timezone

def move_data(apps, schema_editor):
    Page = apps.get_model('pages', 'Page')
    Tutorial = apps.get_model('pages', 'Tutorial')
    Video = apps.get_model('pages', 'Video')

    tutorials = []
    videos = []

    for page in Page.objects.all():
        tutorials.append(Tutorial(content=page.content, page=page))
        videos.append(Video(video=page.video, page=page))

    Tutorial.objects.bulk_create(tutorials)
    Video.objects.bulk_create(videos)

class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_page_type_video_tutorial'),
    ]
    operations = [
        migrations.RunPython(move_data),

    ]
