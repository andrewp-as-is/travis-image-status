#!/usr/bin/env bash
{ set +x; } 2>/dev/null

set -- travis-ci/travis-api
( set -x; travis-image-status "$@" )
