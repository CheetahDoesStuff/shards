from shards import sLogger

logger = sLogger("Test", do_log_saving=True, log_save_folder="out/logs")

def test_log_messages():
    logger.raw("a")
    with open(f"out/logs/{logger.start_timestamp}", "r") as f:
        lines = f.readlines()

    assert lines[0] == "a"