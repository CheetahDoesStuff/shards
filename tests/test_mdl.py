from shards import mdl

mdl = mdl(depth=2, size=3, default="cool")

def test_mdl_init():
    assert mdl.read(coords=(1, 1)) == "cool" # type: ignore

def test_mdl_init_full():
    assert mdl.full() == [['cool', 'cool', 'cool'], ['cool', 'cool', 'cool'], ['cool', 'cool', 'cool']] # type: ignore

def test_mdl_write():
    mdl.set(coords=(1, 1), val="cooler") # type: ignore
    
    assert mdl.read(coords=(1, 1)) == "cooler" # type: ignore
    assert mdl.read(coords=(1, 2)) == "cool" # type: ignore