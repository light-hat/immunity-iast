# Generated by Django 5.1.3 on 2024-12-24 15:15

import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Context",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("vulnerable", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "Контекст выполнения",
                "verbose_name_plural": "Контексты выполнения",
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="DatasetLabel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.TextField()),
                ("label", models.CharField(max_length=255)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "Метка датасета",
                "verbose_name_plural": "Метки датасетов",
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True)),
                (
                    "language",
                    models.CharField(choices=[("python", "Python")], max_length=255),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("last_online", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "Приложение",
                "verbose_name_plural": "Приложения",
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, verbose_name="email address"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "role",
                    models.CharField(
                        choices=[
                            ("admin", "Системный администратор"),
                            ("analyst", "DevSecOps-аналитик"),
                            ("data_engineer", "Инженер по разметке"),
                        ],
                        max_length=13,
                        verbose_name="Роль",
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True, related_name="custom_user_groups", to="auth.group"
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        related_name="custom_user_permissions",
                        to="auth.permission",
                    ),
                ),
            ],
            options={
                "verbose_name": "Пользователь",
                "verbose_name_plural": "Пользователи",
                "ordering": ["-id"],
            },
        ),
        migrations.CreateModel(
            name="Event",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("timestamp", models.DateTimeField()),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("function_call", "Function Call"),
                            ("code_execution", "Code Execution"),
                            ("return_function", "Return Function"),
                            ("error", "Error"),
                        ],
                        max_length=20,
                    ),
                ),
                ("external_call", models.BooleanField(default=False)),
                ("func_name", models.CharField(blank=True, max_length=255, null=True)),
                ("module", models.CharField(blank=True, max_length=255, null=True)),
                ("filename", models.CharField(blank=True, max_length=255, null=True)),
                ("line", models.IntegerField(blank=True, null=True)),
                ("args", models.JSONField(blank=True, null=True)),
                ("code", models.TextField(blank=True, null=True)),
                (
                    "exception_type",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("exception_message", models.TextField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "context",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.context"
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.project"
                    ),
                ),
            ],
            options={
                "verbose_name": "Событие",
                "verbose_name_plural": "События",
                "ordering": ["-created_at"],
            },
        ),
        migrations.AddField(
            model_name="context",
            name="project",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="core.project"
            ),
        ),
        migrations.CreateModel(
            name="Request",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("method", models.CharField(max_length=255)),
                ("path", models.CharField(max_length=255)),
                ("body", models.TextField()),
                ("headers", models.TextField()),
                ("user", models.CharField(max_length=255)),
                ("get_params", models.TextField()),
                ("post_params", models.TextField()),
                ("cookies", models.TextField()),
                ("files", models.TextField()),
                ("meta", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "context",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.context"
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.project"
                    ),
                ),
            ],
            options={
                "verbose_name": "Запрос",
                "verbose_name_plural": "Запросы",
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="Response",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("status_code", models.CharField(max_length=255)),
                ("headers", models.TextField()),
                ("body", models.TextField()),
                ("content_type", models.CharField(max_length=255)),
                (
                    "content_length",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("charset", models.CharField(blank=True, max_length=255, null=True)),
                ("version", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "reason_phrase",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("cookies", models.TextField()),
                ("streaming", models.CharField(blank=True, max_length=255, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                (
                    "context",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.context"
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.project"
                    ),
                ),
            ],
            options={
                "verbose_name": "Ответ",
                "verbose_name_plural": "Ответы",
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="Vulnerability",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("type", models.CharField(max_length=50)),
                ("cwe", models.CharField(max_length=50)),
                ("description", models.TextField()),
                ("evidence", models.TextField()),
                ("detected_at", models.DateTimeField(auto_now_add=True)),
                (
                    "context",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.context"
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.project"
                    ),
                ),
            ],
            options={
                "verbose_name": "Уязвимость",
                "verbose_name_plural": "Уязвимости",
                "ordering": ["-detected_at"],
            },
        ),
    ]
