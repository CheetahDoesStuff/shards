from shards import logger
from pathlib import Path

test_logger = logger("Test", do_log_saving=True, log_save_folder="tmp/log")

def test_log_messages():
    test_logger.raw("a")
    test_logger.info("info")
    test_logger.warn("warn")
    test_logger.error("error")
    test_logger.critical("critical")

    log_file = Path(test_logger.save_folder) / f"{test_logger.start_timestamp}.log"
    with open(log_file, "r") as f:
        lines = f.readlines()

    assert lines[0].strip() == "a"
    assert "[INFO] info" in lines[1]
    assert "[WARN] warn" in lines[2]
    assert "[ERROR] error" in lines[3]
    assert "[CRITICAL] critical" in lines[4]
