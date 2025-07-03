# Reference
## Entities
<details><summary><code>client.entities.<a href="src/anduril/entities/client.py">publish_entity</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Publish an entity for ingest into the Entities API. Entities created with this method are "owned" by the originator: other sources, 
such as the UI, may not edit or delete these entities. The server validates entities at API call time and 
returns an error if the entity is invalid.

An entity ID must be provided when calling this endpoint. If the entity referenced by the entity ID does not exist
then it will be created. Otherwise the entity will be updated. An entity will only be updated if its
provenance.sourceUpdateTime is greater than the provenance.sourceUpdateTime of the existing entity.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from anduril import lattice

client = lattice(
    token="YOUR_TOKEN",
)
client.entities.publish_entity()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `typing.Optional[str]` 

A Globally Unique Identifier (GUID) for your entity. If this field is empty, the Entity Manager API
 automatically generates an ID when it creates the entity.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 

A human-readable entity description that's helpful for debugging purposes and human
 traceability. If this field is empty, the Entity Manager API generates one for you.
    
</dd>
</dl>

<dl>
<dd>

**is_live:** `typing.Optional[bool]` 

Indicates the entity is active and should have a lifecycle state of CREATE or UPDATE.
 Set this field to true when publishing an entity.
    
</dd>
</dl>

<dl>
<dd>

**created_time:** `typing.Optional[dt.datetime]` 

The time when the entity was first known to the entity producer. If this field is empty, the Entity Manager API uses the
 current timestamp of when the entity is first received.
 For example, when a drone is first powered on, it might report its startup time as the created time.
 The timestamp doesn't change for the lifetime of an entity.
    
</dd>
</dl>

<dl>
<dd>

**expiry_time:** `typing.Optional[dt.datetime]` 

