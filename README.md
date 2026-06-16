# Vegelight 🥦🛒

Vegelight is a dynamic e-commerce web application designed for fresh vegetable and grocery delivery. Built with Django, it provides a robust backend and an intuitive user interface for seamless online shopping.

## 🚀 Features

* **Product Catalog:** Browse a wide variety of fresh vegetables and grocery items.
* **Shopping Cart & Checkout:** Add items to your cart and proceed to a secure checkout.
* **Secure Payments:** Fully integrated with **Razorpay** for safe and instant online transactions.
* **Data Population Scripts:** Includes built-in scripts (`populate.py`, `add_more_items.py`) to easily populate the database with dummy products for testing and development.
* **Production Ready:** Pre-configured with Gunicorn and WhiteNoise for efficient static file serving in production environments.

## 🛠️ Tech Stack

* **Backend:** Python, Django 6
* **Database:** SQLite (Default for development)
* **Payment Gateway:** Razorpay API
* **Deployment Utilities:** Gunicorn, WhiteNoise

## ⚙️ Local Setup Instructions

### 1. Prerequisites
Ensure you have Python 3.8+ installed on your system.

### 2. Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Sushravya40/Vegelight.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Vegelight/DjangoPro/vegelight
   ```
3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

### 3. Database & Data Population
1. Apply the database migrations to set up your SQLite database:
   ```bash
   python manage.py migrate
   ```
2. Populate the database with sample grocery items:
   ```bash
   python populate.py
   ```

### 4. Running the Server
Start the Django development server:
```bash
python manage.py runserver
```
Open your web browser and go to `http://127.0.0.1:8000` to start exploring Vegelight!

## 💳 Razorpay Configuration
To enable payments locally, you must provide your Razorpay API keys. 
Update your settings or environment variables with your `RAZORPAY_KEY_ID` and `RAZORPAY_KEY_SECRET` before testing the checkout process.