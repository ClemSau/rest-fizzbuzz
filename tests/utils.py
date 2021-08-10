def make_params(**params):
    return "&".join([f"{k}={v}" for k, v in params.items()])
