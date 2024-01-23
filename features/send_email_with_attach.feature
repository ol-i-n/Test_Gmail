Feature: Send Email with Attachments

  The user should to be able to send emails with attachments
  so that he can share files with his contacts

  Background:
    Given the user is logged in to their email account

  Scenario: Successfully attaching files and sending an email
    When the user clicks on the "Compose" button
    And the user fills in the "To" field with the recipient's email address
    And the user fills in the "Subject" field
    And the user writes the email body
    And the user upload the attachment
    And the user clicks on the "Send" button
    Then the user should see a confirmation that the email was sent