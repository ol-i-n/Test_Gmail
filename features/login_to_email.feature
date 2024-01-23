Feature: Gmail Login

  The user should be able to log into  Gmail account
  So that he can access emails and other Gmail features

  Background: 
    Given the user is on the email login page

  Scenario: Verify login with valid email and password
    When the user provides the valid email
    And the user provides the valid password
    Then the user should be logged in and see their mailbox
