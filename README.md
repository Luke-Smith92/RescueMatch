# RescueMatch

## Project Overview

RescueMatch is a pet rehoming platform designed to connect approved rescue centres with people looking to adopt animals.

The aim of the project was to create a simple and easy to use website where users can browse animals available for adoption and show interest in a pet they would like to adopt. Once matched, the rescue centre contact details are revealed to the user.

The project was built using Django, HTML and CSS and focuses on front-end CRUD functionality along with responsive design and simple navigation.

---

## Live Site

[INSERT LIVE SITE LINK HERE]

---

## Repository

[INSERT GITHUB REPOSITORY LINK HERE]

---

## Responsive Design

The website was designed to work across desktop, tablet and mobile devices.

**SCREENSHOT HERE – Responsive Design**

---

## Home Page

The home page introduces the RescueMatch idea and explains how the adoption process works. Users can navigate to browse animals or access the Rescue Centre Portal.

**SCREENSHOT HERE – Home Page**

---

## Browse Animals

Users can browse available animals displayed in a responsive grid layout. Each animal has its own profile page with information about the animal.

**SCREENSHOT HERE – Browse Animals**

---

## Animal Detail Page

Each animal has its own page showing:

- Animal image
- Breed
- Age
- Description
- Match button

The rescue centre information stays hidden until the user chooses to match with the animal.

**SCREENSHOT HERE – Animal Detail Page**

---

## Rescue Centre Portal

The project includes front-end CRUD functionality through the Rescue Centre Portal.

Approved rescue centres can:

- Add animal listings
- Edit animal listings
- Delete animal listings
- Manage current animals

This was added to meet the CRUD requirements of the project.

**SCREENSHOT HERE – Rescue Centre Portal**

---

## User Experience

### First Time User

- Understand what RescueMatch is
- Browse available animals
- Learn how matching works
- Easily navigate the website

### Returning User

- Check for new animals
- View animal profiles
- Match with animals they are interested in

### Rescue Centre User

- Add new animals
- Update existing listings
- Remove adopted animals

---

## Features

- Responsive design
- Browse animal listings
- Individual animal profile pages
- Match system
- Hidden rescue centre information until matched
- Front-end CRUD functionality
- Previous and next animal navigation
- Rescue Centre Portal
- Responsive navigation bar

---

## Technologies Used

- Python
- Django
- HTML
- CSS
- SQLite
- Git
- GitHub
- VS Code

---

## Database Models

The project uses two main database models:

### RescueCentre

Stores rescue centre information including:

- Name
- Location
- Email
- Phone number

### Animal

Stores animal information including:

- Name
- Animal type
- Breed
- Age
- Description
- Image
- Linked rescue centre

**SCREENSHOT HERE – Database Model / Diagram**

---

## Testing

### Manual Testing

| Feature | Expected Result | Pass/Fail |
|---|---|---|
| Home page loads | Home page displays correctly | Pass |
| Browse animals | Animals display correctly | Pass |
| Animal detail page | Individual animal page loads | Pass |
| Match button | Rescue information is revealed | Pass |
| Add animal | Animal listing added successfully | Pass |
| Edit animal | Animal listing updates correctly | Pass |
| Delete animal | Animal listing removed correctly | Pass |
| Navigation links | Links navigate correctly | Pass |
| Responsive layout | Layout adjusts correctly on mobile/tablet | Pass |

---

## Bugs and Fixes

### Flask to Django Change

Originally the project started using Flask by mistake before realising the project requirements were better suited to Django. The project was then rebuilt using Django so proper models, templates and CRUD functionality could be added.

### Front-End CRUD Issues

There was an issue where the front-end CRUD pages would not load correctly due to missing templates and incorrect file naming. This was fixed by creating the correct Django templates and linking them properly through views and URLs.

### Static File Issues

During development there were issues with image paths and static files not loading correctly. This was fixed by using Django static file structure and updating image paths correctly.

### Navigation/Layout Issues

Some navigation bars and page layouts did not match the rest of the website during development. This was fixed by reusing the same header and styling across all pages.

### Render Deployment Issues

There were several issues during deployment to Render. The project initially failed to deploy due to missing files such as `requirements.txt` and missing dependencies like `gunicorn`.

There were also issues with the Django project root directory not being correctly configured, which caused Render to fail to locate the `rescuematch_project` module.

These issues were fixed by:
- Creating a requirements.txt file
- Installing gunicorn
- Updating the Render start command
- Setting the correct root directory for the Django project

### Render Static File Problems

After the website was successfully deployed to Render, there were still issues with CSS and images not loading correctly on the live site. This caused the website to appear unstyled even though the Django application itself was running.

A lot of troubleshooting was needed to solve this, including using online documentation and some AI assistance to help identify the missing static file configuration settings.

The issue was fixed by:

- Adding the correct ALLOWED_HOSTS settings
- Installing and configuring WhiteNoise
- Setting up STATIC_ROOT
- Running collectstatic during deployment
- Updating the Render build settings

Once these changes were added, the website loaded correctly with styling and images working on the deployed version.
---

## Future Improvements

- User login system for approved rescue centres
- Secure authentication for the Rescue Centre Portal
- User accounts and saved matches
- Swipe style matching system
- Messaging system between rescues and adopters
- Improved search and filtering
- More detailed animal profiles

---

## Deployment

### Local Deployment

1. Clone the repository

2. Install requirements

```bash
pip install -r requirements.txt


---

## Credits

### Images Used

All images used in this project were sourced from Pixabay and are free to use under the Pixabay Content License.

| Animal | Credit |
|---|---|
| Buddy (Chihuahua) | Photo by RebeccasPictures |
| Charlie (Border Collie) | Photo by Alexas_Fotos |
| Peter Rabbit (Rabbit) | Photo by Jackielou DL (JACLOU-DL) |
| Spike (Newfoundland) | Photo by Roksana Helscher (Roksana96) |
| Rodney (Guinea Pig) | Photo by Yvinne |
| Zara (Zebra) | Photo by Pete Ball (peterjohnball0) |
| Willie (Orca) | Photo by James Hills |

---

## Author

Created by Luke Smith for Milestone Project 3.