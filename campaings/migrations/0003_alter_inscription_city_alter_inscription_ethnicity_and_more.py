# Generated by Django 4.2.19 on 2025-02-07 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaings', '0002_alter_inscription_city_other_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscription',
            name='city',
            field=models.CharField(choices=[('BEL', 'Belford Roxo'), ('CDM', 'Cachoeiras de Macacu'), ('DUC', 'Duque de Caxias'), ('GUA', 'Guapimirim'), ('ITB', 'Itaboraí'), ('ITG', 'Itaguaí'), ('JAP', 'Japeri'), ('MAG', 'Magé'), ('MAR', 'Maricá'), ('MES', 'Mesquita'), ('NIL', 'Nilópolis'), ('NIT', 'Niterói'), ('NOI', 'Nova Iguaçu'), ('PAR', 'Paracambi'), ('PET', 'Petrópolis'), ('QUE', 'Queimados'), ('RIB', 'Rio Bonito'), ('RJ', 'Rio de Janeiro'), ('SAG', 'São Gonçalo'), ('SAJ', 'São João de Meriti'), ('SER', 'Seropédica'), ('TAN', 'Tanguá'), ('OUT', 'Outra')], default='RJ', help_text='Clique para selecionar', max_length=50, verbose_name='city'),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='ethnicity',
            field=models.CharField(choices=[('AMA', 'Amarelo (oriental)'), ('BRA', 'Branca'), ('IND', 'Indígena (oriundos de comunidades indígenas, aldeadas ou urbanas)'), ('PAR', 'Parda (negra de pele clara)'), ('PRE', 'Preta (negra de pele escura)'), ('OUT', 'Outra')], default='OUT', help_text='Clique para selecionar', max_length=50, verbose_name='etinia'),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='frequency',
            field=models.CharField(choices=[('DAY', 'Diariamente'), ('WEK', 'Semanalmente'), ('MON', 'Pelo menos uma vez por mês'), ('RAR', 'Raramente desenho')], default='MON', help_text='Clique para selecionar', max_length=50, verbose_name='frequencia'),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='gender',
            field=models.CharField(choices=[('MC', 'Mulher cis'), ('MT', 'Mulher trans'), ('HC', 'Homem cis'), ('HT', 'Homem trans'), ('NB', 'Não binário'), ('OUT', 'Outra')], default='MC', help_text='Clique para selecionar', max_length=50, verbose_name='genero'),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='knowloge',
            field=models.CharField(choices=[('JR', 'Jornais/revistas '), ('SI', 'Sites'), ('FA', 'Facebook'), ('IN', 'Instagram'), ('YT', 'YouTube'), ('TK', 'Tik Tok '), ('TT', 'Twitter'), ('ES', 'Escola'), ('MAI', 'E-mail'), ('WP', 'WhatsApp'), ('OT', 'Outros')], default='OT', help_text='Clique para selecionar', max_length=50, verbose_name='conhecia'),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='prior_inscription',
            field=models.CharField(choices=[('2012', '2012 '), ('2013', '2013 '), ('2014', '2014 '), ('2015', '2015 '), ('2016', '2016 '), ('2017', '2017 '), ('2018', '2018 '), ('2019', '2019 '), ('2020', '2020 '), ('2021', '2021 '), ('2022', '2022 '), ('2023', '2023 '), ('2024', '2024 ')], default='2012', help_text='Clique para selecionar', max_length=50, verbose_name='conhecia'),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='scholl_level',
            field=models.CharField(choices=[('EFIPU', 'Ensino Fundamental incompleto em escola pública'), ('EFIPR', 'Ensino Fundamental incompleto em escola particular'), ('EFCPU', 'Ensino Fundamental completo em escola pública'), ('EFCPR', 'Ensino Fundamental completo em escola particular'), ('EMIPU', 'Ensino Médio incompleto em escola pública'), ('EMIPR', 'Ensino Médio incompleto em escola particular'), ('EMCPU', 'Ensino Médio completo em escola pública'), ('EMCPR', 'Ensino Médio completo em escola particular'), ('ESIPU', 'Ensino superior incompleto em instituição pública'), ('ESIPR', 'Ensino superior incompleto em instituição particular'), ('ESCPU', 'Ensino superior completo em instituição pública'), ('ESCPR', 'Ensino superior completo em instituição particular')], default='EFIPU', help_text='NÍVEL DE ESCOLARIDADE:', max_length=50, verbose_name='escolaridade'),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='studing',
            field=models.CharField(choices=[('MAN', 'manhã'), ('TAR', 'tarde'), ('NOI', 'noite'), ('INT', 'integral')], default='MAN', help_text='SE ESTIVER ESTUDANDO NESTE ANO, INFORME SÉRIE / PERÍODO:', max_length=50, verbose_name='período'),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='tablet',
            field=models.CharField(choices=[('OK', 'Estou tranquilo(a)! Já faço uso da tablet e estou confortável com isso.'), ('EX', 'Estou animado (a) para aprender mais! Sei utilizar um pouco da tablet mas ainda não domino completamente o uso.'), ('NBW', 'Nunca usei mas quero aprender!'), ('NO', 'Nunca usei e não quero aprender a usar.')], default='OK', help_text='Clique para selecionar', max_length=50, verbose_name='tablet'),
        ),
    ]
