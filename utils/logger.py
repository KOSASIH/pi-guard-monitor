import logging.config
import yaml

def setup_logger(logger_name, log_file, level=logging.INFO):
    with open('logging.yaml', 'rt') as f:
        log_cfg = yaml.safe_load(f.read())
    log_cfg['handlers']['file']['filename'] = log_file
    logging.config.dictConfig(log_cfg)
    logger = logging.getLogger(logger_name)
    logger.setLevel(level)
    return logger
