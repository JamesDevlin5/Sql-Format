# SQL Formatter

Will format all keywords, aggregate functions and reserved words to be fully upper case.

## Example

```sql
select * from tbl
where productID is not null;
```

becomes

```sql
SELECT * FROM tbl
WHERE productID IS NOT NULL;
```

## Dependencies

Relies on [Python Lex-Yacc](https://github.com/dabeaz/ply) to lex the input SQL file(s).

## Inner Workings

A basic lexer is used to parse symbolic tokens and delimiters of any kind: `, . ; ( )` ...
Any symbolic token is then checked to see if it's one of the SQL reserved words
([listed here](https://www.drupal.org/docs/develop/coding-standards/list-of-sql-reserved-words)),
and is converted to upper-case if necessary.
Finally, all the lexed tokens, among which are the modified tokens, are printed so that the original file may be recovered but in a better format.

## Usage

`./sqlfmt.py <SQL_FILE>` and the result will be printed to standard output.

## Installation

The lexer library must be downloaded, but it's only one file.
The makefile calls `curl` to handle this.
Otherwise, python3 is the only requirement to run this program.

## Testing

PyTest is used as the testing library.
Tests are defined in `test_fmt.py`.

All the tests can be run via: `pytest test_fmt.py` or by calling the makefile recipe, `make test`.

## ToDo

- Write to file *inplace*
- Separate verbose debug printing from desired output printing
- Ignore contents of comments

