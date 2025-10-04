from shards import mdl

def test_init_default_structure():
    arr = mdl(depth=2, size=3, default="x")
    expected = [
        ["x", "x", "x"],
        ["x", "x", "x"],
        ["x", "x", "x"],
    ]
    assert arr.data == expected

def test_single_index_access():
    arr = mdl(depth=2, size=3, default=0)
    row = arr[1]
    assert row == [0, 0, 0]

def test_tuple_index_access():
    arr = mdl(depth=2, size=3, default="cool")
    assert arr[1, 2] == "cool"
    assert arr[0, 0] == "cool"

def test_depth_3_structure():
    arr = mdl(depth=3, size=2, default=7)
    expected = [
        [
            [7, 7],
            [7, 7],
        ],
        [
            [7, 7],
            [7, 7],
        ]
    ]
    assert arr.data == expected
    assert arr[0, 1, 1] == 7
    assert arr[1, 0, 0] == 7

def test_independent_lists():
    arr = mdl(depth=2, size=3, default=[])
    assert arr[0, 0] is not arr[0, 1]
    assert arr[0, 0] is not arr[1, 0]

def test_size_one_depth_one():
    arr = mdl(depth=1, size=1, default="only")
    assert arr.data == ["only"]
    assert arr[0] == "only"

def test_large_depth_and_size():
    arr = mdl(depth=4, size=2, default=1)
    assert arr[1, 1, 1, 1] == 1
    assert len(arr.data) == 2
