Markdown
# Django Polls App

Introductory django polls app , made using the Django tutorial with a few additional features like searching polls via categories (single or multiple).

## Features

* **Multi-Category Filtering:** Filter polls dynamically using checkboxes with custom "Apply" and "Clear" actions.
* **Standard Django Architecture:** Built using generic class-based views (`ListView`, `DetailView`) with a customized admin site and page.
* **Guide to using the filters and categories:** On the right side section , filters for various categories are visible , you may select any number of categories and click on "Apply" to see the desired results. In case you want to clear all filters  , click on the clear button and all the polls will be visible again.

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
   git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git)
   cd djangotutorial

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