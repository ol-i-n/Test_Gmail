Feature: Gmail Login invalid password

  The user should be able to log into  Gmail account
  so that he can access emails and other Gmail features

  Background: 
    Given the user is on the email login page

   Scenario: Unsuccessful login with invalid password
    When the user provides the valid email
    And the user provides the invalid password
    Then the user should see an error message indicating incorrect password