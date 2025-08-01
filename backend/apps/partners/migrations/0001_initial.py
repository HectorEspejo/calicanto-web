# Generated by Django 5.2.3 on 2025-07-25 10:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('proyectos', '0002_make_short_description_optional'),
    ]

    operations = [
        migrations.CreateModel(
            name='PartnerCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('slug', models.SlugField(blank=True, max_length=100, unique=True)),
                ('description', models.TextField(blank=True, verbose_name='Descripción')),
                ('order', models.IntegerField(default=0, verbose_name='Orden de visualización')),
                ('is_active', models.BooleanField(default=True, verbose_name='Activa')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Categoría de Partner',
                'verbose_name_plural': 'Categorías de Partners',
                'ordering': ['order', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nombre')),
                ('slug', models.SlugField(blank=True, max_length=200, unique=True)),
                ('partner_type', models.CharField(choices=[('company', 'Empresa'), ('ngo', 'ONG'), ('cooperative', 'Cooperativa'), ('foundation', 'Fundación'), ('association', 'Asociación'), ('public', 'Entidad Pública'), ('other', 'Otro')], default='company', max_length=20, verbose_name='Tipo de entidad')),
                ('description', models.TextField(verbose_name='Descripción')),
                ('mission', models.TextField(blank=True, help_text='Misión o propósito de la organización', verbose_name='Misión')),
                ('contact_person', models.CharField(blank=True, max_length=100, verbose_name='Persona de contacto')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('phone', models.CharField(blank=True, max_length=20, verbose_name='Teléfono')),
                ('website', models.URLField(blank=True, verbose_name='Sitio web')),
                ('address', models.CharField(blank=True, max_length=200, verbose_name='Dirección')),
                ('city', models.CharField(max_length=100, verbose_name='Ciudad')),
                ('province', models.CharField(max_length=100, verbose_name='Provincia')),
                ('postal_code', models.CharField(blank=True, max_length=10, verbose_name='Código postal')),
                ('linkedin', models.URLField(blank=True, verbose_name='LinkedIn')),
                ('twitter', models.URLField(blank=True, verbose_name='Twitter/X')),
                ('facebook', models.URLField(blank=True, verbose_name='Facebook')),
                ('instagram', models.URLField(blank=True, verbose_name='Instagram')),
                ('collaboration_areas', models.TextField(blank=True, help_text='Una por línea. Ej: Arquitectura sostenible, Financiación, etc.', verbose_name='Áreas de colaboración')),
                ('collaboration_start', models.DateField(blank=True, null=True, verbose_name='Inicio de colaboración')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='partners/logos/', verbose_name='Logotipo')),
                ('featured_image', models.ImageField(blank=True, null=True, upload_to='partners/images/', verbose_name='Imagen destacada')),
                ('is_featured', models.BooleanField(default=False, help_text='Mostrar en la página principal', verbose_name='Destacado')),
                ('is_active', models.BooleanField(default=True, verbose_name='Activo')),
                ('order', models.IntegerField(default=0, verbose_name='Orden de visualización')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='partners', to='partners.partnercategory', verbose_name='Categoría')),
            ],
            options={
                'verbose_name': 'Partner',
                'verbose_name_plural': 'Partners',
                'ordering': ['-is_featured', 'order', 'name'],
            },
        ),
        migrations.CreateModel(
            name='PartnerProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(help_text='Ej: Financiación, Arquitectura, Construcción, etc.', max_length=200, verbose_name='Rol en el proyecto')),
                ('description', models.TextField(blank=True, verbose_name='Descripción de la colaboración')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Fecha de inicio')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='Fecha de finalización')),
                ('is_active', models.BooleanField(default=True, verbose_name='Activa')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partner_projects', to='partners.partner', verbose_name='Partner')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partner_collaborations', to='proyectos.project', verbose_name='Proyecto')),
            ],
            options={
                'verbose_name': 'Colaboración en Proyecto',
                'verbose_name_plural': 'Colaboraciones en Proyectos',
                'ordering': ['-start_date'],
            },
        ),
        migrations.CreateModel(
            name='PartnerTestimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100, verbose_name='Autor')),
                ('role', models.CharField(max_length=100, verbose_name='Cargo')),
                ('content', models.TextField(verbose_name='Contenido')),
                ('is_active', models.BooleanField(default=True, verbose_name='Activo')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='testimonials', to='partners.partner', verbose_name='Partner')),
            ],
            options={
                'verbose_name': 'Testimonio',
                'verbose_name_plural': 'Testimonios',
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddIndex(
            model_name='partner',
            index=models.Index(fields=['partner_type', 'is_active'], name='partners_pa_partner_5eb2e7_idx'),
        ),
        migrations.AddIndex(
            model_name='partner',
            index=models.Index(fields=['is_featured', 'is_active'], name='partners_pa_is_feat_b86a05_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='partnerproject',
            unique_together={('partner', 'project')},
        ),
    ]
