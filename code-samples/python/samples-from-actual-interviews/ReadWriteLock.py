"""
print("Hello, world!")


int data;
ReadWriteLock lock;

# thread 1
lock.acquireRead(data);
foo = data
lock.releaseRead();

# thread 2
lock.acquireRead();
# read data
lock.releaseRead();

# thread 3
lock.acquireWrite();
data = "5"
lock.releaseWrite();

"""
import datacache


class ReadWriteLock():

    def __init__(self, data):
        """
        """
        # generate ID for later use
        self.id = math.rand(# some criteria for id size)


        self.data = data

        if data in datacache:
            self.lockStatus = datacache[data].lockedStatus

    def read():
        return(self.data)


    @property
    def write(self, params):
        if not self.lockStatus:
            self.data = params['input']


    def Lock(self, exclusive == False):
        """
        """
        # if exclusive lock is needed and the status is not currently locked
        if exclusive and not self.lockStatus:
            Raise(DataAlreadyLocked())
            return(None)

        if exclusive:
            datacache[data]['lockedStatusExclusive'] = True
        datacache[data]['lockedStatus'] = True
        datacache[data]['lockedOwner'].append = self.id

        return(True)


    def unLock(self):
        """
        """
        datacache[data]['lockedOwner'][self.id].pop()

        if len(datacache[data]['lockedOwner']) == 0:
            datacache[data]['lockedStatus'] = False

            if datacache[data]['lockedStatusExclusive'] and self.id in datacache['lockedOwner']:
               datacache[data]['lockedStatusExclusive'] = None

        return(True)


    def acquireRead(self):
        """
        """
        return(self.Lock())


    def releaseRead(self):
        """
        """
        return(self.Unlock())


    def acquireWrite(self):
        """
        """
        while not datacache[data]['lockedStatus']:
            # we're waiting our turn

        return(self.Lock(True))


    def releaseWrite(self):
        """
        """
        return(self.Unlock())


if __main__:
    # put code here..

    #
    lock = ReadWriteLock(data)

    if lock.acquireRead():

        foo = lock.read(data)

        lock.releaseRead()

    lock.acquireWrite()

    data.write = "5"

    lock.releaseWrite()
