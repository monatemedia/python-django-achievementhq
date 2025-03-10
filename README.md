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
  <a href="https://github.com/monatemedia/python-django-achievementhq">
    <img src="images/trophy-logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">AchievementHQ-README</h3>

  <p align="center">
    Keep track of all your achievements, no matter how big or small they are! 🎯 Achievement HQ is a social network for you and your friends to track and celebrate each other's achievements!
    <br />
    <br />
    <a href="https://achievementhq.monatemedia.com/" target="_blank"><strong>View Demo »</strong></a>
    <br />
    <br />
    <a href="mailto:edward@monatemedia.com?subject=Bug%20Report%20for%20AchievementHQ&body=**Bug%20Description:**%0D%0A%0D%0A**Steps%20to%20Reproduce:**%0D%0A1.%20Step%201%0D%0A2.%20Step%202%0D%0A3.%20Step%203%0D%0A%0D%0A**Expected%20Behavior:**%0D%0A%0D%0A**Actual%20Behavior:**%0D%0A%0D%0A**Screenshots%20or%20Error%20Messages:**%0D%0A%0D%0A**Browser%20and%20OS%20(Version):**%0D%0A%0D%0A**Additional%20Information:**%0D%0A%0D%0A">Report Bug</a>
    ·
    <a href="mailto:edward@monatemedia.com?subject=Feature%20Request%20for%20AchievementHQ&body=**Feature%20Description:**%0D%0A%0D%0A**Why%20is%20this%20feature%20important%3F:**%0D%0A%0D%0A**How%20would%20you%20like%20it%20to%20work%3F:**%0D%0A%0D%0A**Additional%20Comments:**%0D%0A%0D%0A">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details open>
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

