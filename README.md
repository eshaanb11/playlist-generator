# Automatic Playlist Generator

## Overview

This **Automatic Playlist Generator** is a Flask-based web application that creates personalized playlists using real music data from the Last.fm API. Users can generate playlists by **genre** and explore music in a clean, modern interface inspired by Spotify.

This project was built as a way to learn **full-stack web development**, **API integration**, and **JSON parsing**, while creating a fun, interactive application.

**Live Demo** : https://playlist-generator-app-0lof.onrender.com

---

## Features

* **Genre-Based Playlists**: Enter a genre and get the most popular tracks in that category.
* **Dynamic Playlist Display**: Clean, modern interface with hover animations for tracks.
* **Error Handling**: Invalid artist or genre input triggers a user-friendly error message.
* **Responsive UI**: Spotify-inspired dark theme, rounded buttons, and smooth micro-interactions.
* **External Links**: Tracks link directly to Last.fm for exploration.

---

## How It Works

1. User opens the homepage (`index.html`) and chooses whether to search by genre.
2. The form sends input to Flask using a POST request.
3. Flask calls the Last.fm API using the `requests` library.
4. JSON data from Last.fm is parsed to extract top tracks.
5. Flask renders the `playlist.html` template with track information and links.
6. Invalid input or missing data is displayed with a clean error message.

---

## Technologies Used

* **Python 3**
* **Flask** – for backend routing and template rendering
* **HTML/CSS** – frontend interface with Spotify-style design
* **Jinja2** – template engine for dynamic content
* **Requests** – to interact with the Last.fm API
* **JSON** – for parsing API responses

---

## Folder Structure

```
playlist-generator/
│
├── playlist-gen-app.py              # Main Flask app
├── .env           # Contains API_KEY (not tracked in GitHub)
├── templates/
│   ├── index.html      # Homepage with form
│   └── playlist.html   # Playlist results page
├── static/
│   └── style.css       # Custom CSS for UI
└── .venv/              # Python virtual environment
```

---

## Skills Gained

* Building **full-stack web applications** with Flask
* Integrating **external APIs** (Last.fm) and parsing JSON data
* Handling **form input and POST requests**
* Implementing **error handling** and user-friendly messages
* Designing **modern, responsive UI** with CSS
* Working with **dynamic templates** using Jinja2

---

## Future Improvements

* Add **album art and preview links** for each track
* Save playlists for later viewing using JSON or a database
* Allow users to filter by **mood, popularity, or tempo**
* Deploy the app online using **Heroku, Render, or Vercel**

Used ChatGPT to help with the HTML and CSS files for the UI of this app. 
