# QuoteProject

### Simply Blog using Django / PostgreSQL / MongoDB

## About This Project
QuoteProject is a simple blog application developed using Django. It uses MongoDB for scraping quotes from other sites and uploading them to a PostgreSQL database. Users can create accounts, add new quotes, and view the history of added quotes.

<*Home pages*>
![alt text](<static/index.png>)
<*Register pages*>
![alt text](<static/register.png>)
<*Account pages*>
![alt text](<static/account.png>)
## Features
- Scrape quotes from various sites and upload to PostgreSQL
- User account creation and management
- Add new quotes
- View history of added quotes
- Display 10 quotes per page
- Search quotes by author name or tag
- Account page for managing user information

## Project Structure
- **Django**: Backend framework
- **MongoDB**: Used for scraping quotes
- **PostgreSQL**: Standard database for storing quotes
- **Frontend**: HTML/CSS/JavaScript/Bootstrap for user interface

## Setup Instructions

### 1. Clone the repository:
```sh
git clone https://github.com/PlatinumDCH/QuoteProject.git
```

### 2. Navigate to the project directory:
```sh
cd QuoteProject
```

### 3. Install dependencies using Poetry:
```sh
poetry install
```

### 4. Set up the PostgreSQL database:
- Configure the database settings in `settings.py`
- Apply migrations:
  ```sh
  poetry run python manage.py migrate
  ```

### 5. Run the development server:
```sh
poetry run python manage.py runserver
```

## Usage
- Access the application at `http://localhost:8000`
- Create an account and log in
- Add new quotes and view the history of added quotes
- Use the search functionality to find quotes by author name or tag

## Contribution Guidelines
1. Fork the repository
2. Create a new feature branch:
   ```sh
   git checkout -b feature/YourFeature
   ```
3. Commit your changes:
   ```sh
   git commit -m 'Add some feature'
   ```
4. Push to the branch:
   ```sh
   git push origin feature/YourFeature
   ```
5. Open a pull request

## License
This project is licensed under the MIT License.

