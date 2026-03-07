# JLPT Countdown

Hello, everyone. This is a demo repository for JLPT Countdown. This is to show the basic logic and setup of the application for the web. It is still in active development, so this only a sample, and some functions stubbed for security purposes.

This application serves study tracker for the JLPT. Students can create timed study sessions, review their progress, and manage their progress until the day of the test.

Any recommendations, feature requests, or bugs can be reported here. Just make a PR on the README, and we will look into it.

Happy Studying!

**Live:** [jlptcountdown.com](https://jlptcountdown.com)

---

## Stack

| Layer | Tech |
|---|---|
| Frontend | Astro, Tailwind CSS, DaisyUI, TypeScript |
| Backend | Django, Django REST Framework |
| Database | PostgreSQL |
| Email | Mailgun (via django-anymail) |

---

## Features

- **Countdown timer** — tracks time until the next JLPT exam date (summer / winter)
- **Study session logging** — log sessions by topic (Grammar, Kanji, Vocabulary, Listening, Reading) with a built-in timer (free run, set time, or Pomodoro)
- **Progress dashboard** — visual progress bars per topic, study calendar with highlighted dates
- **Daily idiom** — a rotating Japanese idiom on the landing page

---

## Project Structure

```
/
├── frontend/          
│   ├── src/
│   │   ├── components/
│   │   ├── layouts/
│   │   ├── lib/           
│   │   ├── pages/
│   │   │   ├── login/
│   │   │   ├── registration/
│   │   │   ├── forgot/
│   │   │   ├── reset/
│   │   │   └── studypage/
│   │   │       ├── progressdashboard/
│   │   │       ├── study/
│   │   │       ├── logs/
│   │   │       └── settings/
│   │   └── styles/
│   └── astro.config.mts
│
└── backend/           
    ├── countdownstudent/
    │   ├── models.py
    │   ├── serializers.py
    │   ├── views.py
    │   ├── urls.py
    │   └── authentication.py  
    └── jlptcountdownstudy/
        ├── settings.py
        └── urls.py
```
