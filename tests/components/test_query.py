from src.cantopy.components.query import Query


def test_to_string() -> None:
    """Test the Query class"""
    query = Query(name="blackbird", grp="1", length=">5", since="2020-01-01")
    assert query.to_string() == "blackbird grp=1 length=>5 since=2020-01-01"
