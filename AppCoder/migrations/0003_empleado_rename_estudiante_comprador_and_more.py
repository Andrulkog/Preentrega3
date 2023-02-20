# Generated by Django 4.1.7 on 2023-02-20 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0002_alter_curso_camada'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.RenameModel(
            old_name='Estudiante',
            new_name='Comprador',
        ),
        migrations.RenameModel(
            old_name='Entregable',
            new_name='Medicamento',
        ),
        migrations.RenameModel(
            old_name='Curso',
            new_name='Producto',
        ),
        migrations.DeleteModel(
            name='Profesor',
        ),
        migrations.RenameField(
            model_name='medicamento',
            old_name='fechaDeEntrega',
            new_name='fechaDeVencimiento',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='camada',
            new_name='codigo',
        ),
    ]
