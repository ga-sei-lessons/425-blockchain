import hashlib
import json # python's json module
from time import time # data module similar to new Date()
from pprint import pprint # pretty print

class Blockchain:
    def __init__(self):
        # list of blocks in the blockchain
        self.chain = []
        # list of transactions that have not been added to a block yet
        self.pending_transactions = []
        # seed the blockchain with a new block
        self.new_block(previous_hash="The Times 03/Jan/2009 Chancellor on brink of second bailout for banks.", proof=100)

    def __len__(self):
        return len(self.chain)

    @property # another decorator
    def last_block(self):
        # return the last block of the chain
        # blockchainInstance.last_block 
        return self.chain[-1] # the last index of our chain

    def new_block(self, proof, previous_hash=None):
        # create a new block based on the pending transactions
        # create a new block 
        block = {
            'index': len(self) + 1,
            'timestamp': time(),
            'transactions': self.pending_transactions,
            'proof': proof, # provided by the miner
            'previous_hash': previous_hash or self.hash(self.last_block)
        }
        # clear out the pending transaction
        self.pending_transactions = []
        # append the new block to our blockchain!
        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        # add a new transactions to the list of pending transactions
        # create new transaction
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        }
        # add the transaction to the list of pending transactions
        self.pending_transactions.append(transaction)
        # return transaction that was added on success
        return transaction

    def hash(self, block):
        # hash blocks
        # order the keys of the block so that they are predictable, encode
        string_block = json.dumps(block, sort_keys=True).encode()

        # return the hexdigest
        return hashlib.sha256(string_block).hexdigest()


bc = Blockchain()
bc.new_transaction('Taylor', 'Weston', 10)
bc.new_transaction('Weston', 'April', 5)
bc.new_transaction('Weston', 'June', 5)
# the chain will be the same
bc.new_block(1000)
bc.new_transaction('Grace', 'Wonjune', 100)
bc.new_transaction('Wonjune', 'Heg', 50)
bc.new_transaction('April', 'Emily H.', 7)
bc.new_block(7000)
pprint(bc.pending_transactions)
pprint(bc.chain)
