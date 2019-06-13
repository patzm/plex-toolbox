# `plex-scripts`
A loose collection of command line scripts to interact with a Plex Media Server (PMS)

## Installation
The easiest way to install this collection of scripts is with `pip`.
You can not use the latest version of `pip` though.
```bash
pip install git+https://github.com/patzm/plex-scripts#egg=plex-scripts
```

## Scripts
* `download-album`

### `download-album`

```text
USAGE: download-album [flags]

flags:
  --output_dir: Path to store the album in. Defaults to the album name in the current working directory.
  --server: The Plex server name
  --username: The Plex username / email
```


