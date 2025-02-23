from azure.storage.blob import BlobServiceClient
from azure.identity import ClientSecretCredential
from django.conf import settings
import datetime, os

tenant_id = settings.AZURE_TENANT_ID
client_id = settings.AZURE_CLIENT_ID
client_secret = settings.AZURE_CLIENT_SECRET
account_name = settings.AZURE_ACCOUNT_NAME
container_name = settings.AZURE_CONTAINER_NAME

def get_client():
    credential = ClientSecretCredential(tenant_id, client_id, client_secret)
    blob_service_url = f"https://{account_name}.blob.core.windows.net/"
    return BlobServiceClient(account_url=blob_service_url, credential=credential)

def existe_archivo(blob_name, container=""):  
    client = get_client()
    if container == "":
        container = container_name
    blob_client = client.get_blob_client(container=container, blob=blob_name)
    return blob_client.exists()

def copiar_archivo(blob_name, nuevo_blob_name, container=""):
    client = get_client()
    if container == "":
        container = container_name
    source_blob = client.get_blob_client(container=container_name, blob=blob_name)
    destination_blob = client.get_blob_client(container=container_name, blob=nuevo_blob_name)
    source_blob_url = source_blob.url
    try:
        copy_operation = destination_blob.start_copy_from_url(source_blob_url)
        copy_status = destination_blob.get_blob_properties().copy.status
        if copy_status == 'success':
            return True
        else:
            return False
    except Exception as e:
        return False

def upload_file(file, blob_name, container=""):
    client = get_client()
    if container == "":
        container = container_name
    blob_client = client.get_blob_client(container=container, blob=blob_name)
    if blob_client.exists():
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        partes = os.path.splitext(blob_name)
        nuevo_blob_name = partes[0] + "_" + timestamp + partes[1]
        if not copiar_archivo(blob_name, nuevo_blob_name):
            return ""    
    try:
        blob_client.upload_blob(file, overwrite=True)
    except Exception as e:
        return ""
    resultado = blob_client.url.split(container + "/")
    return resultado[1]

def descargar_archivo(blob_name, container=""):
    client = get_client()
    if container == "":
        container = container_name
    blob_client = client.get_blob_client(container=container, blob=blob_name)
    try:
        stream = blob_client.download_blob()
        return stream.readall()
    except Exception as e:
        return None
