# selenium-daemon

Run selenium tests faster by spawning a background process that you
can re-use between test runs.

# Installation

```sh
pip install selenium-daemon
```

# Running the daemon

```sh
selenium-daemon &
```

This is beta software!  you're in charge of starting, backgrounding
your own tasks, etc.


# Usage

```python
import seleniumdaemon

class MyTest(unittest.TestCase):

    def test_stuff(self):
        driver = seleniumdaemon.attach()
        driver.get('http://www.duckduckgo.com')
        self.assertIn('Duck', driver.title)
```


# With pytest

```python
# in conftest.py

import seleniumdaemon
@pytest.fixture:
def driver():
      return seleniumdaemon.attach()

# in your tests
def test_stuff(driver):
    driver.get('http://www.duckduckgo.com')
    assert 'Duck' in driver.title
```


# Tips:

To prevent shared state from spilling over between sessions, you probably
want to clear cookies at least, before or after each test.

```python
driver.clear_cookies()
```
