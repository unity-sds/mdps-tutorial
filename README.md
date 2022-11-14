<!-- Header block for project -->
<hr>

<div align="center">

![logo](https://user-images.githubusercontent.com/3129134/163255685-857aa780-880f-4c09-b08c-4b53bf4af54d.png)

<h1 align="center">SoundedSIPS Tutorial</h1>
<!-- ☝️ Replace with your repo name ☝️ -->

</div>

<pre align="center">A Unity SDS quickstart for SounderSIPS personnel.</pre>
<!-- ☝️ Replace with a single sentence describing the purpose of your repo / proj ☝️ -->

<!-- Header block for project -->

[INSERT YOUR BADGES HERE (SEE: https://shields.io)] [![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](code_of_conduct.md) [![SLIM](https://img.shields.io/badge/Best%20Practices%20from-SLIM-blue)](https://nasa-ammos.github.io/slim/)
<!-- ☝️ Add badges via: https://shields.io e.g. ![](https://img.shields.io/github/your_chosen_action/your_org/your_repo) ☝️ -->

[INSERT SCREENSHOT OF YOUR SOFTWARE, IF APPLICABLE]
<!-- ☝️ Screenshot of your software (if applicable) via ![](https://uri-to-your-screenshot) ☝️ -->

This tutorial is meant to allow the SounderSIPS team to get up and running in the Unity Science Data System environment and begin using Unity services.
<!-- ☝️ Replace with a more detailed description of your repository, including why it was made and whom its intended for.  ☝️ -->

[Docs/Wiki](https://unity-sds.gitbook.io/docs/) | [Issue Tracker](https://github.com/unity-sds/sounder-sips-tutorial/issues)

## Features

* [INSERT LIST OF FEATURES IMPORTANT TO YOUR USERS HERE]
  
<!-- ☝️ Replace with a bullet-point list of your features ☝️ -->

## Contents

* [Quick Start](#quick-start)
* [Changelog](#changelog)
* [FAQ](#frequently-asked-questions-faq)
* [Contributing Guide](#contributing)
* [License](#license)
* [Support](#support)

## Quick Start

This guide provides a quick way to get started with our project. Please see our [docs](https://unity-sds.gitbook.io/docs/user-docs/unity-cloud/getting-started) for a more comprehensive overview.

### Requirements

* [INSERT LIST OF REQUIREMENTS HERE]
* Access to Unity JupyterHub environment, available at: [INSERT URL]  
  
<!-- ☝️ Replace with a numbered list of your requirements, including hardware if applicable ☝️ -->

### Setup Instructions

Once you've ensured you've met the requirements above - including having access to the Unity Jupyter Hub environement - you can follow the below setup instructions.

In Jupyter Hub, we want to start a new terminal process. After logging in, the launcher allows us to open a new terminal:

![jupyterlab launcher](/img/jl_01.png)

Specifically, the 'terminal' icon under 'Other':

![terminal icon](/img/jl_02.png)

Double click this to open a new terminal. Once the terminal is open, enter the following command to clone the tutorial repository to your local environment. Once it's in the local environment, you can modify or change anything you'd like without affecting the tutorials in the github repository.

```
jovyan@jupyter-gangl:~$
git clone https://github.com/unity-sds/sounder-sips-tutorial.git
```

**Note** if you receive an error like the following:
```
bash: git: command not found
```
it means the environment you have setup does not have the git command line installed. This usually happens when using the *minimal* environment in jupyter. To fix this, you can run the following command:

```
conda install git
```

and re-run the command.

After a few seconds, you should see a folder called 'sounder-sips-tutorial' in the file navigator on the left hand side:

![tutorial folder](/img/jl_03.png)

Simply double click on that folder to view the contents of the repository within your own jupyter environment. To access the welcome notebook, click:

```
sounder-sips-tutorial > jupyter-notebooks > welcome.ipynb
```
   
<!-- ☝️ Replace with a numbered list of how to set up your software prior to running ☝️ -->

### Running the Tutorials Instructions

After completing the above setup steps, to access and follow along a specific tutorial, click:

```
sounder-sips-tutorial > jupyter-notebooks > tutorials
```

You are now free to follow along with the tutorials.

<!-- ☝️ Replace with a numbered list of your run instructions, including expected results ☝️ -->

### Usage Examples

* [INSERT LIST OF COMMON USAGE EXAMPLES HERE, WITH OPTIONAL SCREENSHOTS]

<!-- ☝️ Replace with a list of your usage examples, including screenshots if possible, and link to external documentation for details ☝️ -->

### Building the Tutorials Instructions (if applicable)

1. [INSERT STEP-BY-STEP BUILD INSTRUCTIONS HERE, WITH OPTIONAL SCREENSHOTS]

<!-- ☝️ Replace with a numbered list of your build instructions, including expected results / outputs with optional screenshots ☝️ -->

### Testing the Tutorials Instructions (if applicable)

1. [INSERT STEP-BY-STEP TEST INSTRUCTIONS HERE, WITH OPTIONAL SCREENSHOTS]

<!-- ☝️ Replace with a numbered list of your test instructions, including expected results / outputs with optional screenshots ☝️ -->

## Changelog

See our [CHANGELOG.md](CHANGELOG.md) for a history of our changes.

<!-- ☝️ Replace with links to your changelog and releases page ☝️ -->

## Frequently Asked Questions (FAQ)

Questions about our project? Please see our: [FAQ](https://unity-sds.gitbook.io/docs/getting-help/faq)

<!-- ☝️ Replace with a list of frequently asked questions from your project, or post a link to your FAQ on a discussion board ☝️ -->

## Contributing

Interested in contributing to our project? Please see our: [CONTRIBUTING.md](CONTRIBUTING.md)

## License

See our: [LICENSE](LICENSE)

## Support

Key points of contact are: [@anilnatha](https://github.com/anilnatha) [@rtapella](https://github.com/rtapella)

<!-- ☝️ Replace with the key individuals who should be contacted for questions ☝️ -->
