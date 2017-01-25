from flask_microservices import (
  MicroServicesApp,
  MicroServicesLoader,
  Router,
  url,
  exceptions
)

def test(x):
  return True

def test_answer():
  assert test(True) == True
