class InvalidModulePath(Exception):
  """Raised when an invalid module path is provided to
  `MicroServicesApp.register_urls()`
  """

  pass


class InvalidURLFunction(Exception):
  """Raised when a url is passed a non-function value.
  """

  pass


class InvalidURLPattern(Exception):
  """Raised when a non `flask_microservices.url` value is
  given as a URLPattern.
  """

  pass

class InvalidURLRule(Exception):
  """Raised when a non-string value is passed as a rule.
  """

  pass

class InvalidURLName(Exception):
  """Raised when a non-string value is passed as a name.
  """

  pass

class UnspecifiedURLMethods(Exception):
  """Raised when an empty list, or a list of blank strings
   is passed as a method.
  """

  pass
