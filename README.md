# docs-pod-browser
The repository for Inrupt PodBrowser documentation:
https://docs.inrupt.com/user-interface/podbrowser/

## To Build

To build:

0. Prereq: [python3](https://www.python.org/downloads/), [Node.js](https://nodejs.org/).

1. Optional but recommended. Create a virtual env.

   ```sh
   python3 -m venv <path to the new virtual environment>
   source <path to the new virtual environment>/bin/activate
   ```

1. Go to the cloned repo directory:

   cd <cloned repo dir>

1. Install the docs requirements (different from API docs requirements):

   ```sh
   pip install -r requirements.txt
   ```

1. Make the docs.

   ```sh
   make dirhtml
   ```

   There should be a `build/<branch>/dirhtml` directory with the html artifacts.

When finished, can deactivate your virtual env.

## Copyright

© Copyright 2021, Inrupt Inc.

## Third Party Licenses

The ``requirements.txt`` lists the 3rd party libraries used. For the
licenses, see the shared [inrupt/docs-assets](https://github.com/inrupt/docs-assets#readme).

