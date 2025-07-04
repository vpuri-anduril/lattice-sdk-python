# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.pagination import AsyncPager, SyncPager
from ..core.request_options import RequestOptions
from ..types.path_metadata import PathMetadata
from .raw_client import AsyncRawObjectsClient, RawObjectsClient
from .types.get_object_request_accept_encoding import GetObjectRequestAcceptEncoding
from .types.list_objects_request_all_objects_in_mesh import ListObjectsRequestAllObjectsInMesh

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class ObjectsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawObjectsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawObjectsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawObjectsClient
        """
        return self._raw_client

    def list_objects(
        self,
        *,
        prefix: typing.Optional[str] = None,
        since_timestamp: typing.Optional[dt.datetime] = None,
        page_token: typing.Optional[str] = None,
        all_objects_in_mesh: typing.Optional[ListObjectsRequestAllObjectsInMesh] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[PathMetadata]:
        """
        Lists objects in your environment. You can define a prefix to list a subset of your objects. If you do not set a prefix, Lattice returns all available objects. By default this endpoint will list local objects only.

        Parameters
        ----------
        prefix : typing.Optional[str]
            Filters the objects based on the specified prefix path. If no path is specified, all objects are returned.

        since_timestamp : typing.Optional[dt.datetime]
            Sets the age for the oldest objects to query across the environment.

        page_token : typing.Optional[str]
            Base64 and URL-encoded cursor returned by the service to continue paging.

        all_objects_in_mesh : typing.Optional[ListObjectsRequestAllObjectsInMesh]
            Lists objects across all environment nodes in a Lattice Mesh.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[PathMetadata]
            Successful operation

        Examples
        --------
        from anduril import lattice

        client = lattice(
            token="YOUR_TOKEN",
        )
        response = client.objects.list_objects()
        for item in response:
            yield item
        # alternatively, you can paginate page-by-page
        for page in response.iter_pages():
            yield page
        """
        return self._raw_client.list_objects(
            prefix=prefix,
            since_timestamp=since_timestamp,
            page_token=page_token,
            all_objects_in_mesh=all_objects_in_mesh,
            request_options=request_options,
        )

    def get_object(
        self,
        object_path: str,
        *,
        accept_encoding: typing.Optional[GetObjectRequestAcceptEncoding] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        Fetches an object from your environment using the objectPath path parameter.

        Parameters
        ----------
        object_path : str
            The path of the object to fetch.

        accept_encoding : typing.Optional[GetObjectRequestAcceptEncoding]
            If set, Lattice will compress the response using the specified compression method. If the header is not defined, or the compression method is set to `identity`, no compression will be applied to the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            Successful operation
        """
        with self._raw_client.get_object(
            object_path, accept_encoding=accept_encoding, request_options=request_options
        ) as r:
            yield from r.data

    def upload_object(
        self,
        object_path: str,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PathMetadata:
        """
        Uploads an object using multiform data. The object must be 1 GiB or smaller.

        Parameters
        ----------
        object_path : str
            Path of the Object that is to be uploaded.

        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PathMetadata
            Successful upload
        """
        _response = self._raw_client.upload_object(object_path, request=request, request_options=request_options)
        return _response.data

    def delete_object(self, object_path: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Deletes an object from your environment given the objectPath path parameter.

        Parameters
        ----------
        object_path : str
            The path of the object to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from anduril import lattice

        client = lattice(
            token="YOUR_TOKEN",
        )
        client.objects.delete_object(
            object_path="objectPath",
        )
        """
        _response = self._raw_client.delete_object(object_path, request_options=request_options)
        return _response.data

    def get_object_metadata(
        self, object_path: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Returns metadata for a specified object path. Use this to fetch metadata such as object size (size_bytes), its expiry time (expiry_time), or its latest update timestamp (last_updated_at).

        Parameters
        ----------
        object_path : str
            The path of the object to query.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from anduril import lattice

        client = lattice(
            token="YOUR_TOKEN",
        )
        client.objects.get_object_metadata(
            object_path="objectPath",
        )
        """
        _response = self._raw_client.get_object_metadata(object_path, request_options=request_options)
        return _response.headers


class AsyncObjectsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawObjectsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawObjectsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawObjectsClient
        """
        return self._raw_client

    async def list_objects(
        self,
        *,
        prefix: typing.Optional[str] = None,
        since_timestamp: typing.Optional[dt.datetime] = None,
        page_token: typing.Optional[str] = None,
        all_objects_in_mesh: typing.Optional[ListObjectsRequestAllObjectsInMesh] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncPager[PathMetadata]:
        """
        Lists objects in your environment. You can define a prefix to list a subset of your objects. If you do not set a prefix, Lattice returns all available objects. By default this endpoint will list local objects only.

        Parameters
        ----------
        prefix : typing.Optional[str]
            Filters the objects based on the specified prefix path. If no path is specified, all objects are returned.

        since_timestamp : typing.Optional[dt.datetime]
            Sets the age for the oldest objects to query across the environment.

        page_token : typing.Optional[str]
            Base64 and URL-encoded cursor returned by the service to continue paging.

        all_objects_in_mesh : typing.Optional[ListObjectsRequestAllObjectsInMesh]
            Lists objects across all environment nodes in a Lattice Mesh.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[PathMetadata]
            Successful operation

        Examples
        --------
        import asyncio

        from anduril import Asynclattice

        client = Asynclattice(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            response = await client.objects.list_objects()
            async for item in response:
                yield item

            # alternatively, you can paginate page-by-page
            async for page in response.iter_pages():
                yield page


        asyncio.run(main())
        """
        return await self._raw_client.list_objects(
            prefix=prefix,
            since_timestamp=since_timestamp,
            page_token=page_token,
            all_objects_in_mesh=all_objects_in_mesh,
            request_options=request_options,
        )

    async def get_object(
        self,
        object_path: str,
        *,
        accept_encoding: typing.Optional[GetObjectRequestAcceptEncoding] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        Fetches an object from your environment using the objectPath path parameter.

        Parameters
        ----------
        object_path : str
            The path of the object to fetch.

        accept_encoding : typing.Optional[GetObjectRequestAcceptEncoding]
            If set, Lattice will compress the response using the specified compression method. If the header is not defined, or the compression method is set to `identity`, no compression will be applied to the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Successful operation
        """
        async with self._raw_client.get_object(
            object_path, accept_encoding=accept_encoding, request_options=request_options
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def upload_object(
        self,
        object_path: str,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PathMetadata:
        """
        Uploads an object using multiform data. The object must be 1 GiB or smaller.

        Parameters
        ----------
        object_path : str
            Path of the Object that is to be uploaded.

        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PathMetadata
            Successful upload
        """
        _response = await self._raw_client.upload_object(object_path, request=request, request_options=request_options)
        return _response.data

    async def delete_object(self, object_path: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Deletes an object from your environment given the objectPath path parameter.

        Parameters
        ----------
        object_path : str
            The path of the object to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from anduril import Asynclattice

        client = Asynclattice(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.objects.delete_object(
                object_path="objectPath",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_object(object_path, request_options=request_options)
        return _response.data

    async def get_object_metadata(
        self, object_path: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Returns metadata for a specified object path. Use this to fetch metadata such as object size (size_bytes), its expiry time (expiry_time), or its latest update timestamp (last_updated_at).

        Parameters
        ----------
        object_path : str
            The path of the object to query.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from anduril import Asynclattice

        client = Asynclattice(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.objects.get_object_metadata(
                object_path="objectPath",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_object_metadata(object_path, request_options=request_options)
        return _response.headers
