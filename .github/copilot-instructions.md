# NAAS Portal - Copilot Instructions

## Project Overview
This is a Django web application for the **National Association of Ankpa Students (NAAS) National Body**.

## Technology Stack
- **Backend**: Django 4.2+
- **Frontend**: Bootstrap 5, HTML5, CSS3, JavaScript
- **Database**: SQLite (development), PostgreSQL (production recommended)
- **Image Processing**: Pillow, qrcode

## Project Structure
- `core/` - Homepage, about page, executives, contact
- `news/` - News posts, categories, comments
- `events/` - Events management with galleries
- `election/` - Election countdown, candidate management
- `members/` - Member registration, profiles, ID card generation
- `gallery/` - Photo albums and video embeds
- `administration/` - Admin dashboard extensions

## Key Features
- Member registration and authentication
- Digital ID card generation with QR codes
- Election countdown timer (December 26)
- News and events management
- Photo gallery and video embeds

## Development Commands
```bash
# Run development server
python manage.py runserver

# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser
```

## Color Theme
- Dark Green: #006400
- Gold: #DAA520
- White: #FFFFFF
