# Teacher-Student-Management-with-Authentication-Using-FastAPI
## Key Features

- **Admin Dashboard:** Administrators wield the ability to seamlessly oversee both student and teacher data.
- **Teacher Dashboard:** Teachers gain access to viewing and updating student information pertinent to the classes they instruct.
- **Student Dashboard:** Students can peruse their individual details and academic progress.
- **Role-Based Access Control:** Varied roles such as admin, teacher, and student dictate distinctive levels of system accessibility.
- **Secure User Authentication:** Robust JWT token-based authentication system ensures secure login.
- **API Endpoints:** Comprehensive CRUD operations are offered for students and teachers, enabling seamless data management.

## Installation and Setup

1. Clone the repository: `git clone https://github.com/yourusername/student-management-system.git`
2. Navigate to the project directory: `cd student-management-system`
3. Create a virtual environment: `python -m venv venv`
4. Activate the virtual environment: `source venv/bin/activate` (Linux/macOS) or `venv\Scripts\activate` (Windows)
5. Install dependencies: `pip install -r requirements.txt`
6. Create the database: `python init_db.py`
7. Start the development server: `uvicorn main:app --reload`

## Usage

Upon completing the installation process, open your web browser and navigate to `http://localhost:8000` to access the application. You can log in using your credentials and explore distinct dashboards tailored to your user role.

## Contribution

We wholeheartedly welcome contributions from the community! To contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Make your changes and commit: `git commit -m "Add your changes"`
4. Push to your branch: `git push origin feature/your-feature-name`
5. Submit a pull request.
