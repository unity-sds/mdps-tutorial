import requests

from . import settings

def get_apps(token):
    
    try:
        headers = _get_headers(token)
        response = requests.get(settings.WPST_API_DOMAIN + "/processes", headers=headers)
        response.raise_for_status()
        json_result = response.json()['processes']
        
    except requests.exceptions.HTTPError as e:
        # Add Logging Mechanism
        raise
        
    return json_result

def get_application(token, app_name):

    try:
        headers = _get_headers(token)
        response = requests.get(settings.WPST_API_DOMAIN + "/processes/{}".format(app_name), headers=headers)
        response.raise_for_status()
        json_result = response.json()['process']
        
    except requests.exceptions.HTTPError as e:
        # Add Logging Mechanism
        raise
        
    return json_result

def deploy_application(token, app_config):
    
    try:
        headers = _get_headers(token, {
           'Content-type': 'application/json'
        })
        response = requests.post(settings.WPST_API_DOMAIN + "/processes", headers=headers, json=app_config)
        response.raise_for_status()
        json_result = response.json()
        
    except requests.exceptions.HTTPError as e:
        # Add Logging Mechanism
        raise
    
    return json_result

def dismiss_application(token, app_name):
    
    try:
        headers = _get_headers(token)
        response = requests.delete(settings.WPST_API_DOMAIN + "/processes/{}".format(app_name), headers=headers)
        response.raise_for_status()
        json_result = response.json()['undeploymentResult']
        
    except requests.exceptions.HTTPError as e:
        # Add Logging Mechanism
        raise
        
    return json_result


def submit_job(token, app_name, data):

    headers = _get_headers(token, {
       'Content-type': 'application/json'
    })
    
    try:
        job_url = settings.WPST_API_DOMAIN + "/processes/{}/jobs".format(app_name)
        response = requests.post(job_url, headers=headers, json=data)
        response.raise_for_status()
        
        job_location = response.headers['location']
        if "http://127.0.0.1:5000" in job_location:
            job_location = job_location.replace("http://127.0.0.1:5000",settings.WPST_API_DOMAIN)

        job_id = job_location.replace(job_url + "/","")

    except requests.exceptions.HTTPError as e:
        # Add Logging Mechanism
        raise
    
    return job_id

def get_job_by_id(token, app_name, job_id):
    
    try:
        headers = _get_headers(token)
        job_status_url = settings.WPST_API_DOMAIN + "/processes/{}/jobs/{}".format(app_name, job_id)
        response = requests.get(job_status_url, headers=headers)
        response.raise_for_status()
        json_result = response.json()
        
    except requests.exceptions.HTTPError as e:
        # Add Logging Mechanism
        raise

    return json_result


def get_job_status(token, app_name, job_id):
    
    try:
        headers = _get_headers(token)
        job_status_url = settings.WPST_API_DOMAIN + "/processes/{}/jobs/{}".format(app_name, job_id)
        response = requests.get(job_status_url, headers=headers)
        response.raise_for_status()
        job_status = response.json()['status']
        
    except requests.exceptions.HTTPError as e:
        # Add Logging Mechanism
        raise

    return job_status

def get_job_result(token, app_name, job_id):

    try:
        headers = _get_headers(token)
        job_result_url = settings.WPST_API_DOMAIN + "/processes/{}/jobs/{}/result".format(app_name, job_id)
        response = requests.get(job_result_url, headers=headers)
        response.raise_for_status()
        json_result = response.json()['outputs']
        
    except requests.exceptions.HTTPError as e:
        # Add Logging Mechanism
        raise

    return json_result    

def get_jobs_for_app(token, app_name):
    
    try:
        headers = _get_headers(token)
        job_url = settings.WPST_API_DOMAIN + "/processes/{}/jobs".format(app_name)
        response = requests.get(job_url, headers=headers)
        response.raise_for_status()
        json_result = response.json()['jobs']
    except:
        # Add Logging Mechanism
        raise

    return json_result

def dismiss_job(token, app_name, job_id):
    
    try:
        headers = _get_headers(token)
        job_url = settings.WPST_API_DOMAIN + "/processes/{}/jobs/{}".format(app_name,job_id)
        response = requests.delete(job_url, headers=headers)
        response.raise_for_status()
        json_result = response.json()['statusInfo']
        
    except:
        # Add Logging Mechanism
        raise

    return json_result


def _get_headers(token, additional_headers = {}):
    
    if token == None:
        raise Exception("No authorization token was provided.")
    
    base_header = {
        "Authorization": "Bearer " + token,
    }
    
    return {**base_header, **additional_headers}