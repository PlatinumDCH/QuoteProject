from srv.utils.connect import connect_pymongo, postgres_connect
from srv.utils.sql_form import create_author_table, create_quote_table


mongo_conn = connect_pymongo()
pg_conn = postgres_connect()



author_collection = mongo_conn['autor']
quote_collection = mongo_conn['quotes']

pg_cursor = pg_conn.cursor()


pg_cursor.execute(create_author_table)
pg_cursor.execute(create_quote_table)
pg_conn.commit()



try:
    authors = list(author_collection.find())
except TypeError as e:
    print(f"Error call  find on author_collection: {e}")
    raise

author_map = {}

for author in authors:
    author_id = author['_id']
    author_data = (
        str(author_id),
        author.get('fullname', ''),
        author.get('born_date', ''),
        author.get('born_location', ''),
        author.get('description', '')
    )
    pg_cursor.execute("""
           INSERT INTO author (_id, fullname, born_date, born_location, description)
           VALUES (%s, %s, %s, %s, %s) RETURNING id;
       """, author_data)
    author_map[str(author_id)] = pg_cursor.fetchone()[0]

pg_conn.commit()


try:
    quotes = list(quote_collection.find())
except TypeError as e:
    print(f"Error where call find in quote_collection: {e}")
    raise

for quote in quotes:
    quote_id = quote["_id"]
    author_id = quote["author"]
    quote_data = (
        str(quote_id),
        quote.get("quote", ""),
        quote.get("tags", []),
        author_map[str(author_id)]
    )
    pg_cursor.execute("""
        INSERT INTO quotes (_id, quote, tags, author_id)
        VALUES (%s, %s, %s, %s);
    """, quote_data)

pg_conn.commit()


pg_cursor.close()
pg_conn.close()

