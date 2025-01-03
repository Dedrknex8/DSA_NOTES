Date: 03-01-2025 || Rohit Tiwari

# IDEA:

> My main motive is to create an todo app with google calendar sync feature so that i can directly visite to my google calendar and see the task without needing to actully visiting the site

# What problem does it solve

> First of all it solve my problem of using it in any device without needing to visite the on all devices

## Requirements for this projects

Here my rough sketch or idea in whiteboard [visite this link](https://miro.com/welcomeonboard/Tzd6cnNMNWFwaGpYSHJJTlZlSU1IUUFXM01IQitvczRpaGtNQnorNFRRUWt4bWNNNmF3d2VrRGRuVHJQNVZhRXhFQ2VnSU1mU0d4Q2NaMkZ2QzBJQ3BFUVVFMU1kMzdZMEkxb1RObWJBM3hZSDB4MUxaRVN2MlRrZ2w2cnBjU2YhZQ==?share_link_id=513944768133)

Inshort the requirements are 
1. Need a frontend system for that i can use reactjs
2. Backend : i can use express js or node js
3. database: postregsql
4. api : google calendar api's
### Steps to Build:

#### 1. **Set Up the Environment**

- Choose a stack for development. A common stack could be:
    - Frontend: React.js or Vue.js
    - Backend: Node.js with Express
    - Database: MongoDB, PostgreSQL, or Firebase

#### 2. **Create a Google Cloud Project**

- Go to Google Cloud Console.
- Create a new project.
- Enable the **Google Calendar API**.
- Set up OAuth 2.0 credentials to allow app integration.

#### 3. **Backend Implementation**

- **Set Up OAuth 2.0 Flow**:
    - Use libraries like `passport-google-oauth20` (Node.js) or similar for authentication.
- **Integrate Google Calendar API**:
    - Use the Google API client library to manage calendar events.
- **Database Management**:
    - Store user tasks and sync status in your database.

#### 4. **Frontend Development**

- **UI/UX Design**:
    - Create task management interfaces (add, edit, delete tasks).
    - Add a calendar view or sync toggle.
- **Google Sign-In**:
    - Use the Google OAuth client library for sign-in.
- **API Integration**:
    - Communicate with the backend for CRUD operations and syncing.

#### 5. **Sync Logic**

- Implement syncing rules:
    - New tasks in the app are added to Google Calendar.
    - Changes in Google Calendar reflect in the app.
- Use **webhooks** or periodic polling to check for updates.

#### 6. **Deployment**

- Deploy your app:
    - Frontend: Vercel, Netlify, or AWS S3
    - Backend: AWS, Heroku, or DigitalOcean
- Ensure the app is secure (HTTPS, secure tokens, etc.).




# Resources 

1. Main idea implement done using chatgpt [link](https://chatgpt.com/c/6777cb1b-9404-8012-a99f-0f0f860fd91d)
2. 