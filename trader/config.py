import os
import yaml


CONFIG_FILE     = 'config.yaml'
CONFIG_FOLDER   = 'conf.d'

env = os.environ


def load_config():
    app_root = os.path.abspath(env.get('APP_ROOT'))
    path = os.path.join(app_root, CONFIG_FOLDER, CONFIG_FILE)
    with(open(path)) as config:
        cfg = yaml.load(config.read())

    return cfg


cfg = load_config()
