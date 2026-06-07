# RescueMatch

(static/images/screenshots/am_i_responsive.png)

## Project Overview

RescueMatch is a pet rehoming website designed to help connect rescue centres with people looking to adopt animals.

Users can browse available animals, view information about each pet and match with animals they are interested in. Once a match has been made, the rescue centre contact details are revealed so the adoption process can begin.

The project was built using Python, Django, HTML and CSS. It includes front-end CRUD (Create, Read, Update and Delete) functionality that allows rescue centres to manage animal listings.

---

## Live Site

https://rescuematch.onrender.com
(static/images/screenshots/live_site.png)
---

## Repository

[INSERT GITHUB REPOSITORY LINK]

---

# User Experience (UX)

## Project Goals

The aim of RescueMatch is to make it easier for people to find animals looking for a new home while also giving rescue centres a simple way to manage their animal listings.

The website was designed to be easy to navigate, responsive across different devices and simple for users to understand.

## User Stories

### First Time User

- Understand what RescueMatch is
- Browse available animals
- Learn how the matching process works
- Easily navigate the website

### Returning User

- Check for newly added animals
- Browse animal profiles
- Match with animals they are interested in

### Rescue Centre User

- Add new animals
- Edit existing animal listings
- Remove adopted animals
- Manage current animal records

---

## Design Planning

![Design Planning](assets/images/screenshots/design-planning.png)

Formal wireframes were not created for this project.

Instead, the website was developed using an iterative approach. Layouts and features were designed directly in the browser and improved throughout development based on testing and usability.

The website was built around three main user journeys:

- Browsing available animals
- Viewing animal details
- Managing animal listings through the Rescue Centre Portal

---

# Features

## Home Page

![Home Page](assets/images/screenshots/home-page.png)

The home page introduces the RescueMatch platform and explains how the adoption process works. Users can navigate to browse animals or access the Rescue Centre Portal.

---

## Browse Animals

![Browse Animals](assets/images/screenshots/browse-animals.png)

Users can browse available animals displayed in a responsive grid layout. Each animal includes an image and summary information.

---

## Animal Detail Page

![Animal Detail Page](assets/images/screenshots/animal-detail-page.png)

Each animal has its own profile page displaying:

- Animal image
- Breed
- Age
- Description
- Match button

Rescue centre information remains hidden until the user chooses to match with the animal.

---

## Match Page

![Match Page](assets/images/screenshots/match-page.png)

When a user chooses to match with an animal, the rescue centre contact details are revealed. This allows the user to contact the rescue centre directly regarding adoption.

---

## Rescue Centre Portal

![Rescue Centre Portal](assets/images/screenshots/rescue-centre-portal.png)

The Rescue Centre Portal allows rescue centres to manage animal listings using CRUD (Create, Read, Update and Delete) functionality.

Rescue centres can:

- Add new animals
- Edit existing animals
- Delete animals
- Manage current listings

For the current version of the project, a single rescue centre record is used to demonstrate the functionality. However, the database structure has been designed so additional rescue centres can be added in future versions of the website.

---

## Add Animal

![Add Animal](assets/images/screenshots/add-animal.png)

Rescue centres can add new animal listings using a form. The information is then stored in the database and displayed on the website.

---

## Edit Animal

![Edit Animal](assets/images/screenshots/edit-animal.png)

Existing animal records can be updated whenever information changes.

---

## Delete Animal

![Delete Animal](assets/images/screenshots/delete-animal.png)

Animal records can be removed when an animal has been adopted or is no longer available.

---

# Database Structure

## Database Diagram

![Database Diagram](assets/images/screenshots/database-diagram.png)

The project uses two main database models.

## Responsive Design

![Responsive Design](static/images/screenshots/am_i_responsive.png)

RescueMatch was designed using responsive design principles to ensure the website works across desktop, tablet and mobile devices.

Testing was carried out using browser developer tools and the Am I Responsive website. The results showed that the layout adjusts correctly across different screen sizes while keeping navigation, images and content accessible.

Users can browse animals, view animal details and access the Rescue Centre Portal regardless of the device being used.

### RescueCentre

Stores:

- Name
- Location
- Email
- Phone Number

### Animal

Stores:

- Name
- Animal Type
- Breed
- Age
- Description
- Image
- Rescue Centre

### Relationships

A one-to-many relationship exists between RescueCentre and Animal.

One rescue centre can have multiple animals available for adoption, while each animal belongs to a single rescue centre.

The database structure was designed this way so that additional rescue centres can be added in future versions of the platform without requiring major changes to the database.

---

# Responsive Design

## Responsive Testing

![Responsive Design](assets/images/screenshots/am-i-responsive.png)

The website was designed to work across desktop, tablet and mobile devices.

Testing was carried out using browser developer tools and responsive testing websites to ensure pages displayed correctly across different screen sizes.

Navigation, images and page layouts adjusted correctly when viewed on smaller screens.

---

# Testing

## Manual Testing

Manual testing was carried out throughout development to ensure all features worked as expected.

