#!/usr/bin/env bash

RESULT=$((1 + $RANDOM % 2))

if [ ${RESULT} -eq "1" ]; then
  echo "Test stage failed"
  exit 1
else
  echo "Test stage success"
fi
