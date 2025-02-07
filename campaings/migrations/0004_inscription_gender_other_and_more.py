# Generated by Django 4.2.19 on 2025-02-07 09:40

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('campaings', '0003_alter_inscription_city_alter_inscription_ethnicity_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='inscription',
            name='gender_other',
            field=models.CharField(blank=True, help_text='em casa de outro:', max_length=80, null=True, verbose_name='genero_outro'),
        ),
        migrations.AddField(
            model_name='inscription',
            name='prior_course_year',
            field=models.CharField(blank=True, max_length=50, verbose_name='curso_anterior'),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='age',
            field=models.CharField(default='15', help_text='Clique para selecionar', max_length=50, verbose_name='idade'),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='city',
            field=models.CharField(default='RJ', help_text='Clique para selecionar', max_length=50, verbose_name='city'),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='dedication',
            field=models.CharField(max_length=50, verbose_name='dedicação'),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='deficincy',
            field=models.CharField(max_length=50, verbose_name='deficiente'),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='ethnicity',
            field=models.CharField(blank=True, default='OUT', help_text='Clique para selecionar', max_length=50, null=True, verbose_name='etinia'),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='frequency',
            field=models.CharField(default='MON', help_text='Clique para selecionar', max_length=50, verbose_name='frequencia'),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='intern',
            field=models.CharField(max_length=50, verbose_name='Estágio'),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='knowloge',
            field=models.CharField(default='outros', help_text='Clique para selecionar', max_length=50, verbose_name='conhecia'),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='likes_to_draw',
            field=models.CharField(max_length=50, verbose_name='desenha'),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='looking_work',
            field=models.CharField(max_length=50, verbose_name='trabalho'),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='parent_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=50, region=None, verbose_name='Telefone'),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='prior_course',
            field=models.CharField(blank=True, max_length=50, verbose_name='curso_anterior'),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='prior_inscription',
            field=models.CharField(default='2012', help_text='Clique para selecionar', max_length=50, verbose_name='conhecia'),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='scholl_level',
            field=models.CharField(default='', help_text='NÍVEL DE ESCOLARIDADE:', max_length=50, verbose_name='escolaridade'),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='special_need',
            field=models.CharField(max_length=50, verbose_name='cuidado_especial'),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='studing',
            field=models.CharField(default='MAN', help_text='SE ESTIVER ESTUDANDO NESTE ANO, INFORME SÉRIE / PERÍODO:', max_length=50, verbose_name='período'),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='tablet',
            field=models.CharField(default='OK', help_text='Clique para selecionar', max_length=50, verbose_name='tablet'),
        ),
    ]