Future time that expires an entity and updates the is_live flag.
 For entities that are constantly updating, the expiry time also updates.
 In some cases, this may differ from is_live.
 Example: Entities with tasks exported to an external system must remain
 active even after they expire.
 This field is required when publishing a prepopulated entity.
 The expiry time must be in the future, but less than 30 days from the current time.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[Status]` — Human-readable descriptions of what the entity is currently doing.
    
</dd>
</dl>

<dl>
<dd>

**location:** `typing.Optional[Location]` — Geospatial data related to the entity, including its position, kinematics, and orientation.
    
</dd>
</dl>

<dl>
<dd>

**location_uncertainty:** `typing.Optional[LocationUncertainty]` — Indicates uncertainty of the entity's position and kinematics.
    
</dd>
</dl>

<dl>
<dd>

**geo_shape:** `typing.Optional[GeoShape]` — Geospatial representation of the entity, including entities that cover an area rather than a fixed point.
    
</dd>
</dl>

<dl>
<dd>

**geo_details:** `typing.Optional[GeoDetails]` — Additional details on what the geospatial area or point represents, along with visual display details.
    
</dd>
</dl>

<dl>
<dd>

**aliases:** `typing.Optional[Aliases]` — Entity name displayed in the Lattice UI side panel. Also includes identifiers that other systems can use to reference the same entity.
    
</dd>
</dl>

<dl>
<dd>

**tracked:** `typing.Optional[Tracked]` — If this entity is tracked by another entity, this component contains data related to how it's being tracked.
    
</dd>
</dl>

<dl>
<dd>

**correlation:** `typing.Optional[Correlation]` — If this entity has been correlated or decorrelated to another one, this component contains information on the correlation or decorrelation.
    
</dd>
</dl>

<dl>
<dd>

**mil_view:** `typing.Optional[MilView]` — View of the entity.
    
</dd>
</dl>

<dl>
<dd>

**ontology:** `typing.Optional[Ontology]` — Ontology defines an entity's categorization in Lattice, and improves data retrieval and integration. Builds a standardized representation of the entity.
    
</dd>
</dl>

<dl>
<dd>

**sensors:** `typing.Optional[Sensors]` — Details an entity's available sensors.
    
</dd>
</dl>

<dl>
<dd>

**payloads:** `typing.Optional[Payloads]` — Details an entity's available payloads.
    
</dd>
</dl>

<dl>
<dd>

**power_state:** `typing.Optional[PowerState]` — Details the entity's power source.
    
</dd>
</dl>

<dl>
<dd>

**provenance:** `typing.Optional[Provenance]` — The primary data source provenance for this entity.
    
</dd>
</dl>

<dl>
<dd>

**overrides:** `typing.Optional[Overrides]` — Provenance of override data.
    
</dd>
</dl>

<dl>
<dd>

**indicators:** `typing.Optional[Indicators]` 

Describes an entity's specific characteristics and the operations that can be performed on the entity.
 For example, "simulated" informs the operator that the entity is from a simulation, and "deletable"
 informs the operator (and system) that the delete operation is valid against the entity.
    
</dd>
</dl>

<dl>
<dd>

**target_priority:** `typing.Optional[TargetPriority]` — The prioritization associated with an entity, such as if it's a threat or a high-value target.
    
</dd>
</dl>

<dl>
<dd>

**signal:** `typing.Optional[Signal]` — Describes an entity's signal characteristics, primarily used when an entity is a signal of interest.
    
</dd>
</dl>

<dl>
<dd>

**transponder_codes:** `typing.Optional[TransponderCodes]` — A message describing any transponder codes associated with Mode 1, 2, 3, 4, 5, S interrogations. These are related to ADS-B modes.
    
</dd>
</dl>

<dl>
<dd>

**data_classification:** `typing.Optional[Classification]` 

Describes an entity's security classification levels at an overall classification level and on a per
 field level.
    
</dd>
</dl>

<dl>
<dd>

**task_catalog:** `typing.Optional[TaskCatalog]` — A catalog of tasks that can be performed by an entity.
    
</dd>
</dl>

<dl>
<dd>

**media:** `typing.Optional[Media]` — Media associated with an entity, such as videos, images, or thumbnails.
    
</dd>
</dl>

<dl>
<dd>

**relationships:** `typing.Optional[Relationships]` — The relationships between this entity and other entities in the common operational picture (COP).
    
</dd>
</dl>

<dl>
<dd>

**visual_details:** `typing.Optional[VisualDetails]` — Visual details associated with the display of an entity in the client.
    
</dd>
</dl>

<dl>
<dd>

**dimensions:** `typing.Optional[Dimensions]` — Physical dimensions of the entity.
    
</dd>
</dl>

<dl>
<dd>

**route_details:** `typing.Optional[RouteDetails]` — Additional information about an entity's route.
    
</dd>
</dl>

<dl>
<dd>

**schedules:** `typing.Optional[Schedules]` — Schedules associated with this entity.
    
</dd>
</dl>

<dl>
<dd>

**health:** `typing.Optional[Health]` — Health metrics or connection status reported by the entity.
    
</dd>
</dl>

<dl>
<dd>

**group_details:** `typing.Optional[GroupDetails]` — Details for the group associated with this entity.
    
</dd>
</dl>

<dl>
<dd>

**supplies:** `typing.Optional[Supplies]` — Contains relevant supply information for the entity, such as fuel.
    
</dd>
</dl>

<dl>
<dd>

**orbit:** `typing.Optional[Orbit]` — Orbit information for space objects.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entities.<a href="src/anduril/entities/client.py">get_entity</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from anduril import lattice

client = lattice(
    token="YOUR_TOKEN",
)
client.entities.get_entity(
    entity_id="entityId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `str` — ID of the entity to return
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entities.<a href="src/anduril/entities/client.py">override_entity</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Only fields marked with overridable can be overridden. Please refer to our documentation to see the comprehensive
list of fields that can be overridden. The entity in the request body should only have a value set on the field 
specified in the field path parameter. Field paths are rooted in the base entity object and must be represented 
using lower_snake_case. Do not include "entity" in the field path.

Note that overrides are applied in an eventually consistent manner. If multiple overrides are created 
concurrently for the same field path, the last writer wins.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from anduril import lattice

client = lattice(
    token="YOUR_TOKEN",
)
client.entities.override_entity(
    entity_id="entityId",
    field_path="mil_view.disposition",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `str` — The unique ID of the entity to override
    
</dd>
</dl>

<dl>
<dd>

**field_path:** `str` — fieldPath to override
    
</dd>
</dl>

<dl>
<dd>

**entity:** `typing.Optional[Entity]` 

The entity containing the overridden fields. The service will extract the overridable fields from 
the object and ignore all other fields.
    
</dd>
</dl>

<dl>
<dd>

**provenance:** `typing.Optional[Provenance]` — Additional information about the source of the override.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entities.<a href="src/anduril/entities/client.py">remove_entity_override</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This operation clears the override value from the specified field path on the entity.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from anduril import lattice

client = lattice(
    token="YOUR_TOKEN",
)
client.entities.remove_entity_override(
    entity_id="entityId",
    field_path="mil_view.disposition",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `str` — The unique ID of the entity to undo an override from.
    
</dd>
</dl>

<dl>
<dd>

**field_path:** `str` — The fieldPath to clear overrides from.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entities.<a href="src/anduril/entities/client.py">long_poll_entity_events</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This is a long polling API that will first return all pre-existing data and then return all new data as
it becomes available. If you want to start a new polling session then open a request with an empty
'sessionToken' in the request body. The server will return a new session token in the response.
If you want to retrieve the next batch of results from an existing polling session then send the session
token you received from the server in the request body. If no new data is available then the server will
hold the connection open for up to 5 minutes. After the 5 minute timeout period, the server will close the 
connection with no results and you may resume polling with the same session token. If your session falls behind 
more than 3x the total number of entities in the environment, the server will terminate your session. 
In this case you must start a new session by sending a request with an empty session token.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from anduril import lattice

client = lattice(
    token="YOUR_TOKEN",
)
client.entities.long_poll_entity_events(
    session_token="sessionToken",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_token:** `str` — Long-poll session identifier. Leave empty to start a new polling session.
    
</dd>
</dl>

<dl>
<dd>

**batch_size:** `typing.Optional[int]` — Maximum size of response batch. Defaults to 100. Must be between 1 and 2000 (inclusive).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Tasking
<details><summary><code>client.tasking.<a href="src/anduril/tasking/client.py">create_task</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submit a request to create a task and schedule it for delivery. Tasks, once delivered, will 
be asynchronously updated by their destined agent. 
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from anduril import lattice

client = lattice(
    token="YOUR_TOKEN",
)
client.tasking.create_task()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**task_id:** `typing.Optional[str]` 

If non-empty, will set the requested Task ID, otherwise will generate a new random
GUID. Will reject if supplied Task ID does not match [A-Za-z0-9_-.]{5,36}.
    
</dd>
</dl>

<dl>
<dd>

**display_name:** `typing.Optional[str]` — Human readable display name for this Task, should be short (<100 chars).
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Longer, free form human readable description of this Task.
    
</dd>
</dl>

<dl>
<dd>

**specification:** `typing.Optional[GoogleProtobufAny]` — Full set of task parameters.
    
</dd>
</dl>

<dl>
<dd>

**author:** `typing.Optional[Principal]` 
    
</dd>
</dl>

<dl>
<dd>

**relations:** `typing.Optional[Relations]` 

Any relationships associated with this Task, such as a parent Task or an assignee
this Task is designated to for execution.
    
</dd>
</dl>

<dl>
<dd>

**is_executed_elsewhere:** `typing.Optional[bool]` 

If set, then the service will not trigger execution of this task on an agent. Useful
for when ingesting tasks from an external system that is triggering execution of tasks
on agents.
    
</dd>
</dl>

<dl>
<dd>

**initial_entities:** `typing.Optional[typing.Sequence[TaskEntity]]` 

Indicates an initial set of entities that can be used to execute an entity aware
task. For example, an entity Objective, an entity Keep In Zone, etc.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tasking.<a href="src/anduril/tasking/client.py">get_task</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from anduril import lattice

client = lattice(
    token="YOUR_TOKEN",
)
client.tasking.get_task(
    task_id="taskId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**task_id:** `str` — ID of task to return
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tasking.<a href="src/anduril/tasking/client.py">update_task_status</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the status of a task.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from anduril import lattice

client = lattice(
    token="YOUR_TOKEN",
)
client.tasking.update_task_status(
    task_id="taskId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**task_id:** `str` — ID of task to update status of
    
</dd>
</dl>

<dl>
<dd>

**status_version:** `typing.Optional[int]` 

The status version of the task to update. This version number increments to indicate the task's 
current stage in its status lifecycle. Specifically, whenever a task's status updates, the status 
version increments by one. Any status updates received with a lower status version number than what 
is known are considered stale and ignored.
    
</dd>
</dl>

<dl>
<dd>

**new_status:** `typing.Optional[TaskStatus]` — The new status of the task.
    
</dd>
</dl>

<dl>
<dd>

**author:** `typing.Optional[Principal]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tasking.<a href="src/anduril/tasking/client.py">query_tasks</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Query for tasks by a specified search criteria.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from anduril import lattice

