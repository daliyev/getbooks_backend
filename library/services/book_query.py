from django.db import connection
from contextlib import closing


def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row)) for row in cursor.fetchall()
    ]


def dictfetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))


def get_category():
    with connection.cursor() as cursor:
        cursor.execute("""
        select name from library_category
        where is_active = true
        """)
        table = dictfetchall(cursor)
        return table


def get_subcategory():
    with connection.cursor() as cursor:
        cursor.execute("""
        select name from library_subcategory
        where is_active = true
        """)
        table = dictfetchall(cursor)
        return table


def get_subcategory_by_category(category_id):
    with connection.cursor() as cursor:
        cursor.execute("""
        select ls.name from library_subcategory ls
        where ls.category_id = category_id and ls.is_active = true
        """)
        table = dictfetchall(cursor)
        return table


def get_book_list():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""
        select b.id, b.name, b.image, c.first_name, c.last_name,
        (SELECT count(*) FROM library_review WHERE b.id = library_review.book_id) AS count_review,
        (SELECT AVG(CASE WHEN rating IS NOT NULL THEN rating ELSE 0 END) FROM library_review WHERE b.id = library_review.book_id) AS average_rating,
        (SELECT view_count from library_bookactions WHERE b.id = library_bookactions.book_id) as view_count
        from library_author c 
        join library_book b on b.author_id  = c.id
        order by average_rating desc 
        limit 50
        """, )
        table = dictfetchall(cursor)
        return table


def get_book_list_by_subcategory_id(subcategory_id):
    with closing(connection.cursor()) as cursor:
        cursor.execute("""
        select b.id, b.name, b.image, c.first_name, c.last_name,
        (SELECT count(*) FROM library_review WHERE b.id = library_review.book_id) AS count_review,
        (SELECT AVG(CASE WHEN rating IS NOT NULL THEN rating ELSE 0 END) FROM library_review WHERE b.id = library_review.book_id) AS average_rating,
        (SELECT view_count from library_bookactions WHERE b.id = library_bookactions.book_id) as view_count
        from library_author c 
        join library_book b on b.author_id  = c.id
        order by average_rating desc 
        where b.subcategory_id  = %s
        """, [subcategory_id])
        table = dictfetchall(cursor)
        return table


def get_book_details(book_id):
    with closing(connection.cursor()) as cursor:
        cursor.execute("""
        select b.id, b.name, b.about_book, b.image, b.pdf_file, b.audio_file, b.published_year, c.first_name, c.last_name, c.about, c.birth_date, c.birth_location, c.death_date, c.death_location, 
        (SELECT count(*) FROM library_review WHERE b.id = library_review.book_id) AS count_review,
        (SELECT AVG(CASE WHEN rating IS NOT NULL THEN rating ELSE 0 END) FROM library_review WHERE b.id = library_review.book_id) AS average_rating,
        (SELECT view_count from library_bookactions WHERE b.id = library_bookactions.book_id),
        (select name from library_publisher where b.publisher_id  = library_publisher.id) as publisher
        from library_bookauthor a
        join library_book b on a.book_id = b.id
        join library_author c on a.author_id = c.id
        where b.id = %s
        """, [book_id])
        table = dictfetchone(cursor)
        return table


def get_book_reviews(book_id):
    with closing(connection.cursor()) as cursor:
        cursor.execute("""
        select b.user_id, b.content, b. rating, b.date_posted,
        (select concat(first_name,' ', last_name) as user_info from custom_auth_customuser where custom_auth_customuser.id = b.user_id)
        from library_book a
        join library_review b
        on a.id = b.book_id
        where a.id  = %s
        """, [book_id])

        table = dictfetchall(cursor)
        return table


def get_book_details_by_id(book_id):
    with closing(connection.cursor()) as cursor:
        cursor.execute("""
        select b.*, c.first_name, c.last_name, c.birth_date, c.birth_location,
        (SELECT count(*) FROM library_review WHERE b.id = library_review.book_id) AS count_review,
        (SELECT AVG(CASE WHEN rating IS NOT NULL THEN rating ELSE 0 END) FROM library_review WHERE b.id = library_review.book_id) AS average_rating,
        (select concat(view_count, ' ', download_count) from library_bookactions ba where b.id = ba.book_id) as view_and_download
        from library_bookauthor a
        join library_book b on a.book_id = b.id
        join library_author c on a.author_id = c.id
        where a.book_id = %s
        """, [book_id])
        table = dictfetchone(cursor)
        return table
