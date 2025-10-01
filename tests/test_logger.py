from shards import sLogger
from pathlib import Path

logger = sLogger("Test", do_log_saving=True, log_save_folder="tmp/log")

def test_log_messages():
    logger.raw("a")
    logger.info("info")
    logger.warn("warn")
    logger.error("error")
    logger.critical("critical")

    log_file = Path(logger.save_folder) / f"{logger.start_timestamp}.log"
    with open(log_file, "r") as f:
        lines = f.readlines()

    assert lines[0].strip() == "a"
    assert "[INFO] info" in lines[1]
    assert "[WARN] warn" in lines[2]
    assert "[ERROR] error" in lines[3]
    assert "[CRITICAL] critical" in lines[4]