client = lattice(
    token="YOUR_TOKEN",
)
client.tasking.query_tasks()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page_token:** `typing.Optional[str]` — If set, returns results starting from the given pageToken.
    
</dd>
</dl>

<dl>
<dd>

**parent_task_id:** `typing.Optional[str]` 

If present matches Tasks with this parent Task ID.
Note: this is mutually exclusive with all other query parameters, i.e., either provide parent Task ID, or
any of the remaining parameters, but not both.
    
</dd>
</dl>

<dl>
<dd>

**status_filter:** `typing.Optional[TaskQueryStatusFilter]` 
    
</dd>
</dl>

<dl>
<dd>

**update_time_range:** `typing.Optional[TaskQueryUpdateTimeRange]` — If provided, only provides Tasks updated within the time range.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tasking.<a href="src/anduril/tasking/client.py">listen_as_agent</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This is a long polling API that will block until a new task is ready for delivery. If no new task is 
available then the server will hold on to your request for up to 5 minutes, after that 5 minute timeout 
period you will be expected to reinitiate a new request.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from anduril import lattice

client = lattice(
    token="YOUR_TOKEN",
)
client.tasking.listen_as_agent()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_selector:** `typing.Optional[EntityIdsSelector]` — Selector criteria to determine which Agent Tasks the agent receives
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Objects
<details><summary><code>client.objects.<a href="src/anduril/objects/client.py">list_objects</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists objects in your environment. You can define a prefix to list a subset of your objects. If you do not set a prefix, Lattice returns all available objects. By default this endpoint will list local objects only.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
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

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**prefix:** `typing.Optional[str]` — Filters the objects based on the specified prefix path. If no path is specified, all objects are returned.
    
</dd>
</dl>

<dl>
<dd>

**since_timestamp:** `typing.Optional[dt.datetime]` — Sets the age for the oldest objects to query across the environment.
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[str]` — Base64 and URL-encoded cursor returned by the service to continue paging.
    
</dd>
</dl>

<dl>
<dd>

**all_objects_in_mesh:** `typing.Optional[ListObjectsRequestAllObjectsInMesh]` — Lists objects across all environment nodes in a Lattice Mesh.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.objects.<a href="src/anduril/objects/client.py">delete_object</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes an object from your environment given the objectPath path parameter.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from anduril import lattice

client = lattice(
    token="YOUR_TOKEN",
)
client.objects.delete_object(
    object_path="objectPath",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**object_path:** `str` — The path of the object to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.objects.<a href="src/anduril/objects/client.py">get_object_metadata</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns metadata for a specified object path. Use this to fetch metadata such as object size (size_bytes), its expiry time (expiry_time), or its latest update timestamp (last_updated_at).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from anduril import lattice

client = lattice(
    token="YOUR_TOKEN",
)
client.objects.get_object_metadata(
    object_path="objectPath",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**object_path:** `str` — The path of the object to query.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

