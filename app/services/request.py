import logging
import requests as req

logger = logging.getLogger(__name__)

def get(**kwargs):
    logger.info(f"{kwargs['url']}")
    try:
        url = kwargs['url']
        response = req.get(
            url, 
            headers=kwargs.get("headers", None), 
            params=kwargs.get("params", None)
        )
        logger.info(f"{response}")
        response.raise_for_status()
        result = response.json()
    except req.exceptions.RequestException as e:
        raise e
    except Exception as e:
        raise e
    return result

def post(**kwargs):
    logger.info(f"{kwargs['url']}")
    try:
        url = kwargs['url']
        response = req.get(
            url, 
            headers=kwargs.get("headers", None), 
            params=kwargs.get("params", None),
            data=kwargs.get("data", None),
            files=kwargs.get("files", None),
        )
        logger.info(f"{response}")
        response.raise_for_status()
        result = response.json()
    except req.exceptions.RequestException as e:
        raise e
    except Exception as e:
        raise e
    return result