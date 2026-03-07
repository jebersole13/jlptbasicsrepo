from rest_framework import serializers
from .models import LearningLog, User, StudyChoices, UserSettings


class UserSerializer(serializers.ModelSerializer):
    password = serializers.RegexField(
        regex=[]
        write_only=True,
        error_messages={
            'invalid': 'Password must be at least 8 characters with one capital letter and one symbol'
        }
    )

    class Meta:
        model = User
        fields = ('email', 'password')

    def create(self, validated_data):
        # Creates user with hashed password
        # Sets username to UUID to satisfy AbstractUser's uniqueness requirement
        pass


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)


class ResetConfirmSerializer(serializers.Serializer):
    new_password = serializers.RegexField(
        regex=[],
        write_only=True,
        error_messages={
            'invalid': 'Password must be at least 8 characters with one capital letter and one symbol'
        }
    )
    confirm_password = serializers.CharField(write_only=True, required=True)


class LearningLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningLog
        fields = ['id', 'text', 'date_logged']


class StudyChoicesSerializer(serializers.ModelSerializer):
    topic_display = serializers.CharField(source='get_topic_display', read_only=True)
    student = serializers.PrimaryKeyRelatedField(read_only=True)
    learning_logs = LearningLogSerializer(many=True, read_only=True)

    class Meta:
        model = StudyChoices
        fields = ['id', 'student', 'topic', 'topic_display', 'date_studied', 'duration', 'notes', 'learning_logs']
        extra_kwargs = {
            'notes': {'required': False},
            'duration': {'required': False},
        }


class UserSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSettings
        fields = ['username', 'jlpt_level', 'next_test_date', 'has_completed_initial_setup']
        extra_kwargs = {
            'has_completed_initial_setup': {'read_only': True},
        }