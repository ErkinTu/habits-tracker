import uuid
from django.conf import settings
from django.db import models
from django.contrib.postgres.fields import ArrayField

class Habit(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="habits",
        db_index=True,
    )

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    importance = models.SmallIntegerField(default=3)
    weight = models.DecimalField(max_digits=6, decimal_places=2, default=1.00)

    start_date = models.DateField()
    archived_at = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=["user"]),
            models.Index(fields=["user", "archived_at"]),
            models.Index(fields=["user", "start_date"]),
        ]

    def __str__(self):
        return f"{self.title} ({self.user_id})"


class HabitSchedule(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    habit = models.OneToOneField(
        Habit,
        on_delete=models.CASCADE,
        related_name="schedule",
        db_index=True,
    )

    # PostgreSQL smallint[]
    # Позволяет хранить дни недели (например, [1, 3, 5])
    days_of_week = ArrayField(
        base_field=models.SmallIntegerField(),
        size=7,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Schedule({self.habit_id})"


class HabitCheckin(models.Model):
    class Status(models.TextChoices):
        DONE = "DONE", "Done"
        SKIPPED = "SKIPPED", "Skipped"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    habit = models.ForeignKey(
        Habit,
        on_delete=models.CASCADE,
        related_name="checkins",
        db_index=True,
    )

    date = models.DateField(db_index=True)
    status = models.CharField(max_length=16, choices=Status.choices, default=Status.DONE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            # Гарантирует, что на одну дату для одной привычки будет только одна запись
            models.UniqueConstraint(fields=["habit", "date"], name="uniq_habit_date"),
        ]
        indexes = [
            models.Index(fields=["habit", "date"]),
            models.Index(fields=["date"]),
        ]

    def __str__(self):
        return f"{self.habit_id} {self.date} {self.status}"