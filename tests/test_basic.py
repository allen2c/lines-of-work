import hashlib

import pytest

import lines_of_work as low


@pytest.mark.parametrize(
    "industry_id, subcategory_id, work_id",
    [
        (industry, subcategory, work)
        for industry in low.list_industry_ids()
        for subcategory in low.list_subcategory_ids(industry)
        for work in low.list_work_ids(industry, subcategory)
    ],
)
def test_read_all_works(
    industry_id: low.IndustryID, subcategory_id: low.SubcategoryID, work_id: low.WorkID
):
    work = low.Work(industry_id, subcategory_id, work_id)
    assert work.agent
    assert work.agent.name
    assert work.agent.instructions

    count = 0
    knowledge_md5_set = set()
    for knowledge_id in work.list_knowledge_ids():
        count += 1
        knowledge = work.get_knowledge(knowledge_id)
        assert knowledge.title.strip()
        assert knowledge.content.strip()
        assert "lines_of_work" not in knowledge.content
        knowledge_md5_set.add(
            hashlib.md5(knowledge.content.strip().encode()).hexdigest()
        )

    assert len(knowledge_md5_set) == count
