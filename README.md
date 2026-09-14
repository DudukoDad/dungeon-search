<a id="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![project_license][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Dudukodad/dungeon-search">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Dungeon Search</h3>

  <p align="center">
    An LLM powered search tool for Dungeon Masters and Players alike
    <br />
    <a href="https://github.com/Dudukodad/dungeon-search"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Dudukodad/dungeon-search">View Demo</a>
    &middot;
    <a href="https://github.com/Dudukodad/dungeon-search/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    &middot;
    <a href="https://github.com/Dudukodad/dungeon-search/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
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
I love Dungeons and Dragons, but if you're like me - your spaghetti brain makes it hard to keep track of campaign lore or character sheets. Especially, as games progress and more documents are added, things can get pretty dicey. This tool provides a way to caterogize and easily retrieve helpful information without having to go searching through all your docs. 

This tool uses Retrieval Augmented Generation to find information regarding your campaign quickly and packages it in an easy to interpret way. It can be used 100% local and offline (If you use a locally Hosted LLM service using Ollama or LM studio), so your data is protected and you're not using up all of our dang water (Your computer might have to work a little harder though). 


This is a tool that players and DMs alike may find useful. If you love it (or hate it), I'd love to know! 

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python]][Python-url]
* [![SQLite][SQLite]][SQLite-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

Install Dependencies
* npm
  ```sh
  npm install npm@latest -g
  ```

### Installation

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/Dudukodad/dungeon-search.git
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your LLM of choice's URL and API key in `.env`
   ```python
   LOCAL_LLM='http://localhost:1234/v1'
   LLM_MODEL='hermes-3-llama-3.1-8b'
   ```
5. Change git remote url to avoid accidental pushes to base project
   ```sh
   git remote set-url origin Dudukodad/dungeon-search
   git remote -v # confirm the changes
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

# TODO

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Basic RAG implementation
- [ ] MCP Server 
- [ ] Google Docs Integration
- [ ] Standalone Voice Chat Feature
    - [ ] Nested Feature

See the [open issues](https://github.com/Dudukodad/dungeon-search/issues) for a full list of proposed features (and known issues).

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

### Top contributors:

<a href="https://github.com/Dudukodad/dungeon-search/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=Dudukodad/dungeon-search" alt="contrib.rocks image" />
</a>



<!-- LICENSE -->
## License

Distributed under the project_license. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [@twitter_handle](https://twitter.com/twitter_handle) - email@email_client.com

Project Link: [https://github.com/Dudukodad/dungeon-search](https://github.com/Dudukodad/dungeon-search)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* []()
* []()
* []()

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/Dudukodad/dungeon-search.svg?style=for-the-badge
[contributors-url]: https://github.com/Dudukodad/dungeon-search/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Dudukodad/dungeon-search.svg?style=for-the-badge
[forks-url]: https://github.com/Dudukodad/dungeon-search/network/members
[stars-shield]: https://img.shields.io/github/stars/Dudukodad/dungeon-search.svg?style=for-the-badge
[stars-url]: https://github.com/Dudukodad/dungeon-search/stargazers
[issues-shield]: https://img.shields.io/github/issues/Dudukodad/dungeon-search.svg?style=for-the-badge
[issues-url]: https://github.com/Dudukodad/dungeon-search/issues
[license-shield]: https://img.shields.io/github/license/Dudukodad/dungeon-search.svg?style=for-the-badge
[license-url]: https://github.com/Dudukodad/dungeon-search/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/christian-dudukovich/
[product-screenshot]: images/screenshot.png
<!-- Shields.io badges. You can a comprehensive list with many more badges at: https://github.com/inttter/md-badges -->
[Python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org/

[SQLite]: https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=python&logoColor=ffdd54
[SQLite-url]: https://sqlite.org/