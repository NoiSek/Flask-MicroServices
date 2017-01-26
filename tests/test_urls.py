import pytest


from flask_microservices import (
    url,
    exceptions
)


def test_url_returns_valid_simple():
    _url = url(rule='/', view_func=lambda x: x)

    # Should return a namedtuple
    assert isinstance(_url, tuple)
    assert hasattr(_url, '_fields')

    # Should default to GET as a method
    assert _url.methods == ['GET']

    # Should not provide a name if not given one.
    assert _url.name is None


def test_url_returns_valid_complex():
    # Should still return correct values when provided unnamed arguments
    _url = url('/', lambda x: x)

    assert _url.view_func(1) == 1
    assert _url.methods == ['GET']
    assert _url.name is None

    # Should return correct values when provided a full list of unnamed arguments.
    _url = url('/', lambda x: x, 'home', ['GET', 'POST'])

    assert _url.view_func(3) == 3
    assert _url.methods == ['GET', 'POST']
    assert _url.name == 'home'

    # Should return correct values when provided a full list of named arguments.
    _url = url(rule='/', view_func=lambda x: x, name='_home', methods=['GET', 'POST', 'PUT'])

    assert _url.view_func(5) == 5
    assert _url.methods == ['GET', 'POST', 'PUT']
    assert _url.name == '_home'

    # Should return correct values when provided a mixture of named and unnamed arguments.
    _url = url('/', lambda x: x, name=None, methods=['GET', 'PUT'])

    assert _url.view_func(7) == 7
    assert _url.methods == ['GET', 'PUT']
    assert _url.name is None

def test_url_returns_invalid_simple():
    with pytest.raises(exceptions.InvalidURLRule):
        _url = url('', lambda x: x)

    with pytest.raises(exceptions.InvalidURLRule):
        _url = url(10, lambda x: x)

    with pytest.raises(exceptions.InvalidURLFunction):
        _url = url('/', 'hypothetical_function_name')

    with pytest.raises(exceptions.InvalidURLFunction):
        do = lambda x: x
        _url = url('/', do(10))

def test_url_returns_invalid_complex():
    with pytest.raises(exceptions.InvalidURLName):
        _url = url('/', lambda x: x, name=1)

    with pytest.raises(exceptions.InvalidURLName):
        _url = url('/', lambda x: x, name='')

    with pytest.raises(exceptions.UnspecifiedURLMethods):
        _url = url('/', lambda x: x, methods=[])

    with pytest.raises(exceptions.UnspecifiedURLMethods):
        _url = url('/', lambda x: x, methods=[''])

    with pytest.raises(exceptions.UnspecifiedURLMethods):
        _url = url('/', lambda x: x, methods='GET')

    with pytest.raises(exceptions.UnspecifiedURLMethods):
        _url = url('/', lambda x: x, methods=1)
