Feature: Gmail Login invalid name

  The user should be able to log into  Gmail account
  so that he can access emails and other Gmail features

  Background: 
    Given the user is on the email login page

  Scenario: Unsuccessful login with invalid username
    When the user provides the invalid email
    Then the user should see an error message indicating invalid username
