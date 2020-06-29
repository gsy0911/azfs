from typing import Union
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobClient, ContainerClient, BlobServiceClient
from .client_interface import ClientInterface


class AzBlobClient(ClientInterface):

    def _get_service_client(
            self,
            storage_account_url: str,
            credential: Union[DefaultAzureCredential, str]) -> BlobServiceClient:
        """
        get BlobServiceClient

        Args:
            storage_account_url:
            credential:

        Returns:
            BlobServiceClient
        """
        return BlobServiceClient(account_url=storage_account_url, credential=credential)

    def _get_file_client(
            self,
            storage_account_url: str,
            file_system: str,
            file_path: str,
            credential: Union[DefaultAzureCredential, str]) -> BlobClient:
        """
        get BlobClient

        Args:
            storage_account_url:
            file_system:
            file_path:
            credential:

        Returns:
            BlobClient
        """
        file_client = self._get_service_client(
            storage_account_url=storage_account_url,
            credential=credential
        ).get_blob_client(container=file_system, blob=file_path)
        return file_client

    def _get_container_client(
            self,
            storage_account_url: str,
            file_system: str,
            credential: Union[DefaultAzureCredential, str]) -> ContainerClient:
        """
        get ContainerClient

        Args:
            storage_account_url:
            file_system:
            credential:

        Returns:
            ContainerClient
        """
        container_client = self._get_service_client(
            storage_account_url=storage_account_url,
            credential=credential
        ).get_container_client(
            container=file_system)
        return container_client

    def _ls(self, path: str, file_path: str):
        blob_list = \
            [f.name for f in self.get_container_client_from_path(path=path).list_blobs(name_starts_with=file_path)]
        return blob_list

    def _get(self, path: str, **kwargs):
        file_bytes = self.get_file_client_from_path(path=path).download_blob().readall()
        return file_bytes

    def _put(self, path: str, data):
        self.get_file_client_from_path(path=path).upload_blob(
            data=data,
            length=len(data),
            overwrite=True
        )
        return True

    def _info(self, path: str):
        return self.get_file_client_from_path(path=path).get_blob_properties()

    def _rm(self, path: str):
        self.get_file_client_from_path(path=path).delete_blob()
        return True
