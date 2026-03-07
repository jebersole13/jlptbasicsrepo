from django.urls import path
from countdownstudent import views

urlpatterns = [
    path('studycountdown/register/', views.account_registration, name='account_registration'),
    path('studycountdown/login/', views.account_login, name='account_login'),
    path('studycountdown/logout/', views.account_logout, name='account_logout'),
    path('studycountdown/token/refresh/', views.token_refresh, name='token_refresh'),
    path('studycountdown/password_forget/', views.password_forget, name='password_forget'),
    path('studycountdown/password_reset/', views.password_reset, name='password_reset'),
    path('studycountdown/student_choices/', views.student_choices, name='student_choices'),
    path('studycountdown/study_logs/', views.study_logs, name='study_logs'),
    path('studycountdown/study_logs/<int:log_id>/', views.study_log_detail, name='study_log_detail'),
    path('studycountdown/settings/', views.user_settings, name='user_settings'),
    path('studycountdown/study_statistics/', views.study_statistics, name='study_statistics'),
]