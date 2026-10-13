# Orange3-DeepSeek-Constructor

DeepSeek add-on for [Orange3](https://orangedatamining.com/) data mining software.

Adds a **DeepSeek Constructor** widget that calls the DeepSeek API to construct
a new text column (e.g. generated responses) from an existing text variable.

## Widgets

- **DeepSeek Constructor** — reads a text column from the input data, sends each
  instance to DeepSeek with user-defined prompt start/end, and outputs the data
  with a new "DeepSeek Response" meta column.

## Installation

From Orange: `Options → Add-ons…` → check *Orange3-DeepSeek-Constructor* → OK.

Or with pip (use the Python environment that Orange uses):

```bash
pip install Orange3-DeepSeek-Constructor
```

## Usage

1. Place a **File** widget, load a dataset containing a text column.
2. Connect it to **DeepSeek Constructor** (category: *DeepSeek*).
3. Paste your [DeepSeek API key](https://platform.deepseek.com/), choose a model,
   select the text variable and write your prompt.
4. Click **Apply**. Connect the output to a **Data Table** to inspect the
   "DeepSeek Response" column.

The API key is stored with Orange's credential manager, never in the workflow.

## License

MIT
