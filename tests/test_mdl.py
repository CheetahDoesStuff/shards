from shards import mdl

def test_default_values():
    arr = mdl(depth=2, size=3, default=0)
    expected = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]
    assert arr.data == expected

def test_get_specific_item():
    arr = mdl(depth=2, size=3, default="cool")
    assert arr[1, 2] == "cool"
    assert arr[0, 0] == "cool"

def test_changing_values():
    arr = mdl(depth=2, size=3, default=[])
    arr[1, 1] = ["coolest"]
    assert arr[1, 1] == ["coolest"]
    assert arr[0, 0] == []
    assert arr[1, 0] == []
