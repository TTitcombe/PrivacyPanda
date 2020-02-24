# PrivacyPanda
**PrivacyPanda** is a package for detecting and removing personal, private data (such as names and addresses) from [**pandas**][pandas] dataframes.

## Why privacypanda
The volume of available information - personal, private information - of each and every one of us is vast and growing. This information can be used to build such a clear picture of who you are that bad actors can know you better than your partner does. In the wrong hands, this data can influence the way you shop, the way you vote, the way you think...

A necessary step to protect ourselves is to anonymize data - to strip it of any identifying features like our names or addresses. While many of the people handling private data are trustworthy, honest and ethical, we can't always trust that they will successfully scrub a dataset of any information which may be used against us.

`privacypanda` aims to make data anonymization a little bit easier by providing tools to detect identifying features in [`pandas`][pandas] dataframes and expunge them.

## How to install
`privacypanda` requires python of `3.7` or above and `pandas >= 1.0.0`.

To install `privacypanda`: clone the repository, navigate to the project folder and run `pip install -e .`

This local installation is currently the only way to install `privacypanda` for use in other projects. A pypi installation is coming soon.

## How to use
_Coming soon_

## Contributing
All contributions are important and welcomed. Please see the [contributing guide](./CONTRIBUTING.md) for more information.

## License
The **PrivacyPanda** project is licensed with Apache 2.0. Please refer to the [license](./LICENSE) for more information.


[pandas]: https://pandas.pydata.org/
