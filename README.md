<div id="top"></div>

# tienda-online
Online e-shop using the Django framework

This is a project I started a couple of months ago, sadly left it gathering dust on my pc due to an avalanche of final exams and college stuff, so I decided to upload it to GitHub to keep track of it and start completing of some of the To-Do items that it badly needs.

### Prerequisites

* [Python 3.8 or greater](https://www.python.org/downloads/release/python-380/)
* [MySQL](https://dev.mysql.com/downloads/)
* [XAMPP](https://www.apachefriends.org/)
The required libraries are listed inside the file *requirements.txt* (see Installation step 2)
I recommend creating a virtual environment to install the necessary libraries the python install on your system.

### Installation

Clone the repo
   ```sh
   git clone https://github.com/felipebertocchi/tienda-online.git
   ```
   
I recommend using `virtualenv` for installing dependencies to this project:

- Start by installing `virtualenv` if you don't have it
  ```
  pip install virtualenv
  ```

- Once installed access the project folder
  ```
  cd tienda-online
  ```

- Create a virtual environment
  ```
  virtualenv venv
  ```

- Enable the virtual environment
  ```
  . venv/Scripts/activate
  ```
  or
  ```
  source venv/bin/activate
  ```

- Install the python dependencies on the virtual environment
  ```
  pip install -r requirements.txt
  ```


### Usage

After installing all the dependencies for this project, open up XAMPP and initialize the Apache y MySQL modules, as show here:
<p align="center">
  <img align="center" src="https://i.imgur.com/AlAaW4b.jpeg" width="500">
</p>

Now it is only a matter of running the following line in a terminal:
  ```sh
  python manage.py runserver
  ```

and that's it. Now you will be running the project from your computer, and can be accessed from http://127.0.0.1:8000/

### Roadmap

- [x] Add product search from database
- [x] Add Cart functionality 
- [ ] Include user registration and log-in 
- [ ] Allow users to upload custom products to database
- [ ] Allow users to purchase products (using virtual fake money of course)
- [ ] Implement live search with Ajax
- [ ] Add better styling
- [ ] Improve on the store and search sections
  - [ ] Add product categories
  - [ ] Add search filters
- [ ] Add additional sections such as Featured products
- [ ] Multi-language Support

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>
  
## Contact

Felipe A. Bertocchi - fabertocchi@gmail.com
