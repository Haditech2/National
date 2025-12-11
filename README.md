# NAAS Portal

**National Association of Ankpa Students (National Body) - Official Web Portal**

A comprehensive Django web application for managing the NAAS organization, featuring member registration, digital ID card generation, news management, event scheduling, election countdown, and photo galleries.

## Features

### 🏠 Core Features
- Modern responsive homepage with Bootstrap 5
- About page with organization information
- Executive members showcase
- Contact page with social links

### 📰 News Module
- CRUD operations for news articles
- Category-based organization
- Search functionality
- Featured posts
- Pagination support

### 📅 Events Module
- Event management with date/time/venue
- Automatic classification (upcoming/past)
- Event photo galleries
- Rich text descriptions

### 🗳️ Election Module
- Fixed election date: December 26 (current year)
- Real-time countdown timer
- Candidate management with manifestos
- Position-based candidate listing

### 👥 Members Module
- User registration and authentication
- Complete profile management
- **Digital ID Card Generation** (PNG format)
- QR code for member verification
- Password reset functionality

### 🖼️ Gallery Module
- Photo albums with multiple images
- YouTube video embeds
- Grid layout display

## Installation

### Prerequisites
- Python 3.10+
- pip (Python package manager)

### Setup Steps

1. **Clone or navigate to the project directory**
   ```bash
   cd naas_portal
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install django pillow qrcode
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Main site: http://localhost:8000
   - Admin panel: http://localhost:8000/admin

## Default Admin Credentials
- **Username**: admin
- **Password**: admin123

⚠️ **Important**: Change these credentials in production!

## Project Structure

```
naas_portal/
├── core/               # Homepage, about, contact, executives
├── news/               # News articles and categories
├── events/             # Event management
├── election/           # Election and candidates
├── members/            # Member registration and ID cards
├── gallery/            # Photo albums and videos
├── administration/     # Admin extensions
├── templates/          # HTML templates
├── static/             # CSS, JS, images
│   ├── css/style.css
│   └── js/countdown.js
├── media/              # User uploads
└── manage.py
```

## Color Theme

| Color | Hex Code | Usage |
|-------|----------|-------|
| Dark Green | #006400 | Primary color |
| Gold | #DAA520 | Accent color |
| White | #FFFFFF | Background |

## ID Card System

Members can generate digital ID cards featuring:
- Passport photograph
- Full name and membership ID (NAAS-ANKPA-YYYY-NNNN)
- School, department, level, chapter
- QR code linking to verification URL

## API Endpoints

| URL | Description |
|-----|-------------|
| `/` | Homepage |
| `/about/` | About page |
| `/contact/` | Contact page |
| `/executives/` | Executive members |
| `/news/` | News listing |
| `/events/` | Events listing |
| `/election/` | Election info |
| `/election/candidates/` | Candidate listing |
| `/members/register/` | Member registration |
| `/members/login/` | Member login |
| `/members/dashboard/` | Member dashboard |
| `/members/id-card/` | Download ID card |
| `/gallery/` | Photo albums |
| `/admin/` | Admin panel |

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is developed for the National Association of Ankpa Students.

## Contact

- **Email**: info@naas.org.ng
- **Website**: [NAAS Portal](http://localhost:8000)

---

*Built with ❤️ for NAAS National Body*
