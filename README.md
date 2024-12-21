# Recipe Assistant API

## Overview

The Recipe Assistant API is a FastAPI application designed to assist users in managing recipes. It provides endpoints for retrieving and managing recipe data, including ingredients, instructions, and user profiles.

## Features

- Create, read, update, and delete recipes
- Manage ingredients
- User profile management
- Health check endpoint

## Technologies Used

- FastAPI
- Uvicorn
- Pydantic
- MongoDB (or any other database you are using)
- HTML/CSS/JavaScript for the frontend

## Project Structure

```
recipe_assistant/
│
├── backend/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── crud.py
│   └── chatbot.py
│
├── frontend/
│   ├── static/
│   │   ├── css/
│   │   │   └── styles.css
│   │   └── js/
│   │       └── app.js
│   └── templates/
│       └── index.html
│
├── .env
├── requirements.txt
└── run.py
```

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/recipe_assistant.git
   cd recipe_assistant
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

5. Set up your environment variables in a `.env` file (if needed).

## Running the Application

To start the FastAPI server, run:

```bash
uvicorn backend.main:app --reload
```

The application will be available at `http://127.0.0.1:8000`.

## API Endpoints

### Health Check

- **Endpoint**: `/api/health`
- **Method**: `GET`
- **Description**: Check the health status of the API.
- **Response**:
  ```json
  {
      "status": "healthy"
  }
  ```

### Get All Recipes

- **Endpoint**: `/api/recipes`
- **Method**: `GET`
- **Description**: Retrieve a list of all recipes.
- **Response**:
  ```json
  [
      {
          "id": "recipe_id",
          "name": "Recipe Name",
          "ingredients": ["Ingredient 1", "Ingredient 2"],
          "instructions": ["Step 1", "Step 2"],
          "preparation_time": 30,
          "difficulty_level": "Easy",
          "cuisine": "Italian",
          "dietary_tags": ["Vegetarian"]
      }
  ]
  ```

### Create a Recipe

- **Endpoint**: `/api/recipes`
- **Method**: `POST`
- **Description**: Create a new recipe.
- **Request Body**:
  ```json
  {
      "name": "Recipe Name",
      "ingredients": ["Ingredient 1", "Ingredient 2"],
      "instructions": ["Step 1", "Step 2"],
      "preparation_time": 30,
      "difficulty_level": "Easy",
      "cuisine": "Italian",
      "dietary_tags": ["Vegetarian"]
  }
  ```
- **Response**:
  ```json
  {
      "id": "new_recipe_id",
      "name": "Recipe Name",
      ...
  }
  ```

### Get a Recipe by ID

- **Endpoint**: `/api/recipes/{id}`
- **Method**: `GET`
- **Description**: Retrieve a specific recipe by its ID.
- **Response**:
  ```json
  {
      "id": "recipe_id",
      "name": "Recipe Name",
      ...
  }
  ```

### Update a Recipe

- **Endpoint**: `/api/recipes/{id}`
- **Method**: `PUT`
- **Description**: Update an existing recipe.
- **Request Body**: Same as Create a Recipe.
- **Response**:
  ```json
  {
      "id": "recipe_id",
      "name": "Updated Recipe Name",
      ...
  }
  ```

### Delete a Recipe

- **Endpoint**: `/api/recipes/{id}`
