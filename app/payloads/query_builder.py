from typing import List
import abc


class BaseQueryBuilder(abc.ABC):
    @abc.abstractclassmethod
    def query_build(cls):
        pass


class QueryBuildStatus(BaseQueryBuilder):
    @classmethod
    def query_build(cls, status: str):
        return {"status": {"$eq": status}}


class QueryBuildPriority(BaseQueryBuilder):
    @classmethod
    def query_build(cls, priority: int):
        return {"priority": {"$eq": priority}}


class QueryBuildTags(BaseQueryBuilder):
    @classmethod
    def query_build(cls, tags: List[str]):
        return {"tags": {"$in": tags}}


class QueryBuildStartDate(BaseQueryBuilder):
    @classmethod
    def query_build(cls, start_date: str):
        return {"due_at": {"$gte": start_date}}


class QueryBuildEndDate(BaseQueryBuilder):
    @classmethod
    def query_build(cls, end_date: str):
        return {"due_at": {"$lte": end_date}}


class NoteOwner(BaseQueryBuilder):
    @classmethod
    def query_build(cls, user_id: str):
        return {"owner": {"$eq": user_id}}


class NoneQueryBuild(BaseQueryBuilder):
    def query_build(cls):
        pass


class FactoryQueryBuilder:

    filters = {
        "status": QueryBuildStatus,
        "priority": QueryBuildPriority,
        "tags": QueryBuildTags,
        "start_date": QueryBuildStartDate,
        "end_date": QueryBuildEndDate,
        "note_owner": NoteOwner,
    }

    @classmethod
    def query_build(cls, filters):
        return [
            cls.filters.get(filter, NoneQueryBuild).query_build(filters[filter])
            for filter in filters.keys()
        ]


# Adjust


class QueryBuildAge(BaseQueryBuilder):
    @classmethod
    def query_build(cls, age: str):
        return {"age": {"$in": age}}


class QueryBuildValue(BaseQueryBuilder):
    @classmethod
    def query_build(cls, value: str):
        return {"value": {"$in": value}}


class FactoryQueryBuilder:

    filters = {
        "status": QueryBuildStatus,
        "priority": QueryBuildPriority,
        "age": QueryBuildAge,
        "value": QueryBuildValue,
        "start_date": QueryBuildStartDate,
        "end_date": QueryBuildEndDate,
    }
