from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class User(AbstractUser):
    email = models.EmailField('Email', unique=True)
    is_verified = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    def __str__(self):
        return self.email


class UserProfile(models.Model):
    class JLPTLevel(models.TextChoices):
        N5 = "N5", "N5"
        N4 = "N4", "N4"
        N3 = "N3", "N3"
        N2 = "N2", "N2"
        N1 = "N1", "N1"

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    display_name = models.CharField(max_length=150, blank=True)
    jlpt_level = models.CharField(max_length=2, choices=JLPTLevel.choices, blank=True)
    target_date = models.DateField(null=True, blank=True)
    setup_complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Profile for {self.user.email}"


class PasswordResetRequest(models.Model):
    email = models.EmailField()
    token = models.CharField(max_length=128, unique=True)
    expires_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reset request for {self.email}"


class StudySession(models.Model):
    class Subject(models.TextChoices):
        GRAMMAR = "GR", "Grammar"
        KANJI = "KN", "Kanji"
        LISTENING = "LI", "Listening"
        READING = "RD", "Reading"
        VOCABULARY = "VO", "Vocabulary"

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sessions')
    subject = models.CharField(max_length=2, choices=Subject.choices)
    started_at = models.DateTimeField()
    ended_at = models.DateTimeField(null=True, blank=True)
    duration_minutes = models.PositiveIntegerField(null=True, blank=True)
    notes = models.TextField(blank=True, default='')

    def __str__(self):
        return f"{self.user.email} — {self.get_subject_display()}"


class SessionNote(models.Model):
    session = models.ForeignKey(StudySession, on_delete=models.CASCADE, related_name='session_notes')
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'session notes'

    def __str__(self):
        return f"Note for session {self.session.id}"