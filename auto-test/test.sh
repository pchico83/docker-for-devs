#!/bin/bash

sleep 3
if curl web:5000 | grep -q 'Hola Openwebinars!'; then
  echo "Tests passed!"
  exit 0
else
  echo "Tests failed!"
  exit 1
fi