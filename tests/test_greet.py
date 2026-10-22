from verify_cc.greet import greet


def test_greet() -> None:
    assert greet("world") == "hello world"
