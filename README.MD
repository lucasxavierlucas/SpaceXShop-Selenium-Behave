# SpaceXShopCheckout Automation, Python + Selenium + Behave

This project uses Python with Selenium and Behave to automate the process of adding two “Occupy Mars” mugs to the cart on the SpaceX shop website. So, we can relax with a hot coffee while discussing rocket engineering.


## Technologies Used

- Python
- Behave
- Selenium

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/SpaceXShopCheckout.git
    cd SpaceXShopCheckout
    ```
   
2. Set up a virtual environment:
    ```sh
    python -m venv venv
    ```

4. Activate the virtual environment:

    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS and Linux:
        ```sh
        source venv/bin/activate
        ```

5. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

## Running the Tests

To run the tests, use the following command:
```sh
behave
```

## Project Structure

- `features/steps/shopping_steps.py`: Contains the step definitions for the Behave tests.
- `page_objects/`: Contains the page object classes for different pages of the SpaceX shop.