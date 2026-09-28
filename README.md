# Project Overview

This is an introductory project in learning Django. This project comprises of 2 basic apps , one polling app which keeps track of vote counts and allows users to vote on polls , and the other being a music tracking app using lastfm's rest API.

## Features

### Polls App
* **Multi-Category Filtering:** Filter polls dynamically using checkboxes with custom "Apply" and "Clear" actions.
* **Standard Django Architecture:** Built using generic class-based views (`ListView`, `DetailView`) with a customized admin site and page.
* **Guide to using the filters and categories:** On the right side section , filters for various categories are visible , you may select any number of categories and click on "Apply" to see the desired results. In case you want to clear all filters  , click on the clear button and all the polls will be visible again.

### Music Tracker
* **Country Charts** Get the top artists and tracks from any popular country present in the list of countries.
* **Search Artists/Tracks/Albums** A comprehensive search feature using which a user can search up any artist/track/album they want 
* **Additional Feature** An additional feature of finding artists similar to any artist entered by the user may be used by simply typing your artist in the search bar.

## Running locally

Follow these steps to set up and run the project locally.

### Prerequisites

* Python 3.10+
* Git
* Requirements.txt mentions the required version of Django.
* Linux/WSL on windows.

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Vihaan192/Votes_and_Vibes

2. **Create venv environemnt:**
    ```bash
    source venv/bin/activate

3. **Install required files**
    ```bash
    pip install -r requirements.txt

4. **Run migrations**
    ```bash
    python manage.py makemigrations
    python manage.py migrate

5. **Run the development Server**
    ```bash
    python manage.py runserver