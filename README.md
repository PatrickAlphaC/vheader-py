# vheader

Generate perfect Vyper code headers every time, pythonically.

> [!NOTE]  
> [There is also a version of this in rust.](https://github.com/PatrickAlphaC/vheader)


# Getting Started 

## Prerequisites

You need to be able to install python packages, with either:
- [pip](https://pypi.org/project/pip/)
- [uv](https://docs.astral.sh/)
- [pipx](https://github.com/pypa/pipx)

Or whatever you prefer to install python packages. We recommend using `uv`. You can head over to their docs, or try to run:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

To install. 

## Installation

We prefer to install this into an insolated virtual environment with `uv`. You can do that as so:

```bash
uv tool install vheader
```

But you can also install any other way you please:

```bash
pip install vheader
pipx install vheader
```

## Usage

```sh
vheader "external functions"
```

```python
# ------------------------------------------------------------------
#                       EXTERNAL FUNCTIONS
# ------------------------------------------------------------------
```

It will also copy the header to your clipboard automatically.

### With VSCode

Set your global [`tasks.json`](https://stackoverflow.com/questions/41046494/making-global-tasks-in-vs-code) like so to add the command as task:

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Generate Header",
      "type": "shell",
      "command": "vheader ${input:header}",
      "presentation": {
        "reveal": "never"
      },
      "problemMatcher": []
    }
  ],
  "inputs": [
    {
      "id": "header",
      "description": "Header",
      "type": "promptString"
    }
  ]
}
```

To really speed-up your workflow, you can even add a keybind for the task in [`keybindings.json`](https://code.visualstudio.com/docs/getstarted/keybindings):

```json
[
  {
    "key": "CMD+h",
    "command": "workbench.action.tasks.runTask",
    "args": "Generate Header"
  }
]
```

This will copy the generated header to your clipboard.

## Credits

- Inspired by [transmissions11 headers](https://github.com/transmissions11/headers)
  - Who was inspired by virtualjpeg's [`blocky`](https://github.com/virtualjpeg/blocky).
