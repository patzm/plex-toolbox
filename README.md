# `plex-toolbox`
A loose collection of command line scripts to interact with a Plex Media Server (PMS)

## Installation
The easiest way to install this collection of scripts is with `pip`.
You can not use the latest version of `pip` though.
```bash
pip install git+https://github.com/patzm/plex-toolbox
```

If this is done inside a `virtualenv`, all scripts have been installed to the `PATH`.
They can then directly be used from the command line.
Otherwise, make sure that the `bin` folder of the used `pip` distribution is in the `PATH`.
For instance, installing with `pip install --user ...` will usually install into `~/.local/bin`.

## Scripts
* `download-album`

### `download-album`

```text
usage: download-album [-h] --server SERVER --username USERNAME [-o OUTPUT_DIR]

optional arguments:
  -h, --help            show this help message and exit
  --server SERVER       The Plex server name
  --username USERNAME   The Plex username / email
  -o OUTPUT_DIR, --output-dir OUTPUT_DIR
                        Path to store the album in. Defaults to the album name
                        in the current working directory.
```


