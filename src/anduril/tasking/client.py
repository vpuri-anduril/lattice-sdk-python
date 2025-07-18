# This file was auto-generated by Fern from our API Definition.

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.agent_request import AgentRequest
from ..types.entity_ids_selector import EntityIdsSelector
from ..types.google_protobuf_any import GoogleProtobufAny
from ..types.principal import Principal
from ..types.relations import Relations
from ..types.task import Task
from ..types.task_entity import TaskEntity
from ..types.task_query_results import TaskQueryResults
from ..types.task_status import TaskStatus
from .raw_client import AsyncRawTaskingClient, RawTaskingClient
from .types.task_query_status_filter import TaskQueryStatusFilter
from .types.task_query_update_time_range import TaskQueryUpdateTimeRange

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class TaskingClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTaskingClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTaskingClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTaskingClient
        """
        return self._raw_client

    def create_task(
        self,
        *,
        task_id: typing.Optional[str] = OMIT,
        display_name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        specification: typing.Optional[GoogleProtobufAny] = OMIT,
        author: typing.Optional[Principal] = OMIT,
        relations: typing.Optional[Relations] = OMIT,
        is_executed_elsewhere: typing.Optional[bool] = OMIT,
        initial_entities: typing.Optional[typing.Sequence[TaskEntity]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Task:
        """
        Submit a request to create a task and schedule it for delivery. Tasks, once delivered, will
        be asynchronously updated by their destined agent.

        Parameters
        ----------
        task_id : typing.Optional[str]
            If non-empty, will set the requested Task ID, otherwise will generate a new random
            GUID. Will reject if supplied Task ID does not match [A-Za-z0-9_-.]{5,36}.

        display_name : typing.Optional[str]
            Human readable display name for this Task, should be short (<100 chars).

        description : typing.Optional[str]
            Longer, free form human readable description of this Task.

        specification : typing.Optional[GoogleProtobufAny]
            Full set of task parameters.

        author : typing.Optional[Principal]

        relations : typing.Optional[Relations]
            Any relationships associated with this Task, such as a parent Task or an assignee
            this Task is designated to for execution.

        is_executed_elsewhere : typing.Optional[bool]
            If set, then the service will not trigger execution of this task on an agent. Useful
            for when ingesting tasks from an external system that is triggering execution of tasks
            on agents.

        initial_entities : typing.Optional[typing.Sequence[TaskEntity]]
            Indicates an initial set of entities that can be used to execute an entity aware
            task. For example, an entity Objective, an entity Keep In Zone, etc.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Task
            Task creation was successful

        Examples
        --------
        from anduril import lattice

        client = lattice(
            token="YOUR_TOKEN",
        )
        client.tasking.create_task()
        """
        _response = self._raw_client.create_task(
            task_id=task_id,
            display_name=display_name,
            description=description,
            specification=specification,
            author=author,
            relations=relations,
            is_executed_elsewhere=is_executed_elsewhere,
            initial_entities=initial_entities,
            request_options=request_options,
        )
        return _response.data

    def get_task(self, task_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Task:
        """
        Parameters
        ----------
        task_id : str
            ID of task to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Task
            Task retrieval was successful.

        Examples
        --------
        from anduril import lattice

        client = lattice(
            token="YOUR_TOKEN",
        )
        client.tasking.get_task(
            task_id="taskId",
        )
        """
        _response = self._raw_client.get_task(task_id, request_options=request_options)
        return _response.data

    def update_task_status(
        self,
        task_id: str,
        *,
        status_version: typing.Optional[int] = OMIT,
        new_status: typing.Optional[TaskStatus] = OMIT,
        author: typing.Optional[Principal] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Task:
        """
        Update the status of a task.

        Parameters
        ----------
        task_id : str
            ID of task to update status of

        status_version : typing.Optional[int]
            The status version of the task to update. This version number increments to indicate the task's
            current stage in its status lifecycle. Specifically, whenever a task's status updates, the status
            version increments by one. Any status updates received with a lower status version number than what
            is known are considered stale and ignored.

        new_status : typing.Optional[TaskStatus]
            The new status of the task.

        author : typing.Optional[Principal]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Task
            Task status update was successful

        Examples
        --------
        from anduril import lattice

        client = lattice(
            token="YOUR_TOKEN",
        )
        client.tasking.update_task_status(
            task_id="taskId",
        )
        """
        _response = self._raw_client.update_task_status(
            task_id,
            status_version=status_version,
            new_status=new_status,
            author=author,
            request_options=request_options,
        )
        return _response.data

    def query_tasks(
        self,
        *,
        page_token: typing.Optional[str] = OMIT,
        parent_task_id: typing.Optional[str] = OMIT,
        status_filter: typing.Optional[TaskQueryStatusFilter] = OMIT,
        update_time_range: typing.Optional[TaskQueryUpdateTimeRange] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TaskQueryResults:
        """
        Query for tasks by a specified search criteria.

        Parameters
        ----------
        page_token : typing.Optional[str]
            If set, returns results starting from the given pageToken.

        parent_task_id : typing.Optional[str]
            If present matches Tasks with this parent Task ID.
            Note: this is mutually exclusive with all other query parameters, i.e., either provide parent Task ID, or
            any of the remaining parameters, but not both.

        status_filter : typing.Optional[TaskQueryStatusFilter]

        update_time_range : typing.Optional[TaskQueryUpdateTimeRange]
            If provided, only provides Tasks updated within the time range.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskQueryResults
            Task query was successful

        Examples
        --------
        from anduril import lattice

        client = lattice(
            token="YOUR_TOKEN",
        )
        client.tasking.query_tasks()
        """
        _response = self._raw_client.query_tasks(
            page_token=page_token,
            parent_task_id=parent_task_id,
            status_filter=status_filter,
            update_time_range=update_time_range,
            request_options=request_options,
        )
        return _response.data

    def listen_as_agent(
        self,
        *,
        agent_selector: typing.Optional[EntityIdsSelector] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AgentRequest:
        """
        This is a long polling API that will block until a new task is ready for delivery. If no new task is
        available then the server will hold on to your request for up to 5 minutes, after that 5 minute timeout
        period you will be expected to reinitiate a new request.

        Parameters
        ----------
        agent_selector : typing.Optional[EntityIdsSelector]
            Selector criteria to determine which Agent Tasks the agent receives

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentRequest
            Requests for the agent to comply with.

        Examples
        --------
        from anduril import lattice

        client = lattice(
            token="YOUR_TOKEN",
        )
        client.tasking.listen_as_agent()
        """
        _response = self._raw_client.listen_as_agent(agent_selector=agent_selector, request_options=request_options)
        return _response.data


class AsyncTaskingClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTaskingClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTaskingClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTaskingClient
        """
        return self._raw_client

    async def create_task(
        self,
        *,
        task_id: typing.Optional[str] = OMIT,
        display_name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        specification: typing.Optional[GoogleProtobufAny] = OMIT,
        author: typing.Optional[Principal] = OMIT,
        relations: typing.Optional[Relations] = OMIT,
        is_executed_elsewhere: typing.Optional[bool] = OMIT,
        initial_entities: typing.Optional[typing.Sequence[TaskEntity]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Task:
        """
        Submit a request to create a task and schedule it for delivery. Tasks, once delivered, will
        be asynchronously updated by their destined agent.

        Parameters
        ----------
        task_id : typing.Optional[str]
            If non-empty, will set the requested Task ID, otherwise will generate a new random
            GUID. Will reject if supplied Task ID does not match [A-Za-z0-9_-.]{5,36}.

        display_name : typing.Optional[str]
            Human readable display name for this Task, should be short (<100 chars).

        description : typing.Optional[str]
            Longer, free form human readable description of this Task.

        specification : typing.Optional[GoogleProtobufAny]
            Full set of task parameters.

        author : typing.Optional[Principal]

        relations : typing.Optional[Relations]
            Any relationships associated with this Task, such as a parent Task or an assignee
            this Task is designated to for execution.

        is_executed_elsewhere : typing.Optional[bool]
            If set, then the service will not trigger execution of this task on an agent. Useful
            for when ingesting tasks from an external system that is triggering execution of tasks
            on agents.

        initial_entities : typing.Optional[typing.Sequence[TaskEntity]]
            Indicates an initial set of entities that can be used to execute an entity aware
            task. For example, an entity Objective, an entity Keep In Zone, etc.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Task
            Task creation was successful

        Examples
        --------
        import asyncio

        from anduril import Asynclattice

        client = Asynclattice(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tasking.create_task()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_task(
            task_id=task_id,
            display_name=display_name,
            description=description,
            specification=specification,
            author=author,
            relations=relations,
            is_executed_elsewhere=is_executed_elsewhere,
            initial_entities=initial_entities,
            request_options=request_options,
        )
        return _response.data

    async def get_task(self, task_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Task:
        """
        Parameters
        ----------
        task_id : str
            ID of task to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Task
            Task retrieval was successful.

        Examples
        --------
        import asyncio

        from anduril import Asynclattice

        client = Asynclattice(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tasking.get_task(
                task_id="taskId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_task(task_id, request_options=request_options)
        return _response.data

    async def update_task_status(
        self,
        task_id: str,
        *,
        status_version: typing.Optional[int] = OMIT,
        new_status: typing.Optional[TaskStatus] = OMIT,
        author: typing.Optional[Principal] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Task:
        """
        Update the status of a task.

        Parameters
        ----------
        task_id : str
            ID of task to update status of

        status_version : typing.Optional[int]
            The status version of the task to update. This version number increments to indicate the task's
            current stage in its status lifecycle. Specifically, whenever a task's status updates, the status
            version increments by one. Any status updates received with a lower status version number than what
            is known are considered stale and ignored.

        new_status : typing.Optional[TaskStatus]
            The new status of the task.

        author : typing.Optional[Principal]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Task
            Task status update was successful

        Examples
        --------
        import asyncio

        from anduril import Asynclattice

        client = Asynclattice(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tasking.update_task_status(
                task_id="taskId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_task_status(
            task_id,
            status_version=status_version,
            new_status=new_status,
            author=author,
            request_options=request_options,
        )
        return _response.data

    async def query_tasks(
        self,
        *,
        page_token: typing.Optional[str] = OMIT,
        parent_task_id: typing.Optional[str] = OMIT,
        status_filter: typing.Optional[TaskQueryStatusFilter] = OMIT,
        update_time_range: typing.Optional[TaskQueryUpdateTimeRange] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TaskQueryResults:
        """
        Query for tasks by a specified search criteria.

        Parameters
        ----------
        page_token : typing.Optional[str]
            If set, returns results starting from the given pageToken.

        parent_task_id : typing.Optional[str]
            If present matches Tasks with this parent Task ID.
            Note: this is mutually exclusive with all other query parameters, i.e., either provide parent Task ID, or
            any of the remaining parameters, but not both.

        status_filter : typing.Optional[TaskQueryStatusFilter]

        update_time_range : typing.Optional[TaskQueryUpdateTimeRange]
            If provided, only provides Tasks updated within the time range.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskQueryResults
            Task query was successful

        Examples
        --------
        import asyncio

        from anduril import Asynclattice

        client = Asynclattice(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tasking.query_tasks()


        asyncio.run(main())
        """
        _response = await self._raw_client.query_tasks(
            page_token=page_token,
            parent_task_id=parent_task_id,
            status_filter=status_filter,
            update_time_range=update_time_range,
            request_options=request_options,
        )
        return _response.data

    async def listen_as_agent(
        self,
        *,
        agent_selector: typing.Optional[EntityIdsSelector] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AgentRequest:
        """
        This is a long polling API that will block until a new task is ready for delivery. If no new task is
        available then the server will hold on to your request for up to 5 minutes, after that 5 minute timeout
        period you will be expected to reinitiate a new request.

        Parameters
        ----------
        agent_selector : typing.Optional[EntityIdsSelector]
            Selector criteria to determine which Agent Tasks the agent receives

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgentRequest
            Requests for the agent to comply with.

        Examples
        --------
        import asyncio

        from anduril import Asynclattice

        client = Asynclattice(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tasking.listen_as_agent()


        asyncio.run(main())
        """
        _response = await self._raw_client.listen_as_agent(
            agent_selector=agent_selector, request_options=request_options
        )
        return _response.data