| Feature | Expected Result | Pass/Fail |
|----------|----------|----------|
| Home Page | Home page loads correctly | Pass |
| Browse Animals | Animal listings display correctly | Pass |
| Animal Detail Page | Animal information displays correctly | Pass |
| Match System | Rescue information is revealed | Pass |
| Add Animal | New animal record created | Pass |
| Edit Animal | Animal record updated | Pass |
| Delete Animal | Animal record removed | Pass |
| Navigation | Links work correctly | Pass |
| Responsive Design | Layout adjusts correctly | Pass |

---

## Automated Testing

Automated testing was used to help identify coding issues and improve website quality.

The following tools were used:

- W3C HTML Validator
- W3C CSS Validator
- Lighthouse
- Browser Developer Tools

---

## HTML Validation

![HTML Validation](assets/images/screenshots/html-validation.png)

All HTML pages were tested using the W3C HTML Validator.

Any validation errors found during development were corrected before submission.

---

## CSS Validation

![CSS Validation](assets/images/screenshots/css-validation.png)

The CSS stylesheet was tested using the W3C CSS Validator.

The final stylesheet passed validation successfully.

---

## Lighthouse Testing

![Lighthouse Testing](assets/images/screenshots/lighthouse-testing.png)

Lighthouse testing was used to assess:

- Performance
- Accessibility
- Best Practices
- SEO (Search Engine Optimisation)

Search Engine Optimisation (SEO) measures how easily search engines can understand and index a website.

The results helped identify areas for improvement during development and testing.

---

# Bugs and Fixes

## Flask to Django Change

The project originally started in Flask before it became clear that Django would be more suitable for handling database models and CRUD functionality.

The project was rebuilt using Django which allowed proper use of models, templates and database relationships.

---

## CRUD Template Issues

During development some CRUD pages failed to load due to missing templates and incorrect file references.

This was fixed by creating the correct Django templates and ensuring views and URLs were linked correctly.

---

## Static File Issues

There were issues with images and static files not loading correctly during development.

This was fixed by organising files using Django's static file structure and updating image paths.

---

## Navigation and Layout Issues

Some pages initially used different navigation layouts which caused inconsistency across the website.

This was fixed by using a consistent header and navigation structure across all pages.

---

## Render Deployment Issues

The website initially failed to deploy to Render due to missing dependencies and configuration problems.

Problems included:

- Missing requirements.txt
- Missing gunicorn package
- Incorrect Django project location
- Incorrect Render start command

These issues were fixed through testing, troubleshooting and deployment configuration changes.

---

## Render Static File Problems

After deployment, CSS and image files were not loading correctly on the live website.

This caused the website to appear unstyled despite the Django application working correctly.

The issue was fixed by:

- Configuring WhiteNoise
- Setting STATIC_ROOT
- Running collectstatic
- Updating deployment settings
- Correcting ALLOWED_HOSTS settings

Online documentation, troubleshooting guides and AI assistance were used to help identify and resolve the issue.

### HTML Validation Error

During HTML validation, the W3C Validator reported an error on the Animal Detail page caused by an unclosed `<section>` element.

This resulted in the validator reporting:

- Unclosed element `section`
- End tag for `body` seen, but there were unclosed elements

The issue was identified using the W3C HTML Validator and fixed by adding the missing closing `</section>` tag to the Animal Detail template.

After the fix was applied, the page validated correctly.

---

# Deployment

## Local Deployment

1. Clone the repository

```bash
git clone INSERT_REPOSITORY_URL
```

2. Open the project in VS Code

3. Create a virtual environment

```bash
python -m venv .venv
```

4. Activate the virtual environment

```bash
.venv\Scripts\activate
```

5. Install requirements

```bash
pip install -r requirements.txt
```

6. Run migrations

```bash
python manage.py migrate
```

7. Start the development server

```bash
python manage.py runserver
```

---

## Render Deployment

The project was deployed using Render.

Deployment steps:

1. Create a new Web Service in Render
2. Connect the GitHub repository
3. Configure environment variables
4. Install dependencies using requirements.txt
5. Configure WhiteNoise for static files
6. Run database migrations
7. Deploy the application

---

# Future Improvements

- Multiple rescue centre accounts
- Secure login system for rescue centres
- Individual rescue centre dashboards
- Rescue centres managing only their own animal listings
- User accounts
- Saved matches
- Swipe-style matching system
- Messaging between adopters and rescue centres
- Advanced search and filtering
- More detailed animal profiles
- Messaging system allowing adopters to contact rescue centres directly through the website instead of using email or telephone details
- mobile hamburger navigation menu
---

# Credits

## Technologies Used

- Python
- Django
- HTML
- CSS
- SQLite
- Git
- GitHub
- VS Code
- Render

---

## Images

All animal images used in this project were sourced from Pixabay and are free to use under the Pixabay Content Licence.

**INSERT IMAGE CREDITS TABLE HERE**

---

## Acknowledgements

- Code Institute
- Django Documentation
- Render Documentation
- Pixabay
- Online troubleshooting resources used during development

---

# Author

Created by Luke Smith for Milestone Project 3.