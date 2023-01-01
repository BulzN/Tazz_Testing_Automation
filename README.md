# Tazz_Testing_Automation

Automation Framework in Python for the public site 'tazz.ro'

#### (Short Detail)
All the principles in which this project was based of can be transposed to other website's with ease

## Getting Started

These instructions will get you a copy of the project up and running on your local machine in order to verify the 
integrity of the given projects

### Prerequisites

You will need to install an Integrated Development Environment (IDE) in order to verify the project. I recommend the
PyCharm one, having a lot of features.
For sure, you will need Python installed on your device, I recommend Python 3.10

For windows:

```
C:\> python --version
Python 3.8.4
```

For macOS:

```
python3 --version
```

For all the listings of the Python versions (MacOS):
```
which -a python
```

It will check automatically if you have python installed on your system. If not, it will redirect you
to Microsoft Store or for an Apple type of device, I suggest going through the official website in order to get it downloaded. 
I recommend to install it through a full installer on an of the operating systems mentioned above
```
https://www.python.org/downloads/
```


### Installing

After that, we can get the code from GitHub directly though the HTTPS link cloning it, or just downloading the project and placing 
it where the IDE saves the project's

After that, we will need some libraries in order to properly test if the framework accomplishes its
task successfully

We will need to install Selenium, Pytest and Pytest-html. I have developed it in the Page Object Models format (POM)

```
pip install selenium
```

```
pip install pytest
```

```
pip install pytest-html
```

After all of this was set in order, we can start running the script tests

## Running the tests

In order to run the tests, we will need to execute in the IDE built-in terminal the following command:

```
pytest
```

The test cases where written so that they could be tested on the Google Chrome browser and Microsoft Edge browser.

In order to do so, it is required some drivers. They are already in the project. But, as time passes and browsers get
updated, the versions of this drivers will change with time. In order to properly run the tests, I strongly suggest 
to check the version of the browser and change the drivers corresponding to the latest version of it

* For Google Chrome:
```
https://chromedriver.chromium.org/downloads
```

* For Microsoft Edge:
```
https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
```

After that, you can start running the tests smoothly

In order to choose from which browser you can run the tests and get a report file from these, run the following commands:
* Google Chrome:
```
pytest --browser_name=Chrome --html=report_chrome.html
```
* Microsoft Edge:
```
pytest --browser_name=Edge --html=report_edge.html
```


### The break-down into end-to-end tests

This tests are done in order to verify the full integrity and operability of the website 'tazz.ro'.

From where a user could selected a certain item from a menu

```
        # SCROLLING SCRIPT
        ref = self.reference_pizza
        coord = ref.location_once_scrolled_into_view
        self.driver.execute_script('window.scrollTo({}, {});'.format(coord['x'], coord['y']))
        time.sleep(3)
        # END OF SCROLLING SCRIPT

        self.choose_belly.click()
        time.sleep(2)

        ref2 = self.second_reference_pizza
        coord = ref2.location_once_scrolled_into_view
        self.driver.execute_script('window.scrollTo({}, {});'.format(coord['x'], coord['y']))
        time.sleep(3)

        self.choose_second_belly.click()
        time.sleep(2)
        self.select_final_both_btn.click()
        time.sleep(2)
```

To registering a new account


## Built With

* [Selenium](https://www.selenium.dev) - The web framework used
* [Github](https://github.com) - Git repository hosting used
* [Git](https://git-scm.com) - Version Control System used


## Authors

* **Bulzan Alex Călin** - *Initial work* - [BulzN](https://github.com/BulzN)

## License

This project is not licensed under any license

## Acknowledgments

* Mihai Postu - Trainer - ITSchool
* Colleagues from the ITSchool course
* To all the free open-source explanations from the web
