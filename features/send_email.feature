Feature: Send Email with Attachment

  The user should be able to send an email
  
  Background:
    Given the user is logged into their Gmail account

  Scenario: Successfully sending an email
    When the user clicks on the "Compose" button
    And the user fills in the "To" field with the recipient's email address
    And the user fills in the "Subject" field
    And the user writes the email body
    And the user clicks on the "Send" button
    Then the user should see a confirmation that the email was sent