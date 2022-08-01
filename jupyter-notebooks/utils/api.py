import requests

from . import settings

def get_apps():
    
    try:
        
        response = requests.get(settings.WPST_API_DOMAIN + "/processes")
        json_result = response.json()['processes']
        
    except requests.exceptions.HTTPError as e:
        # Add Logging Mechanism
        raise
        
    return json_result

def get_application(app_name):

    try:
        
        response = requests.get(settings.WPST_API_DOMAIN + "/processes/{}".format(app_name))
        json_result = response.json()['process']
        
    except requests.exceptions.HTTPError as e:
        # Add Logging Mechanism
        raise
        
    return json_result

def deploy_application(app_config):
    
    headers = {
       'Content-type': 'application/json'
    }
    
    try:
        
        response = requests.post(settings.WPST_API_DOMAIN + "/processes", headers=headers, json=app_config)
        json_result = response.json()
        
    except requests.exceptions.HTTPError as e:
        # Add Logging Mechanism
        raise
    
    return json_result

def dismiss_application(app_name):
    
    try:
        
        response = requests.delete(settings.WPST_API_DOMAIN + "/processes/{}".format(app_name))
        json_result = response.json()['undeploymentResult']
        
    except requests.exceptions.HTTPError as e:
        # Add Logging Mechanism
        raise
        
    return json_result


def submit_job(app_name, data):

    headers = {
       'Content-type': 'application/json'
    }
    
    try:
        job_url = settings.WPST_API_DOMAIN + "/processes/{}/jobs".format(app_name)
        r = requests.post(job_url, headers=headers, json=data)
        
        job_location = r.headers['location']
        if "http://127.0.0.1:5000" in job_location:
            job_location = job_location.replace("http://127.0.0.1:5000",settings.WPST_API_DOMAIN)

        job_id = job_location.replace(job_url + "/","")

    except requests.exceptions.HTTPError as e:
        # Add Logging Mechanism
        raise
    
    return job_id

def get_job_status(app_name, job_id):
    
    try:
        
        job_status_url = settings.WPST_API_DOMAIN + "/processes/{}/jobs/{}".format(app_name, job_id)
        response = requests.get(job_status_url)
        job_status = response.json()['status']
        
    except requests.exceptions.HTTPError as e:
        # Add Logging Mechanism
        raise

    return job_status

def get_job_result(app_name, job_id):

    try:
        
        job_result_url = settings.WPST_API_DOMAIN + "/processes/{}/jobs/{}/result".format(app_name, job_id)
        response = requests.get(job_result_url)
        json_result = response.json()['outputs']
        
    except requests.exceptions.HTTPError as e:
        # Add Logging Mechanism
        raise

    return json_result    

def get_jobs_for_app(app_name):
    
    try:
        job_url = settings.WPST_API_DOMAIN + "/processes/{}/jobs".format(app_name)
        response = requests.get(job_url)
        json_result = response.json()['jobs']
    except:
        # Add Logging Mechanism
        raise

    return json_result

def dismiss_job(app_name, job_id):
    
    try:
        
        job_url = settings.WPST_API_DOMAIN + "/processes/{}/jobs/{}".format(app_name,job_id)
        response = requests.delete(job_url)
        json_result = response.json()['statusInfo']
        
    except:
        # Add Logging Mechanism
        raise

    return json_result