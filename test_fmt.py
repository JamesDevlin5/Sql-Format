
import sqlfmt


def test_simple():
    data = """
select * from tbl
where productID is not null;

"""
    assert sqlfmt.lex_str(data) == """
SELECT * FROM tbl
WHERE productID IS NOT NULL;

"""
