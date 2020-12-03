<!--
https://readme42.com
-->



[![](https://img.shields.io/badge/OS-Unix-blue.svg?longCache=True)]()
[![](https://img.shields.io/pypi/v/travis-image-status.svg?maxAge=3600)](https://pypi.org/project/travis-image-status/)
[![](https://img.shields.io/npm/v/travis-image-status.svg?maxAge=3600)](https://www.npmjs.com/package/travis-image-status)[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/travis-image-status/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/travis-image-status/actions)

### Installation
```bash
$ [sudo] pip install travis-image-status
```

```bash
$ [sudo] npm i -g travis-image-status
```

#### How it works
`https://api.travis-ci.org/owner/repo.svg?branch=master`

```xml
<svg ...<text>{status}</text></g></svg>
```

#### Examples
`travis status`:
```bash
$ travis status -r owner/repo
passed
```

`travis-image-status`:
```bash
$ travis-image-status owner/repo
passing
```


options. `--com`, `--org` (default):
```bash
$ travis-image-status --com owner/repo
```

#### Related
+   [`travis-cron` - travis cron management](https://pypi.org/project/travis-cron/)
+   [`travis-env` - travis environment variables management](https://pypi.org/project/travis-env/)
+   [`travis-exec` - execute command for every travis repo](https://pypi.org/project/travis-exec/)
+   [`travis-generator` - `.travis.yml` generator](https://pypi.org/project/travis-generator/)
+   [`travis-image-status` - quickly get travis status from an image](https://pypi.org/project/travis-image-status/)

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>
