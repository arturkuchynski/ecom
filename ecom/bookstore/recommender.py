from django.conf import settings
from .models import Book
import redis

# connect to redis
r = redis.StrictRedis(host=settings.REDIS_HOST,
                      port=settings.REDIS_PORT,
                      db=settings.REDIS_DB)


class Recommender(object):

    def get_book_key(self, id):
        return 'book:{}:purchased_with'.format(id)

    def books_bought(self, books):
        book_ids = [p.id for p in books]
        for book_id in book_ids:
            for with_id in book_ids:
                # get the other books bought with each book
                if book_id != with_id:
                    # increment score for book purchased together
                    r.zincrby(self.get_book_key(book_id),
                              with_id,
                              amount=1)

    def suggest_books_for(self, books, max_results=6):
        book_ids = [p.id for p in books]
        if len(books) == 1:
            # only 1 book
            suggestions = r.zrange(
                             self.get_book_key(book_ids[0]),
                             0, -1, desc=True)[:max_results]
        else:
            # generate a temporary key
            flat_ids = ''.join([str(id) for id in book_ids])
            tmp_key = 'tmp_{}'.format(flat_ids)
            # multiple books, combine scores of all books
            # store the resulting sorted set in a temporary key
            keys = [self.get_book_key(id) for id in book_ids]
            r.zunionstore(tmp_key, keys)
            # remove ids for the books the recommendation is for
            r.zrem(tmp_key, *book_ids)
            # get the book ids by their score, descendant sort
            suggestions = r.zrange(tmp_key, 0, -1, 
                                   desc=True)[:max_results]
            # remove the temporary key
            r.delete(tmp_key)
        suggested_books_ids = [int(id) for id in suggestions]

        # get suggested books and sort by order of appearance
        suggested_books = list(Book.objects.filter(id__in=suggested_books_ids))
        suggested_books.sort(key=lambda x: suggested_books_ids.index(x.id))
        return suggested_books

    def clear_purchases(self):
            for id in Book.objects.values_list('id', flat=True):
                r.delete(self.get_book_key(id))
