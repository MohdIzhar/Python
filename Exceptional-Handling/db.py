import contextlib

class Connection:
    def __init__(self):
        self.xid = 0

    def _start_transaction(self):
        print('Starting transaction', self.xid)
        rslt = self.xid
        self.xid = self.xid + 1
        return rslt

    def _commit_transaction(self, xid):
        print('committing transaction', xid)

    def _rollback_transaction(self, xid):
        print("rolling back transaction", xid)


class Transaction:
    def __init__(self, conn):
        self.conn = conn
        self.xid = conn._start_transaction()

    def commit(self):
        self.conn._commit_transaction(self.xid)

    def rollback(self):
        self.conn._rollback_transaction(self.xid)

@contextlib.contextmanager
def start_transaction(connection):
    tx =  Transaction(connection)

    try:
        yield
    except:
        tx.rollback()
        raise

    tx.commit()