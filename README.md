# Contributor's Guide to the Petoshield Django Project

Welcome to the Petoshield Django project! We're excited to have you on board. This guide will provide you with a detailed overview of how to contribute, particularly when it comes to adding new APIs or other components.

## Prerequisites

- Familiarity with Django and Django Rest Framework (DRF).
- Basic understanding of the project structure, its apps, and the purpose of each table as outlined in `plan.md`.
- Ensure you have the necessary software and packages installed as per the `requirements.txt` file.

## Getting Started

1. **Setup**:
   - Clone the project repository.
   - Install required dependencies: `make install`.
   - Run the server: `make runserver`.

2. **Project Structure**:
   
   The project is compartmentalized into different Django apps such as `pet`, `user`, `policy`, and `core`. Each app manages its own models, views, serializers, and other related modules.

## Adding a New API

1. **Plan Your API**:

   Always refer to the `plan.md` file before starting. It gives a comprehensive plan of the project, detailing tables, interfaces, and pages.

2. **Models**:
   
   - If you're introducing a new table, define the model in the `models.py` of the relevant app.
   - Ensure you inherit from the `BaseModel` for consistent fields like `created_at` and `updated_at`.
   - Apply database changes with `make makemigrations` and `make migrate`.

3. **Serializers**:

   - Serializers convert complex data types like Django models into Python data types that can be easily rendered into JSON.
   - Define serializers in the `serializers.py` file of the respective app.
   - Maintain foreign key relationships in the serializer for comprehensive data representation.

4. **Views**:

   - Views manage the request-response lifecycle.
   - Use DRF's `viewsets` for CRUD operations, and define your views in the `views.py` file.
   - Apply the appropriate permissions using permission classes.

5. **URLs**:

   - Update the `urls.py` of the respective app to create the endpoint for your new API.
   - The `DefaultRouter` can be used to automatically handle the CRUD operation URLs.

6. **Permissions**:

   - Permissions ensure restricted access to APIs based on user roles.
   - Modify or add permissions in the `permissions.py` file of the respective app when necessary.

7. **Testing**:

   - Write tests for your APIs to validate their behavior.
   - Use the command `make test` to run the tests.

8. **Documentation**:

   - Document your API comprehensively.
   - Detail the endpoint, request method, parameters, and sample responses to guide users.

9. **Commit & Push**:

   - After confirming that your changes are functional and well-tested, commit them.
   - Push to your fork and initiate a pull request to the main project repository.

## Adding Components Other than APIs

1. **Frontend**:

   - If you're working on the frontend, navigate to the `petoshield_ui` directory.
   - Install frontend dependencies using `make install-web`.
   - To run the frontend server, use `make start-web`.

2. **Database Management**:

   - For database-related tasks, refer to the `Makefile` for commands like `migrate`, `makemigrations`, and more.

3. **Code Quality**:

   - Before committing, ensure your code adheres to the quality standards by running `make flake`.

4. **General Guidelines**:

   - Always maintain modularity.
   - Follow the DRY (Don't Repeat Yourself) principle.
   - Ensure your code is well-commented and easily understandable by others.

## Conclusion

Thank you for your interest in contributing to the Petoshield project. Your expertise and dedication play a crucial role in the project's success. Always maintain the code's quality and ensure you're aligned with the project's goals and architecture as described in `plan.md`.

If you have any queries or require further clarifications, feel free to reach out to the maintainers or the community. Happy coding!