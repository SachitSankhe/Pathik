# Pathik





<h1 align="center">
  <a href="https://github.com/Abhishekohm/pathik-backend.git">
    <img src="https://res.cloudinary.com/dm6gcyihe/image/upload/v1670822779/pathik_wnganr.jpg" alt="GE Healthcare" width="400" height="350">
  </a>
</h1>
<h3>The guide for a tourist to visit places on National Importance.</h3>

## Tech Stack

  
**Client:**

<img  src="https://www.vectorlogo.zone/logos/w3_html5/w3_html5-ar21.svg"  style="background-color:white;" alt="drawing"  width="100"/><img  src="https://www.vectorlogo.zone/logos/tailwindcss/tailwindcss-ar21.svg"  alt="drawing"  width="100"/><img 
src="https://www.vectorlogo.zone/logos/w3_css/w3_css-official.svg"
alt="drawing" width="50"/><img 
src="https://www.vectorlogo.zone/logos/javascript/javascript-vertical.svg"
alt="drawing" width="50"/>


**Server:** 

<img 
src="https://www.vectorlogo.zone/logos/djangoproject/djangoproject-ar21.svg"
alt="drawing" width="80"/> <img 
src="https://www.vectorlogo.zone/logos/python/python-ar21.svg"
alt="drawing" width="90"/> <img 
src="https://www.vectorlogo.zone/logos/postgresql/postgresql-ar21.svg"
alt="drawing" width="90"/> <img 
src="https://static.im-cdn.com/assets/images/logo.d8e416049537.jpg"
alt="drawing" width="100"/> <img 
src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/Cloudinary_logo.svg/2560px-Cloudinary_logo.svg.png"
alt="drawing" width="100"/>

## 🔗 Links

- GitHub repo link: [Link to repository](https://github.com/Abhishekohm/pathik-backend)

## Getting Started

Assuming you have git, follow the following process
1. Clone the Git Repo:
   ```
   $ git clone https://github.com/Abhishekohm/pathik-backend.git
   ```
2. Go into the Repo directory
   ```
   $ cd pathik-backend
   ```
3. Setup .env with the help of .env.example file in server app
   ```
   # Sender email address
   EMAIL_HOST_USER=SENDER_EMAIL
   EMAIL_HOST_PASSWORD=SENDER_EMAIL_APP_PASSWORD

   # Postgre-Password
   DB_PASSWORD=POSTRGRE_PASSWORD

   # Your django key
   SECRET_KEY=DJANGO_SECRET_KEY

   # Instamojo Credentials 
   API_PRIVATE_KEY=INSTAMOJO_PRIVATE_API_KEY
   AUTH_PRIVATE_TOKEN=INSTAMOJO_PRIVATE_AUTH_TOKEN
   PRIVATE_SALT=INSTAMOJO_PRIVATE_SALT

   # All of this is available on cloudinary dashboard
   cloud_name=CLOUDINARY_CLOUD_NAME
   api_key=CLOUDINARY_API_KEY
   api_secret=CLOUDINARY_API_SECRET

   CLOUDINARY_URL=CLOUDINARY_URL
   ```
3. Install all the dependencies
   ```
   $ pip install -r requirements.txt
   ```
4. Go into the server
   ```
   $ cd server
   ```
5. Start the server
   ```
   $ python manage.py
   ```
6. Open the website 
   ```
   $ go to http://localhost:8000/
   ```


## Demo

https://user-images.githubusercontent.com/84727394/206970452-2b18362b-e307-4eac-b5fa-38279a6443fe.mp4

