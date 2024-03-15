from django.db import migrations, models

def move_data(apps, schema_editor):
    Page = apps.get_model('pages', 'Page')
    Tutorial = apps.get_model('pages', 'Tutorial')
    Video = apps.get_model('pages', 'Video')

    for page in Page.objects.all():
        Tutorial.objects.create(content=page.content, page=page)
        Video.objects.create(video=page.video, page=page)

class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_page_type_video_tutorial'),
    ]
    operations = [
        migrations.RunPython(move_data)
    ]