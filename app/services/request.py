
import requests as req
from ..core import log

def get(**kwargs):
    log.info(f"{kwargs['url']}")
    try:
        url = kwargs['url']
        response = req.get(
            url, 
            headers=kwargs.get("headers", None), 
            params=kwargs.get("params", None)
        )
        log.info(f"{response}")
        response.raise_for_status()
        result = response.json()
    except req.exceptions.RequestException as e:
        raise e
    except Exception as e:
        raise e
    return result

def post(**kwargs):
    log.info(f"{kwargs['url']}")
    try:
        url = kwargs['url']
        response = req.post(
            url, 
            headers=kwargs.get("headers", None), 
            params=kwargs.get("params", None),
            json=kwargs.get("json", None),
            data=kwargs.get("data", None),
            files=kwargs.get("files", None),
        )
        log.info(f"{response.json()}")
        response.raise_for_status()
        result = response.json()
    except req.exceptions.RequestException as e:
        raise e
    except Exception as e:
        raise e
    return result

def delete(**kwargs):
    log.info(f"{kwargs['url']}")
    try:
        url = kwargs['url']
        response = req.delete(
            url, 
            headers=kwargs.get("headers", None), 
            params=kwargs.get("params", None)
        )
        log.info(f"{response}")
        response.raise_for_status()
        result = response.json()
    except req.exceptions.RequestException as e:
        raise e
    except Exception as e:
        raise e
    return result