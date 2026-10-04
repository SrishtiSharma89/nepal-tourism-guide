# 🇳🇵 Nepal Tourism Guide & Travel Planner

A Django-based web application that helps users explore tourist destinations across Nepal, discover nearby hotels, view locations on interactive maps, plan travel routes, save favorite destinations, and share reviews.

## 🌄 About the Project

**Nepal Tourism Guide** is a tourism and travel planning web application developed using Django.

The project focuses on providing travelers with useful information about popular destinations in Nepal while combining destination discovery, accommodation information, interactive maps, travel routes, favorites, and user reviews in one platform.

The project was built as a portfolio project to practice and demonstrate full-stack web development with Django.

## ✨ Features

### 🗺️ Explore Destinations

* Browse tourist destinations by district.
* Currently includes destinations from:

  * Kathmandu
  * Kaski
  * Mustang
  * Chitwan
  * Solukhumbu
* View destination descriptions, coordinates, best time to visit, and images.
* Search for districts and destinations.

### 🏨 Hotels

* View hotels associated with destinations.
* Hotel information includes:

  * Name
  * Address
  * Description
  * Price range
  * Phone number
  * Location
* View hotel locations using interactive maps.
* Get directions through Google Maps.

### 🛣️ Travel Routes

* Explore travel routes between major locations in Nepal.
* Routes include:

  * Transport type
  * Distance
  * Estimated travel time
  * Route description
* Interactive Leaflet map displays route locations.
* Dynamic **From → To** dropdowns show only available destinations for the selected starting location.
* Supports multiple travel options between the same locations.

### ⭐ Favorites

* Authenticated users can save destinations to their favorites.
* View all saved destinations from the **My Favorites** page.

### ⭐ Reviews & Ratings

* Authenticated users can submit reviews for destinations.
* Destinations can be rated from **1 to 5 stars**.
* Users can view reviews submitted by other users.

### 🔐 User Authentication

* User registration
* Login
* Logout
* Personalized navigation showing the logged-in user's username

## 🛠️ Technologies Used

### Backend

* Python
* Django

### Frontend

* HTML5
* CSS3
* JavaScript
* Bootstrap 5.3.3

### Maps

* Leaflet.js
* OpenStreetMap

### Database

* SQLite (development)

### Admin & Development

* Django Admin
* Jazzmin
* Git & GitHub

## 📂 Project Structure

```text
nepal-tourism-guide/
│
├── manage.py
│
├── tourism/
│   ├── migrations/
│   ├── static/
│   │   └── tourism/
│   │       └── css/
│   │           └── style.css
│   │
│   ├── templates/
│   │   ├── registration/
│   │   │   └── login.html
│   │   │
│   │   └── tourism/
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── districts.html
│   │       ├── district_detail.html
│   │       ├── destination_detail.html
│   │       ├── hotels.html
│   │       ├── favorites.html
│   │       ├── signup.html
│   │       └── travel_routes.html
│   │
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── tourismproject/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
└── .gitignore
```

## 🚀 Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/SrishtiSharma89/nepal-tourism-guide.git
```

### 2. Open the project

```bash
cd nepal-tourism-guide
```

### 3. Create a virtual environment

```bash
python -m venv env
```

### 4. Activate the virtual environment

#### Windows PowerShell

```bash
.\env\Scripts\Activate.ps1
```

### 5. Install Django and required packages

```bash
pip install django pillow django-jazzmin
```

### 6. Apply migrations

```bash
python manage.py migrate
```

### 7. Create a superuser

```bash
python manage.py createsuperuser
```

### 8. Run the development server

```bash
python manage.py runserver
```

Open the application in your browser:

```text
http://127.0.0.1:8000/
```

The Django admin panel is available at:

```text
http://127.0.0.1:8000/admin/
```

## 🗺️ Map Integration

The project uses **Leaflet.js** with **OpenStreetMap** to display:

* Destination locations
* Hotel locations
* Travel route start and end points
* Route connections

Google Maps directions are also provided for supported routes and hotels.

## 📊 Main Database Models

The application currently includes the following major models:

* `District`
* `Destination`
* `Hotel`
* `TravelRoute`
* `Favorite`
* `Review`

These models are connected through Django's ORM to manage tourism information and user interactions.

## 🎯 Learning Objectives

This project helped me practice:

* Django project and app structure
* Django models and relationships
* Django ORM and database queries
* CRUD operations
* Django authentication
* User-specific data
* Form handling
* Django templates
* Template inheritance
* Static and media files
* JavaScript DOM manipulation
* Dynamic dropdowns
* Interactive maps with Leaflet
* API-style JSON data handling
* Git and GitHub
* Project organization and deployment preparation

## 🔮 Future Improvements

Possible future improvements include:

* Persistent production database
* Cloud-based media storage
* More destinations and hotels
* More detailed route information
* Improved route visualization using actual roads and trekking paths
* Weather information for destinations
* More advanced travel planning features
* Production deployment

## 👩‍💻 Author

**Srishti Sharma**

BCA Student
School of Environmental Science and Management (SchEMS)
Pokhara University

GitHub: [SrishtiSharma89](https://github.com/SrishtiSharma89)

---

⭐ If you find this project useful or interesting, feel free to explore the repository.
