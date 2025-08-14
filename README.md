# SHPE UVA Website

Before you begin, make sure you have these installed on your computer:

- **Python 3.10 or higher** - [Download from python.org](https://www.python.org/downloads/)
- **Git** - [Download from git-scm.com](https://git-scm.com/downloads/)
- **Text Editor** - VS Code, PyCharm, or similar

### Checking Your Python Version
```bash
# Check if Python is installed and what version
python --version
# or on some systems:
py --version
```

## Getting Started

### 1. Clone the Repository
```bash
git clone <repository-url>
cd uvaSHPE
```

### 2. Set Up Virtual Environment
A virtual environment keeps your project dependencies separate from other Python projects.

```bash
# Create virtual environment
python -m venv shpe_env

# Activate virtual environment
# On Windows:
shpe_env\Scripts\activate
# On Mac/Linux:
source shpe_env/bin/activate

# You should see (shpe_env) in your terminal prompt when activated
```

### 3. Install Dependencies
```bash
cd shpe_website
pip install -r requirements.txt
```

### 4. Set Up the Database
Django uses SQLite by default (no additional database software needed).

```bash
# Create database tables
py -3.10 manage.py makemigrations
py -3.10 manage.py migrate
```

### 5. Create Admin User
This will let you access the admin panel to add alumni and manage content.

```bash
py -3.10 manage.py createsuperuser
```
- Enter a username (e.g., `admin`)
- Enter an email address
- Create a secure password (you'll need this to log in)

### 6. Run the Development Server
```bash
py -3.10 manage.py runserver 8080
```

Your website should now be running at: `http://127.0.0.1:8080/`

### Main Website
- **Homepage**: `http://127.0.0.1:8000/`

### Admin Panel
- **Admin Interface**: `http://127.0.0.1:8000/admin/`
- Log in with the superuser credentials you created earlier

## Managing Content

### Adding Exec Members

1. Go to `http://127.0.0.1:8000/admin/`
2. Log in with your admin credentials
3. Click **"Alumni"** in the admin panel
4. Click **"Add Alumni"** button
5. Fill out the form:
   - **Name**: Full name (e.g., "Vincent Martinez")
   - **Email**: Contact email
   - **Major**: What they study/studied at UVA
   - **Graduation Year**: Expected graduation year
   - **Position**: Current role (e.g., "Student", "Software Engineer")
   - **Company**: Current organization (e.g., "UVA", "Google")
   - **SHPE Status**: Their role in SHPE (President, Vice President, etc.)
   - **Bio**: Brief description
   - **LinkedIn URL**: (Optional) Their LinkedIn profile
   - **Headshot**: (Optional) Professional photo
   - **Is current exec**: Check this box for current executive board members
   - **Is featured**: Check for special highlighting (optional)

6. Click **"Save"**

### Adding Alumni

Follow the same steps as above, but **DON'T** check the "Is current exec" box. These will appear on the Alumni page instead.

### Updating Content

- **Edit existing entries**: Click on any alumni/exec member in the admin list
- **Delete entries**: Use the checkboxes and "Delete selected" action
- **Search**: Use the search box to find specific people
- **Filter**: Use the filter sidebar to narrow results

## Project Structure

```
uvaSHPE/
├── shpe_website/                 # Main Django project
│   ├── manage.py                # Django management script
│   ├── requirements.txt         # Python dependencies
│   ├── settings.py             # Django settings
│   ├── urls.py                 # Main URL routing
│   └── website/                # Main app
│       ├── models.py           # Database models (Alumni)
│       ├── views.py            # Page logic
│       ├── admin.py            # Admin interface config
│       ├── urls.py             # App URL routing
│       ├── static/             # CSS, images, etc.
│       │   ├── css/            # Modular CSS files
│       │   └── images/         # Image assets
│       └── templates/          # HTML templates
│           ├── base.html       # Site layout
│           ├── index.html      # Homepage
│           ├── eBoard.html     # Executive Board
│           └── alumni.html     # Alumni Directory
```

## Customizing

### Adding New Pages
1. Create a new HTML template in `/website/templates/`
2. Add a view function in `/website/views.py`
3. Add a URL pattern in `/website/urls.py`

### Modifying Styles
CSS is organized into modular files in `/website/static/css/`:
- `base.css` - Global styles and typography
- `header.css` - Navigation and header
- `components.css` - Cards, buttons, forms
- `sections.css` - Page sections and layouts
- `footer.css` - Footer styles
- `responsive.css` - Mobile responsiveness

## Common Commands

### Starting Development
```bash
# Activate virtual environment (if not already active)
shpe_env\Scripts\activate  # Windows
source shpe_env/bin/activate  # Mac/Linux

# Navigate to project
cd shpe_website

# Run server
py -3.10 manage.py runserver
```

### Database Management
```bash
# Create migrations after model changes
py -3.10 manage.py makemigrations

# Apply migrations
py -3.10 manage.py migrate

# Create backup of database
copy data\db.sqlite3 data\db_backup.sqlite3  # Windows
cp data/db.sqlite3 data/db_backup.sqlite3    # Mac/Linux
```

### Creating Admin Users
```bash
# Create additional admin users
py -3.10 manage.py createsuperuser
```

## 🔧 Troubleshooting

### "Command not found: py"
Try using `python` instead of `py -3.10`:
```bash
python manage.py runserver
```

### "No module named django"
Make sure your virtual environment is activated and dependencies are installed:
```bash
pip install -r requirements.txt
```

### "Port already in use"
If port 8080 is busy, use a different port:
```bash
py -3.10 manage.py runserver 8000
```

### Images not loading
Make sure you're in development mode and run:
```bash
py -3.10 manage.py collectstatic
```

### Database errors
If you see database errors, try:
```bash
py -3.10 manage.py makemigrations
py -3.10 manage.py migrate
```

## Learning Resources

Django resources:
- [Django Official Tutorial](https://docs.djangoproject.com/en/4.2/intro/tutorial01/)
- [Django Girls Tutorial](https://tutorial.djangogirls.org/)
- [Mozilla Django Tutorial](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django)

**Built with ❤️ for SHPE UVA**

