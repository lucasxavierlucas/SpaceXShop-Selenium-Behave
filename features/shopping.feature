Feature: SpaceX Shop - Add Mugs to Cart

  Scenario: Add two Occupy Mars mugs to the cart and validate the total cost
    Given I navigate to the SpaceX shop
    When I add two "Occupy Mars Mug" to the cart
    Then The total cost should be 40.00