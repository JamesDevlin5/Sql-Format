
from sqlfmt import lex_str


def test_simple1():
    data = """
select * from tbl
where productID is not null;

"""
    assert lex_str(data) == """
SELECT * FROM tbl
WHERE productID IS NOT NULL;

"""


def test_simple2():
    data = """
    select *
    from prods
    order by
    employeeID ASC,
    employeeName Asc;
    """
    assert lex_str(data) == """
    SELECT *
    FROM prods
    ORDER BY
    employeeID ASC,
    employeeName ASC;
    """


def test_medium1():
    data = """
    select
        call.*,
        datediff("SECOND", call.start_time, call.end_time) as call_duration
    from call
    order by
        call.employee_id asc,
        call.start_time asc;
    """
    assert lex_str(data) == """
    SELECT
        call.*,
        DATEDIFF("SECOND", call.start_time, call.end_time) AS call_duration
    FROM call
    ORDER BY
        call.employee_id ASC,
        call.start_time ASC;
    """


def test_medium2():
    data = """
    -- sum of call duration per each employee
    select
        employee.id,
        employee.first_name,
        employee.last_name,
        Sum(DateDiff("SECOND", call.start_time, call.end_time)) aS call_duration_sum
    From call
    Inner join employee oN call.employee_id = employee.id
    Group by
        employee.id,
        employee.first_name,
        employee.last_name
    Order by
        employee.id asc;
    """
    assert lex_str(data) == """
    -- sum of call duration per each employee
    SELECT
        employee.id,
        employee.first_name,
        employee.last_name,
        SUM(DATEDIFF("SECOND", call.start_time, call.end_time)) AS call_duration_sum
    FROM call
    INNER JOIN employee ON call.employee_id = employee.id
    GROUP BY
        employee.id,
        employee.first_name,
        employee.last_name
    ORDER BY
        employee.id ASC;
    """


def test_hard1():
    data = """
    -- % of call duration per each employee compared to the duration of all his calls
    select
        employee.id,
        employee.first_name,
        employee.last_name,
        call.start_time,
        call.end_time,
        datediff("second", call.start_time, call.end_time) as call_duration,
        duration_sum.call_duration_sum,
        cast( cast(datediff("second", call.start_time, call.end_time) as decimal(7,2)) / cast(duration_sum.call_duration_sum as decimal(7,2)) as decimal(4,4)) as call_percentage
    from call
    inner join employee on call.employee_id = employee.id
    inner join (
        select
            employee.id,
            sum(datediff("second", call.start_time, call.end_time)) as call_duration_sum
        from call
        inner join employee on call.employee_id = employee.id
        group by
            employee.id
    ) as duration_sum on employee.id = duration_sum.id
    order by
        employee.id asc,
        call.start_time asc;
    """
    assert lex_str(data) == """
    -- % of call duration per each employee compared to the duration of all his calls
    SELECT
        employee.id,
        employee.first_name,
        employee.last_name,
        call.start_time,
        call.end_time,
        DATEDIFF("SECOND", call.start_time, call.end_time) AS call_duration,
        duration_sum.call_duration_sum,
        CAST( CAST(DATEDIFF("SECOND", call.start_time, call.end_time) AS DECIMAL(7,2)) / CAST(duration_sum.call_duration_sum AS DECIMAL(7,2)) AS DECIMAL(4,4)) AS call_percentage
    FROM call
    INNER JOIN employee ON call.employee_id = employee.id
    INNER JOIN (
        SELECT
            employee.id,
            SUM(DATEDIFF("SECOND", call.start_time, call.end_time)) AS call_duration_sum
        FROM call
        INNER JOIN employee ON call.employee_id = employee.id
        GROUP BY
            employee.id
    ) AS duration_sum ON employee.id = duration_sum.id
    ORDER BY
        employee.id ASC,
        call.start_time ASC;
    """
