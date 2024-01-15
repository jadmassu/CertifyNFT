from algosdk import account, encoding, mnemonic, transaction

from algosdk.v2client import algod

class AlgorandClient:
    def __init__(self, algod_address, algod_token):
        self.algod_address = algod_address
        self.algod_token = algod_token
        
        self.algod_client = self.connect_to_algod()

    def connect_to_algod(self):
        try:
            algod_client = algod.AlgodClient(self.algod_token, self.algod_address)
            print("algod_client",algod_client)
            return algod_client
        except Exception as e:
            raise Exception("Failed to connect to Algorand node:", str(e))

    def get_account_info(self, account_address):
        try:
            
            print("get_account_info", account_address)
            account_info = self.algod_client.account_info(account_address)
            # account_info = self.algod_client.status()
            
            return account_info
        except Exception as e:
            raise Exception("Failed to get account info:", str(e))
   
    def create_transaction(self, sender_address, recipient_address, amount):
        try:
            params = self.algod_client.suggested_params()
            txn = transaction.PaymentTxn(sender_address, params, recipient_address, amount)
            return txn
        except Exception as e:
            raise Exception("Failed to create transaction:", str(e))

    def sign_transaction(self, txn, private_key):
        try:
            signed_txn = txn.sign(private_key)
            return signed_txn
        except Exception as e:
            raise Exception("Failed to sign transaction:", str(e))

    def send_transaction(self, signed_txn):
        try:
            txid = self.algod_client.send_transaction(signed_txn)
            return txid
        except Exception as e:
            raise Exception("Failed to send transaction:", str(e))

    def create_asset(self, creator_address, asset_name, unit_name, total_supply):
        try:
            params = self.algod_client.suggested_params()
            asset_params = transaction.AssetParams(
                creator=creator_address,
                total=total_supply,
                decimals=0,
                default_frozen=False,
                unit_name=unit_name,
                asset_name=asset_name,
                manager=creator_address,
                reserve=creator_address,
                freeze=creator_address,
                clawback=creator_address,
                url="https://myasset.com"
            )

            create_asset_txn = transaction.AssetConfigTxn(
                sender=creator_address,
                sp=params,
                **asset_params
            )

            signed_create_asset_txn = create_asset_txn.sign(private_key)
            asset_id = self.algod_client.send_transaction(signed_create_asset_txn)
            return asset_id
        except Exception as e:
            raise Exception("Failed to create asset:", str(e))


