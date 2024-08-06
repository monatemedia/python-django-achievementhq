<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->

<a id="readme-top"></a>

<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">AchievementHQ-README</h3>

  <p align="center">
    We highly recommend keeping track of all your achievements, no matter how big or small they are! 🎯 Achievement HQ is a project for you and your friends to track and celebrate each other's achievements!
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template">View Demo</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

Welcome to the official repository for AchievementHQ! AchievementHQ is a web application designed to help you and your friends track, share, and celebrate each other's achievements. Whether it's personal milestones, professional goals, or just daily wins, AchievementHQ makes it easy and fun to stay motivated and connected.

Features:

- Achievement Tracking: Log and monitor your progress on various goals
- Social Sharing: Share your achievements with friends and celebrate their successes
- Notifications: Stay updated with reminders and notifications about your and your friends' milestones :smile:
- Customizable Profiles: Personalize your profile to showcase your top achievements and unique journey
- Privacy Controls: Manage who sees your achievements and ensure your data is secure

Thank you for your interest in AchievementHQ! We look forward to celebrating your achievements together!

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

Python Django and bootstrap

- [![Django][Django]][Django-url]
- [![Bootstrap][Bootstrap.com]][Bootstrap-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

These are the instructions on setting up your project locally. To get a local copy up and running follow these simple example steps.

### Prerequisites

The project requires Python 3 and pipenv to be installed on your local machine.

- Install pipenv
  ```sh
  pip install pipenv
  ```

### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Create Venv

```sh
pipenv shell
```

2. Install Django

```sh
pipenv install django
```

3. Run initial migrations

```sh
python manage.py migrate
```

4. Create admin user

```sh
python manage.py createsuperuser
```

5. Inject Fake Data (Optional)

```sh
python manage.py shell
```

- Delete all users except for the admin user

```sh
python manage.py delete_non_admin_users
```

- Create Fake Users

```sh
python manage.py create_users
```

- Create Fake Posts

```sh
python manage.py create_posts
```

- Create Fake Comments

```sh
python manage.py create_comments
```

6. Run server on http: 127.0.0.1:8000 (ctrl+c to stop)

```sh
python manage.py runserver
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->

## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->

## Roadmap

- [x] Add Bootstrap Theme and Static Files
- [x] Add Templates Folder For Easy Template Management
- [x] Add Polls App
- [ ] Add Users App
  - [ ] Add Sign Up Page
  - [ ] Add Log In Page
- [ ] Add Posts App
  - [ ] Add Posts CRUD
  - [ ] Add Posts Timeline
- [ ] Add Protected Routes
- [ ] Add Comments App
  - [ ] Allow Users To Comment On Posts
  - [ ] Allow Authors to Delete Comments
- [ ] Use Django’s URL Template Tag To Make Navigation Links Dynamic
- [ ] Add Error Pages Template
- [ ] Switch From Broswer Alerts To Bootstrap Alerts
- [ ] Add Emails App
  - [ ] Send Registration And Password Reset Email
  - [ ] Send Marketing Emails

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->

## Contact

Edward Baitsewe - [@LinkedIn](https://www.linkedin.com/in/edwardbaitsewe/) - edward@monatemedia.com

Project Link: [https://github.com/monatemedia/python-django-achievementhq](https://github.com/monatemedia/python-django-achievementhq)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->

## Acknowledgments

A list of resources that I found helpful and inspirational!

- [Brad Traversy Python Django Crash Course](https://www.youtube.com/watch?v=e1IyzVyrLSU)
- [Brad Traversy Python Django Crash Course Gist With Commands](https://gist.github.com/bradtraversy/06538da5924882b2cf30fa6310d505b1)
- [GeeksforGeeks Django Sign Up and Login With Confirmation Email](https://www.geeksforgeeks.org/django-sign-up-and-login-with-confirmation-email-python/)
- [Aman Goyal How To Create A Timeline To Track Your Achievements](https://dev.to/goyalaman/how-to-create-a-timeline-to-track-your-achievements-3cg2)
- [Start Bootstrap Theme Personal](https://startbootstrap.com/theme/personal)
- [Django Project By The Django Software Foundation](https://www.djangoproject.com/)
- [Bootstrap 5 Registration Form Component By Material Design For Bootstrap](https://mdbootstrap.com/docs/standard/extended/registration/)
- [Best README Template By Othneil Drew](https://github.com/othneildrew/Best-README-Template)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
[Django]: https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green
[Django-url]: https://www.djangoproject.com/
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
