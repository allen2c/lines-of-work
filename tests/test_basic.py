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
    for knowledge_id in work.list_knowledge_ids():
        knowledge = work.get_knowledge(knowledge_id)
        assert knowledge.title
        assert knowledge.content
