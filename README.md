<!--
https://pypi.org/project/readme-generator/
https://pypi.org/project/python-readme-generator/
-->

[![](https://img.shields.io/badge/OS-Unix-blue.svg?longCache=True)]()
[![](https://img.shields.io/pypi/v/travis-image-status.svg?maxAge=3600)](https://pypi.org/project/travis-image-status/)
[![](https://img.shields.io/npm/v/travis-image-status.svg?maxAge=3600)](https://www.npmjs.com/package/travis-image-status)
[![Travis](https://api.travis-ci.org/looking-for-a-job/travis-image-status.svg?branch=master)](https://travis-ci.org/looking-for-a-job/travis-image-status/)

#### Installation
```bash
$ [sudo] npm i -g travis-image-status
```
```bash
$ [sudo] pip install travis-image-status
```

#### Benefits
+   no need travis client/authorization
+   **2-10x faster** than `travis status`

#### How it works
`https://api.travis-ci.org/owner/repo.svg?branch=master`

```xml
<svg ...<text>{status}</text></g></svg>
```

#### Scripts usage
```bash
usage: travis-image-status [options] repo
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

#### Related projects
+   [`travis-cron` - travis cron management](https://pypi.org/project/travis-cron/)
+   [`travis-env` - travis environment variables management](https://pypi.org/project/travis-env/)
+   [`travis-exec` - execute command for every travis repo](https://pypi.org/project/travis-exec/)
+   [`travis-generator` - `.travis.yml` generator](https://pypi.org/project/travis-generator/)
+   [`travis-image-status` - quickly get travis status from an image](https://pypi.org/project/travis-image-status/)

<p align="center">
    <a href="https://pypi.org/project/python-readme-generator/">python-readme-generator</a>
</p>