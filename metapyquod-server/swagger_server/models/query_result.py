# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class QueryResult(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, doc_id: int=None, url: str=None, score: float=None, title: str=None):  # noqa: E501
        """QueryResult - a model defined in Swagger

        :param doc_id: The doc_id of this QueryResult.  # noqa: E501
        :type doc_id: int
        :param url: The url of this QueryResult.  # noqa: E501
        :type url: str
        :param score: The score of this QueryResult.  # noqa: E501
        :type score: float
        :param title: The title of this QueryResult.  # noqa: E501
        :type title: str
        """
        self.swagger_types = {
            'doc_id': int,
            'url': str,
            'score': float,
            'title': str
        }

        self.attribute_map = {
            'doc_id': 'doc_id',
            'url': 'url',
            'score': 'score',
            'title': 'title'
        }
        self._doc_id = doc_id
        self._url = url
        self._score = score
        self._title = title

    @classmethod
    def from_dict(cls, dikt) -> 'QueryResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The QueryResult of this QueryResult.  # noqa: E501
        :rtype: QueryResult
        """
        return util.deserialize_model(dikt, cls)

    @property
    def doc_id(self) -> int:
        """Gets the doc_id of this QueryResult.

        The internal index document ID  # noqa: E501

        :return: The doc_id of this QueryResult.
        :rtype: int
        """
        return self._doc_id

    @doc_id.setter
    def doc_id(self, doc_id: int):
        """Sets the doc_id of this QueryResult.

        The internal index document ID  # noqa: E501

        :param doc_id: The doc_id of this QueryResult.
        :type doc_id: int
        """

        self._doc_id = doc_id

    @property
    def url(self) -> str:
        """Gets the url of this QueryResult.

        The URL of the page matching the query  # noqa: E501

        :return: The url of this QueryResult.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url: str):
        """Sets the url of this QueryResult.

        The URL of the page matching the query  # noqa: E501

        :param url: The url of this QueryResult.
        :type url: str
        """

        self._url = url

    @property
    def score(self) -> float:
        """Gets the score of this QueryResult.

        Score assigned for the document by the ranker  # noqa: E501

        :return: The score of this QueryResult.
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score: float):
        """Sets the score of this QueryResult.

        Score assigned for the document by the ranker  # noqa: E501

        :param score: The score of this QueryResult.
        :type score: float
        """

        self._score = score

    @property
    def title(self) -> str:
        """Gets the title of this QueryResult.

        A title (e.g. from an HTML document) or other derived label  # noqa: E501

        :return: The title of this QueryResult.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title: str):
        """Sets the title of this QueryResult.

        A title (e.g. from an HTML document) or other derived label  # noqa: E501

        :param title: The title of this QueryResult.
        :type title: str
        """

        self._title = title
