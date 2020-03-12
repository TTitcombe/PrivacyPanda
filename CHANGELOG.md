# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0] - 2020-03-10
### Added
* Identify simple addresses
    - Up to a four digit building number + street name + street suffix
    - "street", "road", "avenue", "way", "st", "rd", "ave", "wy" are accepted suffixes
* Identify UK postcodes
    - Two characters, 1 or 2 digits, space, 1 digit, 2 characters
    - No validation of postcodes is carried out
* Identify UK mobile numbers
    - "+447" or "07" followed by 9 digits
* Identify simple emails
    - Emails containing an "@" and ending in one of ".com", ".co.uk", ".org", ".edu"
    - Extended suffixes will come later
* Basic reporting structure
    - Can print a report of privacy breaching columns in a dataframe and their breach type
* Function to remove columns containing at least one privacy breach from the dataframe

[Unreleased]: https://github.com/TTitcombe/PrivacyPanda/compare/0.1.0...HEAD
[0.1.0]: https://github.com/TTitcombe/PrivacyPanda/releases/tag/0.1.0