[![AchievementHQ Screen Shot][product-screenshot]](https://example.com)

Welcome to the official repository for AchievementHQ! AchievementHQ is a social network designed to help you and your friends track, share, and celebrate each other's achievements. Whether it's personal milestones, professional goals, or just daily wins, AchievementHQ makes it easy and fun to stay motivated and connected.

Features:

- Achievement Tracking: Log and monitor your progress on various goals
- Social Sharing: Share your achievements with friends and celebrate their successes
- Notifications: Stay updated with reminders and notifications about your and your friends' milestones :smile: (if feature is requested)
- Customizable Profiles: Personalize your profile to showcase your top achievements and unique journey (if feature is requested)
- Privacy Controls: Manage who sees your achievements and ensure your data is secure (if feature is requested)

Thank you for your interest in AchievementHQ! We look forward to celebrating your achievements together!

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

Python Django and Bootstrap

- [![Django][Django]][Django-url]
- [![Bootstrap][Bootstrap.com]][Bootstrap-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

To get a copy set up and running on your local environment follow these simple steps.

### Prerequisites

The project requires Python 3 and pipenv to be installed on your local machine.

- Install pipenv
  ```sh
  pip install pipenv
  ```

### Installation

1.  Download repository

```sh
git clone https://github.com/monatemedia/python-django-achievementhq.git
```

2. Change into main directory

```sh
cd python-django-achievementhq
```

3. Create Venv

```sh
pipenv shell
```

4. Change into app directory

```sh
cd achievementhq
```

5. Run the demo app

```sh
python demo.py
```

- Admin user name is "admin" and password is PennantFernlikeAnnouncerSubsidy
- All other users passwords are DecreasePrototypeEasiestOxidant

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->

## Usage

Logged in users can view all other users by their latest posts:\
\
[![View All Users By Post Screen Shot 1][view-all-users-1-screenshot]](https://example.com)\
\
[![View All Users By Post Screen Shot 2][view-all-users-2-screenshot]](https://example.com)\
\
Logged in users can post and delete their own achievement posts:\
\
[![Posts Create Screen Shot][posts-create-screenshot]](https://example.com)\
\
Posts are organised on a timeline:\
\
[![Posts Timeline Screen Shot][posts-timeline-screenshot]](https://example.com)\
\
Logged in users can make and delete their comments on their own and other users achievement posts:\
\
[![Comments Screen Shot][comments-screenshot]](https://example.com)\
\
Comments are organised on a timeline by post:\
\
[![Comments Timeline Screen Shot][comments-timeline-screenshot]](https://example.com)\
\
Logged in users can delete comments made on posts they own:\
\
[![Delete Confirmation Screen Shot][delete-confirmation-screenshot]](https://example.com)\
\
Administrators can log into the admin area at http://127.0.0.1:8000/admin/ and create, read, update and delete:

- Users
- User Groups
- Polls
- Posts
- Comments
  \
  [![Admin Area Screen Shot][admin-area-screenshot]](https://example.com)\
  \
  _For more examples, please refer to the [Documentation](#getting-started)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->

## Roadmap

- [x] Add Pages App
  - [x] Logged Out Pages
    - [x] Home Page
    - [x] Resume Page
    - [x] Projects Page
    - [ ] Contact Page
      - [ ] Set Up Mail Server
    - [ ] Privacy Page
    - [ ] Terms Page
- [x] Add Polls App
  - [x] Add Polls Pages
    - [x] Add Polls Index Page
    - [x] Add Polls Details Page
    - [x] Add Polls Results Page
  - [x] Set Up Polls In Admin Area
- [x] Add Posts App
  - [x] Add Posts Pages
    - [x] Posts Index Page
    - [x] Posts User List By Latest Post Page
    - [x] Posts Detail Page
    - [x] Posts Form Page
  - [x] Add Comments Pages
    - [x] Comments Detail Page
    - [x] Comments Form Page
  - [x] Add Delete Confirmation Page For Posts & Comments
  - [x] Set Up Posts And Comments In Admin Area
- [x] Add Users App
  - [x] Add Sign Up Page
  - [x] Add Log In Page
- [x] Add Error Pages
  - [x] Add 404 Not Found Page
  - [x] Add 500 Server Error Page
- [ ] Error Logging
- [ ] Pagination
- [ ] Mail Server
- [ ] Update demo.py To Run collectstatic
- [ ] Set Up Docker Container
- [ ] Send Container To VPS
- [ ] Map URL to IP Address

See the [open issues](https://github.com/monatemedia/python-django-achievementhq/issues) for a full list of proposed features (and known issues).

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

Edward Baitsewe - [@LinkedIn](https://www.linkedin.com/in/edwardbaitsewe/) - [Website](https://www.monatemedia.com/)

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
- [The Django Software Foundation Django Project](https://www.djangoproject.com/)
- [Material Design For Bootstrap (Bootstrap 5) Registration Form Component](https://mdbootstrap.com/docs/standard/extended/registration/)
- [Othneil Drew Best README Template](https://github.com/othneildrew/Best-README-Template)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/monatemedia/python-django-achievementhq.svg?style=for-the-badge
[contributors-url]: https://github.com/monatemedia/python-django-achievementhq/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/monatemedia/python-django-achievementhq.svg?style=for-the-badge
[forks-url]: https://github.com/monatemedia/python-django-achievementhq/network/members
[stars-shield]: https://img.shields.io/github/stars/monatemedia/python-django-achievementhq.svg?style=for-the-badge
[stars-url]: https://github.com/monatemedia/python-django-achievementhq/stargazers
[issues-shield]: https://img.shields.io/github/issues/monatemedia/python-django-achievementhq.svg?style=for-the-badge
[issues-url]: https://github.com/monatemedia/python-django-achievementhq/issues
[license-shield]: https://img.shields.io/github/license/monatemedia/python-django-achievementhq.svg?style=for-the-badge
[license-url]: https://github.com/monatemedia/python-django-achievementhq/blob/main/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/edwardbaitsewe/
[product-screenshot]: images/homepage.png
[view-all-users-1-screenshot]: images/view-all-users-1.png
[view-all-users-2-screenshot]: images/view-all-users-2.png
[posts-create-screenshot]: images/post-create.png
[posts-timeline-screenshot]: images/posts-timeline.png
[comments-screenshot]: images/comments.png
[comments-timeline-screenshot]: images/comments-timeline.png
[delete-confirmation-screenshot]: images/delete-confirmation.png
[admin-area-screenshot]: images/admin-area.png
[Django]: https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green
[Django-url]: https://www.djangoproject.com/
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
