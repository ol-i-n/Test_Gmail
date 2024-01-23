Feature: Email logout
  
  The user should be able to logout of his email account

  Background: 
    Given the user is logged in to their email account

  Scenario: Verify logout
    When the user click on profile picture button
    And the user click on Log out button
    Then the user should be logout and redirected to the email welcome page