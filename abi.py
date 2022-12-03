import web3
import json

class OptShop():
    ganache_url = "HTTP://127.0.0.1:7545"
    w3 = web3.Web3(web3.HTTPProvider(ganache_url))

    addres_contract = '0x17b1C5A67804d40Df926D14D7f802bEF42C9405e'

    with open("abi.json", "r") as file:
        abi = json.load(file)


    contract = w3.eth.contract (address = addres_contract, abi = abi)

    def init(self):
        pass

    def accounts(self):
        return self.w3.eth.accounts

    def get_balance(self, address):
        _address = web3.Web3.toChecksumAddress(address)
        return web3.Web3.fromWei(self.w3.eth.getBalance(_address), 'ether')

    def get_deal_num(self):
        return self.contract.functions.get_deal_num().call()


    def get_goods_num(self):
        return self.contract.functions.get_goods_num().call()


    def add_Provider(self,idGood, id,nameFirm, addressFirm, phoneNumber,address_owner):
        tx = self.contract.functions.add_Provider(idGood,id,nameFirm,addressFirm,phoneNumber,address_owner).transact({'from': "0xD03C873C2319B030B840F73FdFA761391AEaf6cA"})
        self.w3.eth.waitForTransactionReceipt(tx)


    def add_Buyer(self,id, nameFirmBuy, addressFirmBuy, phoneNumberBuy,owner_buyer ):
        tx =self.contract.functions.add_Buyer(id, nameFirmBuy, addressFirmBuy, phoneNumberBuy,owner_buyer).transact({'from': "0xD03C873C2319B030B840F73FdFA761391AEaf6cA"})
        self.w3.eth.waitForTransactionReceipt(tx)

    def add_Good(self,idGood, nameFirm, nameGoods, units, amount, valueBuy, valueSell):
        tx =self.contract.functions.add_Good(idGood, nameFirm, nameGoods, units, amount, valueBuy, valueSell).transact({'from': "0xD03C873C2319B030B840F73FdFA761391AEaf6cA"})
        self.w3.eth.waitForTransactionReceipt(tx)


    def add_deals(self, id, amountSellGoods, idBuyer, idSeller):
        tx =self.contract.functions.add_deals(id, amountSellGoods, idBuyer, idSeller).transact({'from': "0xD03C873C2319B030B840F73FdFA761391AEaf6cA"})
        self.w3.eth.waitForTransactionReceipt(tx)

    def buy_good(self,id, removeGood, toShop, price):
        tx = self.contract.functions.buy_good(id, removeGood, toShop).transact(
            {'from': "0xD03C873C2319B030B840F73FdFA761391AEaf6cA", 'value': price})
        self.w3.eth.waitForTransactionReceipt(tx)



OS = OptShop()

acc = OS.accounts()
balance = OS.get_balance(acc[0])
print(acc)

OS.buy_good(1,5,"0xfAdBc3bc03123d67d160C089Fb372657cF92aAf5",5*7)
print(OS.get_goods_num())

print(acc[0])
print(balance)