#Location and Person Management System

#Overview

This is a Django-based web application for managing hierarchical location data (Country, State, City, Area) and person details. 
The system allows users to perform CRUD (Create, Read, Update, Delete) operations on location and person records, with a user-friendly 
interface powered by Bootstrap, HTMX, and jQuery. The application features dependency dropdowns for selecting locations and robust 
form validation to ensure data integrity.

#Features
Location Management:
Create, read, update, and delete records for Countries, States, Cities, and Areas.
Hierarchical dependency: States depend on Countries, Cities depend on States, and Areas depend on Cities.
Status toggling (Active/Deactive) for each location type.
Search and pagination for efficient data browsing.

Person Management:

Create, read, update, and delete person records with fields for name, gender (Male, Female, Others), and associated location (Country, State, City, Area).

Dependency dropdowns ensure valid location selections.

Status toggling for person records.

Search functionality across person name, gender, and location fields.

Frontend Features:

Responsive UI using Bootstrap 5.

Dynamic updates with HTMX for seamless user experience without full page reloads.

Client-side form validation using jQuery Validate to enforce rules (e.g., alphabetical characters, no double spaces).

AJAX-powered dependency dropdowns for location selection.

Backend Features:

Django ORM for database interactions.
Robust error handling and user feedback with Django messages.
Pagination to handle large datasets.

CSRF protection for secure form submissions.

Technologies Used

Backend: Django, Python
Frontend: HTML, CSS, Bootstrap 5, HTMX, jQuery, jQuery Validate
Database: SQLite (default, configurable to other databases like PostgreSQL)
Dependencies: Django, Bootstrap, HTMX, jQuery, Lord Icon (for delete modal icons)
Setup Instructions



Installation

Clone the Repository:

git clone https://github.com/ArunKumarNagidi/Locationapp.git
cd Locations



Create and Activate a Virtual Environment:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate



Install Dependencies:

pip install -r requirements.txt



Apply Database Migrations:

python manage.py makemigrations
python manage.py migrate



Create a Superuser (Optional):

python manage.py createsuperuser



Run the Development Server:

python manage.py runserver

Access the application at http://127.0.0.1:8000.

Project Structure

location-person-management/
├── location_app/
│   ├── migrations/
│   ├── templates/
│   │   ├── location_base/
│   │   ├── locations/
│   │   │   ├── country/
│   │   │   ├── state/
│   │   │   ├── city/
│   │   │   ├── area/
│   │   ├── person_details.html
│   │   ├── person_components_list_data.html
│   │   ├── person_components_status_change.html
│   │   ├── person_components_edit_form.html
│   ├── models.py
│   ├── views.py
│   ├── urls.py
├── static/
│   ├── base_assets/
│   ├── alertcomponents/
├── manage.py
├── requirements.txt
├── README.md

Usage





Access the Application:





Navigate to http://127.0.0.1:8000/ to view the person details management page.

Navigate to http://127.0.0.1:8000/locations to view the locations page.

Use the navigation to access Country, State, City, Area, or Person management sections.



Managing Locations:

Add new records via the "Add" buttons in each section.

Edit or delete records using the action buttons in the table.

Toggle status (Active/Deactive) by clicking the status badge.

Use the search bar to filter records.

Managing Persons:

Add a new person by filling out the form with name, gender, and location details.

Select locations using the dependency dropdowns (Country → State → City → Area).

Edit, delete, or toggle the status of person records similarly to locations.

Form Validation:

Person names must be alphabetical, start with a letter, and have no double spaces.

All dropdowns (gender, country, state, city, area) are required.

Validation errors are displayed in the form modal.


Contributing

Fork the repository.

Create a new branch (git checkout -b feature/your-feature).

Make your changes and commit (git commit -m "Add your feature").

Push to the branch (git push origin feature/your-feature).

Open a pull request.

License

This project is licensed under the MIT License. See the LICENSE file for details.

Contact

For questions or feedback, please open an issue on GitHub or contact arunkumarnagidi@gmail.com.
