import time
from backend.util.crypto_hash import crypto_hash

GENESIS_DATA = {
    'timestamp':1,
    'last_hash':'genesis_last_hash',
    'hash':'gensis_hash',
    'data':[]
}
class Block:
    """
    Block: a unit of storage.
    Store transactions in a blockchain that supports
    a cryptocurrency
    """
    def __init__(self,timestamp,last_hash,hash,data):
        self.timestamp=timestamp
        self.last_hash=last_hash
        self.hash=hash
        self.data=data

    def __repr__(self):
        return (
            'Block('f'timestamp: {self.timestamp}, '
            f'last_hash: {self.last_hash}, '
            f'hash: {self.hash}, '
            f'data:{self.data})'
        )

    @staticmethod
    def mine_block(last_block, data):
        """
        mine a block based on the given last block and data
        """
        timestamp = time.time_ns()
        last_hash = last_block.hash
        hash = crypto_hash(timestamp, last_hash, data)

        return Block(timestamp, last_hash, hash, data)

    @staticmethod
    def genesis():
        """
        generate the genesis block
        """
        # return Block(
        #         GENESIS_DATA['timestamp'],
        #         GENESIS_DATA['last_hash'],
        #         GENESIS_DATA['hash'],
        #         GENESIS_DATA['data']
        # )
        return Block(**GENESIS_DATA) #unpacks dictionary
def main():
    # block=Block('foo')
    # print(block)
    # print(f'block.py __name__: {__name__}')
    genesis_block = Block.genesis()
    block=Block.mine_block(genesis_block,'foo')
    print(block)


if __name__ == '__main__':
    main()