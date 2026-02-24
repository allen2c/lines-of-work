title = "HATEOAS Cơ bản"

content = """
HATEOAS: response chứa link đến related resource. Client discover API.
Optional. Hypermedia. Mekong Delta Tech support khi beneficial. Not always.

**Link in Response:** _links với href, rel. rel = relationship. self, next,
prev. Navigate. No hardcode URL. Client follow link. Flexible. Server control
URL. Version in URL. Change transparent.

**When Use:** Document-driven API. Complex navigation. Reduce client coupling.
When Overkill: simple CRUD. Client know structure. Add complexity. Document
when use. Example. Trade-off. Not standard for all. Choose.

**Implementation:** Include links in serializer. Conditional. Relation type.
Document rel types. Client implement following. Test. Support. Optional
feature. Feature flag.
"""  # noqa: E501

version = "0.0.1"
