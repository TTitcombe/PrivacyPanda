# Contributing

Thank you for contributing to `privacypanda`. Feel free to open an issue reporting a bug
or requesting a new feature.

If you would like to contribute code but don't know where to start,
please see the [open issues](https://github.com/TTitcombe/PrivacyPanda/issues).

When opening a pull request,
please read the information below.

`privacypanda` is in the early stage of development,
so all contributions will play a significant part in shaping the project.

### Environment
If you are using [conda] you can get the correct development environment by running
the command

```python
conda env create -n privacypanda-dev -f environment.yml
```

### Code quality
`privacypanda` uses [`black`][black] to format code and [`isort`][isort] to maintain clean
import statements.
Make sure you run these packages on your code changes otherwise the tests will fail.

You can either run these manually or use [`pre-commit`][precommit] to automatically check the on each commit.
[`pre-commit`][precommit] is included in the [conda] environment.
With [`pre-commit`][precommit] installed,
run `pre-commit install` when in the `privacypanda` project folder to setup.

Where possible,
please use [type hints](https://docs.python.org/3/library/typing.html).

### Tests
We use GitHub CI will be used for testing.
For a new feature or bug fix,
please add a [unit test][tests].


### Pull requests
When working on new code,
please fork `privacypanda` and make a branch off your fork's master branch.
Push your work to your fork and open a pull request from there.

Use the pull request template where possible. The important things to include are:
1. What the pull request does
2. Which issues, if any, are being fixed by the PR (e.g. `Fixes #4`)
3. Which tests were added to test the new feature / bug fix
4. How to manually confirm that your code is working as you expect it to

[black]: https://github.com/psf/black
[conda]: https://www.anaconda.com/
[isort]: https://github.com/search?q=isort
[precommit]: https://github.com/pre-commit/pre-commit

[tests]: tests/
