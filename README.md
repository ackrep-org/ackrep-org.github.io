# ackrep-org.github.io

This repo contains the sources (markdown-content, themes, download files), and the built result of the ackrep landing page.


The rendered page is available at: <https://ackrep-org.github.io> and <http://ackrep.org> (https certificate yet in progress).


## How to built

### Preparation

- Run `pip install -r requirements.txt`
- Note that the most files in the repo root dir were created by `pelican quickstart`. Some files were changed manually:
    - `Makefile` (specify `$OUTPUTDIR`)
    - `pelicanconf.py` (everything after `# *******`)

### Local testing:

- `pelican -lr` # starts a local webserver and makes pelican to regenerate after changes in content or templates

### Building for publication

- Commit your changes to the content and theme (but not yet the the content of `doc`).
- Run `make publish`
- Ensure that you are on the default branch of the repo (i.e. `main`).
- `git add doc/`
- `git commit -m "publication"`
- `git push origin`
