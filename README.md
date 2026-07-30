# PY Live Internet Speed

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.x](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![CI](https://github.com/webkolog/py-live-internet-speed/actions/workflows/python-tests.yml/badge.svg)](https://github.com/webkolog/py-live-internet-speed/actions)

**Version:** 1.0

**Created Date:** 2026-09-01

**Last Updated:** 2026-09-01

**Compatibility:** Python 3.x

**Created By:** Ali Candan ([@webkolog](https://github.com/webkolog))

**Website:** [http://webkolog.net](http://webkolog.net)

**Copyright:** (c) 2026 Ali Candan

**License:** MIT License ([http://mit-license.org](http://mit-license.org))

**PY Live Internet Speed** is a Python tool that measures your real-time internet download speed and visualizes the result directly in an interactive, web-based gauge chart using Plotly.

## Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/webkolog/py-live-internet-speed.git
cd py-live-internet-speed

```

Install the required Python packages:

```bash
pip install speedtest-cli plotly

```

## Usage

Run the main script to initiate the speed test and display the gauge chart:

```bash
python py-live-internet-speed.py

```

### How It Works

1. **Speed Test Initialization:** The script connects to the nearest optimal server using `speedtest-cli`.
2. **Measurement:** Performs a download speed test and converts the result from bits per second to Megabits per second (Mbps).
3. **Visualization:** Generates an interactive Plotly gauge chart configured for speeds between 0 and 300 Mbps and opens it in your default browser.

## Code Structure

`py-live-internet-speed.py`:

```python
# Live Internet Speed
import plotly.graph_objects as go
import speedtest

s = speedtest.Speedtest()
speed = round(s.download() / 1e6, 2)

fig = go.Figure(
    go.Indicator(
        mode="gauge+number",
        value=speed,
        title={"text": "Download Speed (Mbps)"},
        gauge={"axis": {"range": [0, 300]}},
    )
)
fig.show()

```

## Customization

* **Gauge Range:** To adjust the maximum speed shown on the gauge (e.g., for gigabit connections up to 1000 Mbps), update the `range` parameter in the script:
```python
gauge={'axis': {'range': [0, 1000]}}

```



## Dependencies

* **[speedtest-cli](https://pypi.org/project/speedtest-cli/):** Command-line interface for testing internet bandwidth using speedtest.net.
* **[plotly](https://plotly.com/python/):** Graphing library for interactive, publication-quality graphs.

## License

This project is open-source software licensed under the [MIT License](https://mit-license.org/).

## Contributing

Contributions are welcome! If you encounter any bugs or have suggestions for improvements, feel free to open an issue or submit a pull request on the GitHub repository.

## Support

For questions or support regarding PY Live Internet Speed, feel free to check the project's GitHub repository or contact the author at [webkolog.net](http://webkolog.net).

```

---

**LICENSE**

```text
MIT License

Copyright (c) 2026 Ali Candan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

```
